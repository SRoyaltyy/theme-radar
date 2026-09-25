"""Close-is-in guard: a grade for horizon h is written once, only after the
real close of its maturity day is in (War room 2026-09-25).

Run: python3 -m unittest
"""
from __future__ import annotations

import importlib.util
import json
import os
import subprocess
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from io import StringIO
from pathlib import Path
from unittest import mock

import numpy as np
import pandas as pd

from src import attribution, history_guard as hg, label_backfill as lb

_ROOT = Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "check_history_hashes", _ROOT / "scripts" / "check_history_hashes.py")
chh = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(chh)

# EDT: 16:00 ET = 20:00 UTC; next open 09:30 ET = 13:30 UTC
AFTER_CLOSE = "2026-09-24T20:47:00+00:00"   # 16:47 ET
PRE_MARKET = "2026-09-24T11:03:00+00:00"    # 07:03 ET same day
NEXT_MORNING = "2026-09-25T04:26:00+00:00"  # 00:26 ET next day (before open) -> ok
AFTER_OPEN = "2026-09-25T14:00:00+00:00"    # 10:00 ET next day


def quiet(fn, *a, **k):
    with redirect_stdout(StringIO()), redirect_stderr(StringIO()):
        return fn(*a, **k)


def snap(dirp: Path, day: str, ts: str | None, px=(10.0, 20.0), n=40):
    tick = [f"T{i}" for i in range(n)]
    df = pd.DataFrame({"Ticker": tick, "Price": [px[i % 2] for i in range(n)]})
    if ts is not None:
        df["scrape_ts"] = ts
    df.to_csv(dirp / f"{day}.csv", index=False)


class CloseIsInTest(unittest.TestCase):
    def setUp(self):
        self._t = tempfile.TemporaryDirectory()
        self.d = Path(self._t.name)

    def tearDown(self):
        self._t.cleanup()

    def test_scrape_ts_window(self):
        for ts, want in ((AFTER_CLOSE, True), (PRE_MARKET, False),
                         (NEXT_MORNING, True), (AFTER_OPEN, False)):
            snap(self.d, "2026-09-24", ts)
            self.assertEqual(hg.close_is_in(self.d, "2026-09-24")[0], want, ts)
        # Friday close -> window runs to Monday's open
        snap(self.d, "2026-09-25", "2026-09-27T15:00:00+00:00")
        self.assertTrue(hg.close_is_in(self.d, "2026-09-25")[0])
        # missing snapshot / no scrape_ts outside git -> refuse
        self.assertFalse(hg.close_is_in(self.d, "2026-09-23")[0])
        snap(self.d, "2026-09-22", None)
        self.assertFalse(hg.close_is_in(self.d, "2026-09-22")[0])

    def test_git_commit_time_fallback(self):
        env = dict(os.environ, GIT_AUTHOR_NAME="t", GIT_AUTHOR_EMAIL="t@x",
                   GIT_COMMITTER_NAME="t", GIT_COMMITTER_EMAIL="t@x")

        def git(*a, when=None):
            e = dict(env)
            if when:
                e["GIT_COMMITTER_DATE"] = e["GIT_AUTHOR_DATE"] = when
            subprocess.run(["git", "-C", str(self.d), *a], env=e, check=True,
                           capture_output=True)
        git("init", "-q")
        snap(self.d, "2026-08-10", None, px=(1.0, 2.0))
        git("add", "."); git("commit", "-qm", "pre", when="2026-08-10T11:03:31+00:00")
        self.assertFalse(hg.close_is_in(self.d, "2026-08-10")[0])   # 07:03 ET
        snap(self.d, "2026-08-10", None, px=(1.5, 2.5))
        self.assertFalse(hg.close_is_in(self.d, "2026-08-10")[0])   # uncommitted
        git("add", "."); git("commit", "-qm", "post", when="2026-08-10T21:21:24+00:00")
        ok, why = hg.close_is_in(self.d, "2026-08-10")
        self.assertTrue(ok, why)
        self.assertIn("git commit time", why)


class LabelAndAttributionGuardTest(unittest.TestCase):
    def setUp(self):
        self._t = tempfile.TemporaryDirectory()
        root = Path(self._t.name)
        self.snaps = root / "snapshots"
        self.labels = root / "labels"
        self.feats = root / "features"
        for p in (self.snaps, self.labels, self.feats):
            p.mkdir()
        pd.DataFrame({"Ticker": [f"T{i}" for i in range(40)]}).to_csv(
            self.feats / "2026-09-23_1d.csv", index=False)
        snap(self.snaps, "2026-09-23", "2026-09-23T20:47:00+00:00")
        self.p = [mock.patch.object(lb, "LABELS_DIR", self.labels),
                  mock.patch.object(lb, "FEATURES_DIR", self.feats),
                  mock.patch.object(hg, "today_et", lambda: "2026-09-24")]
        for x in self.p:
            x.start()

    def tearDown(self):
        for x in self.p:
            x.stop()
        self._t.cleanup()

    def dates(self):
        return {p.stem: p for p in sorted(self.snaps.glob("????-??-??.csv"))}

    def test_label_fill_waits_for_real_close(self):
        snap(self.snaps, "2026-09-24", PRE_MARKET, px=(11.0, 21.0))
        self.assertIsNone(quiet(lb.backfill_one, "2026-09-23", self.dates()))
        self.assertFalse((self.labels / "2026-09-23_fwd.csv").exists())
        snap(self.snaps, "2026-09-24", AFTER_CLOSE, px=(11.0, 21.0))
        self.assertIsNotNone(quiet(lb.backfill_one, "2026-09-23", self.dates()))
        lab = pd.read_csv(self.labels / "2026-09-23_fwd.csv")
        self.assertAlmostEqual(lab["fwd_1d"].iloc[0], 0.1)
        # next horizon's snapshot is pre-market: 1d kept, 2d not graded
        snap(self.snaps, "2026-09-25", "2026-09-25T12:00:00+00:00", px=(12.0, 22.0))
        with mock.patch.object(hg, "today_et", lambda: "2026-09-25"):
            quiet(lb.backfill_one, "2026-09-23", self.dates())
        lab = pd.read_csv(self.labels / "2026-09-23_fwd.csv")
        self.assertTrue(lab["fwd_2d"].isna().all())
        self.assertAlmostEqual(lab["fwd_1d"].iloc[0], 0.1)

    def test_attribution_refuses_before_close(self):
        snap(self.snaps, "2026-09-24", PRE_MARKET)
        df = pd.DataFrame({"Ticker": [f"T{i}" for i in range(40)],
                           "fwd_1d": np.linspace(-0.1, 0.1, 40),
                           "prediction_day_1d": "2026-09-24"})
        with mock.patch.object(attribution, "_load_joined", lambda d: df), \
             mock.patch.object(attribution, "_keep_existing_pointer", lambda d, l: False), \
             mock.patch.object(attribution.config, "DATA", self.snaps.parent), \
             mock.patch.object(attribution, "analyze",
                               side_effect=AssertionError("graded before close")):
            quiet(attribution.run, "2026-09-23")          # refused -> no analyze
            snap(self.snaps, "2026-09-24", AFTER_CLOSE)
            with self.assertRaises(AssertionError):       # now allowed to grade
                quiet(attribution.run, "2026-09-23")


class NoteTest(unittest.TestCase):
    def test_note_logs_without_touching_manifests(self):
        with tempfile.TemporaryDirectory() as t:
            root = Path(t)
            (root / "data/snapshots").mkdir(parents=True)
            (root / "data/snapshots/2026-09-23.csv").write_text("a")
            args = ["--root", str(root)]
            self.assertEqual(quiet(chh.main, ["add-new", "--today", "2026-09-23", *args]), 0)
            man = (root / chh.MANIFEST_REL).read_text()
            self.assertEqual(quiet(chh.main, ["note", "--file", "data/snapshots/2026-09-23.csv",
                                              "--old", "x", "--new", "y", *args]), 2)
            self.assertEqual(quiet(chh.main, [
                "note", "--file", "data/snapshots/2026-09-23.csv", "--old", "first=a1 ic=0.2",
                "--new", "kept=b2 ic=0.1", "--reason", "one-time data correction", *args]), 0)
            line = (root / chh.RESTATE_LOG_REL).read_text().splitlines()[-1].split("\t")
            self.assertEqual(line[1:], ["data/snapshots/2026-09-23.csv", "first=a1 ic=0.2",
                                        "kept=b2 ic=0.1", "one-time data correction"])
            self.assertEqual((root / chh.MANIFEST_REL).read_text(), man)
            self.assertEqual(quiet(chh.main, ["verify", *args]), 0)


if __name__ == "__main__":
    unittest.main()
