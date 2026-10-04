#!/usr/bin/env python3
"""Create missing Yummy paths only. Python 3.9+, standard library, no network."""

import argparse
import json
import os
from pathlib import Path
import re
import stat
import sys

FOUNDATION = ("AGENTS.md", "PROJECT.md", "STATUS.md", "DECISIONS.md", "DESIGN.md")
DIRECTORIES = (
    "temp-inbox", "areas-sections", "resources", "active-queued-work",
    "active-queued-work/queued", "active-queued-work/active",
    "active-queued-work/completed", "outputs", "archive",
)
PACKAGE = (
    "SKILL.md", "assets/LICENSE", "references/foundation.md", "references/design.md",
    "references/portability.md", "scripts/bootstrap.py",
) + tuple("assets/foundation/" + name for name in FOUNDATION)
RESERVED = {"con", "prn", "aux", "nul"} | {
    prefix + str(number) for prefix in ("com", "lpt") for number in range(1, 10)
}


def occupied(path):
    return os.path.lexists(path)


def linked(path):
    try:
        info = path.lstat()
    except FileNotFoundError:
        return False
    return stat.S_ISLNK(info.st_mode) or bool(
        getattr(info, "st_file_attributes", 0)
        & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0)
    )


def guard(root, path):
    """Reject traversal, linked paths, and nondirectory ancestors."""
    path.relative_to(root)
    for current in (path,) + tuple(path.parents):
        if linked(current):
            raise ValueError("Linked path or junction: " + str(current))
        if current != path and occupied(current) and not current.is_dir():
            raise ValueError("Ancestor is not a directory: " + str(current))
        if current == root:
            break


def validate_area(value):
    if (not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", value)
            or value in RESERVED or len(value) > 64):
        raise ValueError("Area must be a safe lowercase slug: " + value)
    return value


def load_content(path):
    if path is None:
        return {}
    content = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(content, dict) or any(
        key not in FOUNDATION or not isinstance(value, str) or not value.strip()
        for key, value in content.items()
    ):
        raise ValueError("Content JSON must map foundation filenames to nonempty text")
    return content


def build_plan(root, source, host, areas, content):
    # Read and validate the complete bundle before writing any target paths.
    bundle = {name: (source / name).read_bytes() for name in PACKAGE}
    metadata = source / "agents/openai.yaml"
    if metadata.is_file():
        bundle["agents/openai.yaml"] = metadata.read_bytes()
    entries = {name: ("directory", None) for name in DIRECTORIES}
    for area in areas:
        entries["areas-sections/" + validate_area(area)] = ("directory", None)
    for name in FOUNDATION:
        data = content[name].encode("utf-8") if name in content else bundle[
            "assets/foundation/" + name
        ]
        entries[name] = ("file", data)

    preserved_bundles = []
    blocked_bundles = []
    locations = []
    if host in ("universal", "all"):
        locations.append(".agents/skills/yummy")
    if host in ("claude", "all"):
        locations.append(".claude/skills/yummy")
    for location in locations:
        target = root / location
        try:
            guard(root, target)
            if occupied(target):
                if not target.is_dir():
                    raise ValueError("Skill destination is not a directory")
                preserved_bundles.append(location)
                continue
        except (ValueError, OSError) as exc:
            blocked_bundles.append({"path": location, "reason": str(exc)})
            continue
        entries[location] = ("directory", None)
        for name, data in bundle.items():
            entries[location + "/" + name] = ("file", data)

    # Include parents so all conflicts are visible, including hidden skill roots.
    for name in list(entries):
        for parent in Path(name).parents:
            if str(parent) != ".":
                entries.setdefault(parent.as_posix(), ("directory", None))
    return entries, preserved_bundles, blocked_bundles


def bootstrap(root, source, host="all", areas=(), content=None, dry_run=False):
    root = Path(os.path.abspath(root))
    # Check the supplied root before resolving: resolution could hide a junction.
    for ancestor in (root,) + tuple(root.parents):
        if linked(ancestor):
            raise ValueError("Project root has a linked ancestor: " + str(ancestor))
    if not root.is_dir():
        raise ValueError("Project root must be an existing directory: " + str(root))
    entries, preserved_bundles, blocked_bundles = build_plan(
        root, source, host, areas, content or {}
    )
    report = {
        "root": str(root), "dry_run": dry_run, "created": [], "planned": [],
        "preserved": [], "preserved_skill_bundles": preserved_bundles,
        "blocked": blocked_bundles,
    }
    ready = []
    for name, (kind, data) in sorted(
        entries.items(), key=lambda item: (item[0].count("/"), item[0])
    ):
        path = root / name
        try:
            guard(root, path)
            if occupied(path):
                if kind == "directory" and not path.is_dir():
                    raise ValueError("Required directory is occupied by a file")
                if kind == "file" and not path.is_file():
                    raise ValueError("Required document is occupied by a directory")
                report["preserved"].append(name)
                continue
            ready.append((name, kind, data))
        except (ValueError, OSError) as exc:
            report["blocked"].append({"path": name, "reason": str(exc)})

    raced_bundles = []
    for name, kind, data in ready:
        if any(name.startswith(location + "/") for location in raced_bundles):
            continue
        if dry_run:
            report["planned"].append(name)
            continue
        path = root / name
        try:
            guard(root, path)
            if kind == "directory":
                path.mkdir()  # No overwrite or implicit parent creation.
            else:
                with path.open("xb") as handle:  # Exclusive even if a file races us.
                    handle.write(data)
            report["created"].append(name)
        except FileExistsError:
            # A path appeared after preflight. Preserve it, check its type.
            try:
                guard(root, path)
                correct = path.is_dir() if kind == "directory" else path.is_file()
                if not correct:
                    raise ValueError("Newly occupied path has the wrong type")
                report["preserved"].append(name)
                if name in (".agents/skills/yummy", ".claude/skills/yummy"):
                    raced_bundles.append(name)
                    report["preserved_skill_bundles"].append(name)
            except (ValueError, OSError) as exc:
                report["blocked"].append({"path": name, "reason": str(exc)})
        except (ValueError, OSError) as exc:
            report["blocked"].append({"path": name, "reason": str(exc)})
    report["result"] = "partial" if report["blocked"] else (
        "preview" if dry_run else "complete"
    )
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True,
                        help="Actual existing project directory; never changed implicitly")
    parser.add_argument("--host", choices=("universal", "claude", "all"), default="all",
                        help="Local skill destinations; all installs .agents and .claude")
    parser.add_argument("--area", action="append", default=[],
                        help="Evidence-based major area slug (repeat as needed)")
    parser.add_argument("--content-json", type=Path,
                        help="Prepared initial document contents; occupied files still win")
    parser.add_argument("--dry-run", action="store_true", help="Inspect without writing")
    args = parser.parse_args()
    try:
        source = Path(__file__).resolve().parent.parent
        report = bootstrap(args.root, source, args.host, args.area,
                           load_content(args.content_json), args.dry_run)
        print(json.dumps(report, indent=2, ensure_ascii=True))
        return 2 if report["blocked"] else 0
    except (ValueError, OSError) as exc:
        print(json.dumps({"result": "error", "reason": str(exc)}), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
