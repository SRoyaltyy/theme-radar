"""Read-only Finviz Elite probe. Writes probe_out/ only; commits nothing.
The auth key is never printed: every saved/printed text is scrubbed."""
import csv, io, json, os, re, sys
import requests
from html import unescape

from urllib.parse import urlparse, parse_qs
KEY = os.environ.get("FINVIZ_API_KEY", "").strip()
_full = os.environ.get("FINVIZ_EXPORT", "").strip()
if not KEY and _full:  # the Elite key lives inside the FINVIZ_EXPORT link, as in finviz_fetch
    KEY = (parse_qs(urlparse(_full).query).get("auth") or [""])[0].strip()
if KEY:
    print(f"::add-mask::{KEY}", flush=True)
print("key source:", "FINVIZ_API_KEY" if os.environ.get("FINVIZ_API_KEY", "").strip() else "auth= in FINVIZ_EXPORT", "| present:", bool(KEY))
if not KEY:
    sys.exit("FINVIZ_API_KEY missing")
BASE = "https://elite.finviz.com"
UA = {"User-Agent": "Mozilla/5.0 (compatible; theme-radar/1.0; +https://github.com/SRoyaltyy/theme-radar)"}
COLS = ",".join(str(i) for i in range(0, 71)) + ",86"  # same as finviz_fetch.DEFAULT_COLS
OUT = "probe_out"; os.makedirs(OUT, exist_ok=True)
summary = {}

def scrub(s): return s.replace(KEY, "***")

def get(path, params):
    r = requests.get(f"{BASE}/{path}", params={**params, "auth": KEY}, headers=UA, timeout=180)
    return r.status_code, r.headers.get("content-type", ""), r.text

def csvinfo(name, path, params, nsample=3):
    st, ct, txt = get(path, params)
    open(f"{OUT}/{name}.txt", "w").write(scrub(txt))
    info = {"url": f"{BASE}/{path}?" + "&".join(f"{k}={v}" for k, v in params.items()) + "&auth=***",
            "status": st, "content_type": ct, "bytes": len(txt)}
    try:
        rows = list(csv.reader(io.StringIO(txt.lstrip("\ufeff"))))
        if rows and "<html" not in txt[:500].lower():
            info.update(rows=len(rows) - 1, cols=len(rows[0]), header=rows[0],
                        sample=[r for r in rows[1:1 + nsample]])
        else:
            info["note"] = "not CSV: " + scrub(txt[:300])
    except Exception as e:
        info["note"] = f"parse error {e}"
    summary[name] = info

csvinfo("screener_export", "export.ashx", {"v": "152", "c": COLS})
csvinfo("news_export_NFLX", "news_export.ashx", {"v": "3", "t": "NFLX"})
csvinfo("groups_industry_grp_export", "grp_export.ashx", {"g": "industry", "v": "140", "o": "name"})
csvinfo("groups_industry_groups_ashx", "groups.ashx", {"g": "industry", "v": "140", "o": "name"})
csvinfo("groups_sector_grp_export", "grp_export.ashx", {"g": "sector", "v": "140", "o": "name"})

# Quote page ratings (HTML)
st, ct, html = get("quote.ashx", {"t": "NFLX", "p": "d"})
open(f"{OUT}/quote_NFLX.html", "w").write(scrub(html))
info = {"url": f"{BASE}/quote.ashx?t=NFLX&p=d&auth=***", "status": st, "content_type": ct, "bytes": len(html)}
m = re.search(r'<table[^>]*(?:ratings)[^>]*>(.*?)</table>', html, re.S | re.I)
rows = []
if m:
    for tr in re.findall(r"<tr[^>]*>(.*?)</tr>", m.group(1), re.S | re.I):
        cells = [unescape(re.sub(r"<[^>]+>", "", c)).strip() for c in re.findall(r"<td[^>]*>(.*?)</td>", tr, re.S | re.I)]
        if len(cells) >= 4: rows.append(cells)
info.update(ratings_table_found=bool(m), rows=len(rows), sample=rows[:3],
            note="cells: date, action, firm, rating change, price target")
summary["quote_NFLX_ratings"] = info

js = scrub(json.dumps(summary, indent=1))
open(f"{OUT}/summary.json", "w").write(js)
for k, v in summary.items():
    print(f"== {k}: status={v['status']} rows={v.get('rows')} cols={v.get('cols')} bytes={v['bytes']}")
    if "header" in v: print("   header:", scrub(json.dumps(v["header"])))
    print("   sample:", scrub(json.dumps(v.get("sample", v.get("note")))[:1500]))
