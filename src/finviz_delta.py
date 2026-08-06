"""Finviz snapshot delta engine.

Design
------
Always keep TWO universe snapshots on disk, about one month apart:

  data/snapshots/current.csv   ← newest Finviz export
  data/snapshots/previous.csv  ← prior export (~30 days older)

Optional archive:
  data/snapshots/archive/finviz_YYYY-MM-DD.csv

The *delta* between them is the high-signal layer for Theme Radar:
  - which industries accelerated
  - which tickers newly entered strong momentum
  - institutional / insider flow shifts
  - short-float changes
  - valuation (target upside) shifts
  - new names appearing in the universe

Pipeline stages that consume delta:
  Stage 1 Discovery  → industry acceleration + news-keyword clusters
  Stage 2 Trigger    → names whose catalysts / flows flipped recently
  Stage 3 Scoring    → institutional_tx_delta, short_float_delta as
                       validation / kill-switch inputs
  Buy-list ranking   → prefer names with positive flow + accelerating perf
"""
from __future__ import annotations

from pathlib import Path
from typing import Optional

import numpy as np
import pandas as pd

from . import config

SNAPSHOT_DIR = config.DATA / "snapshots"
CURRENT = SNAPSHOT_DIR / "current.csv"
PREVIOUS = SNAPSHOT_DIR / "previous.csv"
ARCHIVE = SNAPSHOT_DIR / "archive"

DELTA_NUMERIC = [
    "Market Cap", "Price", "Average Volume", "Short Float", "Short Ratio",
    "Institutional Transactions", "Institutional Ownership",
    "Insider Transactions", "Insider Ownership",
    "Analyst Recom", "Target Price",
    "Performance (Week)", "Performance (Month)", "Performance (Quarter)",
    "Performance (Half Year)", "Performance (YTD)", "Performance (Year)",
    "Relative Volume", "Relative Strength Index (14)",
    "Sales Year Over Year TTM", "Sales Growth Quarter Over Quarter",
    "EPS Surprise", "Revenue Surprise",
    "Gross Margin", "Operating Margin",
    "20-Day Simple Moving Average", "50-Day Simple Moving Average",
    "200-Day Simple Moving Average",
]

META = [
    "Ticker", "Company", "Industry", "Sector", "Country", "Exchange",
    "Index", "Finviz_Description", "News Title", "Daily Digest", "News Time",
]


def _to_float(s):
    if pd.isna(s):
        return np.nan
    if isinstance(s, (int, float)):
        return float(s)
    try:
        return float(str(s).replace("%", "").replace(",", "").strip())
    except ValueError:
        return np.nan


def normalize_frame(df: pd.DataFrame) -> pd.DataFrame:
    """Standardize a raw Finviz export for delta use."""
    keep = [c for c in META + DELTA_NUMERIC if c in df.columns]
    out = df[keep].copy()
    out = out[out["Ticker"].notna()]
    out["Ticker"] = out["Ticker"].astype(str).str.upper().str.strip()
    for c in DELTA_NUMERIC:
        if c in out.columns:
            out[c] = out[c].map(_to_float)
    if "Finviz_Description" in out.columns:
        out["Finviz_Description"] = (
            out["Finviz_Description"].fillna("").astype(str).str.slice(0, 550)
        )
    return out.drop_duplicates(subset=["Ticker"], keep="first")


def load_snapshot(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(path)
    return normalize_frame(pd.read_csv(path, low_memory=False))


def load_current_previous() -> tuple[pd.DataFrame, Optional[pd.DataFrame]]:
    if not CURRENT.exists():
        from .finviz_mapper import _load_universe
        cur = normalize_frame(_load_universe())
        return cur, None
    cur = load_snapshot(CURRENT)
    prev = load_snapshot(PREVIOUS) if PREVIOUS.exists() else None
    return cur, prev


def promote_snapshot(new_raw_path: Path, as_of: str | None = None) -> None:
    """Install a new Finviz export as current; shift old current → previous."""
    SNAPSHOT_DIR.mkdir(parents=True, exist_ok=True)
    ARCHIVE.mkdir(parents=True, exist_ok=True)

    new_df = normalize_frame(pd.read_csv(new_raw_path, low_memory=False))

    if CURRENT.exists():
        if PREVIOUS.exists():
            PREVIOUS.unlink()
        CURRENT.rename(PREVIOUS)

    new_df.to_csv(CURRENT, index=False)
    if as_of:
        new_df.to_csv(ARCHIVE / f"finviz_{as_of}.csv", index=False)


def compute_delta(
    current: pd.DataFrame,
    previous: pd.DataFrame | None,
) -> pd.DataFrame:
    """Ticker-level delta. If no previous, returns current with NaN deltas."""
    cur = current.set_index("Ticker", drop=False)
    if previous is None:
        out = cur.copy()
        for c in DELTA_NUMERIC:
            if c in out.columns:
                out[f"d_{c}"] = np.nan
        out["is_new"] = False
        out["upside_pct"] = _upside(out)
        return out.reset_index(drop=True)

    prev = previous.set_index("Ticker", drop=False)
    all_tickers = cur.index.union(prev.index)
    rows = []
    for t in all_tickers:
        in_cur = t in cur.index
        in_prev = t in prev.index
        if in_cur:
            row = cur.loc[t].copy()
            if isinstance(row, pd.DataFrame):
                row = row.iloc[0]
            row = row.to_dict()
            row["is_new"] = not in_prev
            if in_prev:
                prow = prev.loc[t]
                if isinstance(prow, pd.DataFrame):
                    prow = prow.iloc[0]
                for c in DELTA_NUMERIC:
                    if c in cur.columns and c in prev.columns:
                        row[f"d_{c}"] = _safe_sub(row.get(c), prow.get(c))
            else:
                for c in DELTA_NUMERIC:
                    row[f"d_{c}"] = np.nan
            rows.append(row)

    out = pd.DataFrame(rows)
    out["upside_pct"] = _upside(out)
    return out


def _safe_sub(a, b):
    try:
        if pd.isna(a) or pd.isna(b):
            return np.nan
        return float(a) - float(b)
    except (TypeError, ValueError):
        return np.nan


def _upside(df: pd.DataFrame) -> pd.Series:
    if "Target Price" not in df.columns or "Price" not in df.columns:
        return pd.Series(np.nan, index=df.index)
    return (df["Target Price"] - df["Price"]) / df["Price"] * 100


def industry_acceleration(delta: pd.DataFrame, min_names: int = 6) -> pd.DataFrame:
    """Industry-level view: median performance + median d_Performance (Month)."""
    if delta.empty:
        return delta
    g = delta.groupby("Industry").agg(
        n=("Ticker", "count"),
        med_month=("Performance (Month)", "median"),
        med_quarter=("Performance (Quarter)", "median"),
        med_d_month=("d_Performance (Month)", "median"),
        med_d_inst=("d_Institutional Transactions", "median"),
        med_inst_tx=("Institutional Transactions", "median"),
        med_short=("Short Float", "median"),
    )
    g = g[g["n"] >= min_names].sort_values("med_month", ascending=False)
    return g


def accelerating_tickers(
    delta: pd.DataFrame,
    min_d_month: float = 10.0,
    min_month: float = 5.0,
    min_mcap: float = 100.0,
    min_adv: float = 200.0,
) -> pd.DataFrame:
    """Names whose Month performance improved vs prior snapshot and are still liquid."""
    d = delta.copy()
    d = d[
        (d["Market Cap"].fillna(0) >= min_mcap)
        & (d["Average Volume"].fillna(0) >= min_adv)
        & (d["Performance (Month)"].fillna(-999) >= min_month)
    ]
    if "d_Performance (Month)" in d.columns:
        d = d[d["d_Performance (Month)"].fillna(-999) >= min_d_month]
    return d.sort_values("Performance (Month)", ascending=False)


def flow_improvers(delta: pd.DataFrame, min_d_inst: float = 1.0) -> pd.DataFrame:
    """Institutional Transactions improved vs prior month."""
    if "d_Institutional Transactions" not in delta.columns:
        return delta.iloc[0:0]
    d = delta[delta["d_Institutional Transactions"].fillna(-999) >= min_d_inst]
    return d.sort_values("d_Institutional Transactions", ascending=False)


def format_delta_brief(delta: pd.DataFrame, top_industries: int = 12) -> str:
    """Compact text block injectable into the LLM as Channel 1."""
    lines = ["=== FINVIZ DELTA (current vs previous snapshot) ===", ""]
    if "d_Performance (Month)" not in delta.columns or delta["d_Performance (Month)"].isna().all():
        lines.append("(No previous snapshot — delta unavailable. Using current levels only.)")
        lines.append("")
    else:
        ind = industry_acceleration(delta).head(top_industries)
        lines.append("Top industries by median Month performance / acceleration:")
        lines.append(
            f"{'Industry':<40} {'n':>4} {'MedM%':>7} {'dMedM':>7} {'InstTx':>7}"
        )
        for name, r in ind.iterrows():
            lines.append(
                f"{str(name)[:40]:<40} {int(r['n']):>4} "
                f"{r['med_month']:>7.1f} {r['med_d_month']:>7.1f} "
                f"{r['med_inst_tx']:>7.1f}"
            )
        lines.append("")

        acc = accelerating_tickers(delta).head(15)
        if not acc.empty:
            lines.append("Accelerating liquid tickers (Month up & improved vs prior):")
            for _, r in acc.iterrows():
                lines.append(
                    f"  {r['Ticker']:<6} {str(r.get('Industry',''))[:28]:<28} "
                    f"M={r.get('Performance (Month)', float('nan')):>6.1f} "
                    f"dM={r.get('d_Performance (Month)', float('nan')):>6.1f} "
                    f"dInst={r.get('d_Institutional Transactions', float('nan')):>5.1f}"
                )
            lines.append("")

        flows = flow_improvers(delta).head(10)
        if not flows.empty:
            lines.append("Largest institutional-transaction improvements:")
            for _, r in flows.iterrows():
                lines.append(
                    f"  {r['Ticker']:<6} dInstTx={r.get('d_Institutional Transactions', float('nan')):>5.1f} "
                    f"InstTx={r.get('Institutional Transactions', float('nan')):>5.1f} "
                    f"{str(r.get('Industry',''))[:30]}"
                )
            lines.append("")

    lines.append(f"Universe size (current): {len(delta)} tickers")
    return "\n".join(lines)
