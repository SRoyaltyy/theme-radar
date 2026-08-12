"""Full-universe suggestion check: did scores predict forward direction?

Every ticker with a score + forward label is graded (not only top/bottom).
Top/bottom tables remain as a readable slice.

CLI:
  python -m src.suggestion_check [--scan-date YYYY-MM-DD] [--top 15] [--bottom 10]
  empty scan-date = every date with scores + labels

Writes:
  01_daily/<signal>_suggestion_check.md
  data/attribution/<signal>_suggestion_check.csv   (ALL tickers)
  01_daily/_suggestion_check_BOARD.md
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
    n = h.replace("d", "")
    leg = f"label_date_{n}"
    if leg in lab.columns and lab[leg].notna().any():
        return str(lab[leg].mode().iloc[0])
    return "?"


def _pct(x) -> str:
    if x is None or (isinstance(x, float) and x != x):
        return "n/a"
    return f"{100 * float(x):.1f}%"


def _fwd_pct(x) -> str:
    if x is None or (isinstance(x, float) and x != x):
        return "n/a"
    return f"{100 * float(x):+.2f}%"


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
    entry_col = "entry_price" if "entry_price" in j.columns else "price_T"

    rows_out = []
    summary_h = {}

    for h in horizons:
        fcol = f"fwd_{h}"
        if fcol not in j.columns or j[fcol].notna().sum() < 5:
            continue
        pred = _pred_day(lab, h)
        exit_col = f"exit_price_{h}" if f"exit_price_{h}" in j.columns else None

        sub = j[j[fcol].notna() & j["total_score"].notna()].copy()
        sub["expected"] = np.where(
            sub["total_score"] > 2, "UP",
            np.where(sub["total_score"] < -2, "DOWN", "NEUTRAL"),
        )
        sub["hit"] = np.where(
            sub["expected"] == "UP", sub[fcol] > 0,
            np.where(sub["expected"] == "DOWN", sub[fcol] < 0, np.nan),
        )

        actionable = sub[sub["expected"] != "NEUTRAL"]
        hits = actionable["hit"].dropna().astype(bool)
        long_m = actionable["expected"] == "UP"
        short_m = actionable["expected"] == "DOWN"
        ic = (
            float(sub["total_score"].rank().corr(sub[fcol].rank()))
            if len(sub) >= 30 else float("nan")
        )

        summary_h[h] = {
            "prediction_day": pred,
            "n_universe": int(len(sub)),
            "n_actionable": int(len(actionable)),
            "n_long": int(long_m.sum()),
            "n_short": int(short_m.sum()),
            "accuracy_actionable": float(hits.mean()) if len(hits) else float("nan"),
            "accuracy_long": float(actionable.loc[long_m, "hit"].mean()) if long_m.any() else float("nan"),
            "accuracy_short": float(actionable.loc[short_m, "hit"].mean()) if short_m.any() else float("nan"),
            "mean_fwd_long": float(actionable.loc[long_m, fcol].mean()) if long_m.any() else float("nan"),
            "mean_fwd_short": float(actionable.loc[short_m, fcol].mean()) if short_m.any() else float("nan"),
            "ic_score_fwd": ic,
        }

        for _, r in sub.iterrows():
            hv = r["hit"]
            hit_v = bool(hv) if hv == hv else None
            rows_out.append({
                "signal_asof": signal,
                "prediction_day": pred,
                "horizon": h,
                "Ticker": r["Ticker"],
                "Industry": r.get("Industry", ""),
                "total_score": r.get("total_score"),
                "entry_price": r.get(entry_col),
                "exit_price": r.get(exit_col) if exit_col else None,
                "fwd": r.get(fcol),
                "expected": r["expected"],
                "hit": hit_v,
            })

    if not summary_h:
        print(f"[suggest] {signal}: no forward horizons with data")
        return None

    result = {
        "signal_asof": signal,
        "top_n": top_n,
        "bottom_n": bottom_n,
        "horizons": summary_h,
        "rows": rows_out,
        "ranked": j,
    }
    _write(result)
    return {k: v for k, v in result.items() if k != "ranked"}


def _write(result: dict) -> None:
    signal = result["signal_asof"]
    ATTR_DIR.mkdir(parents=True, exist_ok=True)
    config.DAILY.mkdir(parents=True, exist_ok=True)

    pdf = pd.DataFrame(result["rows"])
    csv_path = ATTR_DIR / f"{signal}_suggestion_check.csv"
    pdf.to_csv(csv_path, index=False)

    L = [
        f"# Suggestion check — signal **{signal}** (full universe)",
        "",
        "## What this measures",
        "",
        f"- **Signal as-of:** **{signal}** — `total_score` from data through this day only.",
        "- **Expected UP** if score > +2; **Expected DOWN** if score < −2; else NEUTRAL (excluded from accuracy).",
        "- **Hit** = expected UP and fwd>0, or expected DOWN and fwd<0.",
        "- **fwd** = exit/entry − 1 on a **later** snapshot (not scan.md same-window Ret%).",
        f"- **Full universe CSV:** `data/attribution/{signal}_suggestion_check.csv`",
        "",
        "## Prediction accuracy (full universe)",
        "",
        "| Horizon | Pred day | n universe | n actionable | Accuracy | Long acc | Short acc | IC(score,fwd) | Mean fwd long | Mean fwd short |",
        "|---------|----------|------------|--------------|----------|----------|-----------|---------------|---------------|----------------|",
    ]
    for h, s in result["horizons"].items():
        ic = s["ic_score_fwd"]
        ic_s = f"{ic:+.4f}" if ic == ic else "n/a"
        L.append(
            f"| {h} | {s['prediction_day']} | {s['n_universe']} | {s['n_actionable']} | "
            f"**{_pct(s['accuracy_actionable'])}** | {_pct(s['accuracy_long'])} | "
            f"{_pct(s['accuracy_short'])} | {ic_s} | "
            f"{_fwd_pct(s['mean_fwd_long'])} | {_fwd_pct(s['mean_fwd_short'])} |"
        )

    ranked = result["ranked"]
    h0 = "1d" if "1d" in result["horizons"] else next(iter(result["horizons"]))
    pred = result["horizons"][h0]["prediction_day"]
    fcol = f"fwd_{h0}"
    top = ranked.head(result["top_n"])
    bot = ranked.tail(result["bottom_n"])

    L += [
        "",
        f"## Readable slice — horizon {h0} (pred day **{pred}**)",
        "_(every ticker is in the CSV)_",
        "",
    ]

    for part, title, exp in (
        (top, f"Top {result['top_n']} scores", "UP"),
        (bot, f"Bottom {result['bottom_n']} scores", "DOWN"),
    ):
        L.append(f"### {title}")
        L.append("")
        L.append("| Ticker | Score | Entry | Exit | fwd | Hit? |")
        L.append("|---|---|---|---|---|---|")
        for _, r in part.iterrows():
            fwd = r.get(fcol)
            if fwd != fwd:
                hit_s = "n/a"
            elif exp == "UP":
                hit_s = "YES" if fwd > 0 else "NO"
            else:
                hit_s = "YES" if fwd < 0 else "NO"
            entry = r.get("entry_price", r.get("price_T"))
            exit_p = r.get(f"exit_price_{h0}", r.get(f"price_T{h0[0]}"))
            L.append(
                f"| {r['Ticker']} | {r['total_score']:+.1f} | {entry} | {exit_p} | "
                f"{_fwd_pct(fwd)} | **{hit_s}** |"
            )
        L.append("")

    path = config.DAILY / f"{signal}_suggestion_check.md"
    path.write_text("\n".join(L), encoding="utf-8")
    print(f"[suggest] {signal} universe rows={len(pdf)} -> {path.name}")


def write_board(results: list[dict]) -> Path:
    L = [
        "# Suggestion check board — full universe accuracy",
        "",
        "Score on **signal_asof**; grade on later **prediction day**. "
        "Accuracy = share of actionable names (score >+2 or <-2) whose forward "
        "return matched the expected direction.",
        "",
        "| Signal | Pred day (1d) | n actionable | Accuracy | Long acc | Short acc | IC |",
        "|--------|---------------|--------------|----------|----------|-----------|----|",
    ]
    for r in results:
        h = r["horizons"].get("1d") or next(iter(r["horizons"].values()))
        ic = h.get("ic_score_fwd")
        ic_s = f"{ic:+.4f}" if ic == ic else "n/a"
        L.append(
            f"| {r['signal_asof']} | {h.get('prediction_day')} | "
            f"{h.get('n_actionable')} | **{_pct(h.get('accuracy_actionable'))}** | "
            f"{_pct(h.get('accuracy_long'))} | {_pct(h.get('accuracy_short'))} | {ic_s} |"
        )
    L += [
        "",
        "Detail: `01_daily/<signal>_suggestion_check.md`",
        "All tickers: `data/attribution/<signal>_suggestion_check.csv`",
        "Factors + combos: `03_scoreboard/predictive_audit.md`",
        "",
    ]
    path = config.DAILY / "_suggestion_check_BOARD.md"
    config.DAILY.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(L), encoding="utf-8")
    print(f"[suggest] board -> {path}")
    return path


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--scan-date", default=None)
    ap.add_argument("--top", type=int, default=15)
    ap.add_argument("--bottom", type=int, default=10)
    args = ap.parse_args()

    if args.scan_date:
        check_one(args.scan_date, top_n=args.top, bottom_n=args.bottom)
        return

    signals = sorted(p.name.replace("_fwd.csv", "") for p in LABELS_DIR.glob("*_fwd.csv"))
    results = []
    for s in signals:
        r = check_one(s, top_n=args.top, bottom_n=args.bottom)
        if r:
            results.append(r)
    if results:
        write_board(results)


if __name__ == "__main__":
    main()
