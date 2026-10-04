"""Behavior checks for preservation, reruns, conflicts, and portable bundles."""

import hashlib
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
import zipfile

REPO = Path(__file__).resolve().parent.parent
SOURCE = REPO / "skills/yummy"
spec = importlib.util.spec_from_file_location("bootstrap", SOURCE / "scripts/bootstrap.py")
helper = importlib.util.module_from_spec(spec)
spec.loader.exec_module(helper)


def snapshot(root):
    return {p.relative_to(root).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in root.rglob("*") if p.is_file() and not p.is_symlink()}


class BootstrapTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "project"
        self.root.mkdir()

    def run_setup(self, **kwargs):
        return helper.bootstrap(self.root, SOURCE, **kwargs)

    def test_empty_project_installs_complete_bundles_and_reruns_do_nothing(self):
        first = self.run_setup(areas=["research"])
        self.assertEqual(first["result"], "complete")
        for name in helper.FOUNDATION:
            self.assertTrue((self.root / name).is_file())
        for name in helper.DIRECTORIES + ("areas-sections/research",):
            self.assertTrue((self.root / name).is_dir())
        for base in (".agents/skills/yummy", ".claude/skills/yummy"):
            for name in helper.PACKAGE:
                self.assertEqual((self.root / base / name).read_bytes(), (SOURCE / name).read_bytes())
        before = snapshot(self.root)
        second = self.run_setup(areas=["research"])
        self.assertEqual(second["created"], [])
        self.assertEqual(snapshot(self.root), before)

    def test_existing_documents_code_assets_and_git_are_preserved(self):
        for name in helper.FOUNDATION + ("src/app.py", "resources/data.bin", ".git/config"):
            path = self.root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(b"existing\x00\xff\r\n" + name.encode())
        before = snapshot(self.root)
        self.run_setup(content={"PROJECT.md": "A new proposal must not replace this"})
        after = snapshot(self.root)
        for name, digest in before.items():
            self.assertEqual(after[name], digest)
        self.assertFalse((self.root / "archive/data.bin").exists())

    def test_empty_existing_file_is_not_filled(self):
        (self.root / "STATUS.md").touch()
        self.run_setup()
        self.assertEqual((self.root / "STATUS.md").read_bytes(), b"")

    def test_dry_run_does_not_write_anything(self):
        (self.root / "original.txt").write_text("keep", encoding="utf-8")
        before = set(self.root.rglob("*"))
        report = self.run_setup(dry_run=True)
        self.assertEqual(report["result"], "preview")
        self.assertTrue(report["planned"])
        self.assertEqual(report["created"], [])
        self.assertEqual(set(self.root.rglob("*")), before)

    def test_file_directory_conflicts_are_partial_and_untouched(self):
        (self.root / "resources").write_bytes(b"occupied")
        (self.root / "DESIGN.md").mkdir()
        (self.root / ".agents").write_bytes(b"occupied adapter")
        report = self.run_setup()
        self.assertEqual(report["result"], "partial")
        self.assertTrue(report["blocked"])
        self.assertEqual((self.root / "resources").read_bytes(), b"occupied")
        self.assertTrue((self.root / "DESIGN.md").is_dir())
        self.assertEqual((self.root / ".agents").read_bytes(), b"occupied adapter")
        self.assertTrue((self.root / "PROJECT.md").exists())

    def test_existing_partial_skill_folder_is_not_merged(self):
        installed = self.root / ".agents/skills/yummy"
        installed.mkdir(parents=True)
        (installed / "custom.md").write_text("custom", encoding="utf-8")
        report = self.run_setup(host="universal")
        self.assertIn(".agents/skills/yummy", report["preserved_skill_bundles"])
        self.assertEqual(list(installed.iterdir()), [installed / "custom.md"])

    def test_prepared_content_only_populates_missing_document(self):
        text = "# A family project\n\nConfirmed goal: plan a reunion.\n"
        self.run_setup(content={"PROJECT.md": text}, host="claude")
        self.assertEqual((self.root / "PROJECT.md").read_text(encoding="utf-8"), text)
        self.assertFalse((self.root / ".agents").exists())
        self.assertTrue((self.root / ".claude/skills/yummy/SKILL.md").is_file())

    def test_installed_helper_can_fill_a_gap_without_touching_other_files(self):
        self.run_setup(host="universal")
        (self.root / "STATUS.md").unlink()  # Simulate a missing path between invocations.
        before = snapshot(self.root)
        installed = self.root / ".agents/skills/yummy/scripts/bootstrap.py"
        result = subprocess.run([sys.executable, "-B", str(installed), "--root", str(self.root),
                                 "--host", "universal"], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        report = json.loads(result.stdout)
        self.assertEqual(report["created"], ["STATUS.md"])
        after = snapshot(self.root)
        for name, digest in before.items():
            self.assertEqual(after[name], digest)

    def test_invalid_inputs_make_no_changes(self):
        for area in ("../escape", "one/two", "CON", "con", "aux", "bad name"):
            with self.subTest(area=area), self.assertRaises(ValueError):
                self.run_setup(areas=[area])
        invalid = Path(self.temp.name) / "invalid.json"
        invalid.write_text('{"../escape": "bad"}', encoding="utf-8")
        with self.assertRaises(ValueError):
            helper.load_content(invalid)
        self.assertEqual(list(self.root.iterdir()), [])

    def test_exclusive_creation_preserves_file_that_appears_after_preflight(self):
        original_open = Path.open
        raced = self.root / "PROJECT.md"

        def race_open(path, mode="r", *args, **kwargs):
            if path == raced and mode == "xb":
                with original_open(path, "wb") as handle:
                    handle.write(b"other writer")
            return original_open(path, mode, *args, **kwargs)

        with patch.object(Path, "open", race_open):
            report = self.run_setup()
        self.assertEqual(raced.read_bytes(), b"other writer")
        self.assertIn("PROJECT.md", report["preserved"])

    def test_skill_directory_race_is_not_merged(self):
        original_mkdir = Path.mkdir
        target = self.root / ".agents/skills/yummy"

        def race_mkdir(path, *args, **kwargs):
            if path == target and not path.exists():
                original_mkdir(path)
                (path / "other.md").write_text("another installation", encoding="utf-8")
            return original_mkdir(path, *args, **kwargs)

        with patch.object(Path, "mkdir", race_mkdir):
            report = self.run_setup(host="universal")
        self.assertEqual(list(target.iterdir()), [target / "other.md"])
        self.assertIn(".agents/skills/yummy", report["preserved_skill_bundles"])

    def test_windows_junction_or_symlink_cannot_redirect_resource_writes(self):
        outside = Path(self.temp.name) / "outside"
        outside.mkdir()
        (outside / "keep.txt").write_text("safe", encoding="utf-8")
        link = self.root / "resources"
        if os.name == "nt":
            result = subprocess.run(["cmd.exe", "/c", "mklink", "/J", str(link), str(outside)],
                                    capture_output=True, text=True)
            if result.returncode:
                self.skipTest("Junction creation unavailable: " + result.stderr)
            self.addCleanup(lambda: os.rmdir(link))
        else:
            link.symlink_to(outside, target_is_directory=True)
        before = snapshot(outside)
        report = self.run_setup()
        self.assertEqual(report["result"], "partial")
        self.assertEqual(snapshot(outside), before)
        self.assertTrue(any(item["path"] == "resources" for item in report["blocked"]))
        with self.assertRaises(ValueError):
            helper.bootstrap(link, SOURCE)

    def test_package_is_complete_and_refuses_to_replace_archive(self):
        path = Path(self.temp.name) / "yummy.zip"
        packager = REPO / "scripts/package.py"
        command = [sys.executable, "-B", str(packager), "--output", str(path)]
        first = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(first.returncode, 0, first.stderr)
        with zipfile.ZipFile(path) as archive:
            for name in helper.PACKAGE:
                self.assertEqual(archive.read("yummy/" + name), (SOURCE / name).read_bytes())
        original = path.read_bytes()
        second = subprocess.run(command, capture_output=True, text=True)
        self.assertNotEqual(second.returncode, 0)
        self.assertEqual(path.read_bytes(), original)


if __name__ == "__main__":
    unittest.main()
