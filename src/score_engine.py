"""Theme Radar score engine — deterministic per-stock scoring, NO LLM.

For every ticker in the latest Finviz snapshot, and each horizon (1d/1w/1m):
  1. pair the snapshot with the nearest prior snapshot in the horizon window
  2. compute status buckets from LEVELS (extension / trend / crowding / street)
  3. score each rubric rule (level, delta, or true return) with deadzones,
     polarity, and status overrides
  4. apply the ordered interaction gates
  5. emit per-category scores, pos/neg counts and weights, total score
  6. write FULL-UNIVERSE feature log (levels + deltas + scores) for learning

Transparency:
  Every rule can emit an audit row. Use --trace TICKER to print it.

Outputs:
  data/scores/<date>_1d.csv / _1w.csv / _1m.csv
  data/features/<date>_1d.csv     (ALL tickers — never truncated)
  data/scores/<date>_segments.csv
  01_daily/<date>_scan.md
  01_daily/<date>_trace_<TICKER>.md   (when --trace is set)

CLI:
  python -m src.score_engine [--date YYYY-MM-DD]
  python -m src.score_engine --date 2026-08-07 --trace MP,OKLO --horizon 1d
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
from .finviz_delta import SNAPSHOT_DIR, _add_catalyst_flags, normalize_frame
from .score_rubric import (CATEGORY_MAX, HORIZON_WINDOWS, INTERACTIONS,
                           RET_DEADZONE, RUBRIC, STATUS)

SCORES_DIR = config.DATA / "scores"
CATEGORIES = ["price", "flow", "technical", "positioning", "valuation",
              "fundamental", "catalyst"]

_WEIGHT_OVERRIDES: dict | None = None


def _override_mult(rule: dict) -> float:
    """Learned weight multiplier from src/weight_learner.py
    (data/weight_overrides.json). 1.0 when absent — champion behavior.
    Keyed '<field>|<kind>' because the same field can appear as both a
    level and a delta rule."""
    global _WEIGHT_OVERRIDES
    if _WEIGHT_OVERRIDES is None:
        try:
            _WEIGHT_OVERRIDES = json.loads(
                (config.DATA / "weight_overrides.json")
                .read_text(encoding="utf-8")).get("multipliers", {})
        except (OSError, ValueError):
            _WEIGHT_OVERRIDES = {}
    return float(_WEIGHT_OVERRIDES.get(f"{rule['field']}|{rule['kind']}", 1.0))


def snapshot_dates() -> dict[str, Path]:
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


def _g(row, col, default=np.nan):
    v = row.get(col, default)
    try:
        if pd.isna(v):
            return default
        return float(v)
    except (TypeError, ValueError):
        return default


def _fmt(v, pct=False):
    if v is None or (isinstance(v, float) and np.isnan(v)):
        return "n/a"
    if pct:
        return f"{v * 100:+.2f}%" if abs(v) < 5 else f"{v:+.2f}%"
    if isinstance(v, float):
        return f"{v:.4g}"
    return str(v)


def compute_status(row: pd.Series, upside: float) -> dict:
    pw = _g(row, "Performance (Week)")
    pm = _g(row, "Performance (Month)")
    rsi = _g(row, "Relative Strength Index (14)")
    v50 = _g(row, "50-Day Simple Moving Average")
    v200 = _g(row, "200-Day Simple Moving Average")
    sf = _g(row, "Short Float")

    status_inputs = {
        "Performance (Week)": pw,
        "Performance (Month)": pm,
        "RSI (14)": rsi,
        "50-DMA %": v50,
        "200-DMA %": v200,
        "Short Float": sf,
        "upside_pct": upside,
    }

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

    return {
        "status_extension": ext,
        "status_trend": trend,
        "status_short": short,
        "status_street": "STREET_EXTENDED" if upside < 0 else "OK",
        "status_inputs": status_inputs,
    }


def _curves(name: str, v: float) -> float:
    if np.isnan(v):
        return 0.0
    if name == "rsi":
        if v >= 75: return -1.0
        if v >= 65: return 0.5
        if v >= 45: return 1.0
        if v >= 30: return -0.5
        return -0.5
    if name == "rvol":
        if v >= 2.0: return 1.0
        if v >= 1.3: return 0.5
        if v >= 0.6: return 0.0
        return -0.5
    if name == "sma50":
        if v > STATUS["far_above_50dma_pct"]: return -1.0
        if v > 0: return 1.0
        return -1.0
    if name == "sma200":
        return 1.0 if v > 0 else -1.0
    if name == "vol":
        if v >= 8: return -1.0
        if v >= 5: return -0.5
        if v <= 2: return 0.5
        return 0.0
    if name == "short":
        if v > STATUS["high_short_pct"]: return -1.0
        if v > STATUS["elevated_short_pct"]: return -0.3
        return 0.0
    if name == "upside":
        if v >= 30: return 1.0
        if v >= 5: return 0.3
        if v >= 0: return 0.0
        return -1.0
    if name == "debt":
        if v >= 2.0: return -1.0
        if v >= 1.0: return -0.5
        return 0.0
    return 0.0


def _sign_dead(value: float, deadzone: float) -> int:
    if np.isnan(value) or abs(value) < deadzone:
        return 0
    return 1 if value > 0 else -1


def _direction(raw: float, dz: float) -> str:
    if raw is None or (isinstance(raw, float) and np.isnan(raw)):
        return "n/a"
    if abs(raw) < dz:
        return "flat (inside deadzone)"
    return "up" if raw > 0 else "down"


def score_ticker(now: pd.Series, then: pd.Series | None, horizon: str,
                 collect_trace: bool = False) -> dict:
    price_now = _g(now, "Price")
    price_then = _g(then, "Price") if then is not None else np.nan
    ret = (price_now / price_then - 1) if (
        not np.isnan(price_now) and not np.isnan(price_then) and price_then
    ) else np.nan
    upside = ((
        (_g(now, "Target Price") - price_now) / price_now * 100
        if not np.isnan(price_now) and price_now
        and not np.isnan(_g(now, "Target Price")) else np.nan
    ))
    rvol = _g(now, "Relative Volume")
    inst_tx = _g(now, "Institutional Transactions")
    n_cat = int(sum(1 for c in now.index
                    if c.startswith("cat_") and bool(now.get(c))))

    st = compute_status(now, upside if not np.isnan(upside) else 0.0)
    status_inputs = st.pop("status_inputs")
    cat = {c: 0.0 for c in CATEGORIES}
    n_pos = n_neg = 0
    w_pos = w_neg = 0.0
    drivers_pos, drivers_neg = [], []
    trace: list[dict] = []

    for rule in RUBRIC:
        field = rule["field"]
        kind = rule["kind"]
        audit = {
            "field": field, "kind": kind, "category": rule["category"],
            "speed": rule["speed"], "weight": rule["weight"],
            "weight_mult": _override_mult(rule),
            "polarity": rule["polarity"], "note": rule.get("note", ""),
            "now": None, "then": None, "raw": None, "deadzone": None,
            "direction": None, "signal": 0.0, "points": 0.0,
            "skipped": None, "override": None,
        }

        if horizon not in rule["horizons"]:
            audit["skipped"] = f"horizon {horizon} not in {rule['horizons']}"
            if collect_trace:
                trace.append(audit)
            continue
        if rule["speed"] == "slow" and horizon == "1d":
            audit["skipped"] = "slow field blocked on 1d"
            if collect_trace:
                trace.append(audit)
            continue

        if kind == "ret":
            audit["now"], audit["then"] = price_now, price_then
            raw, dz = ret, RET_DEADZONE[horizon]
            audit["deadzone"] = dz
            if then is None:
                audit["skipped"] = "no prior snapshot for true return"
                if collect_trace:
                    trace.append(audit)
                continue
        elif kind == "delta":
            if then is None:
                audit["skipped"] = "no prior snapshot for delta"
                if collect_trace:
                    trace.append(audit)
                continue
            a, b = _g(now, field), _g(then, field)
            audit["now"], audit["then"] = a, b
            if np.isnan(a) or np.isnan(b):
                audit["skipped"] = "missing now or then value"
                if collect_trace:
                    trace.append(audit)
                continue
            raw = (a / b - 1) if str(rule["polarity"]).startswith("pct:") and b else (a - b)
            dz = rule["deadzone"]
            audit["deadzone"] = dz
        elif field == "upside_pct":
            audit["now"] = upside
            raw, dz = upside, rule["deadzone"]
            audit["deadzone"] = dz
        elif field == "n_catalysts":
            audit["now"] = float(n_cat)
            raw, dz = float(n_cat), rule["deadzone"]
            audit["deadzone"] = dz
        else:
            a = _g(now, field)
            audit["now"] = a
            audit["then"] = _g(then, field) if then is not None else np.nan
            raw, dz = a, rule["deadzone"]
            audit["deadzone"] = dz

        if raw is None or (isinstance(raw, float) and np.isnan(raw)):
            audit["skipped"] = "raw is nan"
            if collect_trace:
                trace.append(audit)
            continue

        audit["raw"] = float(raw)
        audit["direction"] = _direction(float(raw), float(dz or 0))

        pol = rule["polarity"]
        if str(pol).startswith("curve:"):
            s = _curves(str(pol)[6:], float(raw))
        else:
            s = float(_sign_dead(float(raw), float(dz or 0)))
            if str(pol).lstrip("pct:") == "-":
                s = -s

        if field == "Relative Volume" and s > 0 and not np.isnan(ret):
            if abs(ret) < RET_DEADZONE[horizon]:
                s = 0.0
                audit["override"] = "RVol zeroed: price flat inside deadzone"
            elif ret < 0:
                s = -s
                audit["override"] = "RVol flipped: hot volume + price down = selling"

        if rule.get("status_mode") == "momentum" and s > 0:
            if st["status_extension"] == "EXTREME":
                s = -1.0
                audit["override"] = "EXTREME extension: momentum signal flipped bearish"
        if rule.get("status_mode") == "rsi":
            rsi_now = _g(now, "Relative Strength Index (14)")
            if not np.isnan(rsi_now) and rsi_now > STATUS["extended_rsi"] and s > 0:
                s = 0.0
                audit["override"] = "RSI already overbought: rising RSI earns 0"

        p = s * rule["weight"] * _override_mult(rule)
        audit["signal"] = s
        audit["points"] = p
        if collect_trace:
            trace.append(audit)
        if p == 0:
            continue
        cat[rule["category"]] += p
        label = f"{field}{'Δ' if kind == 'delta' else ''}"
        if p > 0:
            n_pos += 1
            w_pos += p
            drivers_pos.append(f"{label} +{p:.1f}")
        else:
            n_neg += 1
            w_neg += -p
            drivers_neg.append(f"{label} {p:.1f}")

    flags: list[str] = []
    gate_log: list[str] = []
    confidence = 1.0
    pre_gate_cat = dict(cat)

    for gate in INTERACTIONS:
        gid = gate["id"]
        if gid == "extension_cap" and st["status_extension"] == "EXTENDED" and cat["price"] > 0:
            old = cat["price"]
            cat["price"] *= 0.25
            flags.append("EXTENSION_CAP")
            gate_log.append(f"EXTENSION_CAP: price {old:.2f} → {cat['price']:.2f}")
        elif gid == "extreme_flip" and st["status_extension"] == "EXTREME" and cat["price"] > 0:
            old = cat["price"]
            cat["price"] = -abs(cat["price"]) * 0.5
            flags.append("EXTREME_FLIP")
            gate_log.append(f"EXTREME_FLIP: price {old:.2f} → {cat['price']:.2f}")
        elif gid == "downtrend_bounce_discount" and st["status_trend"] == "DOWNTREND" \
                and horizon in ("1w", "1m") and cat["price"] > 0:
            old = cat["price"]
            cat["price"] *= 0.5
            flags.append("DOWNTREND_BOUNCE_DISCOUNT")
            gate_log.append(f"DOWNTREND_BOUNCE_DISCOUNT: price {old:.2f} → {cat['price']:.2f}")
        elif gid == "street_extended_discount" and not np.isnan(upside) and upside < 0 and cat["price"] > 0:
            old = cat["price"]
            cat["price"] *= 0.5
            flags.append("STREET_EXTENDED_DISCOUNT")
            gate_log.append(f"STREET_EXTENDED_DISCOUNT: price {old:.2f} → {cat['price']:.2f}")
        elif gid == "squeeze_flag" and st["status_short"] == "HIGH_SHORT" \
                and not np.isnan(ret) and ret > 0.05 and not np.isnan(rvol) and rvol > 1.5:
            flags.append("SQUEEZE_SETUP")
            gate_log.append("SQUEEZE_SETUP")
        elif gid == "unconfirmed_rally" and not np.isnan(inst_tx) and inst_tx < 0 \
                and not np.isnan(ret) and ret > 0:
            confidence *= 0.8
            flags.append("UNCONFIRMED_RALLY")
            gate_log.append(f"UNCONFIRMED_RALLY: inst_tx={inst_tx:.2f}")
        elif gid == "capitulation_watch" and st["status_extension"] == "WASHED" \
                and not np.isnan(ret) and ret < -0.03 and not np.isnan(rvol) and rvol > 1.5:
            flags.append("CAPITULATION_WATCH")
            gate_log.append("CAPITULATION_WATCH")

    total = sum(cat.values())
    max_total = sum(CATEGORY_MAX.values())
    score_100 = round(total / max_total * 100, 1)

    out = {
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
    if collect_trace:
        out["_trace"] = trace
        out["_gate_log"] = gate_log
        out["_status_inputs"] = status_inputs
        out["_pre_gate_cat"] = pre_gate_cat
        out["_price_now"] = price_now
        out["_price_then"] = price_then
    return out


def _size_bucket(mcap: float) -> str:
    if np.isnan(mcap): return "unknown"
    if mcap < 300: return "micro"
    if mcap < 2000: return "small"
    if mcap < 10000: return "mid"
    if mcap < 200000: return "large"
    return "mega"


def _beta_bucket(beta: float) -> str:
    if np.isnan(beta): return "unknown"
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
        rec.update(score_ticker(row, then, horizon, collect_trace=False))
        rows.append(rec)
    return pd.DataFrame(rows).sort_values("total_score", ascending=False)


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
    return g[g["n"] >= min_names].sort_values("med_total", ascending=False).round(2)


def brief(date_str: str, per_horizon, pairs, segments) -> str:
    L = [f"# Daily Universe Scan — {date_str}", "",
         "Deterministic rubric. Full-universe CSVs under data/scores and data/features.",
         "Human tables below are truncated; underlying files are not.", "",
         f"Trace: `python -m src.score_engine --date {date_str} --trace TICKER --horizon 1d`", ""]
    for h in ("1d", "1w", "1m"):
        df = per_horizon.get(h)
        pair = pairs.get(h)
        L.append(f"## Horizon {h}  (pair: {pair or 'NONE — levels only'})")
        if df is None:
            L.append("")
            continue
        L.append("")
        L.append(f"Scored **{len(df)}** tickers (full universe). "
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
        L.append("")
    if segments is not None and len(segments):
        L.append("## Industry segments (1w, min 8)")
        L.append("")
        L.append("| Industry | n | Median score | % positive | Median ret% |")
        L.append("|---|---|---|---|---|")
        for name, r in segments.head(20).iterrows():
            L.append(f"| {str(name)[:34]} | {int(r['n'])} | {r['med_total']:+.1f} | "
                     f"{r['pct_positive']}% | {r['med_ret']} |")
        L.append("")
    return "\n".join(L)


def format_trace(ticker, horizon, pair, meta, result) -> str:
    L = [f"# Score audit — {ticker} — horizon {horizon}", "",
         f"- **Pair:** {pair or 'NONE'}",
         f"- **Company:** {meta.get('Company', '')}",
         f"- **Sector / Industry:** {meta.get('Sector', '')} / {meta.get('Industry', '')}",
         f"- **Total score:** {result['total_score']:+.2f}",
         f"- **True return ret_H:** {result.get('ret_H')}%",
         f"- **Status:** {result['status_extension']} / {result['status_trend']} / "
         f"{result['status_short']} / {result['status_street']}",
         f"- **Flags:** {result['kill_flags'] or '—'}", "",
         "## Status inputs", "", "| Metric | Value |", "|---|---|"]
    for k, v in result.get("_status_inputs", {}).items():
        L.append(f"| {k} | {_fmt(v)} |")
    L += ["", "## Per-rule audit", "",
          "| Field | Kind | Now | Then | Raw | Direction | Signal | W | Points | Skip / override |",
          "|---|---|---|---|---|---|---|---|---|---|"]
    for a in result.get("_trace", []):
        skip = a.get("skipped") or a.get("override") or ""
        raw = a.get("raw")
        raw_s = _fmt(raw) if raw is not None else "—"
        if a["kind"] == "ret" and raw is not None and not (isinstance(raw, float) and np.isnan(raw)):
            raw_s = f"{raw * 100:+.2f}%"
        L.append(
            f"| {a['field']} | {a['kind']} | {_fmt(a.get('now'))} | {_fmt(a.get('then'))} | "
            f"{raw_s} | {a.get('direction') or '—'} | {a.get('signal', 0):+.2f} | "
            f"{a['weight']} | {a.get('points', 0):+.2f} | {skip or '—'} |"
        )
    L += ["", "## Category sums", "", "| Category | Pre-gate | Post-gate |", "|---|---|---|"]
    pre = result.get("_pre_gate_cat", {})
    for c in CATEGORIES:
        L.append(f"| {c} | {pre.get(c, 0):+.2f} | {result.get(f'{c}_score', 0):+.2f} |")
    L += ["", "## Gates", ""]
    gl = result.get("_gate_log") or []
    L.append("_None._" if not gl else "\n".join(f"- {g}" for g in gl))
    L += ["", f"**total_score = {result['total_score']:+.2f}**", ""]
    return "\n".join(L)


def run_traces(tickers, date_str, horizon, dates, target) -> None:
    if date_str not in dates:
        raise SystemExit(f"[trace] no snapshot for {date_str}")
    cur = _add_catalyst_flags(load_dated(dates[date_str]))
    prior = find_prior(dates, target, horizon)
    prev = load_dated(dates[prior]) if prior else None
    prev_map = {t: r for t, r in prev.set_index("Ticker", drop=False).iterrows()} if prev is not None else {}
    cur_idx = cur.set_index("Ticker", drop=False)
    config.DAILY.mkdir(parents=True, exist_ok=True)
    for t in tickers:
        t = t.upper().strip()
        if t not in cur_idx.index:
            print(f"[trace] {t}: not in snapshot")
            continue
        row = cur_idx.loc[t]
        if isinstance(row, pd.DataFrame):
            row = row.iloc[0]
        result = score_ticker(row, prev_map.get(t), horizon, collect_trace=True)
        meta = {c: row.get(c, "") for c in META_COLS}
        text = format_trace(t, horizon, prior, meta, result)
        path = config.DAILY / f"{date_str}_trace_{t}_{horizon}.md"
        path.write_text(text, encoding="utf-8")
        print(text)
        print(f"[trace] wrote {path}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", default=None)
    ap.add_argument("--trace", default=None)
    ap.add_argument("--horizon", default="1d", choices=["1d", "1w", "1m"])
    ap.add_argument("--skip-universe", action="store_true")
    ap.add_argument("--skip-features", action="store_true",
                    help="Skip full-universe feature log write")
    args = ap.parse_args()

    target = (date.fromisoformat(args.date) if args.date else
              datetime.now(ZoneInfo(config.TZ)).date())
    date_str = target.isoformat()
    dates = snapshot_dates()

    if args.trace:
        tickers = [x.strip() for x in args.trace.split(",") if x.strip()]
        run_traces(tickers, date_str, args.horizon, dates, target)
        if args.skip_universe:
            return

    if date_str not in dates:
        raise SystemExit(f"[score] no snapshot for {date_str}; have: {list(dates)[-5:]}")
    cur = load_dated(dates[date_str])

    SCORES_DIR.mkdir(parents=True, exist_ok=True)
    per_horizon: dict = {}
    pairs: dict = {}

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
    config.DAILY.mkdir(parents=True, exist_ok=True)
    brief_path = config.DAILY / f"{date_str}_scan.md"
    brief_path.write_text(text, encoding="utf-8")
    print(f"[score] brief -> {brief_path}")

    # Full-universe feature log (learning database)
    if not args.skip_features:
        try:
            from .feature_log import run_for_date
            run_for_date(date_str)
        except Exception as e:  # noqa: BLE001
            print(f"[score] feature_log failed: {e}")


if __name__ == "__main__":
    main()
