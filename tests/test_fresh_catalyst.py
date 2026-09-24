"""Additive dated catalyst flags (fresh_cat_*) + scrape_ts.

Run: python -m unittest discover -s tests -t .
Guarantees:
  * cat_* output is byte-identical to the pre-change implementation on
    historical snapshots (so n_catalysts / scores cannot move);
  * fresh_cat_* only fire on dated headlines newer than the previous trading
    day's snapshot (weekend-aware), never on the undated Daily Digest;
  * finviz_fetch appends News URL + scrape_ts at the END of the CSV.
"""
from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import pandas as pd

from src import finviz_delta as fd
from src import finviz_fetch as ff

SNAP = fd.SNAPSHOT_DIR
FEATURES = fd.config.DATA / "features"
HIST_DATES = ["2026-08-13", "2026-09-21", "2026-09-24"]


def _reference_cat_flags(df: pd.DataFrame) -> pd.DataFrame:
    """Verbatim copy of _add_catalyst_flags before 2026-09-25."""
    blob = (
        df.get("Daily Digest", pd.Series("", index=df.index)).fillna("").astype(str)
        + " "
        + df.get("News Title", pd.Series("", index=df.index)).fillna("").astype(str)
        + " "
        + df.get("Finviz_Description", pd.Series("", index=df.index)).fillna("").astype(str)
    ).str.lower()
    for name, pat in fd.CATALYST_PATTERNS.items():
        df[f"cat_{name}"] = blob.str.contains(pat, regex=True, na=False)
    return df


def _cat_cols(df):
    return [c for c in df.columns if c.startswith("cat_")]


class CatUnchanged(unittest.TestCase):
    def test_cat_columns_byte_identical_on_history(self):
        for d in HIST_DATES:
            path = SNAP / f"{d}.csv"
            if not path.exists():
                self.skipTest(f"missing {path}")
            base = fd.load_snapshot(path)
            old = _reference_cat_flags(base.copy())
            new = fd._add_catalyst_flags(base.copy())
            cols = _cat_cols(old)
            self.assertEqual(cols, _cat_cols(new), d)   # same names, same order
            self.assertEqual(
                old[["Ticker"] + cols].to_csv(index=False).encode(),
                new[["Ticker"] + cols].to_csv(index=False).encode(), d)
            # and identical to what the live pipeline committed to data/features
            fp = FEATURES / f"{d}_1d.csv"
            if fp.exists():
                feat = pd.read_csv(fp, usecols=["Ticker"] + cols)
                mine = new[["Ticker"] + cols].copy()
                mine[cols] = mine[cols].astype(int)
                self.assertTrue(
                    feat.set_index("Ticker")[cols].sort_index().equals(
                        mine.set_index("Ticker")[cols].sort_index()), d)

    def test_fresh_names_never_counted_as_cat(self):
        df = fd._add_catalyst_flags(fd.load_snapshot(SNAP / "2026-09-24.csv"))
        fresh = [c for c in df.columns if c.startswith(fd.FRESH_PREFIX)]
        self.assertEqual(len(fresh), len(fd.CATALYST_PATTERNS))
        self.assertTrue(all(not c.startswith("cat_") for c in fresh + ["news_age_h"]))
        self.assertEqual(len(_cat_cols(df)), len(fd.CATALYST_PATTERNS))


class FreshFlags(unittest.TestCase):
    def test_stale_elfy_headline(self):
        df = fd._add_catalyst_flags(fd.load_snapshot(SNAP / "2026-09-24.csv"))
        row = df[df["Ticker"] == "ELFY"].iloc[0]
        self.assertTrue(str(row["News Time"]).startswith("2025-04-10"))
        self.assertTrue(bool(row["cat_data_center_power"]))        # old tag fires
        self.assertFalse(bool(row["fresh_cat_data_center_power"]))  # dated tag does not
        self.assertGreater(row["news_age_h"], 24 * 365)

    def _frame(self, scrape_ts="2026-09-21T20:45:00+00:00"):
        return pd.DataFrame({
            "Ticker": ["SAT", "FRI", "DIG", "UND", "LATE", "OFF"],
            "News Title": ["New data center deal", "Data center order",
                           "Quarterly results", "Data center plan",
                           "Data center win", "Data center lease"],
            "Daily Digest": ["", "", "Signs AI data center lease", "", "", ""],
            "News Time": ["2026-09-19 10:00:00",   # Saturday: after Fri snapshot
                          "2026-09-18 12:00:00",   # already in Friday's snapshot
                          "2026-09-21 09:00:00",   # fresh, but match is digest-only
                          "-",                     # undated
                          "2026-09-21 17:30:00",   # after this scrape (16:45 ET)
                          "2026-09-21 08:00:00"],  # fresh same-day headline
            "scrape_ts": scrape_ts,
        })

    def test_weekend_news_counts_on_monday(self):
        fri_anchor = pd.Timestamp("2026-09-18 18:31:00")
        df = fd._add_catalyst_flags(self._frame())            # auto prev anchor
        df2 = fd._add_fresh_catalyst_flags(self._frame(), prev_anchor=fri_anchor)
        for out in (df, df2):
            f = dict(zip(out["Ticker"], out["fresh_cat_data_center_power"]))
            self.assertEqual(f, {"SAT": True, "FRI": False, "DIG": False,
                                 "UND": False, "LATE": False, "OFF": True})
        # cat_* keep old semantics (title OR digest, no date check)
        c = dict(zip(df["Ticker"], df["cat_data_center_power"]))
        self.assertTrue(all(c.values()))
        # auto-resolved anchor = newest News Time of the 2026-09-18 file
        if (SNAP / "2026-09-18.csv").exists():
            self.assertEqual(fd.previous_snapshot_anchor(pd.Timestamp("2026-09-21 16:45")),
                             fri_anchor)

    def test_72h_fallback_when_previous_file_missing(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = fd._add_fresh_catalyst_flags(self._frame(), snapshot_dir=Path(tmp))
        f = dict(zip(out["Ticker"], out["fresh_cat_data_center_power"]))
        # lower bound = 2026-09-21 16:45 ET - 72h = 09-18 16:45 -> FRI (12:00) stale
        self.assertTrue(f["SAT"])
        self.assertFalse(f["FRI"])
        self.assertAlmostEqual(
            float(out.loc[out.Ticker == "SAT", "news_age_h"].iloc[0]), 54.75, places=2)

    def test_old_file_anchor_is_newest_news_time(self):
        df = fd.load_snapshot(SNAP / "2026-09-24.csv")
        self.assertNotIn("scrape_ts", df.columns)
        self.assertEqual(fd.snapshot_anchor(df),
                         pd.to_datetime(df["News Time"], errors="coerce").max())


class FetchWritesScrapeTs(unittest.TestCase):
    def test_tail_columns_and_manifest(self):
        raw = (SNAP / "2026-09-24.raw.csv").read_bytes()
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp)
            with mock.patch.object(ff, "SNAPSHOT_DIR", tmp), \
                    mock.patch.object(ff, "ARCHIVE_DIR", tmp / "archive"):
                path = ff.save_dated_snapshot(raw, as_of="2026-09-24")
            out = pd.read_csv(path, low_memory=False)
            self.assertEqual(list(out.columns[-2:]), ["News URL", "scrape_ts"])
            # every earlier column keeps its position vs the committed snapshot
            committed = pd.read_csv(SNAP / "2026-09-24.csv", nrows=0)
            self.assertEqual(list(out.columns[:-2]), list(committed.columns))
            ts = pd.to_datetime(out["scrape_ts"], utc=True)
            self.assertEqual(ts.nunique(), 1)
            run = json.loads((tmp / "manifest.json").read_text())["runs"][-1]
            self.assertEqual(pd.Timestamp(run["scrape_ts_utc"]), ts.iloc[0])
            # fresh flags use scrape_ts as the anchor
            df = fd.load_snapshot(path)
            self.assertEqual(fd.snapshot_anchor(df),
                             ts.iloc[0].tz_convert("America/New_York").tz_localize(None))


if __name__ == "__main__":
    unittest.main()
