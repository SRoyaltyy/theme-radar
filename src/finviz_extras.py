"""Daily add-only save of Finviz fields that Finviz itself keeps no history for.

Runs after src.finviz_fetch in finviz_daily.yml. Never touches data/snapshots/.
Outputs (one set per ET date, never overwritten; a same-day re-run writes a
new file with a _HHMMSS suffix instead):

  data/finviz_extras/fields/YYYY-MM-DD.csv     Ticker + every export column with
      id > 70 that the export returns (after-hours close/change, implied
      volatility, theme/sub-theme tags, ... whatever Finviz serves), raw.
  data/finviz_extras/signals/YYYY-MM-DD.csv    long format: signal,ticker
      (one row per ticker that is a member of that screener signal today).
  data/finviz_extras/groups/YYYY-MM-DD_<group>.csv   group performance view
      (v=140: perf week/month/quarter/half/year/YTD, avg/rel volume, change).
  data/finviz_extras/status/YYYY-MM-DD.json    per item: ok / missing + reason,
      row counts, headers. A failed item is MISSING for that day; it is never
      zero-filled and no empty CSV stands in for it.
"""
from __future__ import annotations

import argparse
import csv
import io
import json
import os
import time
from datetime import datetime
from pathlib import Path
from urllib.parse import parse_qs, urlparse
from zoneinfo import ZoneInfo

import requests

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "finviz_extras"
BASE = "https://elite.finviz.com"
UA = {"User-Agent": "Mozilla/5.0 (compatible; theme-radar/1.0; "
      "+https://github.com/SRoyaltyy/theme-radar)"}
PAUSE_S = float(os.environ.get("FINVIZ_EXTRAS_PAUSE", "1.5"))  # rate limit

# Column ids beyond the 0-70 core export. Unknown ids are ignored by Finviz;
# we keep whatever comes back and record the headers in status.
EXTRA_COLS = ",".join(["1"] + [str(i) for i in range(71, 401)])

# Signal codes as published by Finviz (robots.txt allow-list / screener UI).
SIGNALS = [
    "ta_topgainers", "ta_toplosers", "ta_newhigh", "ta_newlow",
    "ta_mostvolatile", "ta_mostactive", "ta_unusualvolume",
    "ta_overbought", "ta_oversold",
    "n_upgrades", "n_downgrades", "n_earningsbefore", "n_earningsafter",
    "it_latestbuys", "it_latestsales", "n_majornews",
    "f_ssr", "f_halted",
    "ta_p_tlsupport", "ta_p_tlresistance", "ta_p_horizontal",
    "ta_p_wedgeup", "ta_p_wedge", "ta_p_wedgedown",
    "ta_p_wedgeresistance", "ta_p_wedgesupport",
    "ta_p_channelup", "ta_p_channel", "ta_p_channeldown",
    "ta_p_doubletop", "ta_p_multipletop", "ta_p_doublebottom",
    "ta_p_multiplebottom", "ta_p_headandshoulders", "ta_p_headandshouldersinv",
    # After-hours variants (Elite). Codes not publicly documented: if Finviz
    # ignores them the result looks like the whole universe and is rejected.
    "ah_unusualvolume", "ah_topgainers", "ah_toplosers",
]
GROUPS = ["industry", "sector", "theme", "subtheme"]  # theme/subtheme: best effort


def auth_key() -> str | None:
    for var in ("FINVIZ_EXPORT", "FINVIZ_EXPORT_URL"):
        url = os.environ.get(var, "").strip()
        if url:
            a = parse_qs(urlparse(url).query).get("auth")
            if a and a[0]:
                return a[0]
    return os.environ.get("FINVIZ_API_KEY", "").strip() or None


def _get(path: str, params: dict) -> str:
    r = requests.get(f"{BASE}/{path}", params=params, headers=UA, timeout=180)
    r.raise_for_status()
    text = r.content.decode("utf-8-sig", errors="replace")
    head = text[:500].lower()
    if "<html" in head or "," not in head:
        raise RuntimeError(f"not a CSV (status {r.status_code}, {len(text)} chars)")
    return text


def _rows(text: str) -> tuple[list[str], list[list[str]]]:
    rd = list(csv.reader(io.StringIO(text)))
    return (rd[0], rd[1:]) if rd else ([], [])


def _dest(sub: str, name: str, stamp: str) -> Path:
    d = OUT / sub
    d.mkdir(parents=True, exist_ok=True)
    p = d / name
    if p.exists():  # add-only: never overwrite an existing dated file
        p = d / name.replace(".csv", f"_{stamp}.csv").replace(".json", f"_{stamp}.json")
    return p


PAGE_CAPS = (20, 50, 100, 200, 500, 1000)  # page sizes that suggest a truncated export
MAX_PAGES = 60
SIGNAL_BUDGET_S = 5 * 60  # keep the whole step under the 8-minute limit


def _paged_signal(s: str, key: str, deadline: float) -> tuple[list[str], int, bool, str]:
    """Fetch one screener signal, paging with &r=<offset+1> while pages come back
    exactly at a cap size. De-duplicates by ticker, keeping first-seen order."""
    seen: dict[str, None] = {}
    pages, cap, offset = 0, None, 0
    while True:
        params = {"v": "111", "s": s, "c": "1", "auth": key}
        if offset:
            params["r"] = str(offset + 1)
            time.sleep(PAUSE_S)
        hdr, rows = _rows(_get("export.ashx", params))
        pages += 1
        ti = hdr.index("Ticker") if "Ticker" in hdr else 0
        page = [r[ti] for r in rows if len(r) > ti and r[ti]]
        new = [t for t in page if t not in seen]
        for t in new:
            seen[t] = None
        if cap is None:
            if len(page) not in PAGE_CAPS:
                return list(seen), pages, True, ""
            cap = len(page)
        elif not new:
            return list(seen), pages, False, "paging ignored: page repeated earlier tickers"
        if len(page) < cap:
            return list(seen), pages, True, ""
        if pages >= MAX_PAGES:
            return list(seen), pages, False, f"stopped at {MAX_PAGES} pages"
        if time.monotonic() > deadline:
            return list(seen), pages, False, "stopped: time budget"
        offset += len(page)


def run(date_str: str, probe: bool = False) -> dict:
    stamp = datetime.now(ZoneInfo("America/New_York")).strftime("%H%M%S")
    status: dict = {"date": date_str,
                    "scrape_ts_utc": datetime.now(ZoneInfo("UTC")).isoformat(timespec="seconds"),
                    "fields": {}, "signals": {}, "groups": {}}
    key = auth_key()
    if not key:
        status["error"] = "no Finviz auth key in FINVIZ_EXPORT/FINVIZ_EXPORT_URL/FINVIZ_API_KEY"
        print("[finviz_extras]", status["error"])
        if not probe:
            _dest("status", f"{date_str}.json", stamp).write_text(json.dumps(status, indent=2))
        return status

    universe = 0
    # 1) per-ticker extra fields
    try:
        text = _get("export.ashx", {"v": "152", "c": EXTRA_COLS, "auth": key})
        hdr, rows = _rows(text)
        universe = len(rows)
        status["fields"] = {"status": "ok", "rows": universe, "headers": hdr}
        if not probe:
            p = _dest("fields", f"{date_str}.csv", stamp)
            p.write_text(text)
            status["fields"]["file"] = str(p.relative_to(ROOT))
    except Exception as e:  # fail soft
        status["fields"] = {"status": "missing", "reason": repr(e)[:300]}
    print("[finviz_extras] fields:", {k: v for k, v in status["fields"].items() if k != "headers"})
    if status["fields"].get("headers"):
        print("[finviz_extras] field headers:", status["fields"]["headers"])

    # 2) screener signal membership
    long_rows: list[tuple[str, str]] = []
    deadline = time.monotonic() + SIGNAL_BUDGET_S
    for s in SIGNALS:
        time.sleep(PAUSE_S)
        try:
            tickers, pages, complete, note = _paged_signal(s, key, deadline)
            if universe and len(tickers) >= 0.9 * universe:
                raise RuntimeError(f"returned {len(tickers)} of {universe} tickers: "
                                   "signal code likely ignored by Finviz")
            status["signals"][s] = {"status": "ok", "count": len(tickers), "rows": len(tickers),
                                    "pages": pages, "complete": complete}
            if note:
                status["signals"][s]["note"] = note
            long_rows += [(s, t) for t in tickers]
        except Exception as e:
            status["signals"][s] = {"status": "missing", "reason": repr(e)[:300]}
        print(f"[finviz_extras] signal {s}: {status['signals'][s]}")
    if not probe and any(v["status"] == "ok" for v in status["signals"].values()):
        p = _dest("signals", f"{date_str}.csv", stamp)
        with p.open("w", newline="") as fh:
            w = csv.writer(fh)
            w.writerow(["signal", "ticker"])
            w.writerows(long_rows)
        status["signals_file"] = str(p.relative_to(ROOT))

    # 3) group performance (industry ranks etc.)
    for g in GROUPS:
        time.sleep(PAUSE_S)
        try:
            text = _get("grp_export.ashx", {"g": g, "v": "140", "o": "name", "auth": key})
            hdr, rows = _rows(text)
            if not rows:
                raise RuntimeError("no rows")
            status["groups"][g] = {"status": "ok", "rows": len(rows), "headers": hdr}
            if not probe:
                p = _dest("groups", f"{date_str}_{g}.csv", stamp)
                p.write_text(text)
                status["groups"][g]["file"] = str(p.relative_to(ROOT))
        except Exception as e:
            status["groups"][g] = {"status": "missing", "reason": repr(e)[:300]}
        print(f"[finviz_extras] group {g}: {status['groups'][g]}")

    if not probe:
        p = _dest("status", f"{date_str}.json", stamp)
        p.write_text(json.dumps(status, indent=2))
        print("[finviz_extras] wrote", p.relative_to(ROOT))
    return status


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", default=None, help="ET date label (default: today ET)")
    ap.add_argument("--probe", action="store_true", help="fetch and report, write nothing")
    a = ap.parse_args()
    d = a.date or datetime.now(ZoneInfo("America/New_York")).date().isoformat()
    run(d, probe=a.probe)


if __name__ == "__main__":
    main()
