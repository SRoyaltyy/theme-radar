"""DST-safe nightly schedule gate (scripts/schedule_gate.py).

Run: python3 -m unittest
"""
from __future__ import annotations

import importlib.util
import tempfile
import unittest
from datetime import datetime, time, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

import pandas as pd

from src import history_guard as hg
from src.trading_calendar import next_trading_day

_ROOT = Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location("schedule_gate",
                                               _ROOT / "scripts" / "schedule_gate.py")
sg = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(sg)
ET = ZoneInfo("America/New_York")


def utc(s: str) -> datetime:
    return datetime.fromisoformat(s).replace(tzinfo=timezone.utc).astimezone(ET)


class ScheduleGateTest(unittest.TestCase):
    def setUp(self):
        self._t = tempfile.TemporaryDirectory()
        self.root = Path(self._t.name)
        for d in ("data/snapshots", "data/features", "01_daily"):
            (self.root / d).mkdir(parents=True)

    def tearDown(self):
        self._t.cleanup()

    def snap(self, day, scrape_utc):
        pd.DataFrame({"Ticker": ["A"], "Price": [1.0], "scrape_ts": [scrape_utc]}).to_csv(
            self.root / f"data/snapshots/{day}.csv", index=False)

    def run_(self, job, when_utc, event="schedule"):
        return sg.decide(job, event, utc(when_utc), self.root)[0]

    def test_summer_edt(self):
        day = "2026-09-25"                                      # Friday, EDT
        self.assertTrue(self.run_("finviz", f"{day}T20:30:00"))  # 16:30 ET
        self.assertFalse(self.run_("score", f"{day}T21:00:00"))  # finviz late: wait
        self.snap(day, f"{day}T20:47:00+00:00")
        self.assertFalse(self.run_("finviz", f"{day}T21:30:00"))  # 2nd slot: no-op
        self.assertTrue(self.run_("score", f"{day}T21:00:00"))
        self.assertTrue(self.run_("composite", f"{day}T21:20:00"))
        (self.root / f"data/features/{day}_1d.csv").write_text("x")
        (self.root / f"01_daily/{day}_composite_rank.md").write_text("x")
        self.assertFalse(self.run_("score", f"{day}T22:00:00"))
        self.assertFalse(self.run_("composite", f"{day}T22:20:00"))

    def test_winter_est(self):
        day = "2026-11-06"                                      # Friday, EST
        self.assertFalse(self.run_("finviz", f"{day}T20:30:00"))  # 15:30 ET pre-close
        self.assertFalse(self.run_("score", f"{day}T21:00:00"))
        self.assertFalse(self.run_("composite", f"{day}T21:20:00"))
        self.assertTrue(self.run_("finviz", f"{day}T21:30:00"))   # 16:30 ET
        self.snap(day, f"{day}T21:47:00+00:00")
        self.assertTrue(self.run_("score", f"{day}T22:00:00"))
        self.assertTrue(self.run_("composite", f"{day}T22:20:00"))

    def test_pre_close_snapshot_is_refetched(self):
        day = "2026-11-06"
        self.snap(day, f"{day}T20:31:00+00:00")                 # 15:31 EST: not the close
        self.assertTrue(self.run_("finviz", f"{day}T21:30:00"))
        self.assertFalse(self.run_("score", f"{day}T22:00:00"))

    def test_holiday_and_manual(self):
        self.assertFalse(self.run_("finviz", "2026-11-26T21:30:00"))   # Thanksgiving
        self.assertTrue(self.run_("score", "2026-11-26T22:00:00", "workflow_dispatch"))
        self.assertTrue(self.run_("finviz", "2026-09-25T13:00:00", "workflow_dispatch"))

    def test_late_slots_before_next_open_both_seasons(self):
        for day in ("2026-09-25", "2026-11-06", "2026-09-24", "2026-11-05"):
            nxt = next_trading_day(datetime.fromisoformat(day).date())
            nxt_open = datetime.combine(nxt, time(9, 30), ET)
            for hhmm in ("21:30", "22:00", "22:20"):
                t = utc(f"{day}T{hhmm}:00")
                self.assertEqual(t.date().isoformat(), day)       # same ET day
                self.assertGreaterEqual(t.time(), time(16, 0))
                self.assertLess(t, nxt_open)
            self.snap(day, f"{day}T21:30:00+00:00")
            self.assertTrue(hg.close_is_in(self.root / "data/snapshots", day)[0], day)


if __name__ == "__main__":
    unittest.main()
