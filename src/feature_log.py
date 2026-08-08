"""Full-universe feature recorder.

Every ticker in the Finviz pair gets one row: levels, deltas, status, baseline
scores. Human briefs may truncate; this file never does.

CLI: python -m src.feature_log [--date YYYY-MM-DD]
Also invoked automatically from score_engine after scoring.
"""
from __future__ import annotations

import argparse
import json
from datetime import date, datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd

from . import config
from .finviz_delta import (DELTA_NUMERIC, SNAPSHOT_DIR, _add_catalyst_flags,
                           normalize_frame)
from .score_engine import find_prior, snapshot_dates

FEATURES_DIR = config.DATA / "features"

# Core fields always recorded (subset of DELTA_NUMERIC + derived)
LEVEL_COLS = [
    "Price", "Market Cap", "Average Volume", "Relative Volume",
    "Performance (Week)", "Performance (Month)", "Performance (Quarter)",
    "Performance (YTD)", "Relative Strength Index (14)",
    "Short Float", "Short Ratio",
    "Institutional Transactions", "Institutional Ownership",
    "Insider Transactions",
    "Analyst Recom", "Target Price", "Forward P/E",
    "Sales Year Over Year TTM", "Sales Growth Quarter Over Quarter",
    "EPS Surprise", "Profit Margin", "Gross Margin",
    "20-Day Simple Moving Average", "50-Day Simple Moving Average",
    "200-Day Simple Moving Average",
    "Beta", "Volatility (Month)", "Total Debt/Equity",
]

SCORE_JOIN = [
    "total_score", "score_100", "confidence", "ret_H", "upside_pct",
    "status_extension", "status_trend", "status_short", "status_street",
    "kill_flags", "n_pos", "n_neg", "w_pos", "w_neg", "n_catalysts",
    "price_score", "flow_score", "technical_score", "positioning_score",
    "valuation_score", "fundamental_score", "catalyst_score",
    "mcap_bucket", "beta_bucket",
]


def _dir_bucket(v: float, dz: float = 0.0) -> str:
    if v is None or (isinstance(v, float) and np.isnan(v)):
        return "na"
    if abs(v) < dz:
        return "flat"
    return "up" if v > 0 else "down"


def build_feature_table(
    cur: pd.DataFrame,
    prev: pd.DataFrame | None,
    scores: pd.DataFrame | None,
    scan_date: str,
    pair_date: str | None,
) -> pd.DataFrame:
    cur = _add_catalyst_flags(cur.copy())
    cur = cur.drop_duplicates(subset=["Ticker"], keep="first")
    base = cur.set_index("Ticker", drop=False)

    rows_meta = base[["Ticker", "Company", "Sector", "Industry"]].copy()
    if "Index" in base.columns:
        rows_meta["Index"] = base["Index"]

    # levels
    for c in LEVEL_COLS:
        if c in base.columns:
            rows_meta[c] = base[c]

    # true return + deltas
    if prev is not None:
        prev = prev.drop_duplicates(subset=["Ticker"], keep="first").set_index("Ticker")
        p_now = base["Price"] if "Price" in base.columns else pd.Series(np.nan, index=base.index)
        p_then = prev["Price"].reindex(base.index) if "Price" in prev.columns else pd.Series(np.nan, index=base.index)
        rows_meta["price_then"] = p_then
        rows_meta["true_ret"] = (p_now / p_then) - 1
        rows_meta["true_ret_dir"] = rows_meta["true_ret"].map(lambda x: _dir_bucket(x, 0.015))

        for c in LEVEL_COLS:
            if c not in base.columns or c not in prev.columns:
                continue
            then = prev[c].reindex(base.index)
            now = base[c]
            d = now - then
            rows_meta[f"d_{c}"] = d
            rows_meta[f"dir_{c}"] = d.map(lambda x: _dir_bucket(float(x) if pd.notna(x) else np.nan, 0.0))
    else:
        rows_meta["price_then"] = np.nan
        rows_meta["true_ret"] = np.nan
        rows_meta["true_ret_dir"] = "na"

    # catalyst flags
    for c in base.columns:
        if c.startswith("cat_"):
            rows_meta[c] = base[c].astype(int)

    # upside
    if "Target Price" in base.columns and "Price" in base.columns:
        rows_meta["upside_pct_lvl"] = (base["Target Price"] - base["Price"]) / base["Price"] * 100

    rows_meta["scan_date"] = scan_date
    rows_meta["pair_date"] = pair_date or ""
    rows_meta["n_universe"] = len(rows_meta)

    # join scores (full universe expected)
    if scores is not None and len(scores):
        sc = scores.drop_duplicates(subset=["Ticker"], keep="first").set_index("Ticker")
        for c in SCORE_JOIN:
            if c in sc.columns:
                rows_meta[c] = sc[c].reindex(rows_meta.index)

    out = rows_meta.reset_index(drop=True)
    return out


def write_features(df: pd.DataFrame, scan_date: str) -> Path:
    FEATURES_DIR.mkdir(parents=True, exist_ok=True)
    path = FEATURES_DIR / f"{scan_date}_1d.csv"
    df.to_csv(path, index=False)
    # integrity stamp
    stamp = FEATURES_DIR / f"{scan_date}_1d.meta.json"
    stamp.write_text(json.dumps({
        "scan_date": scan_date,
        "n_rows": int(len(df)),
        "n_tickers": int(df["Ticker"].nunique()),
        "pair_date": str(df["pair_date"].iloc[0]) if len(df) else "",
        "columns": list(df.columns),
    }, indent=2), encoding="utf-8")
    print(f"[feature_log] {len(df)} tickers -> {path}")
    if len(df) and df["Ticker"].nunique() != len(df):
        print("[feature_log] WARNING: duplicate tickers in feature file")
    return path


def run_for_date(date_str: str) -> Path | None:
    dates = snapshot_dates()
    if date_str not in dates:
        print(f"[feature_log] no snapshot for {date_str}")
        return None
    target = date.fromisoformat(date_str)
    cur = normalize_frame(pd.read_csv(dates[date_str], low_memory=False))
    prior = find_prior(dates, target, "1d")
    prev = normalize_frame(pd.read_csv(dates[prior], low_memory=False)) if prior else None

    scores_path = config.DATA / "scores" / f"{date_str}_1d.csv"
    scores = pd.read_csv(scores_path, low_memory=False) if scores_path.exists() else None
    if scores is not None:
        print(f"[feature_log] joined scores n={len(scores)} (snapshot n={len(cur)})")
        if abs(len(scores) - len(cur)) > 5:
            print("[feature_log] WARNING: score/snapshot row count mismatch")

    feat = build_feature_table(cur, prev, scores, date_str, prior)
    return write_features(feat, date_str)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", default=None)
    args = ap.parse_args()
    date_str = args.date or datetime.now(ZoneInfo(config.TZ)).date().isoformat()
    run_for_date(date_str)


if __name__ == "__main__":
    main()
