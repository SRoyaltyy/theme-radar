"""scripts/snapshot_guard.py: skip-if-exists and missing/identical alarm.

Run: python3 -m unittest
"""
from __future__ import annotations

import importlib.util
import tempfile
import unittest
from datetime import datetime
from pathlib import Path
from unittest import mock
from zoneinfo import ZoneInfo

_ROOT = Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location("snapshot_guard",
                                               _ROOT / "scripts" / "snapshot_guard.py")
g = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(g)
ET = ZoneInfo("America/New_York")


def et(s: str) -> datetime:
    return datetime.fromisoformat(s).replace(tzinfo=ET)


class GuardTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "data/snapshots").mkdir(parents=True)
        # no git repo in tmp -> working-tree fallback only
        self.p = mock.patch.object(g, "_git_blob", return_value=None)
        self.p.start()

    def tearDown(self):
        self.p.stop()
        self.tmp.cleanup()

    def write(self, day, body):
        (self.root / g.raw_rel(day)).write_bytes(body)

    def test_exists_skips(self):
        self.assertFalse(g.snapshot_exists(self.root, "2026-11-04"))
        self.write("2026-11-04", b"a,b\n1,2\n")
        self.assertTrue(g.snapshot_exists(self.root, "2026-11-04"))

    def test_exists_prefers_main(self):
        with mock.patch.object(g, "_git_blob", return_value=b"x"):
            self.assertTrue(g.snapshot_exists(self.root, "2026-11-04"))

    def test_alarm_missing(self):
        ok, msg = g.alarm_check(self.root, et("2026-11-04T18:00"))
        self.assertFalse(ok)
        self.assertIn("MISSING", msg)

    def test_alarm_present(self):
        self.write("2026-11-03", b"old\n")
        self.write("2026-11-04", b"new\n")
        ok, _ = g.alarm_check(self.root, et("2026-11-04T18:00"))
        self.assertTrue(ok)

    def test_alarm_identical(self):
        self.write("2026-11-03", b"same\n")
        self.write("2026-11-04", b"same\n")
        ok, msg = g.alarm_check(self.root, et("2026-11-04T18:00"))
        self.assertFalse(ok)
        self.assertIn("identical", msg)

    def test_alarm_identical_across_weekend(self):
        self.write("2026-10-30", b"same\n")  # Fri
        self.write("2026-11-02", b"same\n")  # Mon
        ok, _ = g.alarm_check(self.root, et("2026-11-02T18:00"))
        self.assertFalse(ok)

    def test_alarm_noop_weekend_and_early(self):
        self.assertTrue(g.alarm_check(self.root, et("2026-11-07T18:00"))[0])
        self.assertTrue(g.alarm_check(self.root, et("2026-11-04T17:00"))[0])


if __name__ == "__main__":
    unittest.main()
