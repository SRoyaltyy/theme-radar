"""Hash-manifest guard for dated history (scripts/check_history_hashes.py).

Run: python -m unittest discover -s tests -t .
"""
from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from io import StringIO
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "check_history_hashes", _ROOT / "scripts" / "check_history_hashes.py")
chh = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(chh)


def run(root: Path, *args: str) -> int:
    with redirect_stdout(StringIO()), redirect_stderr(StringIO()):
        return chh.main([*args, "--root", str(root)])


class HistoryHashesTest(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        for d in ("data/snapshots", "data/features", "data/scores"):
            (self.root / d).mkdir(parents=True)
        self.w("data/snapshots/2026-09-23.csv", "a")
        self.w("data/snapshots/2026-09-23.raw.csv", "araw")
        self.w("data/snapshots/current.csv", "cur")
        self.w("data/snapshots/previous.csv", "prev")
        self.w("data/snapshots/manifest.json", "{}")
        self.w("data/features/2026-09-23_1d.csv", "f")
        self.w("data/features/2026-09-23_1d.meta.json", "{}")
        self.w("data/scores/2026-09-23_segments.csv", "s")
        self.assertEqual(run(self.root, "add-new", "--today", "2026-09-23"), 0)

    def tearDown(self):
        self._tmp.cleanup()

    def w(self, rel, text):
        (self.root / rel).write_text(text)

    def manifest(self):
        return json.loads((self.root / chh.MANIFEST_REL).read_text())["files"]

    def test_bootstrap_covers_only_dated_files(self):
        m = self.manifest()
        self.assertEqual(sorted(m), [
            "data/features/2026-09-23_1d.csv",
            "data/features/2026-09-23_1d.meta.json",
            "data/scores/2026-09-23_segments.csv",
            "data/snapshots/2026-09-23.csv",
            "data/snapshots/2026-09-23.raw.csv",
        ])
        self.assertTrue(all(v["first_recorded"] == "2026-09-23" for v in m.values()))
        self.assertEqual(run(self.root, "verify"), 0)

    def test_pointer_files_are_ignored(self):
        self.w("data/snapshots/current.csv", "changed")
        self.w("data/snapshots/manifest.json", '{"x":1}')
        self.assertEqual(run(self.root, "verify"), 0)

    def test_verify_fails_on_change_and_delete(self):
        self.w("data/scores/2026-09-23_segments.csv", "rewritten")
        self.assertEqual(run(self.root, "verify"), 1)
        self.w("data/scores/2026-09-23_segments.csv", "s")
        self.assertEqual(run(self.root, "verify"), 0)
        (self.root / "data/snapshots/2026-09-23.raw.csv").unlink()
        self.assertEqual(run(self.root, "verify"), 1)

    def test_add_new_appends_and_never_updates_past(self):
        self.w("data/snapshots/2026-09-24.csv", "b")
        self.w("data/features/2026-09-23_1d.csv", "rewritten past")
        before = (self.root / chh.MANIFEST_REL).read_text()
        self.assertEqual(run(self.root, "add-new", "--today", "2026-09-24"), 1)
        self.assertEqual((self.root / chh.MANIFEST_REL).read_text(), before)
        self.w("data/features/2026-09-23_1d.csv", "f")
        self.assertEqual(run(self.root, "add-new", "--today", "2026-09-24"), 0)
        m = self.manifest()
        self.assertEqual(m["data/snapshots/2026-09-24.csv"]["first_recorded"], "2026-09-24")
        self.assertEqual(m["data/snapshots/2026-09-23.csv"]["first_recorded"], "2026-09-23")

    def test_same_day_rerun_allowed_only_for_today(self):
        self.w("data/snapshots/2026-09-24.csv", "b")
        self.assertEqual(run(self.root, "add-new", "--today", "2026-09-24"), 0)
        self.w("data/snapshots/2026-09-24.csv", "b rerun")
        self.assertEqual(run(self.root, "verify"), 1)
        # next day: yesterday is now strict
        self.assertEqual(run(self.root, "add-new", "--today", "2026-09-25"), 1)
        # same day: replacement allowed
        self.assertEqual(run(self.root, "add-new", "--today", "2026-09-24"), 0)
        self.assertEqual(run(self.root, "verify"), 0)

    def test_restate_requires_reason_and_logs(self):
        self.w("data/scores/2026-09-23_segments.csv", "fixed")
        self.assertEqual(run(self.root, "add-new", "--today", "2026-09-24",
                             "--restate", "data/scores/2026-09-23_segments.csv"), 2)
        self.assertEqual(run(self.root, "add-new", "--today", "2026-09-24",
                             "--restate", "data/scores/2026-09-23_segments.csv",
                             "--reason", "vendor bug fix"), 0)
        self.assertEqual(run(self.root, "verify"), 0)
        log = (self.root / chh.RESTATE_LOG_REL).read_text()
        self.assertIn("data/scores/2026-09-23_segments.csv", log)
        self.assertIn("vendor bug fix", log)
        m = self.manifest()["data/scores/2026-09-23_segments.csv"]
        self.assertEqual(m["first_recorded"], "2026-09-23")
        self.assertEqual(m["sha256"], chh.sha256_file(
            self.root / "data/scores/2026-09-23_segments.csv"))


class RepoManifestTest(unittest.TestCase):
    def test_repo_history_matches_manifest(self):
        if not (_ROOT / chh.MANIFEST_REL).exists():
            self.skipTest("no manifest")
        man = chh.load_manifest(_ROOT)
        self.assertEqual(chh.problems(_ROOT, man), {})


if __name__ == "__main__":
    unittest.main()
