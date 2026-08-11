"""Deep labeling — decompose every stock in the Finviz universe into its
full segment tag bag ("what is it?"), and aggregate each segment's stats
("what kind of market is this?").

Labels are assigned ONLY from columns already present in the daily Finviz
snapshot, using bin edges from 00_grounding/segments.json (the registry —
retune thresholds there, not here). Families whose source columns are not in
the current export (52-week fib zones, earnings proximity) are emitted as
<family>:unknown and listed in the report's coverage section, so activating
them later is an export change, not a code change.

This is Step A of the label → regime → join design (see
00_grounding/regime_questionnaire.md for Step B). No backtesting here.

Outputs (per snapshot date):
  data/universe/<date>_membership.csv    one row per ticker, one column per
                                         family, themes pipe-joined
  data/universe/<date>_segment_stats.csv one row per segment_id: n, breadth,
                                         median momentum/RSI/beta/short,
                                         pct profitable, optional joins to
                                         score_engine scores / 1d returns
  01_daily/<date>_universe.md            human coverage + distribution report

CLI:
  python -m src.segments                # latest snapshot
  python -m src.segments --date 2026-08-10
  python -m src.segments --all          # backfill every snapshot date
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd

from . import config
from .finviz_delta import SNAPSHOT_DIR, _add_catalyst_flags, load_snapshot

UNIVERSE_DIR = config.DATA / "universe"
REGISTRY_PATH = config.GROUNDING / "segments.json"

FAMILY_COLS = ["sector", "industry", "size", "index", "geo", "beta", "short",
               "liq", "rvol", "vol", "profit", "lev", "style", "mom", "ext",
               "range", "earn"]


def _load_registry() -> dict:
    return json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))


def _bin(value: pd.Series, bins: list) -> pd.Series:
    """Vectorized bin assignment; NaN -> 'unknown'."""
    out = pd.Series("unknown", index=value.index)
    for label, lo, hi in bins:
        m = pd.Series(True, index=value.index)
        if lo is not None:
            m &= value >= lo
        if hi is not None:
            m &= value < hi
        out = out.where(~(m & value.notna()), label)
    return out


def assign_membership(df: pd.DataFrame, registry: dict) -> pd.DataFrame:
    """df: normalized snapshot frame. Returns membership DataFrame keyed by
    Ticker with one column per family + themes."""
    fam = registry["families"]
    m = pd.DataFrame(index=df.index)
    m["Ticker"] = df["Ticker"]

    m["sector"] = df.get("Sector", pd.Series("unknown", index=df.index)).fillna("unknown")
    m["industry"] = df.get("Industry", pd.Series("unknown", index=df.index)).fillna("unknown")

    m["size"] = _bin(df.get("Market Cap", pd.Series(np.nan, index=df.index))
                     * fam["size"].get("scale", 1),
                     fam["size"]["bins"])

    idx_map = fam["index"]["map"]
    def _index_tags(v: object) -> str:
        tags = [idx_map[t.strip()] for t in str(v).split(",")
                if t.strip() in idx_map]
        return "|".join(tags) if tags else fam["index"]["none_value"]
    m["index"] = df.get("Index", pd.Series("-", index=df.index)).map(_index_tags)

    country = df.get("Country", pd.Series("", index=df.index)).fillna("")
    domestic = fam["geo"]["domestic"]
    m["geo"] = np.where(country == domestic, "US",
                        "ADR-" + country.where(country != "", "unknown"))

    m["beta"] = _bin(df.get("Beta", pd.Series(np.nan, index=df.index)),
                     fam["beta"]["bins"])
    m["short"] = _bin(df.get("Short Float", pd.Series(np.nan, index=df.index)),
                      fam["short"]["bins"])

    dollar_adv = (df.get("Price", pd.Series(np.nan, index=df.index))
                  * df.get("Average Volume", pd.Series(np.nan, index=df.index))
                  * fam["liq"].get("avg_volume_scale", 1))
    m["liq"] = _bin(dollar_adv, fam["liq"]["bins"])

    m["rvol"] = _bin(df.get("Relative Volume", pd.Series(np.nan, index=df.index)),
                     fam["rvol"]["bins"])

    atr_pct = (df.get("Average True Range", pd.Series(np.nan, index=df.index))
               / df.get("Price", pd.Series(np.nan, index=df.index)) * 100)
    m["vol"] = _bin(atr_pct.replace([np.inf, -np.inf], np.nan),
                    fam["vol"]["bins"])

    m["profit"] = _bin(df.get("Profit Margin", pd.Series(np.nan, index=df.index)),
                       fam["profit"]["bins"])

    de = df.get("Total Debt/Equity", pd.Series(np.nan, index=df.index))
    lev = _bin(de.where(de >= 0), fam["lev"]["bins"])
    m["lev"] = np.where(de < 0, fam["lev"]["negative_value"], lev)

    sales = df.get("Sales Year Over Year TTM", pd.Series(np.nan, index=df.index))
    epsg = df.get("EPS Growth Next Year", pd.Series(np.nan, index=df.index))
    fpe = df.get("Forward P/E", pd.Series(np.nan, index=df.index))
    growth = (sales >= 15) | (epsg >= 20)
    value = (fpe <= 15) & (sales < 10)
    m["style"] = np.where(growth, "growth", np.where(value, "value", "blend"))
    m["style"] = pd.Series(m["style"], index=df.index).where(
        ~(sales.isna() & epsg.isna() & fpe.isna()), "unknown")

    sma50 = df.get("50-Day Simple Moving Average", pd.Series(np.nan, index=df.index))
    sma200 = df.get("200-Day Simple Moving Average", pd.Series(np.nan, index=df.index))
    mom = np.where((sma50 > 0) & (sma200 > 0), "uptrend",
                   np.where((sma50 < 0) & (sma200 < 0), "downtrend", "mixed"))
    m["mom"] = pd.Series(mom, index=df.index).where(
        ~(sma50.isna() | sma200.isna()), "unknown")

    pw = df.get("Performance (Week)", pd.Series(np.nan, index=df.index))
    pm = df.get("Performance (Month)", pd.Series(np.nan, index=df.index))
    rsi = df.get("Relative Strength Index (14)", pd.Series(np.nan, index=df.index))
    extreme = (pw >= 100) | (sma50 >= 40)
    extended = (pw >= 40) | (rsi >= 75)
    washed = (pm <= -25) | (rsi <= 30)
    ext = np.where(extreme, "extreme",
                   np.where(extended, "extended",
                            np.where(washed, "washed", "neutral")))
    m["ext"] = pd.Series(ext, index=df.index).where(
        ~(pw.isna() & pm.isna() & rsi.isna() & sma50.isna()), "unknown")

    # --- fib 52w zones: only if the export carries the source columns ---
    if "52-Week High" in df.columns and "52-Week Low" in df.columns:
        hi_d = df["52-Week High"] / 100.0   # % distance below high (<=0)
        lo_d = df["52-Week Low"] / 100.0    # % above low (>=0)
        price = df.get("Price", pd.Series(np.nan, index=df.index))
        h52 = price / (1 + hi_d)
        l52 = price / (1 + lo_d)
        x = (price - l52) / (h52 - l52)
        x = x.replace([np.inf, -np.inf], np.nan)
        rng = _bin(x, fam["range"]["zones"])
        m["range"] = np.where(hi_d >= 0, fam["range"]["breakout_value"], rng)
    else:
        m["range"] = "unknown"

    # --- earnings proximity: only if the export carries Earnings Date ---
    if "Earnings Date" in df.columns:
        ed = pd.to_datetime(df["Earnings Date"], errors="coerce")
        today = pd.Timestamp.now(tz="America/New_York").normalize().tz_localize(None)
        delta = (ed.dt.normalize() - today).dt.days
        m["earn"] = np.where(delta <= 0, "today",
                             np.where(delta <= 7, "this_week", "later"))
        m["earn"] = pd.Series(m["earn"], index=df.index).where(ed.notna(), "unknown")
    else:
        m["earn"] = "unknown"

    theme_cols = [c for c in df.columns if c.startswith("cat_")]
    def _themes(row) -> str:
        tags = [f"theme:{c[4:]}" for c in theme_cols if bool(row.get(c))]
        return "|".join(tags)
    m["themes"] = df.apply(_themes, axis=1) if theme_cols else ""
    m["n_themes"] = m["themes"].map(lambda s: 0 if not s else s.count("|") + 1)

    return m


def segment_stats(df: pd.DataFrame, mem: pd.DataFrame,
                  scores: pd.DataFrame | None,
                  features: pd.DataFrame | None) -> pd.DataFrame:
    """One row per segment_id across all families (incl. industry + themes)."""
    j = df.set_index("Ticker").join(mem.set_index("Ticker"), rsuffix="_m")
    if scores is not None and "total_score" in scores.columns:
        j = j.join(scores.set_index("Ticker")[["total_score"]])
    if features is not None and "true_ret" in features.columns:
        j = j.join(features.set_index("Ticker")[["true_ret"]])

    rows = []

    def _add(family: str, value: str, mask: pd.Series) -> None:
        if not value or value == "unknown" or value != value:
            return
        sub = j[mask]
        n = len(sub)
        if n == 0:
            return
        row = {
            "segment_id": f"{family}:{value}",
            "family": family,
            "value": value,
            "n": n,
            "pct_universe": round(n / len(j) * 100, 2),
            "median_perf_week": float(sub["Performance (Week)"].median())
                if "Performance (Week)" in sub else np.nan,
            "median_perf_month": float(sub["Performance (Month)"].median())
                if "Performance (Month)" in sub else np.nan,
            "pct_above_50dma": float((sub["50-Day Simple Moving Average"] > 0).mean() * 100)
                if "50-Day Simple Moving Average" in sub else np.nan,
            "median_rsi": float(sub["Relative Strength Index (14)"].median())
                if "Relative Strength Index (14)" in sub else np.nan,
            "median_beta": float(sub["Beta"].median()) if "Beta" in sub else np.nan,
            "median_short_float": float(sub["Short Float"].median())
                if "Short Float" in sub else np.nan,
            "pct_profitable": float((sub["Profit Margin"] > 0).mean() * 100)
                if "Profit Margin" in sub else np.nan,
            "median_dollar_adv": float(sub["_dollar_adv"].median())
                if "_dollar_adv" in sub else np.nan,
            "median_score": float(sub["total_score"].median())
                if "total_score" in sub else np.nan,
            "pct_score_pos": float((sub["total_score"] > 0).mean() * 100)
                if "total_score" in sub else np.nan,
            "median_true_ret_1d": float(sub["true_ret"].median())
                if "true_ret" in sub else np.nan,
        }
        rows.append(row)

    for c in FAMILY_COLS:
        if c == "index":
            continue  # exploded below with themes
        for value, grp in j.groupby(c):
            _add(c, str(value), j[c] == value)
    # multi-membership families: index + themes
    for col, family in (("index", "index"), ("themes", "themes")):
        exploded = j[col].astype(str).str.split("|").explode()
        exploded = exploded[exploded != ""]
        for value in exploded.unique():
            mask = j[col].astype(str).str.split("|").map(lambda xs: value in xs)
            _add(family, str(value), mask)

    out = pd.DataFrame(rows)
    return out.sort_values(["family", "n"], ascending=[True, False])


def _fmt_pct(x: float) -> str:
    return f"{x:.1f}%" if x == x else "n/a"


def write_report(date_str: str, df: pd.DataFrame, mem: pd.DataFrame,
                 stats: pd.DataFrame, registry: dict) -> Path:
    n = len(mem)
    L = [f"# Universe deep labeling — {date_str}", "",
         f"Every one of the **{n:,}** tickers in the Finviz snapshot, "
         f"decomposed into its segment tag bag. Labels answer *what is it?* — "
         f"whether today is good for a label is the regime engine's job "
         f"(see `00_grounding/regime_questionnaire.md`).", ""]

    L += ["## Coverage (per family)", "",
          "| Family | Labels seen | Unknown / inactive |",
          "|---|---|---|"]
    inactive = {k: v.get("status") for k, v in registry["families"].items()
                if v.get("status")}
    for c in FAMILY_COLS:
        unk = int((mem[c] == "unknown").sum())
        note = f"{unk:,} unknown ({unk / n * 100:.1f}%)"
        if c in inactive:
            note += f" — **INACTIVE**: {inactive[c]}"
        L.append(f"| {c} | {mem[c].nunique()} | {note} |")
    L.append("")

    show = [("size", "Size"), ("beta", "Beta"), ("short", "Short float"),
            ("liq", "Liquidity ($ADV)"), ("vol", "Vol regime (ATR%)"),
            ("profit", "Profitability"), ("lev", "Leverage"),
            ("style", "Style"), ("mom", "Momentum trend"), ("ext", "Extension"),
            ("rvol", "Relative volume"), ("geo", "Geography"),
            ("index", "Index membership"), ("sector", "Sector")]
    for col, title in show:
        vc = (mem[col] if col != "index"
              else mem[col].astype(str).str.split("|").explode()).value_counts()
        L.append(f"### {title}")
        L.append("")
        L.append("| Label | Names | % |")
        L.append("|---|---|---|")
        for v, cnt in vc.items():
            L.append(f"| {v} | {cnt:,} | {cnt / n * 100:.1f}% |")
        L.append("")

    ind = stats[stats["family"] == "industry"].copy()
    if len(ind):
        big = ind[ind["n"] >= 20]
        hot = big.nlargest(12, "median_perf_week")
        cold = big.nsmallest(12, "median_perf_week")
        L += ["### Hottest industries (median week perf, n≥20)", "",
              "| Industry | n | Median wk | Median mo | % above 50DMA | "
              "Median score |", "|---|---|---|---|---|---|"]
        for _, r in hot.iterrows():
            L.append(f"| {r['value']} | {r['n']:,} | "
                     f"{_fmt_pct(r['median_perf_week'])} | "
                     f"{_fmt_pct(r['median_perf_month'])} | "
                     f"{_fmt_pct(r['pct_above_50dma'])} | "
                     f"{r['median_score']:.2f} |" if r["median_score"] == r["median_score"]
                     else f"| {r['value']} | {r['n']:,} | "
                     f"{_fmt_pct(r['median_perf_week'])} | "
                     f"{_fmt_pct(r['median_perf_month'])} | "
                     f"{_fmt_pct(r['pct_above_50dma'])} | — |")
        L += ["", "### Coldest industries (median week perf, n≥20)", "",
              "| Industry | n | Median wk | Median mo | % above 50DMA | "
              "Median score |", "|---|---|---|---|---|---|"]
        for _, r in cold.iterrows():
            L.append(f"| {r['value']} | {r['n']:,} | "
                     f"{_fmt_pct(r['median_perf_week'])} | "
                     f"{_fmt_pct(r['median_perf_month'])} | "
                     f"{_fmt_pct(r['pct_above_50dma'])} | "
                     f"{r['median_score']:.2f} |" if r["median_score"] == r["median_score"]
                     else f"| {r['value']} | {r['n']:,} | "
                     f"{_fmt_pct(r['median_perf_week'])} | "
                     f"{_fmt_pct(r['median_perf_month'])} | "
                     f"{_fmt_pct(r['pct_above_50dma'])} | — |")
        L.append("")

    themes = stats[stats["family"] == "themes"]
    if len(themes):
        L += ["### Theme tags", "",
              "| Theme | Names | Median wk | Median score |",
              "|---|---|---|---|"]
        for _, r in themes.iterrows():
            sc = f"{r['median_score']:.2f}" if r["median_score"] == r["median_score"] else "—"
            L.append(f"| {r['value']} | {r['n']:,} | "
                     f"{_fmt_pct(r['median_perf_week'])} | {sc} |")
        L.append("")

    config.DAILY.mkdir(parents=True, exist_ok=True)
    path = config.DAILY / f"{date_str}_universe.md"
    path.write_text("\n".join(L) + "\n", encoding="utf-8")
    return path


def run(date_str: str, registry: dict) -> None:
    snap = SNAPSHOT_DIR / f"{date_str}.csv"
    if not snap.exists():
        print(f"[segments] no snapshot {snap} — skip")
        return
    df = _add_catalyst_flags(load_snapshot(snap))
    df["_dollar_adv"] = (
        df.get("Price", pd.Series(np.nan, index=df.index))
        * df.get("Average Volume", pd.Series(np.nan, index=df.index))
        * registry["families"]["liq"].get("avg_volume_scale", 1))
    mem = assign_membership(df, registry)

    scores = None
    sp = config.DATA / "scores" / f"{date_str}_1d.csv"
    if sp.exists():
        scores = pd.read_csv(sp, low_memory=False)
    features = None
    fp = config.DATA / "features" / f"{date_str}_1d.csv"
    if fp.exists():
        features = pd.read_csv(fp, low_memory=False)

    stats = segment_stats(df, mem, scores, features)

    UNIVERSE_DIR.mkdir(parents=True, exist_ok=True)
    mem_path = UNIVERSE_DIR / f"{date_str}_membership.csv"
    stats_path = UNIVERSE_DIR / f"{date_str}_segment_stats.csv"
    mem.to_csv(mem_path, index=False)
    stats.to_csv(stats_path, index=False)
    rep = write_report(date_str, df, mem, stats, registry)
    print(f"[segments] {date_str}: {len(mem):,} tickers labeled, "
          f"{len(stats)} segments -> {mem_path.name}, {stats_path.name}, "
          f"{rep.name}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", default=None)
    ap.add_argument("--all", action="store_true")
    args = ap.parse_args()
    registry = _load_registry()
    if args.all:
        for p in sorted(SNAPSHOT_DIR.glob("????-??-??.csv")):
            run(p.stem, registry)
        return
    date_str = args.date
    if not date_str:
        dates = sorted(p.stem for p in SNAPSHOT_DIR.glob("????-??-??.csv"))
        if not dates:
            raise SystemExit("[segments] no snapshots found")
        date_str = dates[-1]
    run(date_str, registry)


if __name__ == "__main__":
    main()
