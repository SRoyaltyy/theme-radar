"""Append-only / fill-once guards (src/history_guard.py, oppset builder).

Run: python3 -m unittest
"""
from __future__ import annotations

import importlib.util
import json
import shutil
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from io import StringIO
from pathlib import Path

import pandas as pd

from src import history_guard as hg

_ROOT = Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "check_history_hashes", _ROOT / "scripts" / "check_history_hashes.py")
chh = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(chh)

from research.oppset_clock_b import build_oppset_clock_b as ob  # noqa: E402


def quiet(fn, *a, **k):
    with redirect_stdout(StringIO()), redirect_stderr(StringIO()):
        return fn(*a, **k)


LABEL_HDR = ("Ticker,scan_date,signal_asof,entry_price,price_T,"
             "prediction_day_1d,label_date_1,exit_price_1d,price_T1,fwd_1d,short_fwd_1d,"
             "prediction_day_2d,label_date_2,exit_price_2d,price_T2,fwd_2d,short_fwd_2d,"
             "prediction_day_3d,label_date_3,exit_price_3d,price_T3,fwd_3d,short_fwd_3d,"
             "up_3d,down_3d\n")


def label_row(t, p0, d1="", p1="", d2="", p2=""):
    def f(p):
        return "" if p == "" else repr(p / p0 - 1)
    def s(p):
        return "" if p == "" else repr(-(p / p0 - 1))
    return (f"{t},2026-09-22,2026-09-22,{p0},{p0},{d1},{d1},{p1},{p1},{f(p1)},{s(p1)},"
            f"{d2},{d2},{p2},{p2},{f(p2)},{s(p2)},,,,,,,,\n")


class RowsManifestTest(unittest.TestCase):
    def setUp(self):
        self._t = tempfile.TemporaryDirectory()
        self.root = Path(self._t.name)
        for d in ("data/snapshots", "data/features", "data/scores", "data/labels",
                  "data/attribution"):
            (self.root / d).mkdir(parents=True)
        self.lab = self.root / "data/labels/2026-09-22_fwd.csv"
        self.lab.write_text(LABEL_HDR + label_row("A", 10.0, "2026-09-23", 11.0)
                            + label_row("B", 20.0, "2026-09-23", 19.0))
        self.assertEqual(self.run_chh("add-new", "--today", "2026-09-23"), 0)

    def tearDown(self):
        self._t.cleanup()

    def run_chh(self, *args):
        return quiet(chh.main, [*args, "--root", str(self.root)])

    def test_matured_horizon_fills_once(self):
        # 2d matures on 09-24: allowed (new part)
        self.lab.write_text(LABEL_HDR + label_row("A", 10.0, "2026-09-23", 11.0, "2026-09-24", 12.0)
                            + label_row("B", 20.0, "2026-09-23", 19.0, "2026-09-24", 18.0))
        self.assertEqual(self.run_chh("add-new", "--today", "2026-09-24"), 0)
        self.assertEqual(self.run_chh("verify"), 0)
        # same day re-fetch of the 09-24 snapshot changes 2d: allowed on 09-24 only
        self.lab.write_text(LABEL_HDR + label_row("A", 10.0, "2026-09-23", 11.0, "2026-09-24", 12.5)
                            + label_row("B", 20.0, "2026-09-23", 19.0, "2026-09-24", 18.0))
        self.assertEqual(self.run_chh("verify"), 1)
        self.assertEqual(self.run_chh("add-new", "--today", "2026-09-25"), 1)
        self.assertEqual(self.run_chh("add-new", "--today", "2026-09-24"), 0)
        # a filled 1d value never changes afterwards
        self.lab.write_text(LABEL_HDR + label_row("A", 10.0, "2026-09-23", 11.1, "2026-09-24", 12.5)
                            + label_row("B", 20.0, "2026-09-23", 19.0, "2026-09-24", 18.0))
        self.assertEqual(self.run_chh("add-new", "--today", "2026-09-25"), 1)

    def test_removed_row_or_file_fails(self):
        self.lab.write_text(LABEL_HDR + label_row("A", 10.0, "2026-09-23", 11.0))
        self.assertEqual(self.run_chh("verify"), 1)
        self.lab.unlink()
        self.assertEqual(self.run_chh("verify"), 1)

    def test_attr_pointer_upgrade_only(self):
        sp = self.root / "data/attribution/2026-09-22_summary.json"
        ic = self.root / "data/attribution/2026-09-22_ic.csv"
        sp.write_text(json.dumps({"label": "fwd_1d", "prediction_day": "2026-09-23"}))
        ic.write_text("feature,ic\nx,0.1\n")
        self.assertEqual(self.run_chh("add-new", "--today", "2026-09-23"), 0)
        ic.write_text("feature,ic\nx,0.2\n")               # same label rewritten
        self.assertEqual(self.run_chh("add-new", "--today", "2026-09-24"), 1)
        sp.write_text(json.dumps({"label": "fwd_2d", "prediction_day": "2026-09-24"}))
        self.assertEqual(self.run_chh("add-new", "--today", "2026-09-24"), 0)  # matured
        sp.write_text(json.dumps({"label": "fwd_1d", "prediction_day": "2026-09-23"}))
        self.assertEqual(self.run_chh("add-new", "--today", "2026-09-24"), 1)  # downgrade

    def test_new_dated_dirs_are_hash_locked(self):
        (self.root / "data/composite").mkdir()
        (self.root / "01_daily").mkdir()
        (self.root / "data/composite/2026-09-22_composite_rank.csv").write_text("a")
        (self.root / "01_daily/2026-09-22_scan.md").write_text("s")
        (self.root / "01_daily/2026-09-22_suggestion_check.md").write_text("x")
        self.assertEqual(self.run_chh("add-new", "--today", "2026-09-22"), 0)
        files = json.loads((self.root / chh.MANIFEST_REL).read_text())["files"]
        self.assertIn("data/composite/2026-09-22_composite_rank.csv", files)
        self.assertIn("01_daily/2026-09-22_scan.md", files)
        self.assertNotIn("01_daily/2026-09-22_suggestion_check.md", files)
        (self.root / "data/composite/2026-09-22_composite_rank.csv").write_text("b")
        self.assertEqual(self.run_chh("add-new", "--today", "2026-09-23"), 1)


class KeepExistingPastTest(unittest.TestCase):
    def test_keep_existing_past(self):
        with tempfile.TemporaryDirectory() as t:
            p = Path(t) / "x.csv"
            self.assertFalse(quiet(hg.keep_existing_past, [p], "2026-09-22", "t", "2026-09-25"))
            p.write_text("a")
            self.assertTrue(quiet(hg.keep_existing_past, [p], "2026-09-22", "t", "2026-09-25"))
            self.assertFalse(quiet(hg.keep_existing_past, [p], "2026-09-25", "t", "2026-09-25"))


def raw_df(n_shift=0.0):
    return pd.DataFrame({
        "Ticker": ["AAA", "BBB", "CCC", "ETFX"],
        "Company": ["Aaa Inc", "Bbb Corp", "Ccc Ltd", "Some ETF"],
        "Industry": ["Software", "Banks", "Biotech", "Exchange Traded Fund"],
        "Sector": ["Tech", "Fin", "Health", "Fin"],
        "ETF Type": ["", "", "", "Equity"],
        "Price": [50 + n_shift, 20.0, 8.0, 30.0],
        "Average Volume": [900, 1200, 600, 5000],
        "Market Cap": [5000, 800, 300, 1000],
        "Relative Volume": [2.5, 1.0, 5.2, 1.0],
        "Change": ["6.1%", "-1.0%", "12%", "0%"],
        "Change from Open": ["1%", "0%", "3%", "0%"],
        "Gap": ["0.5%", "4%", "1%", "0%"],
        "After-Hours Change": ["", "", "", ""],
        "Performance (Week)": ["3%", "1%", "45%", "0%"],
    })


class OppsetAppendOnlyTest(unittest.TestCase):
    def setUp(self):
        self._t = tempfile.TemporaryDirectory()
        self.root = Path(self._t.name)
        self.raw = self.root / "data/snapshots"
        self.out = self.root / "research/oppset_clock_b"
        self.raw.mkdir(parents=True)
        self.out.mkdir(parents=True)
        for d in ("2026-09-22", "2026-09-23"):
            self.write_raw(d)

    def tearDown(self):
        self._t.cleanup()

    def write_raw(self, d, shift=0.0):
        df = raw_df(shift)
        df = pd.concat([df] * 30, ignore_index=True)  # > 1000 bytes
        df.to_csv(self.raw / f"{d}.raw.csv", index=False)

    def build(self, *a):
        return quiet(ob.main, ["--raw-dir", str(self.raw), "--out", str(self.out), *a])

    def rows(self):
        return pd.read_csv(self.out / "oppset_all.csv", dtype=str, keep_default_na=False)

    def test_appends_one_day_at_a_time_from_t_minus_1_only(self):
        self.assertEqual(self.build("--asof", "2026-09-22", "--today", "2026-09-22"), 0)
        self.assertEqual(sorted(self.rows()["join_morning"].unique()), ["2026-09-23"])
        before = (self.out / "oppset_all.csv").read_bytes()
        # later raw appears; next night appends only 09-24 (asof 09-23)
        self.assertEqual(self.build("--today", "2026-09-23"), 0)
        after = (self.out / "oppset_all.csv").read_bytes()
        self.assertTrue(after.startswith(before))           # past bytes untouched
        r = self.rows()
        self.assertEqual(sorted(r["join_morning"].unique()), ["2026-09-23", "2026-09-24"])
        self.assertTrue((r["finviz_asof"] < r["join_morning"]).all())
        self.assertNotIn("ETFX", set(r["ticker"]))
        # re-fetched old raw never changes recorded rows
        self.write_raw("2026-09-22", shift=7.0)
        self.assertEqual(self.build("--today", "2026-09-24"), 0)
        self.assertEqual((self.out / "oppset_all.csv").read_bytes(), after)
        # explicit rebuild of a past morning is refused
        self.assertEqual(self.build("--asof", "2026-09-22", "--join-morning", "2026-09-22",
                                  "--today", "2026-09-24"), 1)
        log = (self.out / "APPEND_LOG.tsv").read_text().splitlines()
        self.assertEqual(len(log), 3)

    def test_catch_up_is_sequential_and_same_day_replace(self):
        self.write_raw("2026-09-24")
        self.assertEqual(self.build("--asof", "2026-09-22", "--today", "2026-09-22"), 0)
        self.assertEqual(self.build("--today", "2026-09-24"), 0)  # 09-23 then 09-24
        self.assertEqual(sorted(self.rows()["join_morning"].unique()),
                         ["2026-09-23", "2026-09-24", "2026-09-25"])
        # same-day re-fetch of today's snapshot: only today's morning may change
        self.write_raw("2026-09-24", shift=1.0)
        self.assertEqual(self.build("--today", "2026-09-24"), 0)
        r = self.rows()
        self.assertEqual(r[r.join_morning == "2026-09-25"]["price"].iloc[0], "51.0")
        self.assertEqual(r[r.join_morning == "2026-09-24"]["price"].iloc[0], "50.0")
        # next day the same rerun is refused? -> no: already recorded, no-op
        self.write_raw("2026-09-24", shift=2.0)
        self.assertEqual(self.build("--asof", "2026-09-24", "--today", "2026-09-25"), 0)
        self.assertEqual(self.rows()[lambda x: x.join_morning == "2026-09-25"]["price"].iloc[0],
                         "51.0")

    def test_tampered_past_rows_fail_refresh(self):
        self.assertEqual(self.build("--asof", "2026-09-22", "--today", "2026-09-22"), 0)
        p = self.out / "oppset_all.csv"
        p.write_text(p.read_text().replace("50.0", "49.0", 1))
        self.assertEqual(self.build("--today", "2026-09-23"), 1)
        self.assertEqual(self.build("--verify-only"), 1)

    def test_grade_columns_fill_once(self):
        self.assertEqual(self.build("--asof", "2026-09-22", "--today", "2026-09-22"), 0)
        df = pd.read_csv(self.out / "oppset_all.csv", dtype=str, keep_default_na=False)
        df["fwd_2d"] = ""
        df.to_csv(self.out / "oppset_all.csv", index=False)
        self.assertEqual(quiet(ob.record, self.out, "2026-09-24"), [])
        df["fwd_2d"] = "0.01"                               # matures: filled once
        df.to_csv(self.out / "oppset_all.csv", index=False)
        self.assertEqual(quiet(ob.record, self.out, "2026-09-25"), [])
        df["fwd_2d"] = "0.02"                               # never changes
        df.to_csv(self.out / "oppset_all.csv", index=False)
        self.assertNotEqual(quiet(ob.verify, self.out, "2026-09-26"), [])

    def test_knowable_by_0930(self):
        self.assertIsNotNone(ob.knowable_check("2026-09-23", "2026-09-23"))
        ob.RAW = self.raw
        pd.DataFrame({"Ticker": ["A"], "scrape_ts": ["2026-09-24T14:00:00+00:00"]}).to_csv(
            self.raw / "2026-09-23.csv", index=False)
        self.assertIsNotNone(ob.knowable_check("2026-09-23", "2026-09-24"))  # 10:00 ET
        pd.DataFrame({"Ticker": ["A"], "scrape_ts": ["2026-09-23T20:47:00+00:00"]}).to_csv(
            self.raw / "2026-09-23.csv", index=False)
        self.assertIsNone(ob.knowable_check("2026-09-23", "2026-09-24"))


if __name__ == "__main__":
    unittest.main()
