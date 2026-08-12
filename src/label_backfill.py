"""Attach forward returns to feature rows using later Finviz snapshot Prices.

Wording (logic unchanged):
  signal_asof / scan_date  = last snapshot used to form the signal (data BEFORE the trade)
  prediction_day_kd        = calendar day the k-step forward trade is graded on
  entry_price              = Price on signal_asof (long buy / short sell entry)
  exit_price_kd            = Price on prediction_day_kd (session close proxy)
  fwd_kd                   = exit/entry - 1  (long return; short = opposite sign)

CLI: python -m src.label_backfill [--scan-date YYYY-MM-DD]
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd

from . import config
from .finviz_delta import normalize_frame
from .snapshots import snapshot_dates

LABELS_DIR = config.DATA / "labels"
FEATURES_DIR = config.DATA / "features"


def _price_map(path) -> dict[str, float]:
    df = normalize_frame(pd.read_csv(path, low_memory=False))
    if "Price" not in df.columns:
        return {}
    return dict(zip(df["Ticker"], df["Price"]))


def backfill_one(scan_date: str, dates: dict) -> Path | None:
    feat_path = FEATURES_DIR / f"{scan_date}_1d.csv"
    if not feat_path.exists():
        print(f"[labels] no features for {scan_date}")
        return None
    if scan_date not in dates:
        print(f"[labels] no snapshot for scan {scan_date}")
        return None

    sorted_dates = sorted(dates.keys())
    try:
        idx = sorted_dates.index(scan_date)
    except ValueError:
        return None

    forward = sorted_dates[idx + 1: idx + 4]
    if not forward:
        print(f"[labels] {scan_date}: no later snapshots yet — skip "
              f"(cannot grade trades that need a close after signal_asof={scan_date})")
        return None

    feat = pd.read_csv(feat_path, low_memory=False)
    p0 = _price_map(dates[scan_date])
    maps = [_price_map(dates[d]) for d in forward]

    rows = []
    for t in feat["Ticker"].astype(str):
        entry = p0.get(t, np.nan)
        row = {
            "Ticker": t,
            "scan_date": scan_date,
            "signal_asof": scan_date,
            "entry_price": entry,
            "price_T": entry,
        }
        for i, (pred_day, mp) in enumerate(zip(forward, maps), start=1):
            exit_px = mp.get(t, np.nan)
            long_ret = (
                (exit_px / entry - 1)
                if (entry and entry == entry and exit_px == exit_px and entry)
                else np.nan
            )
            row[f"prediction_day_{i}d"] = pred_day
            row[f"label_date_{i}"] = pred_day
            row[f"exit_price_{i}d"] = exit_px
            row[f"price_T{i}"] = exit_px
            row[f"fwd_{i}d"] = long_ret
            row[f"short_fwd_{i}d"] = (-long_ret) if long_ret == long_ret else np.nan
        for i in range(len(forward) + 1, 4):
            row[f"prediction_day_{i}d"] = ""
            row[f"label_date_{i}"] = ""
            row[f"exit_price_{i}d"] = np.nan
            row[f"price_T{i}"] = np.nan
            row[f"fwd_{i}d"] = np.nan
            row[f"short_fwd_{i}d"] = np.nan
        if "fwd_3d" in row and row["fwd_3d"] == row["fwd_3d"]:
            row["up_3d"] = int(row["fwd_3d"] > 0.015)
            row["down_3d"] = int(row["fwd_3d"] < -0.015)
        else:
            row["up_3d"] = np.nan
            row["down_3d"] = np.nan
        rows.append(row)

    out = pd.DataFrame(rows)
    LABELS_DIR.mkdir(parents=True, exist_ok=True)
    path = LABELS_DIR / f"{scan_date}_fwd.csv"
    out.to_csv(path, index=False)
    meta = {
        "signal_asof": scan_date,
        "scan_date": scan_date,
        "n_rows": len(out),
        "prediction_days": forward,
        "forward_snapshots": forward,
        "entry_definition": "Finviz Price on signal_asof snapshot (long buy / short sell entry)",
        "exit_definition": "Finviz Price on prediction_day snapshot (close proxy)",
        "fwd_definition": "long: exit/entry - 1; short_fwd: opposite sign",
        "n_fwd_1d_valid": int(out["fwd_1d"].notna().sum()) if "fwd_1d" in out else 0,
        "n_fwd_3d_valid": int(out["fwd_3d"].notna().sum()) if "fwd_3d" in out else 0,
        "wording": {
            "signal_asof": "Snapshot that formed the score (only data on/before this date).",
            "prediction_day_1d": "First trading snapshot AFTER signal_asof — the day the 1d trade is for.",
            "entry_price": "Price at signal_asof.",
            "exit_price_1d": "Price on prediction_day_1d.",
        },
    }
    (LABELS_DIR / f"{scan_date}_fwd.meta.json").write_text(
        json.dumps(meta, indent=2), encoding="utf-8")
    print(
        f"[labels] signal_asof={scan_date} | prediction_days={forward} | "
        f"n={len(out)} | entry=Price@{scan_date} | exits=Price@prediction_days "
        f"-> {path.name}"
    )
    return path


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--scan-date", default=None,
                    help="Signal as-of date (not the prediction day)")
    args = ap.parse_args()
    dates = snapshot_dates()
    if args.scan_date:
        p = backfill_one(args.scan_date, dates)
        if p is not None:
            print(f"[labels] refresh scan.md: "
                  f"python -m src.score_engine --date {args.scan_date} --skip-features")
        return
    feat_dates = sorted(p.stem.replace("_1d", "") for p in FEATURES_DIR.glob("*_1d.csv"))
    for d in feat_dates:
        p = backfill_one(d, dates)
        if p is not None:
            print(f"[labels] refresh scan.md: "
                  f"python -m src.score_engine --date {d} --skip-features")


if __name__ == "__main__":
    main()
