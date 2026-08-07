"""Finviz dual-snapshot engine — full resource extraction.

Always keep two exports ~one month apart:
  data/snapshots/current.csv
  data/snapshots/previous.csv

Extracted layers (all feed Channel 1 / scoring):
  1. Catalyst text       — Daily Digest + News Title keyword hits
  2. Industry breadth    — % of names green on Month/Quarter, median RSI
  3. Acceleration        — d_Performance across Week/Month/Quarter/YTD
  4. Smart-money flows   — d_Institutional / d_Insider Transactions
  5. Crowding            — d_Short Float, Short Ratio
  6. Technical structure — RSI, % vs 20/50/200 DMA, Relative Volume
  7. Fundamentals        — Sales YoY/QoQ, EPS/Revenue surprise, margins
  8. Valuation           — upside-to-target, Forward P/E, EV/Sales shifts
  9. Cross-section ranks — percentile within industry + rank change
 10. New listings        — is_new flag
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
    "Analyst Recom", "Target Price", "Forward P/E", "EV/Sales", "PEG",
    "Performance (Week)", "Performance (Month)", "Performance (Quarter)",
    "Performance (Half Year)", "Performance (YTD)", "Performance (Year)",
    "Relative Volume", "Relative Strength Index (14)",
    "Sales Year Over Year TTM", "Sales Growth Quarter Over Quarter",
    "EPS Surprise", "Revenue Surprise",
    "Gross Margin", "Operating Margin", "Profit Margin",
    "20-Day Simple Moving Average", "50-Day Simple Moving Average",
    "200-Day Simple Moving Average",
    "EPS Growth This Year", "EPS Growth Next Year",
    # added for scoring engine (levels only; deltas computed when present)
    "Beta", "Volume", "Average True Range",
    "Volatility (Week)", "Volatility (Month)",
    "Total Debt/Equity", "Current Ratio",
]

META = [
    "Ticker", "Company", "Industry", "Sector", "Country", "Exchange",
    "Index", "Finviz_Description", "News Title", "Daily Digest", "News Time",
]

CATALYST_PATTERNS: dict[str, str] = {
    "nuclear_smr": r"nuclear|smr|small modular|uranium|reactor|\boklo\b|cameco",
    "optics_transceiver": r"optical|transceiver|photonic|coherent optics|lumentum|fiber.?optic|laser diode",
    "data_center_power": r"data.?center|datacenter|transformer|grid congestion|electrification|ge vernova|vertiv|power shortage",
    "hbm_memory": r"\bhbm\b|high.?bandwidth|dram|nand|memory shortage|sk hynix",
    "copper_metals": r"\bcopper\b|lithium|rare earth|critical mineral|cobalt",
    "ai_capex": r"ai capex|hyperscaler|ai infrastructure|gpu cluster|nvidia.*order|broadcom.*ai",
    "defense": r"\bdefense\b|missile|naval nuclear|pentagon|rearmament|munition",
    "semiconductor_equip": r"wafer|euv|lithography|semiconductor equipment|asml|applied materials",
}


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
    keep = [c for c in META + DELTA_NUMERIC if c in df.columns]
    out = df[keep].copy()
    out = out[out["Ticker"].notna()]
    out["Ticker"] = out["Ticker"].astype(str).str.upper().str.strip()
    for c in DELTA_NUMERIC:
        if c in out.columns:
            out[c] = out[c].map(_to_float)
    if "Finviz_Description" in out.columns:
        out["Finviz_Description"] = (
            out["Finviz_Description"].fillna("").astype(str).str.slice(0, 600)
        )
    for c in ("News Title", "Daily Digest"):
        if c in out.columns:
            out[c] = out[c].fillna("").astype(str)
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
    cur = current.set_index("Ticker", drop=False)
    if previous is None:
        out = cur.copy()
        for c in DELTA_NUMERIC:
            if c in out.columns:
                out[f"d_{c}"] = np.nan
        out["is_new"] = False
        out["upside_pct"] = _upside(out)
        out = _add_catalyst_flags(out)
        out = _add_cross_section_ranks(out)
        return out.reset_index(drop=True)

    prev = previous.set_index("Ticker", drop=False)
    rows = []
    for t in cur.index.unique():
        row = cur.loc[t]
        if isinstance(row, pd.DataFrame):
            row = row.iloc[0]
        row = row.to_dict()
        row["is_new"] = t not in prev.index
        if t in prev.index:
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
    out = _add_catalyst_flags(out)
    out = _add_cross_section_ranks(out)
    if previous is not None and "Performance (Month)" in previous.columns:
        prev_rank = previous.copy()
        prev_rank["_rm"] = prev_rank.groupby("Industry")["Performance (Month)"].rank(pct=True)
        prev_map = prev_rank.set_index("Ticker")["_rm"].to_dict()
        out["d_rank_month"] = out["rank_month"] - out["Ticker"].map(prev_map)
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
        return pd.Series(np.nan, index=df.index if hasattr(df, "index") else range(len(df)))
    return (df["Target Price"] - df["Price"]) / df["Price"] * 100


def _add_catalyst_flags(df: pd.DataFrame) -> pd.DataFrame:
    blob = (
        df.get("Daily Digest", pd.Series("", index=df.index)).fillna("").astype(str)
        + " "
        + df.get("News Title", pd.Series("", index=df.index)).fillna("").astype(str)
        + " "
        + df.get("Finviz_Description", pd.Series("", index=df.index)).fillna("").astype(str)
    ).str.lower()
    for name, pat in CATALYST_PATTERNS.items():
        df[f"cat_{name}"] = blob.str.contains(pat, regex=True, na=False)
    return df


def _add_cross_section_ranks(df: pd.DataFrame) -> pd.DataFrame:
    if "Performance (Month)" in df.columns and "Industry" in df.columns:
        df["rank_month"] = df.groupby("Industry")["Performance (Month)"].rank(pct=True)
    if "Performance (Quarter)" in df.columns and "Industry" in df.columns:
        df["rank_quarter"] = df.groupby("Industry")["Performance (Quarter)"].rank(pct=True)
    return df


def industry_dashboard(delta: pd.DataFrame, min_names: int = 8) -> pd.DataFrame:
    def pct_pos(s):
        s = s.dropna()
        return (s > 0).mean() * 100 if len(s) else np.nan

    def pct_above(s):
        s = s.dropna()
        return (s > 0).mean() * 100 if len(s) else np.nan

    agg = {
        "n": ("Ticker", "count"),
        "breadth_M": ("Performance (Month)", pct_pos),
        "med_M": ("Performance (Month)", "median"),
        "med_Q": ("Performance (Quarter)", "median"),
        "med_RSI": ("Relative Strength Index (14)", "median"),
        "pct_above_50": ("50-Day Simple Moving Average", pct_above),
        "med_short": ("Short Float", "median"),
        "med_sales_yoy": ("Sales Year Over Year TTM", "median"),
        "med_inst_tx": ("Institutional Transactions", "median"),
    }
    if "d_Performance (Month)" in delta.columns:
        agg["med_d_M"] = ("d_Performance (Month)", "median")
    if "d_Institutional Transactions" in delta.columns:
        agg["med_d_inst"] = ("d_Institutional Transactions", "median")

    g = delta.groupby("Industry").agg(**{k: v for k, v in agg.items() if v[0] in delta.columns})
    g = g[g["n"] >= min_names].sort_values("breadth_M", ascending=False)
    return g


def catalyst_summary(delta: pd.DataFrame) -> list[str]:
    lines = []
    for name in CATALYST_PATTERNS:
        col = f"cat_{name}"
        if col not in delta.columns:
            continue
        hits = delta[delta[col]]
        n = len(hits)
        if n == 0:
            continue
        top = hits.nlargest(5, "Performance (Month)") if "Performance (Month)" in hits.columns else hits.head(5)
        tickers = ",".join(top["Ticker"].tolist())
        lines.append(f"  {name}: {n} names | leaders: {tickers}")
    return lines


def technical_stress(delta: pd.DataFrame) -> list[str]:
    lines = []
    if "Sector" not in delta.columns:
        return lines
    for sector, g in delta.groupby("Sector"):
        n = len(g)
        if n < 20:
            continue
        rsi = g["Relative Strength Index (14)"].median() if "Relative Strength Index (14)" in g else np.nan
        above50 = (g["50-Day Simple Moving Average"] > 0).mean() * 100 if "50-Day Simple Moving Average" in g else np.nan
        rvol = g["Relative Volume"].median() if "Relative Volume" in g else np.nan
        lines.append(
            f"  {sector:<22} n={n:<4} medRSI={rsi:>5.1f}  above50DMA={above50:>5.1f}%  medRVol={rvol:>4.2f}"
        )
    return lines


def accelerating_tickers(
    delta: pd.DataFrame,
    min_d_month: float = 8.0,
    min_month: float = 5.0,
    min_mcap: float = 100.0,
    min_adv: float = 200.0,
) -> pd.DataFrame:
    d = delta.copy()
    d = d[
        (d["Market Cap"].fillna(0) >= min_mcap)
        & (d["Average Volume"].fillna(0) >= min_adv)
        & (d["Performance (Month)"].fillna(-999) >= min_month)
    ]
    if "d_Performance (Month)" in d.columns and d["d_Performance (Month)"].notna().any():
        d = d[d["d_Performance (Month)"].fillna(-999) >= min_d_month]
    return d.sort_values("Performance (Month)", ascending=False)


def flow_improvers(delta: pd.DataFrame, min_d_inst: float = 1.0) -> pd.DataFrame:
    if "d_Institutional Transactions" not in delta.columns:
        return delta.iloc[0:0]
    d = delta[delta["d_Institutional Transactions"].fillna(-999) >= min_d_inst]
    return d.sort_values("d_Institutional Transactions", ascending=False)


def valuation_stretched(delta: pd.DataFrame, min_ytd: float = 100.0) -> pd.DataFrame:
    d = delta.copy()
    if "upside_pct" not in d.columns or "Performance (YTD)" not in d.columns:
        return d.iloc[0:0]
    return d[
        (d["Performance (YTD)"].fillna(0) >= min_ytd)
        & (d["upside_pct"].fillna(0) < 0)
    ].sort_values("Performance (YTD)", ascending=False)


def relative_volume_spikes(delta: pd.DataFrame, min_rvol: float = 2.0) -> pd.DataFrame:
    if "Relative Volume" not in delta.columns:
        return delta.iloc[0:0]
    d = delta[delta["Relative Volume"].fillna(0) >= min_rvol]
    return d.sort_values("Relative Volume", ascending=False)


def format_delta_brief(delta: pd.DataFrame, top_industries: int = 15) -> str:
    lines = [
        "=== FINVIZ CHANNEL 1 (universe snapshot + delta) ===",
        f"Universe: {len(delta)} tickers",
        "",
    ]

    lines.append("--- Catalyst keyword hits (News Title + Daily Digest + Description) ---")
    cat_lines = catalyst_summary(delta)
    lines.extend(cat_lines if cat_lines else ["  (none matched)"])
    lines.append("")

    lines.append("--- Industry breadth (Month>0 share) + momentum / RSI / shorts / sales ---")
    try:
        ind = industry_dashboard(delta).head(top_industries)
        lines.append(f"{'Industry':<36} {'n':>4} {'BrdM%':>6} {'MedM':>6} {'MedQ':>6} {'RSI':>5} {'>50%':>5} {'Short':>5}")
        for name, r in ind.iterrows():
            lines.append(
                f"{str(name)[:36]:<36} {int(r['n']):>4} "
                f"{r.get('breadth_M', float('nan')):>6.1f} "
                f"{r.get('med_M', float('nan')):>6.1f} "
                f"{r.get('med_Q', float('nan')):>6.1f} "
                f"{r.get('med_RSI', float('nan')):>5.1f} "
                f"{r.get('pct_above_50', float('nan')):>5.1f} "
                f"{r.get('med_short', float('nan')):>5.1f}"
            )
    except Exception as e:  # noqa: BLE001
        lines.append(f"  (industry dashboard error: {e})")
    lines.append("")

    lines.append("--- Sector technical structure ---")
    lines.extend(technical_stress(delta) or ["  (n/a)"])
    lines.append("")

    has_delta = (
        "d_Performance (Month)" in delta.columns
        and delta["d_Performance (Month)"].notna().any()
    )
    if has_delta:
        lines.append("--- Acceleration vs previous snapshot ---")
        acc = accelerating_tickers(delta).head(12)
        for _, r in acc.iterrows():
            lines.append(
                f"  {r['Ticker']:<6} {str(r.get('Industry',''))[:26]:<26} "
                f"M={r.get('Performance (Month)', float('nan')):>6.1f} "
                f"dM={r.get('d_Performance (Month)', float('nan')):>6.1f} "
                f"dInst={r.get('d_Institutional Transactions', float('nan')):>5.1f} "
                f"RSI={r.get('Relative Strength Index (14)', float('nan')):>5.1f}"
            )
        lines.append("")
        flows = flow_improvers(delta).head(8)
        if not flows.empty:
            lines.append("Institutional-transaction improvers:")
            for _, r in flows.iterrows():
                lines.append(
                    f"  {r['Ticker']:<6} dInst={r.get('d_Institutional Transactions', float('nan')):>5.1f} "
                    f"{str(r.get('Industry',''))[:30]}"
                )
            lines.append("")
    else:
        lines.append("--- Delta ---")
        lines.append("(No previous snapshot yet — promote a second Finviz export to unlock acceleration/flow deltas.)")
        lines.append("")

    stretched = valuation_stretched(delta).head(8)
    if not stretched.empty:
        lines.append("--- Valuation stretched (YTD big + negative target upside) ---")
        for _, r in stretched.iterrows():
            lines.append(
                f"  {r['Ticker']:<6} YTD={r.get('Performance (YTD)', float('nan')):>6.1f} "
                f"upside={r.get('upside_pct', float('nan')):>6.1f}%  "
                f"{str(r.get('Industry',''))[:28]}"
            )
        lines.append("")

    spikes = relative_volume_spikes(delta).head(8)
    if not spikes.empty:
        lines.append("--- Relative volume spikes (>=2x) ---")
        for _, r in spikes.iterrows():
            lines.append(
                f"  {r['Ticker']:<6} RVol={r.get('Relative Volume', float('nan')):>5.2f} "
                f"W={r.get('Performance (Week)', float('nan')):>5.1f}  "
                f"{str(r.get('Industry',''))[:28]}"
            )
        lines.append("")

    lines.append(
        "Use this block as PRIMARY evidence of what is already moving, "
        "where breadth is real, where catalysts exist in text, and where "
        "valuation/extension kill switches are flashing. "
        "Supplement with web_search for dated macro/policy triggers only."
    )
    return "\n".join(lines)
