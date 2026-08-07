"""Theme Radar score engine — deterministic per-stock scoring, NO LLM.

For every ticker in the latest Finviz snapshot, and each horizon (1d/1w/1m):
  1. pair the snapshot with the nearest prior snapshot in the horizon window
  2. compute status buckets from LEVELS (extension / trend / crowding / street)
  3. score each rubric rule (level, delta, or true return) with deadzones,
     polarity, and status overrides
  4. apply the ordered interaction gates
  5. emit per-category scores, pos/neg counts and weights, total score

Outputs:
  data/scores/<date>_1d.csv / _1w.csv / _1m.csv   (one row per ticker)
  data/scores/<date>_segments.csv                  (industry aggregates)
  01_daily/<date>_scan.md                          (human-readable brief)

CLI: python -m src.score_engine [--date YYYY-MM-DD]
"""
from __future__ import annotations

import argparse
import json
from datetime import date, datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd

from . import config
from .finviz_delta import SNAPSHOT_DIR, _add_catalyst_flags, normalize_frame
from .score_rubric import (CATEGORY_MAX, HORIZON_WINDOWS, INTERACTIONS,
                           RET_DEADZONE, RUBRIC, STATUS)

SCORES_DIR = config.DATA / "scores"
CATEGORIES = ["price", "flow", "technical", "positioning", "valuation",
              "fundamental", "catalyst"]


# ------------------------------------------------------------------ pairing
def snapshot_dates() -> dict[str, Path]:
    """date -> canonical dated CSV path (manifest first, glob fallback)."""
    out = {}
    man = SNAPSHOT_DIR / "manifest.json"
    if man.exists():
        data = json.loads(man.read_text())
        for d, fname in data.get("files", {}).items():
            p = SNAPSHOT_DIR / fname
            if p.exists():
                out[d] = p
    for p in SNAPSHOT_DIR.glob("????-??-??.csv"):
        out.setdefault(p.stem, p)
    return dict(sorted(out.items()))


def find_prior(dates: dict[str, Path], target: date, horizon: str):
    """Nearest snapshot date inside the horizon window before target."""
    lo, hi = HORIZON_WINDOWS[horizon]
    best = None
    for d in dates:
        try:
            dd = date.fromisoformat(d)
        except ValueError:
            continue
        gap = (target - dd).days
        if lo <= gap <= hi:
            if best is None or dd > best:
                best = dd
    return best.isoformat() if best else None


def load_dated(path: Path) -> pd.DataFrame:
    return normalize_frame(pd.read_csv(path, low_memory=False))


# ------------------------------------------------------------------ status
def _g(row, col, default=np.nan):
    v = row.get(col, default)
    try:
        if pd.isna(v):
            return default
        return float(v)
    except (TypeError, ValueError):
        return default


def compute_status(row: pd.Series, upside: float) -> dict:
    pw = _g(row, "Performance (Week)")
    pm = _g(row, "Performance (Month)")
    rsi = _g(row, "Relative Strength Index (14)")
    v50 = _g(row, "50-Day Simple Moving Average")
    v200 = _g(row, "200-Day Simple Moving Average")
    sf = _g(row, "Short Float")

    if not np.isnan(pw) and pw > STATUS["extreme_week_pct"]:
        ext = "EXTREME"
    elif ((not np.isnan(pw) and pw > STATUS["extended_week_pct"])
          or (not np.isnan(pm) and pm > STATUS["extended_month_pct"])
          or (not np.isnan(rsi) and rsi > STATUS["extended_rsi"])
          or (not np.isnan(v50) and v50 > STATUS["far_above_50dma_pct"])):
        ext = "EXTENDED"
    elif ((not np.isnan(pm) and pm < STATUS["washed_month_pct"])
          or (not np.isnan(rsi) and rsi < STATUS["washed_rsi"])):
        ext = "WASHED"
    else:
        ext = "NEUTRAL"

    if not np.isnan(v50) and not np.isnan(v200):
        trend = ("UPTREND" if v50 > 0 and v200 > 0 else
                 "DOWNTREND" if v50 < 0 and v200 < 0 else "MIXED")
    else:
        trend = "UNKNOWN"

    short = ("HIGH_SHORT" if not np.isnan(sf) and sf > STATUS["high_short_pct"]
             else "ELEVATED" if not np.isnan(sf) and sf > STATUS["elevated_short_pct"]
             else "LOW")

    return {"status_extension": ext, "status_trend": trend,
            "status_short": short,
            "status_street": "STREET_EXTENDED" if upside < 0 else "OK"}


# ------------------------------------------------------------------ curves
def _curves(name: str, v: float) -> float:
    """Level -> signal in [-1, +1] for curve: polarity rules."""
    if np.isnan(v):
        return 0.0
    if name == "rsi":
        if v >= 75: return -1.0
        if v >= 65: return 0.5
        if v >= 45: return 1.0
        if v >= 30: return -0.5
        return -0.5  # oversold: falling knife until repair confirms
    if name == "rvol":
        if v >= 2.0: return 1.0
        if v >= 1.3: return 0.5
        if v >= 0.6: return 0.0
        return -0.5  # dead tape
    if name == "sma50":
        if v > STATUS["far_above_50dma_pct"]: return -1.0  # extension
        if v > 0: return 1.0
        return -1.0
    if name == "sma200":
        return 1.0 if v > 0 else -1.0
    if name == "vol":
        if v >= 8: return -1.0
        if v >= 5: return -0.5
        if v <= 2: return 0.5   # coiled
        return 0.0
    if name == "short":
        if v > STATUS["high_short_pct"]: return -1.0
        if v > STATUS["elevated_short_pct"]: return -0.3
        return 0.0
    if name == "upside":
        if v >= 30: return 1.0
        if v >= 5: return 0.3
        if v >= 0: return 0.0
        return -1.0  # price above target
    if name == "debt":
        if v >= 2.0: return -1.0
        if v >= 1.0: return -0.5
        return 0.0
    return 0.0


# ------------------------------------------------------------------ scoring
def _sign_dead(value: float, deadzone: float) -> int:
    if np.isnan(value) or abs(value) < deadzone:
        return 0
    return 1 if value > 0 else -1


def score_ticker(now: pd.Series, then: pd.Series | None, horizon: str) -> dict:
    """One ticker, one horizon. `then` is None in levels-only mode."""
    price_now, price_then = _g(now, "Price"), (_g(then, "Price") if then is not None else np.nan)
    ret = (price_now / price_then - 1) if (not np.isnan(price_now) and not np.isnan(price_then) and price_then) else np.nan
    upside = ((_g(now, "Target Price") - price_now) / price_now * 100
              if not np.isnan(price_now) and price_now
              and not np.isnan(_g(now, "Target Price")) else np.nan)
    rvol = _g(now, "Relative Volume")
    inst_tx = _g(now, "Institutional Transactions")
    n_cat = int(sum(1 for c in now.index
                    if c.startswith("cat_") and bool(now.get(c))))

    st = compute_status(now, upside if not np.isnan(upside) else 0.0)
    cat = {c: 0.0 for c in CATEGORIES}
    n_pos = n_neg = 0
    w_pos = w_neg = 0.0
    drivers_pos, drivers_neg = [], []

    for rule in RUBRIC:
        if horizon not in rule["horizons"]:
            continue
        if rule["speed"] == "slow" and horizon == "1d":
            continue

        # raw value
        if rule["kind"] == "ret":
            raw = ret
            dz = RET_DEADZONE[horizon]
        elif rule["kind"] == "delta":
            if then is None:
                continue
            a, b = _g(now, rule["field"]), _g(then, rule["field"])
            if np.isnan(a) or np.isnan(b):
                continue
            if str(rule["polarity"]).startswith("pct:"):
                raw = (a / b - 1) if b else np.nan  # relative change
            else:
                raw = a - b
            dz = rule["deadzone"]
        elif rule["field"] == "upside_pct":
            raw, dz = upside, rule["deadzone"]
        elif rule["field"] == "n_catalysts":
            raw, dz = float(n_cat), rule["deadzone"]
        else:
            raw, dz = _g(now, rule["field"]), rule["deadzone"]
        if raw is None or (isinstance(raw, float) and np.isnan(raw)):
            continue

        # signal
        pol = rule["polarity"]
        if str(pol).startswith("curve:"):
            s = _curves(str(pol)[6:], float(raw))
        else:
            s = float(_sign_dead(float(raw), dz))
            base = str(pol).lstrip("pct:")
            if base == "-":
                s = -s
        # RVol direction follows the tape: hot + up = ignition, hot + down = event selling
        if rule["field"] == "Relative Volume" and s > 0 and not np.isnan(ret):
            if abs(ret) < RET_DEADZONE[horizon]:
                s = 0.0
            elif ret < 0:
                s = -s

        # status overrides (field level)
        if rule["status_mode"] == "momentum" and s > 0:
            if st["status_extension"] == "EXTREME":
                s = -1.0
        if rule["status_mode"] == "rsi":
            rsi_now = _g(now, "Relative Strength Index (14)")
            if not np.isnan(rsi_now) and rsi_now > STATUS["extended_rsi"] and s > 0:
                s = 0.0  # rising INTO overbought earns nothing

        p = s * rule["weight"]
        if p == 0:
            continue
        cat[rule["category"]] += p
        label = f"{rule['field']}{'Δ' if rule['kind'] == 'delta' else ''}"
        if p > 0:
            n_pos += 1
            w_pos += p
            drivers_pos.append(f"{label} +{p:.1f}")
        else:
            n_neg += 1
            w_neg += -p
            drivers_neg.append(f"{label} {p:.1f}")

    # ---------------- interaction gates (ordered) ----------------
    flags: list[str] = []
    confidence = 1.0
    ctx = {"cat": cat, "ret": 0.0 if np.isnan(ret) else ret, "rvol": rvol,
           "upside_pct": upside, "inst_tx": inst_tx, "horizon": horizon,
           "flags": flags, **st}

    for gate in INTERACTIONS:
        gid = gate["id"]
        if gid == "extension_cap" and st["status_extension"] == "EXTENDED" and cat["price"] > 0:
            cat["price"] *= 0.25
            flags.append("EXTENSION_CAP")
        elif gid == "extreme_flip" and st["status_extension"] == "EXTREME" and cat["price"] > 0:
            cat["price"] = -abs(cat["price"]) * 0.5
            flags.append("EXTREME_FLIP")
        elif gid == "downtrend_bounce_discount" and st["status_trend"] == "DOWNTREND" \
                and horizon in ("1w", "1m") and cat["price"] > 0:
            cat["price"] *= 0.5
            flags.append("DOWNTREND_BOUNCE_DISCOUNT")
        elif gid == "street_extended_discount" and not np.isnan(upside) and upside < 0 and cat["price"] > 0:
            cat["price"] *= 0.5
            flags.append("STREET_EXTENDED_DISCOUNT")
        elif gid == "squeeze_flag" and st["status_short"] == "HIGH_SHORT" \
                and not np.isnan(ret) and ret > 0.05 and not np.isnan(rvol) and rvol > 1.5:
            flags.append("SQUEEZE_SETUP")
        elif gid == "unconfirmed_rally" and not np.isnan(inst_tx) and inst_tx < 0 \
                and not np.isnan(ret) and ret > 0:
            confidence *= 0.8
            flags.append("UNCONFIRMED_RALLY")
        elif gid == "capitulation_watch" and st["status_extension"] == "WASHED" \
                and not np.isnan(ret) and ret < -0.03 and not np.isnan(rvol) and rvol > 1.5:
            flags.append("CAPITULATION_WATCH")

    total = sum(cat.values())
    max_total = sum(CATEGORY_MAX.values())
    score_100 = round(total / max_total * 100, 1)

    return {
        "ret_H": round(ret * 100, 2) if not np.isnan(ret) else None,
        "upside_pct": round(upside, 1) if not np.isnan(upside) else None,
        **st,
        **{f"{c}_score": round(cat[c], 2) for c in CATEGORIES},
        "n_pos": n_pos, "n_neg": n_neg,
        "w_pos": round(w_pos, 2), "w_neg": round(w_neg, 2),
        "total_score": round(total, 2), "score_100": score_100,
        "confidence": round(confidence, 2),
        "kill_flags": "|".join(flags),
        "top_pos": "; ".join(drivers_pos[:4]),
        "top_neg": "; ".join(drivers_neg[:4]),
        "n_catalysts": n_cat,
    }


# ------------------------------------------------------------------ identity
def _size_bucket(mcap: float) -> str:
    if np.isnan(mcap):
        return "unknown"
    if mcap < 300: return "micro"
    if mcap < 2000: return "small"
    if mcap < 10000: return "mid"
    if mcap < 200000: return "large"
    return "mega"


def _beta_bucket(beta: float) -> str:
    if np.isnan(beta):
        return "unknown"
    if beta > 1.5: return "high"
    if beta < 0.8: return "defensive"
    return "mid"


META_COLS = ["Ticker", "Company", "Sector", "Industry"]


def score_universe(cur: pd.DataFrame, prev: pd.DataFrame | None,
                   horizon: str) -> pd.DataFrame:
    cur = _add_catalyst_flags(cur)
    prev_map = {}
    if prev is not None:
        prev_map = {t: r for t, r in prev.set_index("Ticker", drop=False).iterrows()}
    rows = []
    for _, row in cur.iterrows():
        then = prev_map.get(row["Ticker"])
        rec = {c: row.get(c, "") for c in META_COLS}
        rec["Price"] = _g(row, "Price")
        rec["mcap_bucket"] = _size_bucket(_g(row, "Market Cap"))
        rec["beta_bucket"] = _beta_bucket(_g(row, "Beta"))
        rec.update(score_ticker(row, then, horizon))
        rows.append(rec)
    df = pd.DataFrame(rows)
    return df.sort_values("total_score", ascending=False)


# ------------------------------------------------------------------ segments
def segment_table(scores: pd.DataFrame, min_names: int = 8) -> pd.DataFrame:
    def pct_pos(s):
        return round((s > 0).mean() * 100, 1) if len(s) else np.nan
    g = scores.groupby("Industry").agg(
        n=("Ticker", "count"),
        med_total=("total_score", "median"),
        pct_positive=("total_score", pct_pos),
        med_ret=("ret_H", "median"),
        n_squeeze=("kill_flags", lambda s: s.str.contains("SQUEEZE_SETUP").sum()),
        n_extreme=("status_extension", lambda s: (s == "EXTREME").sum()),
    )
    g = g[g["n"] >= min_names]
    return g.sort_values("med_total", ascending=False).round(2)


# ------------------------------------------------------------------ brief
def brief(date_str: str, per_horizon: dict[str, pd.DataFrame | None],
          pairs: dict[str, str | None], segments: pd.DataFrame | None) -> str:
    L = [f"# Daily Universe Scan — {date_str}", ""]
    L.append("Deterministic rubric over dated Finviz snapshots. No LLM. "
             "Score > 0 = more bullish evidence than bearish, after status "
             "gates and interaction dampeners.")
    L.append("")
    for h in ("1d", "1w", "1m"):
        df = per_horizon.get(h)
        pair = pairs.get(h)
        L.append(f"## Horizon {h}  (pair: {pair or 'NONE — levels only, no delta/return evidence'})")
        if df is None:
            L.append("")
            continue
        L.append("")
        L.append(f"Scored {len(df)} tickers. "
                 f"Bullish (>+2): {(df['total_score'] > 2).sum()} | "
                 f"bearish (<-2): {(df['total_score'] < -2).sum()}")
        L.append("")
        L.append("**Top 15:**")
        L.append("")
        L.append("| Ticker | Industry | Score | Ret% | Status | Flags | Top drivers |")
        L.append("|---|---|---|---|---|---|---|")
        for _, r in df.head(15).iterrows():
            L.append(f"| {r['Ticker']} | {str(r['Industry'])[:24]} | "
                     f"{r['total_score']:+.1f} | {r['ret_H']} | "
                     f"{r['status_extension']}/{r['status_trend']}/{r['status_short']} | "
                     f"{r['kill_flags'] or '—'} | {str(r['top_pos'])[:60]} |")
        L.append("")
        L.append("**Bottom 10:**")
        L.append("")
        L.append("| Ticker | Industry | Score | Ret% | Status | Top negatives |")
        L.append("|---|---|---|---|---|---|")
        for _, r in df.tail(10).iloc[::-1].iterrows():
            L.append(f"| {r['Ticker']} | {str(r['Industry'])[:24]} | "
                     f"{r['total_score']:+.1f} | {r['ret_H']} | "
                     f"{r['status_extension']}/{r['status_trend']}/{r['status_short']} | "
                     f"{str(r['top_neg'])[:60]} |")
        sq = df[df["kill_flags"].str.contains("SQUEEZE_SETUP", na=False)]
        if len(sq):
            L.append("")
            L.append(f"**⚡ Squeeze setups ({len(sq)}):** "
                     + ", ".join(sq.head(10)["Ticker"].tolist()))
        cap = df[df["kill_flags"].str.contains("CAPITULATION_WATCH", na=False)]
        if len(cap):
            L.append("")
            L.append(f"**⚠️ Capitulation watch ({len(cap)}):** "
                     + ", ".join(cap.head(10)["Ticker"].tolist()))
        L.append("")
    if segments is not None and len(segments):
        L.append("## Industry segments (1w horizon, min 8 names)")
        L.append("")
        L.append("| Industry | n | Median score | % positive | Median ret% | Squeezes |")
        L.append("|---|---|---|---|---|---|")
        for name, r in segments.head(20).iterrows():
            L.append(f"| {str(name)[:34]} | {int(r['n'])} | {r['med_total']:+.1f} | "
                     f"{r['pct_positive']}% | {r['med_ret']} | {int(r['n_squeeze'])} |")
        L.append("")
    return "\n".join(L)


# ------------------------------------------------------------------ main
def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", default=None)
    args = ap.parse_args()
    target = (date.fromisoformat(args.date) if args.date else
              datetime.now(ZoneInfo(config.TZ)).date())
    date_str = target.isoformat()

    dates = snapshot_dates()
    if date_str not in dates:
        raise SystemExit(f"[score] no snapshot for {date_str}; "
                         f"have: {list(dates)[-5:]}")
    cur = load_dated(dates[date_str])

    SCORES_DIR.mkdir(parents=True, exist_ok=True)
    per_horizon: dict[str, pd.DataFrame | None] = {}
    pairs: dict[str, str | None] = {}

    for h in ("1d", "1w", "1m"):
        prior = find_prior(dates, target, h)
        pairs[h] = prior
        prev = load_dated(dates[prior]) if prior else None
        scored = score_universe(cur, prev, h)
        per_horizon[h] = scored
        out = SCORES_DIR / f"{date_str}_{h}.csv"
        scored.to_csv(out, index=False)
        print(f"[score] {h}: {len(scored)} tickers, pair={prior} -> {out.name}")

    seg = segment_table(per_horizon["1w"]) if per_horizon["1w"] is not None else None
    if seg is not None:
        seg.to_csv(SCORES_DIR / f"{date_str}_segments.csv")

    text = brief(date_str, per_horizon, pairs, seg)
    daily_dir = config.DAILY
    daily_dir.mkdir(parents=True, exist_ok=True)
    brief_path = daily_dir / f"{date_str}_scan.md"
    brief_path.write_text(text, encoding="utf-8")
    print(f"[score] brief -> {brief_path}")


if __name__ == "__main__":
    main()
