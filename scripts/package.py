#!/usr/bin/env python3
"""Build an uploadable Yummy skill ZIP without replacing an existing archive."""

import argparse
import importlib.util
from pathlib import Path
import zipfile


def package(output):
    skill = Path(__file__).resolve().parent.parent / "skills/yummy"
    spec = importlib.util.spec_from_file_location("yummy_bootstrap", skill / "scripts/bootstrap.py")
    helper = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(helper)
    names = list(helper.PACKAGE) + ["agents/openai.yaml"]
    payloads = {name: (skill / name).read_bytes() for name in names}
    # ZipFile's exclusive mode refuses an occupied archive path.
    with zipfile.ZipFile(output, "x", compression=zipfile.ZIP_DEFLATED) as archive:
        for name, data in payloads.items():
            archive.writestr("yummy/" + name, data)
    return len(payloads)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    count = package(args.output)
    print("Created " + str(args.output) + " with " + str(count) + " skill files")
