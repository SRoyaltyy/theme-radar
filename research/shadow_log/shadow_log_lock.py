#!/usr/bin/env python3
"""IRONCLAD append-only lock for Theme Radar's research-only shadow shorts.

Research only. These cells are never on James's buy/sell list and never sent to Webull.

Subcommands (run from anywhere; paths are relative to this file's folder):
  check      Exit 1 if any pinned fingerprint no longer matches, any pinned or
             pre_lock row is missing, the log has duplicate keys, or the
             rules_frozen.json sha256 changed. Prints every problem.
             --against-git REF  also verify the manifest is a pure append-only
             superset of the manifest at git REF (used by CI on push/PR).
  pin        Run check first (abort on failure). Then pin a signal fingerprint
             for every newly appended row and an outcome fingerprint for every
             newly scored row. Never alters or removes an existing pin.
  scorecard  Rewrite scorecard.md (LOCKED / CLEAN pre-lock / MIXED per cell,
             after 15bp fee + 0.3% borrow, vs shorting IWM).

Stdlib only.
"""
import argparse, csv, datetime as dt, hashlib, json, os, statistics, subprocess, sys, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
LOG = os.path.join(HERE, "log.csv")
RULES = os.path.join(HERE, "rules_frozen.json")
MANIFEST = os.path.join(HERE, "lock_manifest.json")
SCORECARD = os.path.join(HERE, "scorecard.md")
IWM_CACHE = os.path.join(HERE, "iwm_daily.csv")
REL_MANIFEST = "research/shadow_log/lock_manifest.json"

LOCK_START = "2026-10-06"
CLEAN_FROM = "2026-09-28"
EXPECTED_COLUMNS = ["cell", "date", "ticker", "entry", "hold_days", "exit_date", "short_ret",
                    "short_ret_fee_only", "short_ret_fee_borrow", "tape", "feature_date", "source", "meta"]
KEY_FIELDS = ["cell", "date", "ticker"]
SIGNAL_FIELDS = ["cell", "date", "ticker", "entry", "hold_days", "feature_date", "source"]
OUTCOME_FIELDS = ["exit_date", "short_ret", "short_ret_fee_only", "short_ret_fee_borrow", "tape"]
INT_FIELDS = {"hold_days"}
FLOAT_FIELDS = {"short_ret", "short_ret_fee_only", "short_ret_fee_borrow"}
# A new row is counted as LOCKED only if its signal pin lands within this many
# calendar days (UTC) after its signal date and before it is scored.
MAX_PIN_LAG_DAYS = 5
CELLS = ["fpe_delta_t3_earn_today_3d", "fresh_dcp_t1_ep_ge03_2d", "fresh_dcp_t1_avoid_ah_3d"]
FINGERPRINT_METHOD = (
    "sha256 of UTF-8 JSON array [field values in the listed order], json.dumps(separators=(',',':'), "
    "ensure_ascii=False). Each value is the CSV string with surrounding whitespace stripped; "
    "hold_days -> str(int(float(v))); short_ret* -> repr(float(v)); empty stays ''. "
    "This tolerates harmless re-serialisation (e.g. pandas round-trip) but any value change breaks the pin.")


# ---------------------------------------------------------------- helpers
def sha256_file(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def norm(field, v):
    v = (v or "").strip()
    if v == "":
        return ""
    if field in INT_FIELDS:
        return str(int(float(v)))
    if field in FLOAT_FIELDS:
        return repr(float(v))
    return v


def fingerprint(row, fields):
    vals = [norm(f, row.get(f, "")) for f in fields]
    return hashlib.sha256(json.dumps(vals, separators=(",", ":"), ensure_ascii=False).encode("utf-8")).hexdigest()


def key_of(row):
    return "|".join((row.get(f) or "").strip() for f in KEY_FIELDS)


def is_scored(row):
    return (row.get("short_ret") or "").strip() != ""


def read_log(path=LOG):
    with open(path, newline="", encoding="utf-8") as f:
        rd = csv.DictReader(f)
        cols = rd.fieldnames or []
        rows = list(rd)
    return cols, rows


def load_manifest(path=MANIFEST):
    if not os.path.exists(path):
        return None
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def write_manifest(m, path=MANIFEST):
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(m, f, indent=2, ensure_ascii=False, sort_keys=False)
        f.write("\n")
    os.replace(tmp, path)


def now_utc():
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0)


# ---------------------------------------------------------------- check
def run_check(against_git=None, quiet=False):
    problems = []
    m = load_manifest()
    if m is None:
        problems.append(f"lock_manifest.json missing ({MANIFEST})")
        return problems, None, None
    # rules
    pinned_rules = m.get("rules_frozen", {}).get("sha256")
    actual_rules = sha256_file(RULES) if os.path.exists(RULES) else None
    if actual_rules is None:
        problems.append("rules_frozen.json is missing")
    elif actual_rules != pinned_rules:
        problems.append(f"rules_frozen.json sha256 changed: pinned {pinned_rules} now {actual_rules}")
    # log shape
    cols, rows = read_log()
    if cols != EXPECTED_COLUMNS:
        problems.append(f"log.csv columns changed: {cols} != {EXPECTED_COLUMNS}")
    by_key = {}
    for i, r in enumerate(rows):
        k = key_of(r)
        if k in by_key:
            problems.append(f"duplicate row key {k} (csv rows {by_key[k][0] + 2} and {i + 2})")
        else:
            by_key[k] = (i, r)
    # pre_lock rows: presence only (their content is deliberately NOT fingerprinted)
    for k in m.get("pre_lock", {}).get("keys", []):
        if k not in by_key:
            problems.append(f"pre_lock row missing from log.csv: {k}")
    # pinned rows
    for k, e in m.get("rows", {}).items():
        if k not in by_key:
            problems.append(f"pinned row missing from log.csv: {k}")
            continue
        r = by_key[k][1]
        sig = e.get("signal")
        if sig and fingerprint(r, SIGNAL_FIELDS) != sig["sha256"]:
            problems.append(f"signal fingerprint mismatch for {k}: signal fields were edited after pinning "
                            f"(pinned {sig['pinned_at_utc']})")
        out = e.get("outcome")
        if out and fingerprint(r, OUTCOME_FIELDS) != out["sha256"]:
            problems.append(f"outcome fingerprint mismatch for {k}: outcome fields were edited after pinning "
                            f"(pinned {out['pinned_at_utc']})")
    # pre-lock rows that were open at lock time: once outcome is pinned it is covered above
    if against_git:
        problems += check_against_git(m, against_git)
    if not quiet:
        if problems:
            print(f"CHECK FAILED ({len(problems)} problem(s)):")
            for p in problems:
                print("  - " + p)
        else:
            n_sig = sum(1 for e in m["rows"].values() if e.get("signal"))
            n_out = sum(1 for e in m["rows"].values() if e.get("outcome"))
            print(f"CHECK OK: rules sha256 {actual_rules}; log rows {len(rows)}; "
                  f"pre_lock {len(m['pre_lock']['keys'])}; signal pins {n_sig}; outcome pins {n_out}"
                  + (f"; manifest append-only vs {against_git}" if against_git else ""))
    return problems, m, (cols, rows, by_key)


def _same(a, b):
    return json.dumps(a, sort_keys=True) == json.dumps(b, sort_keys=True)


def manifest_superset_problems(old, new, label):
    p = []
    for fld in ("schema", "lock_start", "clean_from", "signal_fields", "outcome_fields", "key_fields",
                "fingerprint_method", "rules_frozen", "pre_lock"):
        if not _same(old.get(fld), new.get(fld)):
            p.append(f"manifest field '{fld}' changed vs {label}")
    old_runs, new_runs = old.get("pin_runs", []), new.get("pin_runs", [])
    if not _same(old_runs, new_runs[:len(old_runs)]):
        p.append(f"manifest pin_runs history rewritten vs {label}")
    for k, e in old.get("rows", {}).items():
        ne = new.get("rows", {}).get(k)
        if ne is None:
            p.append(f"manifest entry for {k} removed vs {label}")
            continue
        for part, val in e.items():
            if not _same(val, ne.get(part)):
                p.append(f"manifest entry {k}.{part} modified vs {label}")
    return p


def check_against_git(m, ref):
    try:
        root = subprocess.check_output(["git", "rev-parse", "--show-toplevel"], cwd=HERE, text=True).strip()
        rel = os.path.relpath(MANIFEST, root).replace(os.sep, "/")
        blob = subprocess.run(["git", "show", f"{ref}:{rel}"], cwd=root, capture_output=True, text=True)
    except Exception as ex:  # noqa
        return [f"could not read manifest at git {ref}: {ex}"]
    if blob.returncode != 0:
        print(f"note: no manifest at {ref} (first commit of the lock?) - append-only diff skipped")
        return []
    return manifest_superset_problems(json.loads(blob.stdout), m, f"git {ref}")


# ---------------------------------------------------------------- pin
def run_pin():
    if not os.path.exists(MANIFEST):
        print("pin: no manifest yet - creating the lock (one time only).")
        rc = run_init()
        if rc:
            return rc
    problems, m, parsed = run_check()
    if problems:
        print("pin refused: check failed. Fix (or report) before appending/pinning.")
        return 1
    old = json.loads(json.dumps(m))
    cols, rows, by_key = parsed
    ts = now_utc()
    ts_s = ts.strftime("%Y-%m-%dT%H:%M:%SZ")
    pre = set(m["pre_lock"]["keys"])
    open_at_lock = set(m["pre_lock"]["open_at_lock"])
    added_sig = added_out = 0
    for r in rows:
        k = key_of(r)
        e = m["rows"].get(k)
        if k in pre:
            # pre_lock: signal never pinned; outcome pinned only if it was open at lock time
            if k in open_at_lock and is_scored(r) and not (e and e.get("outcome")):
                e = m["rows"].setdefault(k, {"status": "pre_lock"})
                e["outcome"] = {"sha256": fingerprint(r, OUTCOME_FIELDS), "pinned_at_utc": ts_s}
                added_out += 1
            continue
        if e is None:
            # newly appended row
            lag = (ts.date() - dt.date.fromisoformat(r["date"].strip())).days
            reasons = []
            if r["date"].strip() < LOCK_START:
                reasons.append(f"signal date {r['date']} is before lock_start {LOCK_START}")
            if lag > MAX_PIN_LAG_DAYS:
                reasons.append(f"signal pinned {lag} days after signal date (> {MAX_PIN_LAG_DAYS})")
            if is_scored(r):
                reasons.append("row was already scored when first pinned")
            e = {"status": "locked" if not reasons else "late_append",
                 "signal": {"sha256": fingerprint(r, SIGNAL_FIELDS), "pinned_at_utc": ts_s}}
            if reasons:
                e["late_reason"] = "; ".join(reasons)
            m["rows"][k] = e
            added_sig += 1
        if is_scored(r) and not e.get("outcome"):
            e["outcome"] = {"sha256": fingerprint(r, OUTCOME_FIELDS), "pinned_at_utc": ts_s}
            added_out += 1
    # append-only guard: every old pin must survive untouched
    bad = manifest_superset_problems(old, m, "pre-pin manifest")
    if bad:
        print("pin refused: would modify/remove existing pins:\n  - " + "\n  - ".join(bad))
        return 1
    if added_sig or added_out:
        m["pin_runs"].append({"at_utc": ts_s, "log_sha256": sha256_file(LOG), "log_rows": len(rows),
                              "new_signal_pins": added_sig, "new_outcome_pins": added_out})
        write_manifest(m)
    print(f"pin: +{added_sig} signal pin(s), +{added_out} outcome pin(s)"
          + ("" if (added_sig or added_out) else " (nothing new; manifest unchanged)"))
    p2, _, _ = run_check(quiet=True)
    if p2:
        print("post-pin check FAILED:\n  - " + "\n  - ".join(p2))
        return 1
    return 0


def run_init():
    if os.path.exists(MANIFEST):
        print("init refused: lock_manifest.json already exists (append-only).")
        return 1
    cols, rows = read_log()
    if cols != EXPECTED_COLUMNS:
        print(f"init refused: unexpected columns {cols}")
        return 1
    keys = [key_of(r) for r in rows]
    if len(keys) != len(set(keys)):
        print("init refused: duplicate keys in log.csv")
        return 1
    ts_s = now_utc().strftime("%Y-%m-%dT%H:%M:%SZ")
    m = {
        "schema": "shadow_log_lock_v1",
        "purpose": "IRONCLAD append-only lock for Theme Radar research-only shadow shorts (never traded).",
        "lock_start": LOCK_START,
        "clean_from": CLEAN_FROM,
        "key_fields": KEY_FIELDS,
        "signal_fields": SIGNAL_FIELDS,
        "outcome_fields": OUTCOME_FIELDS,
        "fingerprint_method": FINGERPRINT_METHOD,
        "rules_frozen": {"path": "rules_frozen.json", "sha256": sha256_file(RULES), "pinned_at_utc": ts_s},
        "pre_lock": {
            "note": ("Rows already in log.csv when the lock started. Built before the lock; their content is "
                     "NOT fingerprinted (git history from the lock commit is their only record). Only their keys "
                     "are listed so check can tell them apart from new rows and flag deletions. Rows in "
                     "open_at_lock were unscored at lock time: their OUTCOME is pinned when scored "
                     "(a new fact recorded going forward); their signal stays unpinned."),
            "count": len(keys),
            "keys": keys,
            "open_at_lock": [key_of(r) for r in rows if not is_scored(r)],
        },
        "rows": {},
        "pin_runs": [{"at_utc": ts_s, "log_sha256": sha256_file(LOG), "log_rows": len(rows),
                      "new_signal_pins": 0, "new_outcome_pins": 0, "note": "lock created; rules hash pinned"}],
    }
    write_manifest(m)
    print(f"init: manifest created; pre_lock rows {len(keys)} ({len(m['pre_lock']['open_at_lock'])} open); "
          f"rules sha256 {m['rules_frozen']['sha256']}")
    return 0


# ---------------------------------------------------------------- scorecard
def fetch_iwm(start, end):
    """Yahoo daily IWM close (split-adjusted, not dividend-adjusted - same basis as the trade prices)."""
    p1 = int(dt.datetime.combine(dt.date.fromisoformat(start) - dt.timedelta(days=7), dt.time(), dt.timezone.utc).timestamp())
    p2 = int(dt.datetime.combine(dt.date.fromisoformat(end) + dt.timedelta(days=3), dt.time(), dt.timezone.utc).timestamp())
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/IWM?period1={p1}&period2={p2}&interval=1d"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        d = json.load(resp)["chart"]["result"][0]
    q = d["indicators"]["quote"][0]
    gmt = d.get("meta", {}).get("gmtoffset", -14400)
    out = {}
    for t, o, c in zip(d["timestamp"], q["open"], q["close"]):
        if o is None or c is None:
            continue
        day = dt.datetime.fromtimestamp(t + gmt, dt.timezone.utc).date().isoformat()
        out[day] = (round(o, 4), round(c, 4))
    return out


def load_iwm(need_dates):
    cache = {}
    if os.path.exists(IWM_CACHE):
        with open(IWM_CACHE, newline="") as f:
            for r in csv.DictReader(f):
                cache[r["date"]] = (float(r["open"]), float(r["close"]))
    missing = [d for d in need_dates if d not in cache]
    err = None
    if missing:
        try:
            fresh = fetch_iwm(min(need_dates), max(need_dates))
            today = dt.date.today().isoformat()
            for k, v in fresh.items():
                if k < today:  # never cache today's possibly-partial bar
                    cache[k] = v
            with open(IWM_CACHE, "w", newline="") as f:
                w = csv.writer(f)
                w.writerow(["date", "open", "close"])
                for k in sorted(cache):
                    w.writerow([k, cache[k][0], cache[k][1]])
        except Exception as ex:  # noqa
            err = f"{type(ex).__name__}: {ex}"
    return cache, err


def fmt_rate(x):
    return "n/a" if x is None else f"{100 * x:.1f}%"


def pct(x):
    return "n/a" if x is None else f"{100 * x:+.2f}%"


def bucket_stats(all_rows, scored, iwm):
    fb = [float(r["short_ret_fee_borrow"]) for r in scored]
    n = len(fb)
    s = {"n": n, "dates": len({r["date"] for r in scored}), "open": len(all_rows) - n,
         "win": (sum(1 for x in fb if x > 0) / n) if n else None,
         "mean": statistics.fmean(fb) if n else None,
         "median": statistics.median(fb) if n else None,
         "mean_ex_best": statistics.fmean(sorted(fb)[:-1]) if n >= 2 else None}
    bench, exc, miss = [], [], 0
    for r, x in zip(scored, fb):
        a, b = iwm.get(r["entry"]), iwm.get(r["exit_date"])
        if a and b:
            ib = -(b[1] / a[1] - 1.0)
            bench.append(ib)
            exc.append(x - ib)
        else:
            miss += 1
    s["iwm_n"] = len(bench)
    s["iwm_missing"] = miss
    s["iwm_mean"] = statistics.fmean(bench) if bench else None
    s["excess_mean"] = statistics.fmean(exc) if exc else None
    s["excess_win"] = (sum(1 for x in exc if x > 0) / len(exc)) if exc else None
    return s


def verdict(s, can_clear=True):
    if not can_clear:
        return "CONTEXT ONLY - mixed history can never clear the bar"
    if s["n"] < 30:
        return f"TOO FEW FOR A VERDICT (n={s['n']} < 30)"
    ok = s["n"] >= 60 and s["dates"] >= 12 and s["win"] > 0.55 and s["mean"] > 0
    if ok:
        return "CLEARS THE BAR"
    why = []
    if s["n"] < 60: why.append(f"n {s['n']}<60")
    if s["dates"] < 12: why.append(f"dates {s['dates']}<12")
    if s["win"] <= 0.55: why.append(f"win {100*s['win']:.1f}%<=55%")
    if s["mean"] <= 0: why.append(f"mean {pct(s['mean'])}<=0")
    return "NOT CLEARED (" + ", ".join(why) + ")"


def run_scorecard():
    problems, m, parsed = run_check(quiet=True)
    cols, rows, by_key = parsed if parsed else read_log() + (None,)
    m = m or {"rows": {}, "pre_lock": {"keys": []}}
    pre = set(m["pre_lock"]["keys"])
    locked = {k for k, e in m["rows"].items() if e.get("status") == "locked" and e.get("signal")}
    need = sorted({r["entry"] for r in rows if is_scored(r)} | {r["exit_date"] for r in rows if is_scored(r)})
    iwm, iwm_err = load_iwm(need) if need else ({}, None)
    L = []
    L.append("# Shadow-short scorecard (research only - never traded)")
    L.append("")
    L.append(f"Generated by `shadow_log_lock.py scorecard` from `log.csv` (sha256 `{sha256_file(LOG)}`, "
             f"{len(rows)} rows, last signal date {max(r['date'] for r in rows)}). Lock started {LOCK_START}.")
    L.append(f"Lock check at generation: **{'PASS' if not problems else 'FAIL - ' + '; '.join(problems)}**.")
    L.append("")
    L.append("All returns are per trade **after the 15bp fee and 0.3% borrow** (`short_ret_fee_borrow`). "
             "Win = return > 0. Entry/exit are the after-close prices on `entry` and `exit_date`.")
    L.append("")
    L.append("**The bar** (counted on LOCKED or CLEAN rows only): closed n >= 60 over >= 12 distinct signal dates, "
             "win rate > 55%, mean > 0 after fee+borrow. MIXED can never clear it. Under 30 closed trades = "
             "too few for any verdict.")
    L.append("")
    L.append("Buckets:")
    L.append("- **LOCKED** - signal fingerprint pinned the run the row was appended (signal date >= lock start). The only fully tamper-evident record.")
    L.append(f"- **CLEAN pre-lock** - built before the lock, signal date >= {CLEAN_FROM} (live shadow days only). Not fingerprinted; git history is the record.")
    L.append(f"- **CLEAN+LOCKED** - both together: every forward shadow row since {CLEAN_FROM}.")
    L.append("- **MIXED** - every row, including reconstructed/backfilled history from before the shadow started. Context only.")
    L.append("")
    if iwm_err and any(d not in iwm for d in need):
        L.append(f"TODO: IWM comparison incomplete - Yahoo fetch failed ({iwm_err}); rows without IWM prices are excluded from the IWM columns.")
        L.append("")
    L.append("IWM column: shorting IWM over the exact same entry/exit days, gross (no fee/borrow), Yahoo split-adjusted close. "
             "Excess = trade (after fee+borrow) minus that IWM short, per trade.")
    L.append("")
    for c in CELLS:
        allc = [r for r in rows if r["cell"] == c]
        bk = {
            "LOCKED": [r for r in allc if key_of(r) in locked],
            "CLEAN pre-lock": [r for r in allc if key_of(r) in pre and r["date"] >= CLEAN_FROM],
            "CLEAN+LOCKED": [r for r in allc if key_of(r) in locked or (key_of(r) in pre and r["date"] >= CLEAN_FROM)],
            "MIXED": allc,
        }
        L.append(f"## {c}")
        L.append("")
        L.append("| bucket | closed n | distinct dates | win | mean | median | mean w/o best | still open | IWM short mean (n) | excess vs IWM mean | excess win | verdict |")
        L.append("|---|---|---|---|---|---|---|---|---|---|---|---|")
        for name, rs in bk.items():
            sc = [r for r in rs if is_scored(r)]
            s = bucket_stats(rs, sc, iwm)
            v = verdict(s, can_clear=(name != "MIXED"))
            if name == "LOCKED" and s["n"] == 0:
                v = "nothing locked yet" if not rs else v
            iwm_cell = f"{pct(s['iwm_mean'])} ({s['iwm_n']}{', ' + str(s['iwm_missing']) + ' missing' if s['iwm_missing'] else ''})"
            L.append(f"| {name} | {s['n']} | {s['dates']} | {fmt_rate(s['win'])} | "
                     f"{pct(s['mean'])} | {pct(s['median'])} | {pct(s['mean_ex_best'])} | {s['open']} | {iwm_cell} | "
                     f"{pct(s['excess_mean'])} | {fmt_rate(s['excess_win'])} | {v} |")
        L.append("")
    with open(SCORECARD, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print(f"scorecard written: {SCORECARD}" + (f" (IWM note: {iwm_err})" if iwm_err else ""))
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    c = sp.add_parser("check")
    c.add_argument("--against-git", default=None, help="git ref whose manifest must be a subset of the current one")
    sp.add_parser("pin")
    sp.add_parser("scorecard")
    sp.add_parser("init", help="one-time: create the manifest (refuses if it exists)")
    a = ap.parse_args()
    if a.cmd == "check":
        p, _, _ = run_check(against_git=a.against_git)
        return 1 if p else 0
    if a.cmd == "pin":
        return run_pin()
    if a.cmd == "scorecard":
        return run_scorecard()
    if a.cmd == "init":
        return run_init()


if __name__ == "__main__":
    sys.exit(main())
