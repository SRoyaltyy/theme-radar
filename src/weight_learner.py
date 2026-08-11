"""Weight learner — champion/challenger tuning of rubric rule weights.

Reads every features+labels pair and, for each rubric rule with a PLAIN
polarity (+, -, pct:+, pct:-), measures the rule's *aligned* IC vs forward
returns (feature direction corrected for the rule's polarity). From that it
proposes a weight multiplier, then re-scores the whole universe with the
challenger weights and compares against the champion (current) score.

Curved-polarity rules (curve:rvol, curve:rsi, ...) are never auto-adjusted:
their sign depends on the level, so a single IC cannot describe them. They
are listed as "not adjustable" in the log.

Promotion gates (ALL must hold, else nothing changes):
  * >= 3 distinct label dates — anything less is curve-fitting noise
  * challenger mean per-date IC > champion mean per-date IC + MIN_IC_GAIN
    on the primary horizon (the horizon with the most label dates)
  * challenger >= champion on at least half of the individual dates

Only rules that actually vote on the 1d score can be challenger-tested,
because only 1d feature logs exist. Proposals for 1w/1m-only rules are
logged as UNTESTED.

Outputs:
  data/weight_overrides.json        {"multipliers": {"<field>|<kind>": m}}
                                    (only written/updated on promotion)
  03_scoreboard/weight_learning.md  full decision log (always written)

CLI: python -m src.weight_learner
"""
from __future__ import annotations

import json
from datetime import datetime
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd

from . import config
from .score_rubric import RET_DEADZONE, RUBRIC, STATUS

FEATURES_DIR = config.DATA / "features"
LABELS_DIR = config.DATA / "labels"
OVERRIDES_PATH = config.DATA / "weight_overrides.json"
LOG_PATH = config.SCOREBOARD_DIR / "weight_learning.md"

HORIZONS = ("1d", "2d", "3d")
MIN_ROWS = 30
MIN_DATES = 3
MIN_IC_GAIN = 0.001
MAX_DELTA = (0.5, 1.5)     # per-run multiplier clamp
ABS_CLAMP = (0.25, 2.0)    # absolute multiplier clamp (compounded)
PLAIN_POLARITIES = {"+", "-", "pct:+", "pct:-"}


def _key(rule: dict) -> str:
    return f"{rule['field']}|{rule['kind']}"


def _spearman(a: pd.Series, b: pd.Series) -> float:
    m = a.notna() & b.notna()
    if m.sum() < MIN_ROWS:
        return float("nan")
    return float(a[m].rank().corr(b[m].rank()))


def _load_overrides() -> dict:
    try:
        return json.loads(OVERRIDES_PATH.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def _rule_raw(df: pd.DataFrame, rule: dict) -> pd.Series | None:
    """Reconstruct the exact raw series score_engine uses for this rule."""
    field, kind, pol = rule["field"], rule["kind"], rule["polarity"]
    if kind == "ret":
        return df["true_ret"] if "true_ret" in df.columns else None
    if kind == "delta":
        dcol = f"d_{field}"
        if dcol not in df.columns:
            return None
        if str(pol).startswith("pct:"):
            if field not in df.columns:
                return None
            then = df[field] - df[dcol]          # d_ = now - then
            return df[dcol] / then.replace(0, np.nan)
        return df[dcol]
    # level
    if field == "n_catalysts":
        return df["n_catalysts"] if "n_catalysts" in df.columns else None
    if field == "upside_pct":
        return df["upside_pct_lvl"] if "upside_pct_lvl" in df.columns else None
    return df[field] if field in df.columns else None


def _rule_signal(df: pd.DataFrame, rule: dict) -> pd.Series | None:
    """Replicate score_engine's signal s (plain polarities only), including
    the momentum/rsi status overrides."""
    raw = _rule_raw(df, rule)
    if raw is None:
        return None
    dz = (RET_DEADZONE["1d"] if rule["kind"] == "ret"
          else float(rule["deadzone"] or 0))
    s = pd.Series(0.0, index=df.index)
    s[raw > dz] = 1.0
    s[raw < -dz] = -1.0
    if str(rule["polarity"]).lstrip("pct:") == "-":
        s = -s
    if rule.get("status_mode") == "momentum" and "status_extension" in df:
        extreme = df["status_extension"] == "EXTREME"
        s = s.where(~(extreme & (s > 0)), -1.0)
    if rule.get("status_mode") == "rsi" \
            and "Relative Strength Index (14)" in df:
        rsi = df["Relative Strength Index (14)"]
        s = s.where(~((rsi > STATUS["extended_rsi"]) & (s > 0)), 0.0)
    return s


def _gate_price(pre: pd.Series, status_ext: pd.Series,
                upside: pd.Series) -> pd.Series:
    """Replicate the ordered elif gates that touch cat.price on the 1d
    horizon (downtrend gate never fires on 1d)."""
    post = pre.copy()
    m1 = (status_ext == "EXTENDED") & (pre > 0)
    post = post.where(~m1, pre * 0.25)
    m2 = ~m1 & (status_ext == "EXTREME") & (pre > 0)
    post = post.where(~m2, -pre.abs() * 0.5)
    m3 = ~m1 & ~m2 & (upside < 0) & (pre > 0)
    post = post.where(~m3, pre * 0.5)
    return post


def _load_pairs() -> list[tuple[str, pd.DataFrame]]:
    pairs = []
    for fp in sorted(FEATURES_DIR.glob("*_1d.csv")):
        d = fp.stem.replace("_1d", "")
        lp = LABELS_DIR / f"{d}_fwd.csv"
        if not lp.exists():
            continue
        f = pd.read_csv(fp, low_memory=False)
        l = pd.read_csv(lp, low_memory=False)
        j = f.merge(l, on="Ticker", how="inner", suffixes=("", "_lbl"))
        pairs.append((d, j))
    return pairs


def main() -> None:
    pairs = _load_pairs()
    log = ["# Weight learning — decision log", "",
           f"_Generated {datetime.now(ZoneInfo(config.TZ)).strftime('%Y-%m-%d %H:%M %Z')}_",
           ""]
    if not pairs:
        print("[weights] no labeled pairs — nothing to learn")
        return

    overrides = _load_overrides()
    base_mult: dict[str, float] = {k: float(v) for k, v in
                                   overrides.get("multipliers", {}).items()}

    plain_rules = [r for r in RUBRIC if r["polarity"] in PLAIN_POLARITIES]
    curved = [r for r in RUBRIC if r["polarity"] not in PLAIN_POLARITIES]
    active_1d = [r for r in plain_rules
                 if "1d" in r["horizons"] and r["speed"] == "fast"]

    # ---- per-rule aligned ICs (all plain rules, all horizons) ----
    aligned: dict[str, dict[str, list[float]]] = {}
    label_dates: dict[str, set] = {h: set() for h in HORIZONS}
    for d, df in pairs:
        for h in HORIZONS:
            y = df.get(f"fwd_{h}")
            if y is None or y.notna().sum() < MIN_ROWS:
                continue
            label_dates[h].add(d)
            for rule in plain_rules:
                raw = _rule_raw(df, rule)
                if raw is None:
                    continue
                a = -raw if str(rule["polarity"]).lstrip("pct:") == "-" else raw
                ic = _spearman(a, y)
                if ic == ic:
                    aligned.setdefault(_key(rule), {}).setdefault(h, []).append(ic)

    n_dates_primary = max((len(v) for v in label_dates.values()), default=0)
    primary_h = max(label_dates, key=lambda h: len(label_dates[h])) \
        if n_dates_primary else "1d"

    log += [f"- label dates per horizon: "
            + ", ".join(f"{h}: {len(label_dates[h])}" for h in HORIZONS),
            f"- primary horizon for promotion test: **{primary_h}** "
            f"({len(label_dates[primary_h])} dates)",
            f"- existing overrides: {base_mult or 'none (champion = base rubric)'}",
            "", "## Per-rule aligned IC (direction corrected for polarity)", "",
            "| Rule | Horizon | Mean aligned IC | Dates | Proposed × | Testable |",
            "|---|---|---|---|---|---|"]

    proposals: dict[str, float] = {}
    for rule in plain_rules:
        k = _key(rule)
        testable = rule in active_1d
        for h in HORIZONS:
            ics = aligned.get(k, {}).get(h, [])
            if not ics:
                continue
            mean_ic = float(np.mean(ics))
            delta = float(np.clip(1 + 2 * mean_ic, *MAX_DELTA))
            new = float(np.clip(base_mult.get(k, 1.0) * delta, *ABS_CLAMP))
            if h == primary_h:
                proposals[k] = new
            log.append(f"| {k} | {h} | {mean_ic:+.4f} | {len(ics)} | "
                       f"{new:.3f} | {'yes' if testable else 'NO — logs only'} |")
    for rule in curved:
        log.append(f"| {_key(rule)} | — | n/a (curved polarity) | — | 1.000 "
                   f"| not adjustable |")
    log.append("")

    # ---- champion vs challenger on the 1d score ----
    price_rules = [r for r in active_1d if r["category"] == "price"]
    other_rules = [r for r in active_1d if r["category"] != "price"]

    per_date_rows = []
    for d, df in pairs:
        sig = {}
        for rule in active_1d:
            s = _rule_signal(df, rule)
            if s is not None:
                sig[_key(rule)] = s
        if "total_score" not in df.columns or not sig:
            continue
        base_pre = sum(sig[_key(r)] * r["weight"] * base_mult.get(_key(r), 1.0)
                       for r in price_rules if _key(r) in sig)
        status_ext = df.get("status_extension", pd.Series("", index=df.index))
        upside = df.get("upside_pct", pd.Series(np.nan, index=df.index))

        # champion reconstruction sanity check vs stored price_score
        recon_post = _gate_price(base_pre, status_ext, upside)
        recon_err = float((recon_post - df["price_score"]).abs().mean()) \
            if "price_score" in df.columns else float("nan")

        chal_pre = sum(sig[_key(r)] * r["weight"]
                       * proposals.get(_key(r), base_mult.get(_key(r), 1.0))
                       for r in price_rules if _key(r) in sig)
        chal_post = _gate_price(chal_pre, status_ext, upside)
        challenger = (df["total_score"] - df["price_score"] + chal_post
                      if "price_score" in df.columns else df["total_score"])
        for r in other_rules:
            k = _key(r)
            if k not in sig:
                continue
            challenger = challenger + sig[k] * r["weight"] * (
                proposals.get(k, base_mult.get(k, 1.0))
                - base_mult.get(k, 1.0))

        row = {"scan_date": d, "recon_err": recon_err, "horizons": {}}
        for h in HORIZONS:
            y = df.get(f"fwd_{h}")
            if y is None or y.notna().sum() < MIN_ROWS:
                continue
            row["horizons"][h] = {
                "champion_ic": _spearman(df["total_score"], y),
                "challenger_ic": _spearman(challenger, y),
                "n": int(y.notna().sum()),
            }
        per_date_rows.append(row)

    log += ["## Champion vs challenger (1d score)", "",
            "| Scan date | Horizon | Champion IC | Challenger IC | Δ |",
            "|---|---|---|---|---|"]
    gains: dict[str, list[float]] = {h: [] for h in HORIZONS}
    for row in per_date_rows:
        for h, st in row["horizons"].items():
            c, x = st["champion_ic"], st["challenger_ic"]
            if c != c or x != x:
                continue
            gains[h].append(x - c)
            log.append(f"| {row['scan_date']} | {h} | {c:+.4f} | {x:+.4f} | "
                       f"{x - c:+.4f} |")
    recon_errs = [r["recon_err"] for r in per_date_rows
                  if r["recon_err"] == r["recon_err"]]
    if recon_errs:
        log.append(f"\n_Champion reconstruction check: mean |rebuilt price "
                   f"category − stored price_score| = {np.mean(recon_errs):.4f} "
                   f"(should be ~0; large values mean the learner's model of "
                   f"the engine has drifted from score_engine — distrust this "
                   f"run)._")
    log.append("")

    # ---- decision ----
    g = [v for v in gains.get(primary_h, []) if v == v]
    mean_gain = float(np.mean(g)) if g else float("nan")
    frac_nonneg = float(np.mean([v >= 0 for v in g])) if g else 0.0
    changed = {k: v for k, v in proposals.items()
               if abs(v - base_mult.get(k, 1.0)) > 1e-9}

    log.append("## Decision")
    log.append("")
    if n_dates_primary < MIN_DATES:
        verdict = (f"NO PROMOTION — only {n_dates_primary} distinct label "
                   f"date(s) on {primary_h}; need >= {MIN_DATES}. Learning "
                   f"starts once more daily snapshots accumulate.")
    elif not changed:
        verdict = "NO PROMOTION — no rule's proposal differs from current weights."
    elif not (mean_gain == mean_gain):
        verdict = "NO PROMOTION — no evaluable dates."
    elif mean_gain <= MIN_IC_GAIN:
        verdict = (f"NO PROMOTION — challenger mean IC gain "
                   f"{mean_gain:+.4f} on {primary_h} does not clear "
                   f"+{MIN_IC_GAIN}.")
    elif frac_nonneg < 0.5:
        verdict = (f"NO PROMOTION — challenger only improved on "
                   f"{frac_nonneg * 100:.0f}% of dates (< 50%).")
    else:
        verdict = (f"PROMOTED — challenger mean IC gain {mean_gain:+.4f} on "
                   f"{primary_h}, improved on {frac_nonneg * 100:.0f}% of "
                   f"{len(g)} dates. New multipliers: "
                   + ", ".join(f"{k} ×{v:.3f}" for k, v in changed.items()))
        new_mults = dict(base_mult)
        new_mults.update(changed)
        OVERRIDES_PATH.parent.mkdir(parents=True, exist_ok=True)
        OVERRIDES_PATH.write_text(json.dumps({
            "promoted_at": datetime.now(ZoneInfo(config.TZ)).isoformat(),
            "primary_horizon": primary_h,
            "mean_ic_gain": mean_gain,
            "multipliers": new_mults,
        }, indent=2), encoding="utf-8")
        print(f"[weights] PROMOTED new multipliers: {changed}")
    log.append(verdict)
    log.append("")
    log.append("_Note: curved-polarity rules (rvol/rsi/sma/short/upside/debt "
               "curves) are never auto-adjusted; change those in "
               "score_rubric.py by hand with git history as the audit "
               "trail._")

    config.SCOREBOARD_DIR.mkdir(parents=True, exist_ok=True)
    LOG_PATH.write_text("\n".join(log) + "\n", encoding="utf-8")
    print(f"[weights] {verdict}")
    print(f"[weights] log -> {LOG_PATH}")


if __name__ == "__main__":
    main()
