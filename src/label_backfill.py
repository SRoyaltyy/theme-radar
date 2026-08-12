"""Attach forward returns to feature rows using later Finviz snapshot Prices.

For scan date T, labels:
  fwd_1d = P(T+1)/P(T) - 1
  fwd_2d = P(T+2)/P(T) - 1
  fwd_3d = P(T+3)/P(T) - 1
where T+k are the next k *available snapshot dates* (proxy for trading days).

CLI: python -m src.label_backfill [--scan-date YYYY-MM-DD]
"""
from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path

import numpy as np
import pandas as pd

from . import config
from .finviz_delta import normalize_frame
from .score_engine import snapshot_dates

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
        print(f"[labels] {scan_date}: no later snapshots yet — skip")
        return None

    feat = pd.read_csv(feat_path, low_memory=False)
    p0 = _price_map(dates[scan_date])
    maps = [_price_map(dates[d]) for d in forward]

    rows = []
    for t in feat["Ticker"].astype(str):
        row = {"Ticker": t, "scan_date": scan_date}
        base = p0.get(t, np.nan)
        row["price_T"] = base
        for i, (d, mp) in enumerate(zip(forward, maps), start=1):
            px = mp.get(t, np.nan)
            row[f"price_T{i}"] = px
            row[f"fwd_{i}d"] = (px / base - 1) if (base and base == base and px == px and base) else np.nan
            row[f"label_date_{i}"] = d
        for i in range(len(forward) + 1, 4):
            row[f"price_T{i}"] = np.nan
            row[f"fwd_{i}d"] = np.nan
            row[f"label_date_{i}"] = ""
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
        "scan_date": scan_date,
        "n_rows": len(out),
        "forward_snapshots": forward,
        "n_fwd_3d_valid": int(out["fwd_3d"].notna().sum()) if "fwd_3d" in out else 0,
    }
    (LABELS_DIR / f"{scan_date}_fwd.meta.json").write_text(
        json.dumps(meta, indent=2), encoding="utf-8")
    print(f"[labels] {scan_date}: {len(out)} rows, forward={forward} -> {path.name}")
    return path


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--scan-date", default=None,
                    help="Backfill one scan date; default = all feature dates")
    args = ap.parse_args()
    dates = snapshot_dates()
    if args.scan_date:
        p = backfill_one(args.scan_date, dates)
        if p is not None:
            print(f"[labels] refresh scan.md with fwd cols: "
                  f"python -m src.score_engine --date {args.scan_date} --skip-features")
        return
    feat_dates = sorted(p.stem.replace("_1d", "") for p in FEATURES_DIR.glob("*_1d.csv"))
    for d in feat_dates:
        p = backfill_one(d, dates)
        if p is not None:
            print(f"[labels] refresh scan.md with fwd cols: "
                  f"python -m src.score_engine --date {d} --skip-features")


if __name__ == "__main__":
    main()
