"""Simple market-wide composite residual ranker.

Uses Finviz snapshots only (no LLM). Goal: practical output we can iterate on.

For each ticker:
  - raw X buckets from the as-of snapshot
  - a few composites (SPEC_DURATION, QUALITY_DEFENSIVE, CROWDING, SIZE)
  - Y from universe breadth (risk-on proxy)
  - residual return vs median stock (market proxy)
  - pressure score = f(composites, Y)  [hand priors; audit later]

CLI:
  python -m src.composite_rank [--date YYYY-MM-DD]

Writes:
  01_daily/<date>_composite_rank.md
  data/composite/<date>_composite_rank.csv
  data/composite/<date>_y_snapshot.json
"""
from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd

from . import config
from .snapshots import load_dated, snapshot_dates

OUT_DIR = config.DATA / "composite"


def _num(s: pd.Series) -> pd.Series:
    return pd.to_numeric(s, errors="coerce")


def _mcap_bucket(mcap: float) -> str:
    if mcap != mcap or mcap is None:
        return "unknown"
    # Finviz often stores Market Cap in millions or as raw; handle both
    v = float(mcap)
    if v > 1e12:  # raw dollars
        v = v / 1e6
    if v < 300:
        return "micro"
    if v < 2000:
        return "small"
    if v < 10000:
        return "mid"
    if v < 100000:
        return "large"
    return "mega"


def _beta_bucket(b: float) -> str:
    if b != b:
        return "unknown"
    if b < 0.8:
        return "low"
    if b < 1.3:
        return "mid"
    return "high"


def _short_bucket(sf: float) -> str:
    if sf != sf:
        return "unknown"
    if sf < 5:
        return "low"
    if sf < 15:
        return "elevated"
    return "very_high"


def _mom_bucket(row: pd.Series) -> str:
    rsi = row.get("rsi")
    perf_w = row.get("perf_w")
    if rsi == rsi and rsi >= 70:
        return "extended"
    if rsi == rsi and rsi <= 30:
        return "washed"
    if perf_w == perf_w and perf_w >= 20:
        return "extended"
    if perf_w == perf_w and perf_w <= -20:
        return "washed"
    return "neutral"


def _index_bucket(idx) -> str:
    s = str(idx or "").upper()
    if "S&P 500" in s or "SPX" in s:
        return "SPX"
    if "NASDAQ 100" in s or "NDX" in s:
        return "NDX"
    if "RUT" in s or "RUSSELL 2000" in s:
        return "RUT"
    return "none"


def build_xy(cur: pd.DataFrame, prev: pd.DataFrame | None) -> tuple[pd.DataFrame, dict]:
    cur = cur.drop_duplicates(subset=["Ticker"], keep="first").copy()
    cur["Ticker"] = cur["Ticker"].astype(str).str.strip()

    price = _num(cur["Price"]) if "Price" in cur.columns else pd.Series(np.nan, index=cur.index)
    mcap = _num(cur["Market Cap"]) if "Market Cap" in cur.columns else pd.Series(np.nan, index=cur.index)
    beta = _num(cur["Beta"]) if "Beta" in cur.columns else pd.Series(np.nan, index=cur.index)
    short = _num(cur["Short Float"]) if "Short Float" in cur.columns else pd.Series(np.nan, index=cur.index)
    rsi = _num(cur["Relative Strength Index (14)"]) if "Relative Strength Index (14)" in cur.columns else pd.Series(np.nan, index=cur.index)
    perf_w = _num(cur["Performance (Week)"]) if "Performance (Week)" in cur.columns else pd.Series(np.nan, index=cur.index)
    debt = _num(cur["Total Debt/Equity"]) if "Total Debt/Equity" in cur.columns else pd.Series(np.nan, index=cur.index)
    pm = _num(cur["Profit Margin"]) if "Profit Margin" in cur.columns else pd.Series(np.nan, index=cur.index)
    eps = _num(cur["EPS (ttm)"]) if "EPS (ttm)" in cur.columns else pd.Series(np.nan, index=cur.index)

    # returns vs prior snapshot
    if prev is not None and "Price" in prev.columns:
        p = prev.drop_duplicates(subset=["Ticker"], keep="first").set_index("Ticker")
        prev_px = _num(p["Price"])
        ret = price.values / prev_px.reindex(cur["Ticker"].values).values - 1.0
        ret = pd.Series(ret, index=cur.index)
    else:
        ret = pd.Series(np.nan, index=cur.index)

    med_ret = float(np.nanmedian(ret.values)) if ret.notna().any() else 0.0
    resid = ret - med_ret

    pct_up = float((ret > 0).mean()) if ret.notna().any() else 0.5
    # crude risk-on probability from breadth
    p_risk_on = float(np.clip((pct_up - 0.35) / 0.40, 0.0, 1.0))

    y = {
        "p_risk_on": round(p_risk_on, 4),
        "pct_up": round(pct_up, 4),
        "median_ret": round(med_ret, 6),
        "n_universe": int(len(cur)),
        "conviction": round(abs(p_risk_on - 0.5) * 2, 4),
        "z_note": "price_derived breadth only (v1)",
    }

    rows = []
    for i, r in cur.iterrows():
        t = r["Ticker"]
        b_beta = _beta_bucket(beta.loc[i] if i in beta.index else np.nan)
        b_short = _short_bucket(short.loc[i] if i in short.index else np.nan)
        b_size = _mcap_bucket(mcap.loc[i] if i in mcap.index else np.nan)
        b_idx = _index_bucket(r.get("Index"))
        e = eps.loc[i] if i in eps.index else np.nan
        pvm = pm.loc[i] if i in pm.index else np.nan
        profitable = bool((e == e and e > 0) or (pvm == pvm and pvm > 0))
        mom = _mom_bucket(pd.Series({"rsi": rsi.loc[i] if i in rsi.index else np.nan,
                                     "perf_w": perf_w.loc[i] if i in perf_w.index else np.nan}))
        lev = "high" if (debt.loc[i] == debt.loc[i] and debt.loc[i] > 1.5) else "low"

        # --- composites in [0, 1] ---
        spec = 0.0
        if b_beta == "high":
            spec += 0.35
        elif b_beta == "mid":
            spec += 0.15
        if not profitable:
            spec += 0.25
        if b_size in ("micro", "small"):
            spec += 0.15
        elif b_size == "mid":
            spec += 0.08
        if b_idx == "RUT":
            spec += 0.10
        if mom == "extended":
            spec += 0.10
        spec = float(min(1.0, spec))

        quality = 0.0
        if profitable:
            quality += 0.40
        if b_beta == "low":
            quality += 0.30
        elif b_beta == "mid":
            quality += 0.10
        if b_size in ("large", "mega"):
            quality += 0.20
        if mom == "neutral":
            quality += 0.10
        quality = float(min(1.0, quality))

        crowding = 0.0
        if b_short == "very_high":
            crowding += 0.45
        elif b_short == "elevated":
            crowding += 0.25
        if mom == "extended":
            crowding += 0.35
        if mom == "washed" and b_short in ("elevated", "very_high"):
            crowding += 0.15  # squeeze candidate
        crowding = float(min(1.0, crowding))

        size_tilt = {"micro": 1.0, "small": 0.8, "mid": 0.5, "large": 0.2, "mega": 0.0}.get(b_size, 0.4)

        # priors: residual pressure (not absolute price)
        # risk-on lifts SPEC_DURATION and SIZE_TILT; lifts QUALITY less / inverse
        pr = y["p_risk_on"]
        conv = max(y["conviction"], 0.15)
        pressure = conv * (
            (pr - 0.5) * 2.0 * spec          # high spec → + when risk-on
            + (0.5 - pr) * 1.5 * quality     # quality → + when risk-off
            + (pr - 0.5) * 1.2 * size_tilt   # small → + when risk-on
            + (pr - 0.5) * 0.6 * crowding    # crowded high-beta often rides risk-on; weak prior
        )

        rows.append({
            "Ticker": t,
            "Company": r.get("Company", ""),
            "Sector": r.get("Sector", ""),
            "Industry": r.get("Industry", ""),
            "size": b_size,
            "index": b_idx,
            "beta": b_beta,
            "short": b_short,
            "mom": mom,
            "profitable": profitable,
            "leverage": lev,
            "SPEC_DURATION": round(spec, 3),
            "QUALITY_DEFENSIVE": round(quality, 3),
            "CROWDING": round(crowding, 3),
            "SIZE_TILT": round(size_tilt, 3),
            "ret": ret.loc[i] if i in ret.index else np.nan,
            "resid": resid.loc[i] if i in resid.index else np.nan,
            "pressure": round(float(pressure), 4),
            "Price": price.loc[i] if i in price.index else np.nan,
        })

    df = pd.DataFrame(rows)
    df = df.sort_values("pressure", ascending=False)
    return df, y


def write_report(date_str: str, pair: str | None, df: pd.DataFrame, y: dict) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    config.DAILY.mkdir(parents=True, exist_ok=True)

    csv_path = OUT_DIR / f"{date_str}_composite_rank.csv"
    df.to_csv(csv_path, index=False)
    (OUT_DIR / f"{date_str}_y_snapshot.json").write_text(
        json.dumps({"date": date_str, "pair": pair, **y}, indent=2), encoding="utf-8"
    )

    top = df.head(20)
    bot = df.tail(15).iloc[::-1]

    L = [
        f"# Composite residual rank — **{date_str}**",
        "",
        f"Generated: {datetime.now(ZoneInfo(config.TZ)).isoformat()}",
        f"Prior snapshot (for returns): **{pair or 'none'}**",
        "",
        "## Y snapshot (v1 — breadth only)",
        "",
        f"- **p_risk_on:** {y['p_risk_on']} (from % names up)",
        f"- **pct_up:** {y['pct_up']}",
        f"- **median_ret:** {y['median_ret']*100:.2f}%",
        f"- **conviction:** {y['conviction']}",
        f"- **n:** {y['n_universe']}",
        f"- note: {y['z_note']}",
        "",
        "## Method (deliberately simple)",
        "",
        "- **residual** = stock return − median stock return (same pair window)",
        "- **composites:** SPEC_DURATION, QUALITY_DEFENSIVE, CROWDING, SIZE_TILT",
        "- **pressure** = conviction × prior effects of composites given p_risk_on",
        "- Ranking is **cross-sectional residual bias**, not an absolute SPY call",
        "- Hand priors only — replace with audit weights later",
        "",
        f"CSV: `data/composite/{date_str}_composite_rank.csv`",
        "",
        "## Top 20 by residual pressure (favor when risk-on / current Y)",
        "",
        "| Ticker | Sector | pressure | SPEC | QUAL | CROWD | SIZE | resid | beta | short |",
        "|--------|--------|----------|------|------|-------|------|-------|------|-------|",
    ]
    for _, r in top.iterrows():
        resid_s = f"{r['resid']*100:+.2f}%" if r["resid"] == r["resid"] else "n/a"
        L.append(
            f"| {r['Ticker']} | {str(r['Sector'])[:18]} | {r['pressure']:+.3f} | "
            f"{r['SPEC_DURATION']:.2f} | {r['QUALITY_DEFENSIVE']:.2f} | "
            f"{r['CROWDING']:.2f} | {r['SIZE_TILT']:.2f} | {resid_s} | "
            f"{r['beta']} | {r['short']} |"
        )

    L += [
        "",
        "## Bottom 15 (lowest pressure)",
        "",
        "| Ticker | Sector | pressure | SPEC | QUAL | resid | beta |",
        "|--------|--------|----------|------|------|-------|------|",
    ]
    for _, r in bot.iterrows():
        resid_s = f"{r['resid']*100:+.2f}%" if r["resid"] == r["resid"] else "n/a"
        L.append(
            f"| {r['Ticker']} | {str(r['Sector'])[:18]} | {r['pressure']:+.3f} | "
            f"{r['SPEC_DURATION']:.2f} | {r['QUALITY_DEFENSIVE']:.2f} | {resid_s} | {r['beta']} |"
        )

    # sector rollup
    L += ["", "## Sector median pressure", "",
          "| Sector | n | median pressure | median resid |", "|--------|---|-----------------|--------------|"]
    g = df.groupby("Sector", dropna=False)
    sec = g.agg(n=("Ticker", "count"), med_p=("pressure", "median"), med_r=("resid", "median"))
    sec = sec.sort_values("med_p", ascending=False)
    for name, r in sec.head(15).iterrows():
        mr = f"{r['med_r']*100:+.2f}%" if r["med_r"] == r["med_r"] else "n/a"
        L.append(f"| {name} | {int(r['n'])} | {r['med_p']:+.3f} | {mr} |")

    L += ["", "## Composite averages by size", "",
          "| size | n | SPEC | QUAL | pressure |", "|------|---|------|------|----------|"]
    for size, part in df.groupby("size"):
        L.append(
            f"| {size} | {len(part)} | {part['SPEC_DURATION'].mean():.2f} | "
            f"{part['QUALITY_DEFENSIVE'].mean():.2f} | {part['pressure'].mean():+.3f} |"
        )

    path = config.DAILY / f"{date_str}_composite_rank.md"
    path.write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"[composite] {path}  rows={len(df)}  p_risk_on={y['p_risk_on']}")


def run(date_str: str | None = None) -> None:
    dates = snapshot_dates()
    if not dates:
        raise SystemExit("no snapshots in data/snapshots")
    if date_str is None:
        date_str = sorted(dates.keys())[-1]
    if date_str not in dates:
        raise SystemExit(f"no snapshot for {date_str}")

    keys = sorted(dates.keys())
    idx = keys.index(date_str)
    pair = keys[idx - 1] if idx > 0 else None

    cur = load_dated(dates[date_str])
    prev = load_dated(dates[pair]) if pair else None
    df, y = build_xy(cur, prev)
    write_report(date_str, pair, df, y)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", default=None, help="As-of snapshot date")
    args = ap.parse_args()
    run(args.date)


if __name__ == "__main__":
    main()
