#!/usr/bin/env python3
"""Nightly add-only saver: analyst ratings table from Finviz Elite quote pages.

Writes data/finviz_extras/ratings/<ET date>.csv and
data/finviz_extras/status/<ET date>_ratings.json. Never overwrites an existing
date file. The Elite key (auth= inside FINVIZ_EXPORT) is masked and never printed.

Universe: top N tickers by dollar volume (Average Volume x Price) from
data/snapshots/current.csv. A wall-clock deadline stops fetching early so the
job never runs past its timeout; whatever was fetched is saved and the status
json records where it stopped.
"""
from __future__ import annotations
import argparse, csv, json, os, re, sys, time
from datetime import datetime, timezone, date, time as dtime
from html import unescape
from pathlib import Path
from urllib.parse import urlparse, parse_qs
from zoneinfo import ZoneInfo
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src.trading_calendar import is_trading_day  # noqa: E402

ET = ZoneInfo("America/New_York")
OUT_DIR = ROOT / "data/finviz_extras/ratings"
STATUS_DIR = ROOT / "data/finviz_extras/status"
SNAP = ROOT / "data/snapshots/current.csv"
BASE = "https://elite.finviz.com/quote.ashx"
UA = {"User-Agent": "Mozilla/5.0 (compatible; theme-radar/1.0; +https://github.com/SRoyaltyy/theme-radar)"}
COLS = ["ticker", "rating_date", "action", "firm", "rating_from", "rating_to",
        "price_target_from", "price_target_to", "fetched_at_utc"]
ARROW = re.compile(r"\s*(?:\u2192|&rarr;|->)\s*")


def get_key() -> str:
    key = os.environ.get("FINVIZ_API_KEY", "").strip()
    full = os.environ.get("FINVIZ_EXPORT", "").strip()
    if not key and full:
        key = (parse_qs(urlparse(full).query).get("auth") or [""])[0].strip()
    if key and os.environ.get("GITHUB_ACTIONS"):
        print(f"::add-mask::{key}", flush=True)
    return key


def parse_date(s: str, run_d: date) -> str:
    """'Today' / 'Today 08:30AM' -> run date; 'Oct-15-26' (+ optional time) -> ISO."""
    s = (s or "").strip()
    if not s:
        return ""
    if s.lower().startswith("today"):
        return run_d.isoformat()
    tok = s.split()[0]
    for fmt in ("%b-%d-%y", "%b-%d-%Y", "%Y-%m-%d", "%m/%d/%Y", "%m/%d/%y"):
        try:
            return datetime.strptime(tok, fmt).date().isoformat()
        except ValueError:
            pass
    return ""


def split_change(s: str) -> tuple[str, str]:
    s = (s or "").strip()
    if not s:
        return "", ""
    parts = ARROW.split(s, maxsplit=1)
    return (parts[0].strip(), parts[1].strip()) if len(parts) == 2 else ("", s)


def clean_pt(s: str) -> str:
    return s.replace("$", "").replace(",", "").strip()


def parse_ratings(html: str, run_d: date):
    m = re.search(r"<table[^>]*ratings[^>]*>(.*?)</table>", html, re.S | re.I)
    if not m:
        return None
    rows = []
    for tr in re.findall(r"<tr[^>]*>(.*?)</tr>", m.group(1), re.S | re.I):
        tds = re.findall(r"<td([^>]*)>(.*?)</td>", tr, re.S | re.I)
        if len(tds) < 4:
            continue
        cells = [unescape(re.sub(r"<[^>]+>", "", c)).strip() for _, c in tds]
        raw_date = cells[0]
        d_iso = ""
        if raw_date.lower().startswith("today"):
            d_iso = run_d.isoformat()  # replace "Today" with the run's ET date
        else:
            d_iso = parse_date(raw_date, run_d)
        if not d_iso:  # fall back to the cell's title attribute if present
            t = re.search(r'title="([^"]+)"', tds[0][0])
            d_iso = parse_date(t.group(1), run_d) if t else ""
        rf, rt = split_change(cells[3])
        pf, pt = split_change(cells[4] if len(cells) > 4 else "")
        rows.append({"rating_date": d_iso, "action": cells[1], "firm": cells[2],
                     "rating_from": rf, "rating_to": rt,
                     "price_target_from": clean_pt(pf), "price_target_to": clean_pt(pt),
                     "_raw_date": raw_date})
    return rows


def universe(n: int) -> list[str]:
    def num(x):
        try:
            return float(str(x).replace(",", ""))
        except ValueError:
            return 0.0
    rows = list(csv.DictReader(open(SNAP, newline="", encoding="utf-8-sig")))
    rows = [r for r in rows if r.get("Ticker") and r.get("Industry", "") != "Exchange Traded Fund"]  # funds have no analyst ratings
    rows.sort(key=lambda r: num(r.get("Average Volume")) * num(r.get("Price")), reverse=True)
    return [r["Ticker"].strip() for r in rows[:n]]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--event", default="workflow_dispatch")
    ap.add_argument("--n", type=int, default=1000)
    ap.add_argument("--sleep", type=float, default=1.5)
    ap.add_argument("--deadline-min", type=float, default=45.0)
    a = ap.parse_args()

    now_et = datetime.now(ET)
    run_d = now_et.date()
    day = run_d.isoformat()
    out = OUT_DIR / f"{day}.csv"
    status_p = STATUS_DIR / f"{day}_ratings.json"
    gh_out = os.environ.get("GITHUB_OUTPUT")

    def gate(ok: bool, why: str):
        print(f"[gate] {day} {now_et:%H:%M} ET: {'RUN' if ok else 'SKIP'} - {why}", flush=True)
        if gh_out:
            open(gh_out, "a").write(f"saved={'true' if ok else 'false'}\net_date={day}\n")

    if not is_trading_day(run_d):
        gate(False, "not a US trading day"); return 0
    if a.event == "schedule" and now_et.time() < dtime(16, 30):
        gate(False, "before 16:30 ET (other cron slot runs)"); return 0
    if out.exists() or status_p.exists():
        gate(False, f"{out.relative_to(ROOT)} already exists (add-only)"); return 0

    key = get_key()
    if not key:
        print("Elite key missing"); return 1

    tickers = universe(a.n)
    t0 = time.monotonic()
    sess = requests.Session()
    allrows, failures, no_table, empty = [], [], [], []
    done = 0
    stopped = ""
    for i, t in enumerate(tickers):
        if time.monotonic() - t0 > a.deadline_min * 60:
            stopped = f"deadline after {done} tickers"; break
        if i:
            time.sleep(a.sleep)
        html, err = None, ""
        for attempt in range(3):
            try:
                r = sess.get(BASE, params={"t": t, "p": "d", "auth": key}, headers=UA, timeout=30)
                if r.status_code == 200:
                    html = r.text; break
                err = f"HTTP {r.status_code}"
                if r.status_code in (429, 500, 502, 503, 504):
                    time.sleep(10 * (attempt + 1)); continue
                break
            except requests.RequestException as e:
                err = type(e).__name__; time.sleep(5)
        done += 1
        if html is None:
            failures.append({"ticker": t, "error": err.replace(key, "***")}); continue
        fetched = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        rows = parse_ratings(html, run_d)
        if rows is None:
            no_table.append(t); continue
        if not rows:
            empty.append(t)
        for rr in rows:
            if not rr["rating_date"]:
                failures.append({"ticker": t, "error": f"unparsed date {rr['_raw_date']!r}"})
            rr.pop("_raw_date")
            allrows.append({"ticker": t, **rr, "fetched_at_utc": fetched})
        if done % 100 == 0:
            print(f"[progress] {done}/{len(tickers)} tickers, {len(allrows)} rows, {time.monotonic()-t0:.0f}s", flush=True)

    if not allrows:
        print("no rows fetched; writing nothing"); gate(False, "0 rows"); return 1
    OUT_DIR.mkdir(parents=True, exist_ok=True); STATUS_DIR.mkdir(parents=True, exist_ok=True)
    with open(out, "x", newline="", encoding="utf-8") as f:  # 'x' = never overwrite
        w = csv.DictWriter(f, fieldnames=COLS); w.writeheader(); w.writerows(allrows)
    status = {"et_date": day, "run_started_et": now_et.isoformat(timespec="seconds"),
              "event": a.event, "universe": "top N by Average Volume x Price, data/snapshots/current.csv",
              "n_requested": len(tickers), "n_fetched": done, "stopped_early": stopped,
              "tickers_with_rows": len({r["ticker"] for r in allrows}), "rows": len(allrows),
              "rows_dated_today": sum(r["rating_date"] == day for r in allrows),
              "no_ratings_table": no_table, "empty_table": empty, "failures": failures,
              "elapsed_s": round(time.monotonic() - t0, 1), "sleep_s": a.sleep}
    with open(status_p, "x", encoding="utf-8") as f:
        json.dump(status, f, indent=1)
    print(json.dumps({k: (v if not isinstance(v, list) else len(v)) for k, v in status.items()}, indent=1))
    gate(True, f"saved {len(allrows)} rows")
    return 0


if __name__ == "__main__":
    sys.exit(main())
