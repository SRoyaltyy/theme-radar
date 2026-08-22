"""Focused checks for the dated Finviz snapshot loaders used by run_outcome."""
from __future__ import annotations

import re
import unittest

from src.finviz_delta import list_dates, load_by_date

_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


class DatedSnapshotLoadersTest(unittest.TestCase):
    def test_list_dates_returns_available_labels(self) -> None:
        dates = list_dates()
        self.assertGreaterEqual(len(dates), 3)
        self.assertTrue(all(_DATE_RE.match(d) for d in dates))
        for needed in ("2026-08-06", "2026-08-12", "2026-08-19"):
            self.assertIn(needed, dates)

    def test_load_by_date_normalizes_existing_snapshots(self) -> None:
        for date_str in ("2026-08-06", "2026-08-12", "2026-08-19"):
            df = load_by_date(date_str)
            self.assertIn("Ticker", df.columns)
            self.assertGreater(len(df), 100)
            self.assertTrue(df["Ticker"].is_unique)
            self.assertTrue((df["Ticker"] == df["Ticker"].str.upper()).all())

    def test_load_by_date_missing_label_raises(self) -> None:
        with self.assertRaises(FileNotFoundError):
            load_by_date("1999-01-01")


if __name__ == "__main__":
    unittest.main()
