#!/usr/bin/env python3
"""Clock-B opportunity set — APPEND-ONLY builder (features from finviz_asof=T-1
for join_morning=T).

Replaces the old full-rebuild script (/workspace/theme-radar-top-gainers/
build_oppset_clock_b.py, which re-derived every past morning from whatever raw
files were on disk and so silently rewrote past rows when a snapshot was
re-fetched — e.g. join_morning 2026-09-22 in dea3ff6 and 2026-09-23 in 69d7c6b).

Rules (IRONCLAD, 2026-09-25):
  * Each refresh adds ONE new join_morning: T = next US trading day after
    finviz_asof (default: latest data/snapshots/YYYY-MM-DD.raw.csv).
  * Rows of earlier mornings are never recomputed or rewritten. They are
    fingerprinted in research/oppset_clock_b/FINGERPRINTS.json (row-level
    sha256 per join_morning, see src/history_guard.py); the refresh verifies
    them first and fails if any committed row changed.
  * The only overwrite allowed is a same-day rerun: the morning whose
    finviz_asof == today (ET), e.g. after today's snapshot is re-fetched.
  * Columns added later as outcome grades (e.g. fwd_2d/3d/5d) are fill-once:
    once a morning's cells in such a column are set, their fingerprint is
    recorded and may never change (history_guard.fp_grouped "grade:" parts).
  * oppset_0916_0918.csv (proof mornings) is static.

Feature/filter/flag logic is byte-for-byte the original (load_raw, clean_midcap,
add_flags, OUT_COLS) — not a strategy change.

Usage (from repo root):
  python -m research.oppset_clock_b.build_oppset_clock_b            # append latest
  python -m research.oppset_clock_b.build_oppset_clock_b --asof 2026-09-25
  python -m research.oppset_clock_b.build_oppset_clock_b --verify-only
Exit codes: 0 ok / nothing to add, 1 past rows changed or refused, 2 bad input.
"""
from __future__ import annotations

import argparse
import csv
import io
import re
import sys
from datetime import date
from pathlib import Path

import numpy as np
import pandas as pd

REPO = Path(__file__).resolve().parents[2]
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))
from src import history_guard as hg  # noqa: E402
from src.trading_calendar import next_trading_day  # noqa: E402

OUT_DEFAULT = REPO / "research" / "oppset_clock_b"
RAW_DEFAULT = REPO / "data" / "snapshots"
RAW_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})\.raw\.csv$")
RAW = RAW_DEFAULT  # load_raw() reads RAW / f"{date}.raw.csv"

NOISE_CO = re.compile(
    r"\b(ETF|Fund|Trust|Warrant|Acquisition Corp|Blank Check|SPAC|Unit|Preferred)\b",
    re.I,
)
NOISE_IND = re.compile(r"\b(Exchange Traded Fund|Closed-End Fund|Shell Company)\b", re.I)


def parse_num(s):
    if pd.isna(s):
        return np.nan
    if isinstance(s, (int, float)):
        return float(s)
    t = str(s).strip().replace(",", "").replace("%", "")
    if t in ("", "-", "None", "nan"):
        return np.nan
    mult = 1.0
    if t.endswith(("M", "B", "K")):
        mult = {"K": 1e3, "M": 1e6, "B": 1e9}[t[-1]]
        t = t[:-1]
    try:
        return float(t) * mult
    except ValueError:
        return np.nan


def pick(df, *cands):
    for c in cands:
        if c in df.columns:
            return c
    return None


def load_raw(date: str) -> pd.DataFrame:
    path = RAW / f"{date}.raw.csv"
    if not path.exists() or path.stat().st_size < 1000:
        raise FileNotFoundError(f"missing raw {path}")
    df = pd.read_csv(path, low_memory=False)
    df = df.rename(columns={c: c.strip() for c in df.columns})
    tcol = pick(df, "Ticker", "ticker")
    etf = pick(df, "ETF Type", "ETFType")
    company = pick(df, "Company")
    industry = pick(df, "Industry")
    out = pd.DataFrame({
        "ticker": df[tcol].astype(str).str.upper().str.strip() if tcol else np.nan,
        "company": df[company].astype(str) if company else "",
        "industry": df[industry].astype(str) if industry else "",
        "etf_type": df[etf] if etf else np.nan,
        "sector": df[pick(df, "Sector")].astype(str) if pick(df, "Sector") else "",
        "price": df[pick(df, "Price")].map(parse_num) if pick(df, "Price") else np.nan,
        # Finviz Average Volume is in thousands
        "avg_vol": df[pick(df, "Average Volume", "Avg Volume")].map(parse_num)
        if pick(df, "Average Volume", "Avg Volume") else np.nan,
        # Finviz Market Cap is in millions
        "mcap": df[pick(df, "Market Cap", "Market Cap.")].map(parse_num)
        if pick(df, "Market Cap", "Market Cap.") else np.nan,
        "rvol": df[pick(df, "Relative Volume", "Rel Volume")].map(parse_num)
        if pick(df, "Relative Volume", "Rel Volume") else np.nan,
        "change_pct": df[pick(df, "Change", "Change %")].map(parse_num)
        if pick(df, "Change", "Change %") else np.nan,
        "chg_open_pct": df[pick(df, "Change from Open")].map(parse_num)
        if pick(df, "Change from Open") else np.nan,
        "gap_pct": df[pick(df, "Gap", "Gap %")].map(parse_num)
        if pick(df, "Gap", "Gap %") else np.nan,
        "ah_change_pct": df[pick(df, "After-Hours Change")].map(parse_num)
        if pick(df, "After-Hours Change") else np.nan,
        "pweek": df[pick(df, "Performance (Week)")].map(parse_num)
        if pick(df, "Performance (Week)") else np.nan,
    })
    return out


def is_noise(r) -> bool:
    et = r.get("etf_type")
    if pd.notna(et) and str(et).strip() not in ("", "nan", "None"):
        return True
    if NOISE_CO.search(str(r.get("company", ""))):
        return True
    if NOISE_IND.search(str(r.get("industry", ""))):
        return True
    return False


def clean_midcap(df: pd.DataFrame) -> pd.DataFrame:
    df = df[df["ticker"].notna() & (df["ticker"] != "") & (df["ticker"] != "NAN")].copy()
    df = df[~df.apply(is_noise, axis=1)].copy()
    # Price≥5, avg_vol_k≥500, mcap_m≥200
    df = df[
        (df["price"] >= 5)
        & (df["avg_vol"] >= 500)
        & (df["mcap"].notna())
        & (df["mcap"] >= 200)
    ].copy()
    return df


def add_flags(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    abs_chg = df["change_pct"].abs()
    abs_gap = df["gap_pct"].abs()
    abs_ah = df["ah_change_pct"].abs()
    pweek = df["pweek"]
    rvol = df["rvol"]

    df["flag_rvol_ge_2"] = (rvol >= 2).astype(int)
    df["flag_rvol_ge_3"] = (rvol >= 3).astype(int)
    df["flag_rvol_ge_5"] = (rvol >= 5).astype(int)
    df["flag_abs_chg_ge_5"] = (abs_chg >= 5).astype(int)
    df["flag_abs_chg_ge_8"] = (abs_chg >= 8).astype(int)
    df["flag_abs_chg_ge_10"] = (abs_chg >= 10).astype(int)
    df["flag_abs_gap_ge_3"] = (abs_gap >= 3).astype(int)
    df["flag_abs_gap_ge_5"] = (abs_gap >= 5).astype(int)
    # AH: only flag when parseable (not NaN)
    df["flag_abs_ah_chg_ge_2"] = ((abs_ah >= 2) & abs_ah.notna()).astype(int)
    df["flag_abs_ah_chg_ge_5"] = ((abs_ah >= 5) & abs_ah.notna()).astype(int)
    df["flag_pweek_ge_15"] = (pweek >= 15).astype(int)
    df["flag_pweek_ge_40"] = (pweek >= 40).astype(int)

    df["any_opp"] = (
        (df["flag_rvol_ge_2"] == 1)
        | (df["flag_abs_chg_ge_5"] == 1)
        | (df["flag_abs_gap_ge_3"] == 1)
        | (df["flag_abs_ah_chg_ge_2"] == 1)
        | (df["flag_pweek_ge_15"] == 1)
    ).astype(int)
    return df


FLAG_COLS = [
    "flag_rvol_ge_2", "flag_rvol_ge_3", "flag_rvol_ge_5",
    "flag_abs_chg_ge_5", "flag_abs_chg_ge_8", "flag_abs_chg_ge_10",
    "flag_abs_gap_ge_3", "flag_abs_gap_ge_5",
    "flag_abs_ah_chg_ge_2", "flag_abs_ah_chg_ge_5",
    "flag_pweek_ge_15", "flag_pweek_ge_40",
    "any_opp",
]

OUT_COLS = [
    "join_morning", "finviz_asof", "ticker", "sector",
    "price", "avg_vol", "mcap", "rvol",
    "change_pct", "chg_open_pct", "gap_pct", "ah_change_pct", "pweek",
] + FLAG_COLS


# ------------------------------------------------------------ append-only io

FILES = ("oppset_all.csv", "oppset_flagged.csv")


def _read(path: Path) -> tuple[list[str], list[list[str]]]:
    return hg.read_csv_path(path) if path.exists() else ([], [])


def _rows_text(header: list[str], rows: list[list[str]]) -> str:
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(header)
    w.writerows(rows)
    return buf.getvalue()


def build_day(join_morning: str, asof: str) -> pd.DataFrame:
    raw = load_raw(asof)
    clean = add_flags(clean_midcap(raw))
    clean.insert(0, "finviz_asof", asof)
    clean.insert(0, "join_morning", join_morning)
    return clean[OUT_COLS]


def _summary(out_dir: Path) -> None:
    """Regenerate OPPSET_SUMMARY.md from the append-only CSV (past rows are
    frozen, so past lines are stable; totals grow)."""
    df = pd.read_csv(out_dir / "oppset_all.csv", low_memory=False)
    lines = [
        "# Clock-B Opportunity Set — Summary",
        "",
        "Per `join_morning` (T): features from `finviz_asof` = prior date in list (T−1).",
        "Append-only since 2026-09-25: each refresh adds one morning; earlier rows are "
        "fingerprinted in `FINGERPRINTS.json` and never rewritten.",
        "",
        "| join_morning | finviz_asof | n_clean | n_flagged | top5 by rvol | top5 by \\|chg\\| |",
        "|---|---|---:|---:|---|---|",
    ]
    order = list(dict.fromkeys(df["join_morning"].astype(str)))
    for jm in order:
        clean = df[df["join_morning"].astype(str) == jm]
        t1 = str(clean["finviz_asof"].iloc[0])
        flagged = clean[clean["any_opp"] == 1]
        top_rvol = clean.dropna(subset=["rvol"]).sort_values("rvol", ascending=False).head(5)
        top_chg = clean.dropna(subset=["change_pct"]).assign(_a=lambda x: x["change_pct"].abs())
        top_chg = top_chg.sort_values("_a", ascending=False).head(5)
        lines.append(
            f"| {jm} | {t1} | {len(clean)} | {len(flagged)} "
            f"| {', '.join(f'{r.ticker} rvol={r.rvol:.2f}' for _, r in top_rvol.iterrows())} "
            f"| {', '.join(f'{r.ticker} chg={r.change_pct:+.2f}%' for _, r in top_chg.iterrows())} |"
        )
    flagged_all = df[df["any_opp"] == 1]
    lines += ["", f"**Totals:** clean rows={len(df):,} · flagged={len(flagged_all):,} · "
              f"join mornings={len(order)}", "",
              "## Taskforce proof mornings (09-16/17/18)", ""]
    for jm in ("2026-09-16", "2026-09-17", "2026-09-18"):
        sub = flagged_all[flagged_all["join_morning"].astype(str) == jm]
        sample = ", ".join(sub.sort_values("rvol", ascending=False)["ticker"].head(8).tolist())
        n_all = int((df["join_morning"].astype(str) == jm).sum())
        lines.append(f"- **{jm}**: n_clean={n_all}, n_flagged={len(sub)}; "
                     f"sample flagged (by rvol): {sample}")
    (out_dir / "OPPSET_SUMMARY.md").write_text("\n".join(lines) + "\n")


def verify(out_dir: Path, today: str) -> list[str]:
    root = out_dir.parents[1]
    rel = out_dir.relative_to(root).as_posix() + "/FINGERPRINTS.json"
    specs = [(out_dir.relative_to(root).as_posix(), hg.OPPSET_SPECS[0][1], "oppset")]
    probs, _ = hg.check_manifest(root, rel, specs, today, update=False)
    return probs


def record(out_dir: Path, today: str) -> list[str]:
    root = out_dir.parents[1]
    rel = out_dir.relative_to(root).as_posix() + "/FINGERPRINTS.json"
    specs = [(out_dir.relative_to(root).as_posix(), hg.OPPSET_SPECS[0][1], "oppset")]
    probs, man = hg.check_manifest(root, rel, specs, today, update=True)
    if not probs:
        hg.save_rows_manifest(root, rel, man)
    return probs


def latest_raw(raw_dir: Path, today: str) -> str | None:
    ds = sorted(m.group(1) for p in raw_dir.iterdir()
                if (m := RAW_RE.match(p.name)) and p.stat().st_size >= 1000)
    ds = [d for d in ds if d <= today]
    return ds[-1] if ds else None


def knowable_check(asof: str, jm: str) -> str | None:
    """Day N (= join_morning) may use only inputs knowable by 09:30 ET on N.
    Inputs are the single raw file dated finviz_asof (< N). If the companion
    normalized snapshot carries scrape_ts, the export must predate N 09:30 ET.
    The asof snapshot must also be the real close: taken after 16:00 ET on
    finviz_asof and before the next trading day's open (history_guard.
    close_is_in: scrape_ts, else git commit time of the on-disk file)."""
    if not asof < jm:
        return f"finviz_asof {asof} is not before join_morning {jm}"
    ok, why = hg.close_is_in(RAW, asof)
    if not ok:
        return f"asof snapshot is not the real close: {why}"
    snap = RAW / f"{asof}.csv"
    if snap.exists():
        cols = pd.read_csv(snap, nrows=0).columns
        if "scrape_ts" in cols:
            ts = pd.to_datetime(pd.read_csv(snap, usecols=["scrape_ts"])["scrape_ts"],
                                utc=True, errors="coerce").max()
            cutoff = pd.Timestamp(f"{jm} 09:30", tz="America/New_York")
            if pd.notna(ts) and ts >= cutoff:
                return f"{snap.name} scrape_ts {ts} is after {jm} 09:30 ET"
    return None


def _log(out_dir: Path, jm: str, asof: str, today: str, mode: str) -> None:
    """APPEND_LOG.tsv: when each morning was built. A morning built after its
    own 09:30 ET (catch-up of a missed night) is visible as built_late=1.
    Refused builds are logged too (mode "refused: <reason>"; nothing appended)."""
    path = out_dir / "APPEND_LOG.tsv"
    now = pd.Timestamp.now(tz="UTC")
    late = int(now >= pd.Timestamp(f"{jm} 09:30", tz="America/New_York"))
    new = not path.exists()
    with open(path, "a", encoding="utf-8") as fh:
        if new:
            fh.write("built_at_utc\tjoin_morning\tfinviz_asof\tmode\tbuilt_late\n")
        fh.write(f"{now.strftime('%Y-%m-%dT%H:%M:%SZ')}\t{jm}\t{asof}\t{mode}\t{late}\n")


def _existing(out_dir: Path) -> dict[str, str]:
    header, rows = _read(out_dir / "oppset_all.csv")
    if not header:
        return {}
    if header[:len(OUT_COLS)] != OUT_COLS:
        raise SystemExit(f"[oppset] unexpected columns in {out_dir / 'oppset_all.csv'}")
    ji, ai = header.index("join_morning"), header.index("finviz_asof")
    ex: dict[str, str] = {}
    for r in rows:
        ex.setdefault(r[ji], r[ai])
    return ex


def append_one(out_dir: Path, asof: str, jm: str, today: str) -> int:
    """verify -> build day N from its own T-1 file -> append -> fingerprint.
    Day N+1 is only started after this returns 0."""
    probs = verify(out_dir, today)
    if probs:
        for p in probs:
            print(f"[oppset] FAIL past rows: {p}", file=sys.stderr)
        print("[oppset] committed past rows no longer match FINGERPRINTS.json — "
              "refusing to refresh (append-only).", file=sys.stderr)
        return 1
    existing = _existing(out_dir)
    replace = False
    if jm in existing:
        if existing[jm] != today:
            print(f"[oppset] join_morning {jm} (asof {existing[jm]}) already recorded — "
                  "nothing to add; past mornings are never rebuilt.")
            return 0
        replace = True  # same-day rerun: asof == today
    elif existing and (asof <= max(existing.values()) or jm <= max(existing)):
        print(f"[oppset] REFUSE: asof {asof} / join_morning {jm} is not after the latest "
              f"recorded morning {max(existing)} (asof {max(existing.values())}). "
              "Inserting a past day would rebuild history.", file=sys.stderr)
        return 1
    why = knowable_check(asof, jm)
    if why:
        print(f"[oppset] REFUSE: {why}", file=sys.stderr)
        _log(out_dir, jm, asof, today, "refused: " + " ".join(why.split()))
        return 1

    day = build_day(jm, asof)
    print(f"[oppset] Clock-B join_morning={jm} finviz_asof={asof} "
          f"n_clean={len(day)} n_flagged={int((day['any_opp'] == 1).sum())}"
          + (" (same-day replace)" if replace else ""))

    backups = {}
    for name, sub in (("oppset_all.csv", day), ("oppset_flagged.csv", day[day["any_opp"] == 1])):
        path = out_dir / name
        h, rs = _read(path)
        backups[path] = path.read_bytes() if path.exists() else None
        if h and h != list(sub.columns):
            # grade columns were added later: keep them, the new morning gets blanks
            sub = sub.reindex(columns=h)
        new_text = sub.to_csv(index=False, header=not h)
        if replace:
            jidx = h.index("join_morning")
            path.write_text(_rows_text(h, [r for r in rs if r[jidx] != jm]) + new_text)
        else:
            with open(path, "a", encoding="utf-8", newline="") as fh:
                fh.write(new_text)

    probs = record(out_dir, today)
    if probs:
        for path, b in backups.items():
            if b is None:
                path.unlink(missing_ok=True)
            else:
                path.write_bytes(b)
        for p in probs:
            print(f"[oppset] FAIL: {p}", file=sys.stderr)
        print("[oppset] restored previous files; nothing written.", file=sys.stderr)
        return 1
    _summary(out_dir)
    _log(out_dir, jm, asof, today, "replace-same-day" if replace else "append")
    print(f"[oppset] appended {jm}; fingerprints recorded in {out_dir / 'FINGERPRINTS.json'}")
    return 0


def main(argv: list[str] | None = None) -> int:
    global RAW
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--asof", default=None,
                    help="last finviz_asof (T-1) to build up to; default latest raw <= today")
    ap.add_argument("--join-morning", default=None,
                    help="T for a single --asof; default next US trading day after asof")
    ap.add_argument("--raw-dir", default=str(RAW_DEFAULT))
    ap.add_argument("--out", default=str(OUT_DEFAULT))
    ap.add_argument("--today", default=None, help="ET today (default: now)")
    ap.add_argument("--verify-only", action="store_true")
    ap.add_argument("--record-only", action="store_true",
                    help="fingerprint mornings not yet in FINGERPRINTS.json (bootstrap)")
    a = ap.parse_args(argv)
    today = a.today or hg.today_et()
    out_dir = Path(a.out).resolve()
    RAW = Path(a.raw_dir).resolve()

    probs = verify(out_dir, today)
    if probs:
        for p in probs:
            print(f"[oppset] FAIL past rows: {p}", file=sys.stderr)
        print("[oppset] committed past rows no longer match FINGERPRINTS.json — "
              "refusing to refresh (append-only).", file=sys.stderr)
        return 1
    if a.verify_only:
        print(f"[oppset] OK: fingerprints match ({out_dir})")
        return 0
    if a.record_only:
        probs = record(out_dir, today)
        for p in probs:
            print(f"[oppset] FAIL: {p}", file=sys.stderr)
        print("[oppset] recorded" if not probs else "[oppset] not recorded")
        return 1 if probs else 0

    target = a.asof or latest_raw(RAW, today)
    if not target:
        print(f"[oppset] no raw snapshot in {RAW}", file=sys.stderr)
        return 2
    if a.join_morning:
        return append_one(out_dir, target, a.join_morning, today)

    # One day at a time, in order: every raw asof after the last recorded one
    # (normally exactly one: tonight's). Each morning is verified, built from
    # its own T-1 file only, appended and fingerprinted before the next starts.
    existing = _existing(out_dir)
    last = max(existing.values()) if existing else ""
    todo = sorted(m.group(1) for q in RAW.iterdir()
                  if (m := RAW_RE.match(q.name)) and last < m.group(1) <= target)
    if not todo:
        # nothing newer: allow the same-day rerun path / no-op message
        todo = [target]
    if len(todo) > 1:
        print(f"[oppset] catching up {len(todo)} missed mornings one day at a time: {todo}")
    for asof in todo:
        jm = next_trading_day(date.fromisoformat(asof)).isoformat()
        rc = append_one(out_dir, asof, jm, today)
        if rc != 0:
            return rc
    return 0


if __name__ == "__main__":
    sys.exit(main())
