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
  plan-pin   Run check first. Then record the sha256 of every plans/plan_<entry>.csv
             not yet in the manifest. Never alters or removes an existing plan pin.
  plan-status [ENTRY_DATE]
             Show each plan file's first git commit time vs 09:30 America/New_York on
             its entry date. With a date: exit 0 if that plan was committed pre-open,
             1 if it exists but is not (yet) a pre-open commit, 2 if there is no plan.

Pre-open plans: from entry date PLAN_REQUIRED_FROM on, a log row counts as LOCKED only if
its signal was pinned on the append run AND it matches (cell, ticker, entry, hold_days) a
row of plans/plan_<entry>.csv whose FIRST commit in git (git log --diff-filter=A
--format=%cI) is before 09:30 America/New_York on the entry date. Other such rows get
status no_preopen_plan and are never LOCKED. Plan rows without a log row are listed as
missing in the scorecard.

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
PLANS_DIR = os.path.join(HERE, "plans")
PLAN_COLUMNS = ["cell", "signal_date", "ticker", "entry_date", "hold_days", "rules_sha256", "source"]
# Rows with entry >= this date need a pre-09:30 ET plan to count as LOCKED.
PLAN_REQUIRED_FROM = "2026-10-06"
PREOPEN_HHMM = (9, 30)
# NYSE full closures (same list as theme-radar src/trading_calendar.py). Extend yearly.
NYSE_HOLIDAYS = {"2026-01-01", "2026-01-19", "2026-02-16", "2026-04-03", "2026-05-25", "2026-06-19",
                 "2026-07-03", "2026-09-07", "2026-11-26", "2026-12-25", "2027-01-01", "2027-01-18",
                 "2027-02-15", "2027-03-26", "2027-05-31", "2027-06-18", "2027-07-05", "2027-09-06",
                 "2027-11-25", "2027-12-24", "2027-12-31"}

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


# ---------------------------------------------------------------- plans
def is_trading_day(iso):
    d = dt.date.fromisoformat(iso)
    return d.weekday() < 5 and iso not in NYSE_HOLIDAYS


def ny_open_utc(iso):
    """09:30 America/New_York on date iso, as an aware UTC datetime (US DST rules since 2007;
    stdlib only, no tzdata needed)."""
    d = dt.date.fromisoformat(iso)

    def nth_sunday(year, month, n):
        x = dt.date(year, month, 1)
        x += dt.timedelta(days=(6 - x.weekday()) % 7)
        return x + dt.timedelta(weeks=n - 1)
    dst = nth_sunday(d.year, 3, 2) <= d < nth_sunday(d.year, 11, 1)
    off = 4 if dst else 5
    return dt.datetime(d.year, d.month, d.day, PREOPEN_HHMM[0] + off, PREOPEN_HHMM[1], tzinfo=dt.timezone.utc)


def plan_files():
    if not os.path.isdir(PLANS_DIR):
        return []
    return sorted(f for f in os.listdir(PLANS_DIR) if f.startswith("plan_") and f.endswith(".csv"))


def plan_entry(name):
    return name[len("plan_"):-len(".csv")]


def parse_plan_bytes(b):
    """-> (columns, rows, status_lines). Lines starting with '#' are status/provenance."""
    text = b.decode("utf-8")
    lines = text.splitlines(keepends=True)
    status = [l.strip() for l in lines if l.startswith("#")]
    rd = csv.DictReader([l for l in lines if not l.startswith("#")])
    rows = list(rd)
    return (rd.fieldnames or []), rows, status


def read_plan(name):
    with open(os.path.join(PLANS_DIR, name), "rb") as f:
        return parse_plan_bytes(f.read())


def plan_format_problems(name, cols, rows, status):
    p = []
    entry = plan_entry(name)
    try:
        dt.date.fromisoformat(entry)
    except ValueError:
        return [f"plan file name {name} is not plan_<YYYY-MM-DD>.csv"]
    if cols != PLAN_COLUMNS:
        p.append(f"plan {name}: columns {cols} != {PLAN_COLUMNS}")
        return p
    if not any(l.startswith("# status=") for l in status):
        p.append(f"plan {name}: no '# status=' line (needed to tell 'no fires' from 'no plan')")
    seen = set()
    for r in rows:
        if r["entry_date"] != entry:
            p.append(f"plan {name}: row {r['cell']}|{r['ticker']} has entry_date {r['entry_date']} != {entry}")
        if r["cell"] not in CELLS:
            p.append(f"plan {name}: unknown cell {r['cell']}")
        k = (r["cell"], r["ticker"])
        if k in seen:
            p.append(f"plan {name}: duplicate {r['cell']}|{r['ticker']}")
        seen.add(k)
        try:
            int(r["hold_days"])
        except ValueError:
            p.append(f"plan {name}: bad hold_days {r['hold_days']!r}")
    return p


def _git(args, binary=False, cwd=None):
    """Run git at the repo top level (so repo-relative paths work), or in HERE before the root is known."""
    if cwd is None:
        cwd = (_GIT_STATE[1] if _GIT_STATE and _GIT_STATE[1] else HERE)
    try:
        r = subprocess.run(["git"] + args, cwd=cwd, capture_output=True, text=not binary)
    except Exception as ex:  # noqa - git not installed
        return 127, ("" if not binary else b""), str(ex)
    return r.returncode, r.stdout, r.stderr


_GIT_STATE = None


def git_state():
    """-> (state, root). state: 'ok' | 'no_git' | 'shallow'. Cached."""
    global _GIT_STATE
    if _GIT_STATE is None:
        rc, root, _ = _git(["rev-parse", "--show-toplevel"], cwd=HERE)
        if rc != 0:
            _GIT_STATE = ("no_git", None)
        else:
            rc2, sh, _ = _git(["rev-parse", "--is-shallow-repository"], cwd=HERE)
            _GIT_STATE = ("shallow" if sh.strip() == "true" else "ok", root.strip())
    return _GIT_STATE


def plan_relpath(name):
    root = git_state()[1]
    return os.path.relpath(os.path.join(PLANS_DIR, name), root).replace(os.sep, "/")


def plan_timing(name):
    """First commit of a plan file vs 09:30 ET on its entry date.
    -> dict(preopen=True/False/None, first_commit=iso|None, sha, reason)."""
    entry = plan_entry(name)
    cutoff = ny_open_utc(entry)
    state, root = git_state()
    out = {"entry": entry, "cutoff_utc": cutoff.strftime("%Y-%m-%dT%H:%M:%SZ"), "first_commit": None,
           "first_commit_sha": None, "preopen": None, "reason": ""}
    if state != "ok":
        out["reason"] = f"timing unverifiable ({state}: full git history needed)"
        return out
    rc, log, err = _git(["log", "--diff-filter=A", "--format=%H %cI", "--", plan_relpath(name)])
    lines = [l for l in log.splitlines() if l.strip()]
    if rc != 0:
        out["reason"] = f"timing unverifiable (git log failed: {err.strip()[:120]})"
        return out
    if not lines:
        out["reason"] = "not committed yet"
        return out
    sha, when = lines[-1].split()  # oldest add
    t = dt.datetime.fromisoformat(when)
    out.update(first_commit=when, first_commit_sha=sha, preopen=t < cutoff)
    if len(lines) > 1:
        out["reason"] = f"added {len(lines)} times (deleted and re-added); earliest add used"
    if not out["preopen"]:
        out["reason"] = (out["reason"] + "; " if out["reason"] else "") + "first committed at/after 09:30 ET on entry date"
    return out


def plan_history_problems(name):
    """With full git history: the working file must equal the version first added."""
    t = plan_timing(name)
    if not t["first_commit_sha"]:
        return []
    rc, blob, _ = _git(["show", f"{t['first_commit_sha']}:{plan_relpath(name)}"], binary=True)
    with open(os.path.join(PLANS_DIR, name), "rb") as f:
        cur = f.read()
    if rc == 0 and blob != cur:
        return [f"plan {name} differs from the version first committed in {t['first_commit_sha'][:9]} (plans are append-only)"]
    return []


def plan_index():
    """entry_date -> {name, rows:set((cell,ticker,entry,hold)), timing, status_lines}"""
    idx = {}
    for name in plan_files():
        try:
            cols, rows, status = read_plan(name)
        except Exception as ex:  # noqa
            idx[plan_entry(name)] = {"name": name, "rows": set(), "raw": [], "timing": {"preopen": None, "reason": f"unreadable: {ex}"}, "status": []}
            continue
        keyset = set()
        for r in rows:
            try:
                keyset.add((r["cell"], r["ticker"].strip(), r["entry_date"], int(r["hold_days"])))
            except (KeyError, ValueError):
                pass
        idx[plan_entry(name)] = {"name": name, "rows": keyset, "raw": rows, "timing": plan_timing(name), "status": status}
    return idx


def plan_class(r, pidx):
    """For a log row with entry >= PLAN_REQUIRED_FROM: (True, '') if it matches a pre-open plan,
    else (False, reason)."""
    entry = r["entry"].strip()
    p = pidx.get(entry)
    if p is None:
        return False, "no plan file"
    t = p["timing"]
    if t["preopen"] is not True:
        return False, t["reason"] or "plan not pre-open"
    try:
        k = (r["cell"].strip(), r["ticker"].strip(), entry, int(float(r["hold_days"])))
    except ValueError:
        return False, "bad hold_days"
    if k not in p["rows"]:
        if any(x[0] == k[0] and x[1] == k[1] for x in p["rows"]):
            return False, "hold_days differs from the pre-open plan"
        return False, "row not in the pre-open plan"
    return True, ""


def plan_check_problems(m, by_key):
    p = []
    for name, e in (m.get("plans") or {}).items():
        path = os.path.join(PLANS_DIR, name)
        if not os.path.exists(path):
            p.append(f"pinned plan {name} was deleted")
        elif sha256_file(path) != e.get("sha256"):
            p.append(f"pinned plan {name} changed: sha256 pinned {e.get('sha256')} now {sha256_file(path)}")
    for name in plan_files():
        try:
            cols, rows, status = read_plan(name)
        except Exception as ex:  # noqa
            p.append(f"plan {name} unreadable: {ex}")
            continue
        p += plan_format_problems(name, cols, rows, status)
        if git_state()[0] == "ok":
            p += plan_history_problems(name)
    return p


def plans_against_git(ref):
    """Every plan file present at ref must still exist, byte-identical (adds are fine)."""
    state, root = git_state()
    if state == "no_git":
        return [f"could not compare plans against git {ref}: not a git checkout"]
    rel_dir = os.path.relpath(PLANS_DIR, root).replace(os.sep, "/")
    rc, out, err = _git(["ls-tree", "-r", "--name-only", ref, "--", rel_dir + "/"])
    if rc != 0:
        return [f"could not list plans at git {ref}: {err.strip()[:160]}"]
    p = []
    for rel in out.splitlines():
        name = rel.rsplit("/", 1)[-1]
        if not (name.startswith("plan_") and name.endswith(".csv")):
            continue
        rc2, old, _ = _git(["show", f"{ref}:{rel}"], binary=True)
        cur_path = os.path.join(root, rel)
        if not os.path.exists(cur_path):
            p.append(f"plan {name} existed at git {ref} and was deleted")
            continue
        with open(cur_path, "rb") as f:
            if rc2 == 0 and f.read() != old:
                p.append(f"plan {name} was modified vs git {ref} (plans may only be added)")
    return p


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
    # pre-open plan files: pinned sha256, format, unchanged since first commit
    problems += plan_check_problems(m, by_key)
    if against_git:
        problems += check_against_git(m, against_git)
        problems += plans_against_git(against_git)
    if not quiet:
        if problems:
            print(f"CHECK FAILED ({len(problems)} problem(s)):")
            for p in problems:
                print("  - " + p)
        else:
            n_sig = sum(1 for e in m["rows"].values() if e.get("signal"))
            n_out = sum(1 for e in m["rows"].values() if e.get("outcome"))
            print(f"CHECK OK: rules sha256 {actual_rules}; log rows {len(rows)}; "
                  f"pre_lock {len(m['pre_lock']['keys'])}; signal pins {n_sig}; outcome pins {n_out}; "
                  f"plan files {len(plan_files())} (pinned {len(m.get('plans') or {})}; git {git_state()[0]})"
                  + (f"; manifest + plans append-only vs {against_git}" if against_git else ""))
            pidx = plan_index()
            for entry, pl in sorted(pidx.items()):
                miss = [x for x in pl["rows"] if f"{x[0]}|{x[2]}|{x[1]}" not in by_key]
                if miss and entry < dt.datetime.now(dt.timezone.utc).date().isoformat():
                    print(f"  note: {pl['name']}: {len(miss)} plan row(s) have no log row yet - append them: "
                          + ", ".join(f"{c}|{tk}" for c, tk, _, _ in sorted(miss)))
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
    for name, e in (old.get("plans") or {}).items():
        if not _same(e, (new.get("plans") or {}).get(name)):
            p.append(f"manifest plan pin {name} removed or modified vs {label}")
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


def run_plan_pin():
    problems, m, parsed = run_check()
    if problems:
        print("plan-pin refused: check failed. Fix (or report) first.")
        return 1
    old = json.loads(json.dumps(m))
    plans = m.setdefault("plans", {})
    ts = now_utc()
    ts_s = ts.strftime("%Y-%m-%dT%H:%M:%SZ")
    added = []
    for name in plan_files():
        if name in plans:
            continue
        cols, rows, status = read_plan(name)
        bad = plan_format_problems(name, cols, rows, status)
        if bad:
            print("plan-pin refused:\n  - " + "\n  - ".join(bad))
            return 1
        st = next((l for l in status if l.startswith("# status=")), "")
        plans[name] = {"sha256": sha256_file(os.path.join(PLANS_DIR, name)), "pinned_at_utc": ts_s,
                       "rows": len(rows), "status": st[len("# status="):].split()[0] if st else "",
                       "pinned_before_open": ts < ny_open_utc(plan_entry(name))}
        added.append(name)
    bad = manifest_superset_problems(old, m, "pre-plan-pin manifest")
    if bad:
        print("plan-pin refused: would modify/remove existing pins:\n  - " + "\n  - ".join(bad))
        return 1
    if added:
        m["pin_runs"].append({"at_utc": ts_s, "plan_pins": added})
        write_manifest(m)
    print(f"plan-pin: +{len(added)} plan pin(s)" + (f" {added}" if added else " (nothing new; manifest unchanged)"))
    for n in added:
        if not plans[n]["pinned_before_open"]:
            print(f"  WARNING: {n} pinned at/after 09:30 ET on its entry date - its rows can never be LOCKED")
    p2, _, _ = run_check(quiet=True)
    if p2:
        print("post-plan-pin check FAILED:\n  - " + "\n  - ".join(p2))
        return 1
    return 0


def run_plan_status(entry=None):
    pidx = plan_index()
    m = load_manifest() or {}
    print(f"git history: {git_state()[0]}")
    for e, pl in sorted(pidx.items()):
        if entry and e != entry:
            continue
        t = pl["timing"]
        st = next((l[len("# status="):].split()[0] for l in pl["status"] if l.startswith("# status=")), "?")
        print(f"{pl['name']}: {st}, {len(pl['rows'])} row(s); pinned={'yes' if pl['name'] in (m.get('plans') or {}) else 'NO'}; "
              f"first commit {t.get('first_commit')}; cutoff {t.get('cutoff_utc')} (09:30 ET); "
              f"pre-open={t.get('preopen')}" + (f" ({t['reason']})" if t.get("reason") else ""))
    if entry:
        if entry not in pidx:
            print(f"no plan for {entry}")
            return 2
        return 0 if pidx[entry]["timing"].get("preopen") is True else 1
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
    pinned_locked = {k for k, e in m["rows"].items() if e.get("status") == "locked" and e.get("signal")}
    pidx = plan_index()
    plan_reason = {}
    locked = set()
    for r in rows:
        k = key_of(r)
        if r["entry"].strip() >= PLAN_REQUIRED_FROM:
            ok, why = plan_class(r, pidx)
            if not ok:
                plan_reason[k] = why
            if ok and k in pinned_locked:
                locked.add(k)
            elif ok:
                plan_reason[k] = "matches pre-open plan but signal not pinned on the append run (" + \
                    (m["rows"].get(k, {}).get("status") or "unpinned") + ")"
        elif k in pinned_locked:
            locked.add(k)
    log_keys = {key_of(r) for r in rows}
    missing = []  # plan rows with no log row
    for e, pl in sorted(pidx.items()):
        for c, tk, en, h in sorted(pl["rows"]):
            if f"{c}|{en}|{tk}" not in log_keys:
                missing.append((pl["name"], c, tk, en, h))
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
    L.append(f"- **LOCKED** - signal fingerprint pinned the run the row was appended (signal date >= lock start) AND, for entry dates >= {PLAN_REQUIRED_FROM}, "
             "the row matches (cell, ticker, entry, hold_days) a row of `plans/plan_<entry>.csv` first committed to git before 09:30 America/New_York on the entry date. The only fully tamper-evident record.")
    L.append(f"- **CLEAN pre-lock** - built before the lock, signal date >= {CLEAN_FROM} (live shadow days only). Not fingerprinted; git history is the record.")
    L.append(f"- **CLEAN+LOCKED** - both together: every forward shadow row since {CLEAN_FROM}.")
    L.append("- **MIXED** - every row, including reconstructed/backfilled history from before the shadow started. Context only.")
    L.append("")
    if iwm_err and any(d not in iwm for d in need):
        L.append(f"TODO: IWM comparison incomplete - Yahoo fetch failed ({iwm_err}); rows without IWM prices are excluded from the IWM columns.")
        L.append("")
    # ---- pre-open plans
    L.append("## Pre-open plans")
    L.append("")
    L.append(f"Git history for plan timing: **{git_state()[0]}**" + ("" if git_state()[0] == "ok" else
             " - plan commit times cannot be verified here, so no row from a plan day can count as LOCKED in this run."))
    L.append("")
    last = max([r["entry"].strip() for r in rows] + list(pidx.keys()) + [PLAN_REQUIRED_FROM])
    days, d = [], dt.date.fromisoformat(PLAN_REQUIRED_FROM)
    while d.isoformat() <= last:
        if is_trading_day(d.isoformat()):
            days.append(d.isoformat())
        d += dt.timedelta(days=1)
    L.append("| entry date | plan | plan rows | first commit (UTC) | before 09:30 ET? | log rows |")
    L.append("|---|---|---|---|---|---|")
    for day in days:
        nlog = sum(1 for r in rows if r["entry"].strip() == day)
        pl = pidx.get(day)
        if pl is None:
            L.append(f"| {day} | no plan | - | - | no pre-09:30 plan | {nlog} |")
            continue
        t = pl["timing"]
        st = next((l[len("# status="):].split()[0] for l in pl["status"] if l.startswith("# status=")), "?")
        L.append(f"| {day} | `{pl['name']}` ({st}) | {len(pl['rows'])} | {t.get('first_commit') or '-'} | "
                 f"{'yes' if t.get('preopen') is True else 'NO' + (' - ' + t['reason'] if t.get('reason') else '')} | {nlog} |")
    L.append("")
    if missing:
        L.append(f"**MISSING log rows: {len(missing)} plan row(s) have no log row. Append them (never skip):**")
        for name, c, tk, en, h in missing:
            L.append(f"- `{name}`: {c} | {tk} | entry {en} | hold {h}")
    else:
        L.append("Plan rows missing from log.csv: none.")
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
        lk = bk["LOCKED"]
        npp = [r for r in allc if key_of(r) in plan_reason]
        why = {}
        for r in npp:
            why[plan_reason[key_of(r)]] = why.get(plan_reason[key_of(r)], 0) + 1
        L.append(f"LOCKED (pre-09:30 plan): {len(lk)} row(s), {sum(1 for r in lk if is_scored(r))} closed, "
                 f"{sum(1 for r in lk if not is_scored(r))} open. no_preopen_plan rows (entry >= {PLAN_REQUIRED_FROM}, never LOCKED): "
                 f"{len(npp)}" + (" (" + "; ".join(f"{v} {k}" for k, v in sorted(why.items())) + ")" if why else "")
                 + f". Plan rows missing from log: {sum(1 for x in missing if x[1] == c)}.")
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
    sp.add_parser("plan-pin", help="pin sha256 of new plans/plan_<entry>.csv files (append-only)")
    ps = sp.add_parser("plan-status", help="first-commit time of plan files vs 09:30 ET")
    ps.add_argument("entry", nargs="?", default=None)
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
    if a.cmd == "plan-pin":
        return run_plan_pin()
    if a.cmd == "plan-status":
        return run_plan_status(a.entry)


if __name__ == "__main__":
    sys.exit(main())
