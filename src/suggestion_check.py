"""Did high/low score names actually move the expected way *after* the signal?

This is the non-circular check the scan.md table cannot answer:
  - Signal = scores on day T (data through T only)
  - Outcome = price change from T → later snapshot(s)
  - Top scores are treated as long suggestions; bottom as short/avoid

CLI:
  python -m src.suggestion_check [--scan-date YYYY-MM-DD] [--top 15] [--bottom 10]
  (empty scan-date = every date that has scores + labels)

Writes:
  01_daily/<signal>_suggestion_check.md
  data/attribution/<signal>_suggestion_check.csv
  01_daily/_suggestion_check_BOARD.md   (when running all dates)
"""
from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd

from . import config

SCORES_DIR = config.DATA / "scores"
LABELS_DIR = config.DATA / "labels"
ATTR_DIR = config.DATA / "attribution"


def _load_scores(signal: str) -> pd.DataFrame | None:
    path = SCORES_DIR / f"{signal}_1d.csv"
    if not path.exists():
        # fall back to features if scores missing but total_score present
        alt = config.DATA / "features" / f"{signal}_1d.csv"
        if not alt.exists():
            return None
        path = alt
    df = pd.read_csv(path, low_memory=False)
    if "total_score" not in df.columns or "Ticker" not in df.columns:
        return None
    return df


def _load_labels(signal: str) -> pd.DataFrame | None:
    path = LABELS_DIR / f"{signal}_fwd.csv"
    if not path.exists():
        return None
    return pd.read_csv(path, low_memory=False)


def _pred_day(lab: pd.DataFrame, h: str) -> str:
    col = f"prediction_day_{h}"
    if col in lab.columns and lab[col].astype(str).str.len().gt(0).any():
        return str(lab[col].mode().iloc[0])
    legacy = f"label_date_{h[0]}" if h.endswith("d") else ""
    # label_date_1 for 1d
    n = h.replace("d", "")
    leg = f"label_date_{n}"
    if leg in lab.columns and lab[leg].notna().any():
        return str(lab[leg].mode().iloc[0])
    return "?"


def _hit_long(fwd) -> bool | None:
    if fwd is None or (isinstance(fwd, float) and fwd != fwd):
        return None
    return bool(fwd > 0)


def _hit_short(fwd) -> bool | None:
    if fwd is None or (isinstance(fwd, float) and fwd != fwd):
        return None
    return bool(fwd < 0)


def check_one(signal: str, top_n: int = 15, bottom_n: int = 10,
              horizons: tuple[str, ...] = ("1d", "2d", "3d")) -> dict | None:
    scores = _load_scores(signal)
    lab = _load_labels(signal)
    if scores is None or lab is None:
        print(f"[suggest] {signal}: need scores + labels — skip")
        return None

    j = scores.merge(lab, on="Ticker", how="inner", suffixes=("", "_lbl"))
    if j.empty or j["total_score"].notna().sum() < 20:
        print(f"[suggest] {signal}: insufficient join rows")
        return None

    j = j.sort_values("total_score", ascending=False)
    top = j.head(top_n).copy()
    bot = j.tail(bottom_n).copy()
    top["bucket"] = "TOP_LONG"
    bot["bucket"] = "BOTTOM_SHORT"

    rows_out = []
    summary_h = {}

    for h in horizons:
        fcol = f"fwd_{h}"
        if fcol not in j.columns or j[fcol].notna().sum() < 5:
            continue
        pred = _pred_day(lab, h)
        entry_col = "entry_price" if "entry_price" in j.columns else "price_T"
        exit_col = f"exit_price_{h}" if f"exit_price_{h}" in j.columns else f"price_T{h[0]}"

        def pack(part: pd.DataFrame, side: str):
            local = []
            hits = []
            for _, r in part.iterrows():
                fwd = r.get(fcol)
                if side == "long":
                    hit = _hit_long(fwd)
                else:
                    hit = _hit_short(fwd)
                if hit is not None:
                    hits.append(hit)
                local.append({
                    "signal_asof": signal,
                    "prediction_day": pred,
                    "horizon": h,
                    "bucket": r["bucket"],
                    "Ticker": r["Ticker"],
                    "Industry": r.get("Industry", ""),
                    "total_score": r.get("total_score"),
                    "entry_price": r.get(entry_col),
                    "exit_price": r.get(exit_col),
                    "fwd": fwd,
                    "expected": "UP" if side == "long" else "DOWN",
                    "hit": hit,
                })
            return local, hits

        t_rows, t_hits = pack(top, "long")
        b_rows, b_hits = pack(bot, "short")
        rows_out.extend(t_rows)
        rows_out.extend(b_rows)

        summary_h[h] = {
            "prediction_day": pred,
            "top_n": len(t_hits),
            "top_hit_rate": float(np.mean(t_hits)) if t_hits else float("nan"),
            "top_mean_fwd": float(top[fcol].mean()) if top[fcol].notna().any() else float("nan"),
            "bottom_n": len(b_hits),
            "bottom_hit_rate": float(np.mean(b_hits)) if b_hits else float("nan"),
            "bottom_mean_fwd": float(bot[fcol].mean()) if bot[fcol].notna().any() else float("nan"),
        }

    if not summary_h:
        print(f"[suggest] {signal}: no forward horizons with data")
        return None

    result = {
        "signal_asof": signal,
        "top_n": top_n,
        "bottom_n": bottom_n,
        "horizons": summary_h,
        "rows": rows_out,
    }
    _write(result)
    return result


def _pct(x) -> str:
    if x is None or (isinstance(x, float) and x != x):
        return "n/a"
    return f"{100 * float(x):.1f}%"


def _fwd_pct(x) -> str:
    if x is None or (isinstance(x, float) and x != x):
        return "n/a"
    return f"{100 * float(x):+.2f}%"


def _write(result: dict) -> None:
    signal = result["signal_asof"]
    ATTR_DIR.mkdir(parents=True, exist_ok=True)
    config.DAILY.mkdir(parents=True, exist_ok=True)

    pdf = pd.DataFrame(result["rows"])
    csv_path = ATTR_DIR / f"{signal}_suggestion_check.csv"
    pdf.to_csv(csv_path, index=False)

    L = [
        f"# Suggestion check — signal **{signal}**",
        "",
        "## What this is (not the scan.md Ret% table)",
        "",
        f"- **Signal as-of:** **{signal}** — scores ranked using only data through this day.",
        "- **TOP_LONG:** highest `total_score` → we *expected* price **up** after the signal.",
        "- **BOTTOM_SHORT:** lowest `total_score` → we *expected* price **down** after the signal.",
        "- **Hit:** long and forward return > 0, or short and forward return < 0.",
        "- **fwd** uses **entry = Price @ signal**, **exit = Price @ prediction day** "
        "(later snapshot). This is *after* the signal — not the same-day Ret% on the scan.",
        "",
        "## Summary by horizon",
        "",
        "| Horizon | Prediction day | Top hit rate | Top mean fwd | Bottom hit rate | Bottom mean fwd |",
        "|---------|----------------|--------------|--------------|-----------------|-----------------|",
    ]
    for h, s in result["horizons"].items():
        L.append(
            f"| {h} | {s['prediction_day']} | {_pct(s['top_hit_rate'])} "
            f"(n={s['top_n']}) | {_fwd_pct(s['top_mean_fwd'])} | "
            f"{_pct(s['bottom_hit_rate'])} (n={s['bottom_n']}) | "
            f"{_fwd_pct(s['bottom_mean_fwd'])} |"
        )

    # detail for 1d if present else first horizon
    h0 = "1d" if "1d" in result["horizons"] else next(iter(result["horizons"]))
    pred = result["horizons"][h0]["prediction_day"]
    L += ["", f"## Detail — horizon {h0} (prediction day **{pred}**)", ""]

    for bucket, title in (("TOP_LONG", "Top scores (expected UP)"),
                          ("BOTTOM_SHORT", "Bottom scores (expected DOWN)")):
        sub = pdf[(pdf["bucket"] == bucket) & (pdf["horizon"] == h0)]
        L.append(f"### {title}")
        L.append("")
        L.append(
            "| Ticker | Score | Entry @ signal | Exit @ pred day | fwd | Expected | Hit? |"
        )
        L.append("|---|---|---|---|---|---|---|")
        for _, r in sub.iterrows():
            hit = r["hit"]
            hit_s = "YES" if hit is True else ("NO" if hit is False else "n/a")
            L.append(
                f"| {r['Ticker']} | {r['total_score']:+.1f} | "
                f"{r.get('entry_price')} | {r.get('exit_price')} | "
                f"{_fwd_pct(r.get('fwd'))} | {r['expected']} | **{hit_s}** |"
            )
        L.append("")

    L.append(f"CSV: `data/attribution/{signal}_suggestion_check.csv`")
    L.append("")
    path = config.DAILY / f"{signal}_suggestion_check.md"
    path.write_text("\n".join(L), encoding="utf-8")
    print(f"[suggest] {signal} -> {path.name} + {csv_path.name}")


def write_board(results: list[dict]) -> Path:
    L = [
        "# Suggestion check — all eligible signal dates",
        "",
        "Each row: scores on **signal_asof**, graded on a **later** prediction day.",
        "",
        "| Signal as-of | Pred day (1d) | Top hit | Top mean fwd | Bottom hit | Bottom mean fwd |",
        "|--------------|---------------|---------|--------------|------------|-----------------|",
    ]
    for r in results:
        h = r["horizons"].get("1d") or next(iter(r["horizons"].values()))
        L.append(
            f"| {r['signal_asof']} | {h.get('prediction_day')} | "
            f"{_pct(h.get('top_hit_rate'))} | {_fwd_pct(h.get('top_mean_fwd'))} | "
            f"{_pct(h.get('bottom_hit_rate'))} | {_fwd_pct(h.get('bottom_mean_fwd'))} |"
        )
    L.append("")
    L.append("Per-date detail: `01_daily/<signal>_suggestion_check.md`")
    L.append("")
    path = config.DAILY / "_suggestion_check_BOARD.md"
    config.DAILY.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(L), encoding="utf-8")
    print(f"[suggest] board -> {path}")
    return path


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--scan-date", default=None, help="Signal as-of date; empty = all")
    ap.add_argument("--top", type=int, default=15)
    ap.add_argument("--bottom", type=int, default=10)
    args = ap.parse_args()

    if args.scan_date:
        check_one(args.scan_date, top_n=args.top, bottom_n=args.bottom)
        return

    signals = sorted(
        p.name.replace("_fwd.csv", "")
        for p in LABELS_DIR.glob("*_fwd.csv")
    )
    results = []
    for s in signals:
        r = check_one(s, top_n=args.top, bottom_n=args.bottom)
        if r:
            results.append(r)
    if results:
        write_board(results)


if __name__ == "__main__":
    main()
