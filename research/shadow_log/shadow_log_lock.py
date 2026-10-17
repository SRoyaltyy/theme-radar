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
             after 15bp fee + 0.3% borrow, vs shorting IWM). Each cell is judged
             against Cyrus's bar first (win > 55% over >= 30 closed trades, after-fee
             mean shown), then the stricter extra check (n >= 60, >= 12 dates,
             win > 55%, mean > 0). Also adds/refreshes the scorecard_* keys in
             summary.json (other keys are left untouched).
  plan-pin   Run check first. Then record the sha256 of every plans/plan_<entry>.csv
             not yet in the manifest. Never alters or removes an existing plan pin.
  plan-status [ENTRY_DATE]
             Show each plan file's first git commit time vs 09:30 America/New_York on
             its entry date. With a date: exit 0 if that plan was committed pre-open,
             1 if it exists but is not (yet) a pre-open commit, 2 if there is no plan.
  audit      Fail-closed first-seal fingerprint audit (strategy
             theme_radar_research_shorts). Compares every sealed pre-open plan and
             every closed LOCKED/CLEAN log row to its first-seal fingerprint in
             lock_manifest.json. Exit 0 = pass, non-zero = fail. Prints a console
             report and a JSON summary (``--json PATH`` or ``--json -``).
             ``--seal`` appends first-seal fingerprints that are missing for
             currently sealed days. It never rewrites a seal, a plan, or a log row.
             A seal that already exists and no longer matches is a hard fail; the
             manifest is left untouched. Days with no plan stay missing (no backfill).

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
SUMMARY = os.path.join(HERE, "summary.json")
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
STRATEGY = "theme_radar_research_shorts"
# Closed-row seal covers the buy/sell (signal) and the close (outcome). meta is
# not hashed: an added note is allowed; a rewrite of meta is still a hard fail.
SEAL_LOG_FIELDS = SIGNAL_FIELDS + OUTCOME_FIELDS
SEAL_PLAN_FIELDS = list(PLAN_COLUMNS)
REL_LOG = "research/shadow_log/log.csv"
FIRST_SEAL_NOTE = (
    "Append-only first-seal fingerprints for sealed pre-open plans and closed LOCKED/CLEAN "
    "shadow-log rows (strategy theme_radar_research_shorts). Written once; never rewritten. "
    "A missing plan day stays missing (no backfill). meta may only grow by an added note. "
    "Rewriting a sealed field is a hard fail. The audit never rewrites row content.")
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


def _nth_sunday(year, month, n):
    x = dt.date(year, month, 1)
    x += dt.timedelta(days=(6 - x.weekday()) % 7)
    return x + dt.timedelta(weeks=n - 1)


def _eastern_offset_hours(day):
    """Hours behind UTC for America/New_York on this date (US DST rules since 2007)."""
    dst = _nth_sunday(day.year, 3, 2) <= day < _nth_sunday(day.year, 11, 1)
    return 4 if dst else 5


def ny_open_utc(iso):
    """09:30 America/New_York on date iso, as an aware UTC datetime (US DST rules since 2007;
    stdlib only, no tzdata needed)."""
    d = dt.date.fromisoformat(iso)
    off = _eastern_offset_hours(d)
    return dt.datetime(d.year, d.month, d.day, PREOPEN_HHMM[0] + off, PREOPEN_HHMM[1], tzinfo=dt.timezone.utc)


def to_et(utc_dt):
    """Aware UTC datetime -> America/New_York wall time (naive clock, DST-adjusted)."""
    if utc_dt.tzinfo is None:
        utc_dt = utc_dt.replace(tzinfo=dt.timezone.utc)
    utc_dt = utc_dt.astimezone(dt.timezone.utc)
    day = utc_dt.date()
    et = utc_dt - dt.timedelta(hours=_eastern_offset_hours(day))
    if et.date() != day:
        et = utc_dt - dt.timedelta(hours=_eastern_offset_hours(et.date()))
    # Wall clock in America/New_York. tzinfo is dropped so callers compare .time()
    # against naive ET times (the instant is already shifted).
    return et.replace(tzinfo=None)


def today_et():
    return to_et(now_utc()).date().isoformat()


def audit_slot_due(now_et, event):
    """Weekday crons fire at 22:30 and 23:30 UTC so one of them is 18:30 ET.

    Manual events (pull_request, workflow_dispatch, push) always run. The other
    scheduled slot is a no-op so the audit runs once per weekday, after the
    evening append. Returns (run, reason)."""
    if event != "schedule":
        return True, f"{event}: always run"
    t = now_et.time()
    if dt.time(18, 30) <= t < dt.time(19, 30):
        return True, "weekday 18:30 America/New_York slot"
    return False, "other DST cron slot (no-op; the 18:30 ET slot runs the audit)"


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
    # first-seal fingerprints: existing seals must still match. Missing seals are
    # not a check failure (pin / audit --seal append them); a mismatch is.
    problems += [format_drift(d) for d in existing_seal_drifts(m, by_key)]
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
            fs = m.get("first_seals") or {}
            print(f"CHECK OK: rules sha256 {actual_rules}; log rows {len(rows)}; "
                  f"pre_lock {len(m['pre_lock']['keys'])}; signal pins {n_sig}; outcome pins {n_out}; "
                  f"plan files {len(plan_files())} (pinned {len(m.get('plans') or {})}; git {git_state()[0]}); "
                  f"first seals plans {len(fs.get('plans') or {})} log rows {len(fs.get('log_rows') or {})}"
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
    p += first_seal_superset_problems(old, new, label)
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
    # First-seal any pre-open plan and closed LOCKED/CLEAN row that does not have
    # one yet. Never rewrites a seal or a CSV row. Skipped (with a warning) when
    # git history cannot prove which plans were committed before the open.
    n_seal_plans = n_seal_logs = 0
    scope, scope_err = sealed_scope(m, rows, today_et())
    if scope_err:
        print(f"pin: first-seal skipped ({scope_err})")
    else:
        n_seal_plans, n_seal_logs = apply_scope_seals(m, scope, ts_s)
    # append-only guard: every old pin must survive untouched
    bad = manifest_superset_problems(old, m, "pre-pin manifest")
    if bad:
        print("pin refused: would modify/remove existing pins:\n  - " + "\n  - ".join(bad))
        return 1
    if added_sig or added_out or n_seal_plans or n_seal_logs:
        entry = {"at_utc": ts_s}
        if added_sig or added_out:
            entry.update(log_sha256=sha256_file(LOG), log_rows=len(rows),
                         new_signal_pins=added_sig, new_outcome_pins=added_out)
        if n_seal_plans or n_seal_logs:
            entry["first_seals"] = {"plans": n_seal_plans, "log_rows": n_seal_logs}
        m["pin_runs"].append(entry)
        write_manifest(m)
    print(f"pin: +{added_sig} signal pin(s), +{added_out} outcome pin(s), "
          f"+{n_seal_plans} plan seal(s), +{n_seal_logs} log-row seal(s)"
          + ("" if (added_sig or added_out or n_seal_plans or n_seal_logs) else " (nothing new; manifest unchanged)"))
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
    sealed_now = []
    for name in added:
        if not plans[name]["pinned_before_open"]:
            continue
        # The plan file is not in git yet (plan-pin runs before the commit). The
        # clock says this pin is before 09:30 ET, so record the first seal of
        # these bytes in the same manifest write. A later edit fails closed.
        fs = ensure_first_seals_block(m)
        snap = plan_snapshot(name, fs.get("plan_fields"))
        if record_plan_seal(fs, snap, ts_s, True):
            sealed_now.append(plan_entry(name))
    bad = manifest_superset_problems(old, m, "pre-plan-pin manifest")
    if bad:
        print("plan-pin refused: would modify/remove existing pins:\n  - " + "\n  - ".join(bad))
        return 1
    if added:
        run = {"at_utc": ts_s, "plan_pins": added}
        if sealed_now:
            run["first_seals"] = {"plans": len(sealed_now), "log_rows": 0, "plan_dates": sealed_now}
        m["pin_runs"].append(run)
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


# Reporting only. Cyrus's standing bar is the primary verdict; the older 60/12 bar
# is kept as a stricter extra check. Both are counted on LOCKED or CLEAN rows only.
CYRUS_MIN_N = 30
WIN_BAR = 0.55
EXTRA_MIN_N = 60
EXTRA_MIN_DATES = 12
CYRUS_BAR_TEXT = (f"Cyrus's bar (primary): win rate > {100*WIN_BAR:.0f}% over >= {CYRUS_MIN_N} closed trades, "
                  "after-fee+borrow mean shown (and called out if <= 0). LOCKED or CLEAN rows only; MIXED never counts.")
EXTRA_BAR_TEXT = (f"Stricter extra check: closed n >= {EXTRA_MIN_N} over >= {EXTRA_MIN_DATES} distinct signal dates, "
                  f"win rate > {100*WIN_BAR:.0f}%, mean > 0 after fee+borrow. LOCKED or CLEAN rows only; MIXED never counts.")


def cyrus_verdict(s, can_clear=True):
    """Return (code, text). code in CONTEXT_ONLY / TOO_FEW / MET / MET_BUT_MEAN_NEGATIVE /
    MET_BUT_MEAN_ZERO / NOT_MET. The after-fee+borrow mean is always in the text."""
    if not can_clear:
        return "CONTEXT_ONLY", "CONTEXT ONLY - mixed history never counts"
    if s["n"] < CYRUS_MIN_N:
        return "TOO_FEW", f"TOO FEW FOR A VERDICT (n={s['n']} < {CYRUS_MIN_N})"
    m = f"mean after fee+borrow {pct(s['mean'])}"
    if s["win"] > WIN_BAR:
        head = f"MEETS CYRUS BAR (win {100*s['win']:.1f}% > {100*WIN_BAR:.0f}%, n {s['n']} >= {CYRUS_MIN_N})"
        if s["mean"] < 0:
            return "MET_BUT_MEAN_NEGATIVE", head + f" BUT LOSES MONEY: {m} is NEGATIVE"
        if s["mean"] == 0:
            return "MET_BUT_MEAN_ZERO", head + f" BUT MAKES NO MONEY: {m}"
        return "MET", head + f"; {m}"
    return "NOT_MET", (f"DOES NOT MEET CYRUS BAR (win {100*s['win']:.1f}% <= {100*WIN_BAR:.0f}%, n {s['n']}); {m}"
                       + (" (negative)" if s["mean"] < 0 else ""))


def extra_code(s, can_clear=True):
    if not can_clear:
        return "CONTEXT_ONLY"
    if s["n"] < CYRUS_MIN_N:
        return "TOO_FEW"
    ok = s["n"] >= EXTRA_MIN_N and s["dates"] >= EXTRA_MIN_DATES and s["win"] > WIN_BAR and s["mean"] > 0
    return "CLEARS" if ok else "NOT_CLEARED"


def verdict(s, can_clear=True):
    """Stricter extra check (the original 60/12 bar). Text unchanged from before."""
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
    L.append("**The bar** - each cell is judged against Cyrus's bar first; the older 60/12 bar is shown as a stricter extra check. "
             "Both count LOCKED or CLEAN rows only; MIXED can never meet either. Under 30 closed trades = too few for any verdict.")
    L.append("")
    L.append(f"1. **{CYRUS_BAR_TEXT.split(':', 1)[0]}**:{CYRUS_BAR_TEXT.split(':', 1)[1]} "
             "A cell that meets it on win rate but loses money after fee+borrow is flagged **LOSES MONEY** on the same line.")
    L.append(f"2. **{EXTRA_BAR_TEXT.split(':', 1)[0]}**:{EXTRA_BAR_TEXT.split(':', 1)[1]}")
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
    sv = {}
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
        L.append("| bucket | closed n | distinct dates | win | mean | median | mean w/o best | still open | IWM short mean (n) | excess vs IWM mean | excess win | Cyrus bar (>55% win over >=30) | stricter extra check (60/12) |")
        L.append("|---|---|---|---|---|---|---|---|---|---|---|---|---|")
        vlines = []
        sv[c] = {}
        for name, rs in bk.items():
            sc = [r for r in rs if is_scored(r)]
            s = bucket_stats(rs, sc, iwm)
            can = name != "MIXED"
            ccode, cv = cyrus_verdict(s, can_clear=can)
            v = verdict(s, can_clear=can)
            if name == "LOCKED" and s["n"] == 0 and not rs:
                cv = v = "nothing locked yet"
            iwm_cell = f"{pct(s['iwm_mean'])} ({s['iwm_n']}{', ' + str(s['iwm_missing']) + ' missing' if s['iwm_missing'] else ''})"
            L.append(f"| {name} | {s['n']} | {s['dates']} | {fmt_rate(s['win'])} | "
                     f"{pct(s['mean'])} | {pct(s['median'])} | {pct(s['mean_ex_best'])} | {s['open']} | {iwm_cell} | "
                     f"{pct(s['excess_mean'])} | {fmt_rate(s['excess_win'])} | {cv} | {v} |")
            vlines.append(f"- **{name}** - Cyrus bar: {cv}. Stricter extra check (60/12): {v}.")
            sv[c][name] = {
                "closed_n": s["n"], "distinct_dates": s["dates"], "open": s["open"],
                "win_fee_borrow": s["win"], "mean_fee_borrow": s["mean"],
                "counts_toward_bar": can,
                "cyrus_bar": ccode, "cyrus_bar_text": cv,
                "cyrus_bar_met_but_mean_negative": bool(ccode == "MET_BUT_MEAN_NEGATIVE"),
                "extra_check": extra_code(s, can_clear=can), "extra_check_text": v,
            }
        L.append("")
        L.append("Verdicts (Cyrus's bar first, then the stricter extra check):")
        L.append("")
        L.extend(vlines)
        L.append("")
    with open(SCORECARD, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print(f"scorecard written: {SCORECARD}" + (f" (IWM note: {iwm_err})" if iwm_err else ""))
    write_summary_verdicts(sv, problems, rows)
    return 0


def write_summary_verdicts(sv, problems, rows):
    """Add/refresh scorecard_* keys in summary.json. Every other key is kept as is
    (including the older 'bar' and seen_designed_after verdict fields)."""
    if not os.path.exists(SUMMARY):
        print(f"summary.json not found - scorecard verdict fields not written ({SUMMARY})")
        return
    try:
        with open(SUMMARY, encoding="utf-8") as f:
            d = json.load(f)
    except Exception as ex:  # noqa
        print(f"summary.json unreadable - scorecard verdict fields not written ({type(ex).__name__}: {ex})")
        return
    if not isinstance(d, dict):
        print("summary.json is not a JSON object - scorecard verdict fields not written")
        return
    d["scorecard_bar_primary"] = CYRUS_BAR_TEXT
    d["scorecard_bar_extra"] = EXTRA_BAR_TEXT
    d["scorecard_verdicts"] = {
        "note": "From shadow_log_lock.py scorecard (LOCKED / CLEAN only count; MIXED is context). "
                "cyrus_bar is the primary verdict; extra_check is the stricter 60/12 bar. "
                "Returns are short_ret_fee_borrow. Supersedes seen_designed_after.*.verdict, which is computed on mixed history.",
        "log_sha256": sha256_file(LOG),
        "log_rows": len(rows),
        "lock_check": "PASS" if not problems else "FAIL",
        "cells": sv,
    }
    with open(SUMMARY, "w", encoding="utf-8") as f:
        json.dump(d, f, indent=2, ensure_ascii=False)
    print(f"summary.json updated: scorecard_bar_primary, scorecard_bar_extra, scorecard_verdicts")


# ---------------------------------------------------------------- first-seal audit
def hash_values(vals):
    return hashlib.sha256(json.dumps(list(vals), separators=(",", ":"), ensure_ascii=False).encode("utf-8")).hexdigest()


def seal_values(row, fields):
    return [norm(f, row.get(f, "")) for f in fields]


def meta_note_ok(sealed, current):
    """True if current meta is the sealed text or the sealed text plus an added note."""
    sealed = (sealed or "").strip()
    current = (current or "").strip()
    if current == sealed:
        return True
    if not current.startswith(sealed):
        return False
    if sealed == "":
        return True
    return current[len(sealed):len(sealed) + 1] in " \t|;,\n"


def _clip(v, n=160):
    if not isinstance(v, str):
        v = json.dumps(v, ensure_ascii=False)
    return v if len(v) <= n else v[:n] + "..."


def format_drift(d):
    bits = []
    for c in d.get("what_changed") or []:
        bits.append(f"{c.get('field')}: sealed {_clip(c.get('sealed'))!r} current {_clip(c.get('current'))!r}")
    detail = "; ".join(bits) if bits else "content moved"
    return f"first-seal drift {d.get('kind')} {d.get('date')} {d.get('key')}: {detail}"


def _row_from_by_key(by_key, key):
    item = (by_key or {}).get(key)
    if item is None:
        return None
    if isinstance(item, tuple):
        return item[1]
    return item


def plan_repo_path(date):
    return f"research/shadow_log/plans/plan_{date}.csv"


def ensure_first_seals_block(m):
    fs = m.get("first_seals")
    if fs:
        fs.setdefault("plans", {})
        fs.setdefault("log_rows", {})
        return fs
    fs = {
        "strategy": STRATEGY,
        "note": FIRST_SEAL_NOTE,
        "fingerprint_method": FINGERPRINT_METHOD,
        "log_fields": list(SEAL_LOG_FIELDS),
        "plan_fields": list(SEAL_PLAN_FIELDS),
        "plans": {},
        "log_rows": {},
    }
    m["first_seals"] = fs
    return fs


def first_seal_superset_problems(old, new, label):
    """Existing first seals may only gain new keys. A rewrite or deletion is a hard fail."""
    old_fs = old.get("first_seals")
    if not old_fs:
        return []
    new_fs = new.get("first_seals")
    if not new_fs:
        return [f"manifest first_seals removed vs {label}"]
    p = []
    for fld in ("strategy", "note", "fingerprint_method", "log_fields", "plan_fields"):
        if not _same(old_fs.get(fld), new_fs.get(fld)):
            p.append(f"manifest first_seals.{fld} changed vs {label}")
    for section in ("plans", "log_rows"):
        for k, e in (old_fs.get(section) or {}).items():
            if not _same(e, (new_fs.get(section) or {}).get(k)):
                p.append(f"manifest first_seal {section}.{k} removed or modified vs {label}")
    return p


def plan_snapshot(name, fields):
    cols, rows, status = read_plan(name)
    entry = plan_entry(name)
    rowmap = {}
    for r in rows:
        k = f"{(r.get('cell') or '').strip()}|{(r.get('ticker') or '').strip()}"
        vals = seal_values(r, fields)
        rowmap[k] = {"sha256": hash_values(vals), "values": vals}
    return {
        "entry": entry,
        "file": f"plans/{name}",
        "path": plan_repo_path(entry),
        "file_sha256": sha256_file(os.path.join(PLANS_DIR, name)),
        "status_lines": list(status),
        "rows": rowmap,
    }


def log_snapshot(row, bucket, fields):
    vals = seal_values(row, fields)
    return {
        "bucket": bucket,
        "signal_date": (row.get("date") or "").strip(),
        "entry": (row.get("entry") or "").strip(),
        "sha256": hash_values(vals),
        "values": vals,
        "meta": (row.get("meta") or "").strip(),
    }


def record_plan_seal(fs, snap, ts_s, preopen):
    """Append one plan seal. Returns False if that day is already sealed (left untouched)."""
    entry = snap["entry"]
    plans = fs.setdefault("plans", {})
    if entry in plans:
        return False
    plans[entry] = {
        "entry": entry,
        "file": snap["file"],
        "file_sha256": snap["file_sha256"],
        "sealed_at_utc": ts_s,
        "preopen": bool(preopen),
        "status_lines": list(snap["status_lines"]),
        "rows": {k: {"sha256": v["sha256"], "values": list(v["values"])} for k, v in snap["rows"].items()},
    }
    return True


def record_log_seal(fs, key, snap, ts_s):
    rows = fs.setdefault("log_rows", {})
    if key in rows:
        return False
    rows[key] = {
        "bucket": snap["bucket"],
        "signal_date": snap["signal_date"],
        "entry": snap["entry"],
        "sha256": snap["sha256"],
        "values": list(snap["values"]),
        "meta": snap["meta"],
        "sealed_at_utc": ts_s,
    }
    return True


def row_bucket(r, m, pidx):
    """'LOCKED' or 'CLEAN' for a closed row that counts, else None.

    Same buckets as the scorecard: LOCKED needs a signal pin (and, from
    PLAN_REQUIRED_FROM, a pre-open plan match). CLEAN is a pre_lock row whose
    signal date is on or after CLEAN_FROM. Open rows are not sealed.
    """
    if not is_scored(r):
        return None
    k = key_of(r)
    pre = set((m.get("pre_lock") or {}).get("keys") or [])
    e = (m.get("rows") or {}).get(k) or {}
    pinned_locked = e.get("status") == "locked" and bool(e.get("signal"))
    entry = (r.get("entry") or "").strip()
    if entry >= PLAN_REQUIRED_FROM:
        ok, _why = plan_class(r, pidx)
        if ok and pinned_locked:
            return "LOCKED"
    elif pinned_locked:
        return "LOCKED"
    if k in pre and (r.get("date") or "").strip() >= CLEAN_FROM:
        return "CLEAN"
    return None


def plan_gap_dates(today, have_files):
    """Past trading days from PLAN_REQUIRED_FROM with no plan file. Not a failure."""
    out = []
    d = dt.date.fromisoformat(PLAN_REQUIRED_FROM)
    end = dt.date.fromisoformat(today) - dt.timedelta(days=1)
    while d <= end:
        iso = d.isoformat()
        if is_trading_day(iso) and iso not in have_files:
            out.append({"date": iso, "reason": "no plan file; left missing (no backfill)"})
        d += dt.timedelta(days=1)
    return out


def sealed_scope(m, rows, today):
    """Plans committed before 09:30 ET on or before today, and closed LOCKED/CLEAN rows.

    Returns (scope, error). error is set when git history cannot prove plan timing;
    the caller must fail closed and must not invent seals.
    """
    state = git_state()[0]
    if state != "ok":
        return None, f"git history {state}: full clone required to enumerate sealed pre-open plans"
    pidx = plan_index()
    plan_fields = (m.get("first_seals") or {}).get("plan_fields") or list(SEAL_PLAN_FIELDS)
    log_fields = (m.get("first_seals") or {}).get("log_fields") or list(SEAL_LOG_FIELDS)
    plans = {}
    late = []
    have = set()
    for name in plan_files():
        entry = plan_entry(name)
        have.add(entry)
        if entry > today:
            continue
        t = (pidx.get(entry) or {}).get("timing") or {}
        if t.get("preopen") is True:
            plans[entry] = plan_snapshot(name, plan_fields)
        else:
            late.append({"date": entry, "file": f"plans/{name}",
                         "reason": t.get("reason") or "not a pre-open commit"})
    logs = {}
    for r in rows:
        b = row_bucket(r, m, pidx)
        if not b:
            continue
        logs[key_of(r)] = log_snapshot(r, b, log_fields)
    scope = {
        "plans": plans,
        "log_rows": logs,
        "gaps": plan_gap_dates(today, have),
        "not_preopen_plans": late,
        "counts": {
            "plans": len(plans),
            "plan_rows": sum(len(s["rows"]) for s in plans.values()),
            "log_rows": len(logs),
            "log_rows_locked": sum(1 for s in logs.values() if s["bucket"] == "LOCKED"),
            "log_rows_clean": sum(1 for s in logs.values() if s["bucket"] == "CLEAN"),
        },
    }
    return scope, None


def apply_scope_seals(m, scope, ts_s):
    """Append first seals for in-scope plans and log rows that do not have one. Returns counts."""
    fs = ensure_first_seals_block(m)
    n_plans = n_logs = 0
    for date in sorted(scope["plans"]):
        if record_plan_seal(fs, scope["plans"][date], ts_s, True):
            n_plans += 1
    for key in sorted(scope["log_rows"]):
        if record_log_seal(fs, key, scope["log_rows"][key], ts_s):
            n_logs += 1
    return n_plans, n_logs


def plan_content_drifts(date, seal, snap, fields):
    """Compare one stored plan seal to a snapshot (None if the file is gone)."""
    path = plan_repo_path(date)
    name = f"plan_{date}.csv"
    if snap is None:
        return [{"kind": "plan_file", "date": date, "key": name, "path": path,
                 "what_changed": [{"field": "file", "sealed": "present", "current": "missing"}]}]
    if snap.get("file_sha256") == seal.get("file_sha256"):
        return []
    drifts = []
    changes = [{"field": "file_sha256", "sealed": seal.get("file_sha256"), "current": snap.get("file_sha256")}]
    if list(seal.get("status_lines") or []) != list(snap.get("status_lines") or []):
        changes.append({"field": "status_lines", "sealed": seal.get("status_lines") or [],
                        "current": snap.get("status_lines") or []})
    drifts.append({"kind": "plan_file", "date": date, "key": name, "path": path, "what_changed": changes})
    srows = seal.get("rows") or {}
    crows = snap.get("rows") or {}
    for k in sorted(set(srows) | set(crows)):
        if k not in crows:
            drifts.append({"kind": "plan_row", "date": date, "key": k, "path": path,
                           "what_changed": [{"field": "row", "sealed": "present", "current": "missing"}]})
            continue
        if k not in srows:
            drifts.append({"kind": "plan_row", "date": date, "key": k, "path": path,
                           "what_changed": [{"field": "row", "sealed": "missing", "current": "present"}]})
            continue
        sv = list((srows[k] or {}).get("values") or [])
        cv = list((crows[k] or {}).get("values") or [])
        if sv == cv:
            continue
        if len(sv) != len(cv) or len(fields) != len(sv):
            ch = [{"field": "values", "sealed": sv, "current": cv}]
        else:
            ch = [{"field": f, "sealed": a, "current": b} for f, a, b in zip(fields, sv, cv) if a != b]
        if ch:
            drifts.append({"kind": "plan_row", "date": date, "key": k, "path": path, "what_changed": ch})
    return drifts


def diff_log_seal(key, seal, row, fields):
    signal = (seal or {}).get("signal_date") or ""
    entry = (seal or {}).get("entry") or signal
    if not entry and isinstance(key, str) and key.count("|") >= 2:
        entry = key.split("|")[1]
    base = {"kind": "log_row", "date": entry, "signal_date": signal, "key": key,
            "bucket": (seal or {}).get("bucket") or "", "path": REL_LOG}
    if not isinstance(seal, dict) or "values" not in seal:
        base["what_changed"] = [{"field": "seal", "sealed": "unreadable", "current": "present" if row else "missing"}]
        return [base]
    if row is None:
        base["what_changed"] = [{"field": "row", "sealed": "present", "current": "missing"}]
        return [base]
    cur = seal_values(row, fields)
    sealed_vals = list(seal.get("values") or [])
    changes = []
    if sealed_vals != cur:
        if len(sealed_vals) != len(cur) or len(fields) != len(sealed_vals):
            changes.append({"field": "values", "sealed": sealed_vals, "current": cur})
        else:
            changes.extend({"field": f, "sealed": a, "current": b} for f, a, b in zip(fields, sealed_vals, cur) if a != b)
    if not meta_note_ok(seal.get("meta", ""), row.get("meta", "")):
        changes.append({"field": "meta", "sealed": seal.get("meta") or "",
                        "current": (row.get("meta") or "").strip(),
                        "note": "meta is add-only; rewriting it is a hard fail"})
    if hash_values(sealed_vals) != seal.get("sha256"):
        changes.append({"field": "sha256", "sealed": seal.get("sha256"), "current": hash_values(sealed_vals),
                        "note": "stored sha256 does not match stored values"})
    if not changes:
        return []
    base["what_changed"] = changes
    return [base]


def existing_seal_drifts(m, by_key):
    """Drifts of seals already in the manifest. Does not complain about missing seals."""
    fs = m.get("first_seals") or {}
    if not fs:
        return []
    drifts = []
    if fs.get("strategy") not in (None, STRATEGY):
        drifts.append({
            "kind": "manifest", "date": "", "key": "strategy", "path": REL_MANIFEST,
            "what_changed": [{"field": "strategy", "sealed": fs.get("strategy"), "current": STRATEGY}],
        })
    plan_fields = fs.get("plan_fields") or list(SEAL_PLAN_FIELDS)
    log_fields = fs.get("log_fields") or list(SEAL_LOG_FIELDS)
    for date, seal in (fs.get("plans") or {}).items():
        name = f"plan_{date}.csv"
        path = os.path.join(PLANS_DIR, name)
        if not os.path.exists(path):
            drifts.extend(plan_content_drifts(date, seal, None, plan_fields))
            continue
        try:
            snap = plan_snapshot(name, plan_fields)
        except Exception as ex:  # noqa
            drifts.append({"kind": "plan_file", "date": date, "key": name, "path": plan_repo_path(date),
                           "what_changed": [{"field": "file", "sealed": seal.get("file_sha256"),
                                             "current": f"unreadable: {ex}"}]})
            continue
        drifts.extend(plan_content_drifts(date, seal, snap, plan_fields))
    for key, seal in (fs.get("log_rows") or {}).items():
        drifts.extend(diff_log_seal(key, seal, _row_from_by_key(by_key, key), log_fields))
    return drifts


def build_report(m, rows, by_key, mode, today):
    drifts = existing_seal_drifts(m, by_key)
    scope, err = sealed_scope(m, rows, today)
    fs = m.get("first_seals") or {}
    missing, gaps, late = [], [], []
    in_scope = {"plans": 0, "plan_rows": 0, "log_rows": 0, "log_rows_locked": 0, "log_rows_clean": 0}
    if scope:
        gaps = scope["gaps"]
        late = scope["not_preopen_plans"]
        in_scope = scope["counts"]
        for date, snap in sorted(scope["plans"].items()):
            if date not in (fs.get("plans") or {}):
                missing.append({"kind": "plan", "date": date, "key": f"plan_{date}.csv", "path": snap["path"]})
        for key, snap in sorted(scope["log_rows"].items()):
            if key not in (fs.get("log_rows") or {}):
                missing.append({"kind": "log_row", "date": snap["entry"] or snap["signal_date"], "key": key,
                                "bucket": snap["bucket"], "path": REL_LOG})
    sealed_logs = fs.get("log_rows") or {}
    return {
        "schema": "theme_radar_research_shorts_ironclad_audit_v1",
        "strategy": STRATEGY,
        "ok": False,
        "mode": mode,
        "checked_at_utc": now_utc().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "asof_et": today,
        "in_scope": in_scope,
        "sealed": {
            "plans": len(fs.get("plans") or {}),
            "plan_dates": sorted((fs.get("plans") or {}).keys()),
            "log_rows": len(sealed_logs),
            "log_rows_locked": sum(1 for e in sealed_logs.values() if e.get("bucket") == "LOCKED"),
            "log_rows_clean": sum(1 for e in sealed_logs.values() if e.get("bucket") == "CLEAN"),
        },
        "summary": {},
        "drift_dates": [],
        "drift": drifts,
        "missing_seals": missing,
        "gaps": gaps,
        "not_preopen_plans": late,
        "blocked": err,
        "lock_problems": [],
        "notes": (
            "Pass (exit 0): every sealed pre-open plan and every closed LOCKED/CLEAN log row matches its "
            "first-seal fingerprint. Fail (non-zero): a previously sealed fingerprint does not match current "
            "content, a sealed plan or closed LOCKED/CLEAN row has no first-seal fingerprint, the lock check "
            "failed, or git history cannot enumerate pre-open plans. Gaps (trading days with no plan file) "
            "stay missing and are not a failure. meta may gain an added note; rewriting a sealed field is a hard fail."
        ),
    }


def finalize_report(report, problems):
    others = [p for p in (problems or []) if not str(p).startswith("first-seal drift")]
    report["lock_problems"] = others
    report["summary"] = {
        "drifts": len(report.get("drift") or []),
        "missing_seals": len(report.get("missing_seals") or []),
        "gaps": len(report.get("gaps") or []),
        "lock_problems": len(others),
    }
    report["drift_dates"] = sorted({d.get("date") for d in (report.get("drift") or []) if d.get("date")})
    report["ok"] = not (report["drift"] or report["missing_seals"] or report.get("blocked") or others)
    return report


def _human_report(report):
    L = []
    L.append(f"IRONCLAD fingerprint audit: {'PASS' if report.get('ok') else 'FAIL'}")
    L.append(f"strategy: {report.get('strategy')}")
    L.append(f"asof_et: {report.get('asof_et')}  checked_at_utc: {report.get('checked_at_utc')}  mode: {report.get('mode')}")
    scope = report.get("in_scope") or {}
    sealed = report.get("sealed") or {}
    L.append(
        f"in scope: plans {scope.get('plans', 0)} ({scope.get('plan_rows', 0)} rows); "
        f"closed log rows {scope.get('log_rows', 0)} "
        f"(LOCKED {scope.get('log_rows_locked', 0)}, CLEAN {scope.get('log_rows_clean', 0)})"
    )
    L.append(
        f"first seals: plans {sealed.get('plans', 0)} "
        f"log rows {sealed.get('log_rows', 0)} "
        f"(LOCKED {sealed.get('log_rows_locked', 0)}, CLEAN {sealed.get('log_rows_clean', 0)})"
    )
    if report.get("newly_sealed"):
        ns = report["newly_sealed"]
        L.append(f"newly sealed this run: plans {ns.get('plans', 0)}, log rows {ns.get('log_rows', 0)}")
    if report.get("blocked"):
        L.append(f"BLOCKED: {report['blocked']}")
    if report.get("lock_problems"):
        L.append(f"lock check ({len(report['lock_problems'])} problem(s)):")
        for p in report["lock_problems"]:
            L.append("  - " + p)
    if report.get("drift"):
        L.append(f"drift dates: {', '.join(report.get('drift_dates') or []) or '(none named)'}")
        for d in report["drift"]:
            L.append("  - " + format_drift(d))
    else:
        L.append("drift: none")
    missing = report.get("missing_seals") or []
    if missing:
        L.append(f"missing first seals: {len(missing)} (fail closed; run audit --seal only if the rows are still the original seal)")
        for item in missing[:40]:
            L.append(f"  - {item.get('kind')} {item.get('date')} {item.get('key')} {item.get('bucket', '')}".rstrip())
        if len(missing) > 40:
            L.append(f"  - ... {len(missing) - 40} more")
    else:
        L.append("missing first seals: none")
    gaps = report.get("gaps") or []
    if gaps:
        L.append("gaps left missing (no backfill): " + ", ".join(g["date"] for g in gaps))
    else:
        L.append("gaps: none")
    if report.get("seal_refused"):
        L.append(f"seal: {report['seal_refused']}")
    L.append("result: PASS (exit 0)" if report.get("ok") else "result: FAIL (exit 1)")
    return "\n".join(L) + "\n"


def emit_report(report, json_path):
    human = _human_report(report)
    text = json.dumps(report, indent=2, ensure_ascii=False) + "\n"
    if json_path == "-":
        sys.stderr.write(human)
        sys.stdout.write(text)
        return
    sys.stdout.write(human)
    if json_path:
        parent = os.path.dirname(os.path.abspath(json_path))
        if parent:
            os.makedirs(parent, exist_ok=True)
        with open(json_path, "w", encoding="utf-8") as f:
            f.write(text)
        sys.stdout.write(f"json: {json_path}\n")
    else:
        sys.stdout.write("--- json ---\n")
        sys.stdout.write(text)


def run_audit(seal=False, json_path=None):
    """Exit 0 when every sealed plan and closed LOCKED/CLEAN row matches its first seal.

    ``--seal`` appends missing first seals and does not rewrite row content. A drift,
    a lock-check failure, or unverifiable git history refuses the write.
    """
    mode = "seal" if seal else "check"
    today = today_et()
    problems, m, parsed = run_check(quiet=True)
    if m is None or parsed is None:
        report = finalize_report({
            "schema": "theme_radar_research_shorts_ironclad_audit_v1",
            "strategy": STRATEGY,
            "ok": False,
            "mode": mode,
            "checked_at_utc": now_utc().strftime("%Y-%m-%dT%H:%M:%SZ"),
            "asof_et": today,
            "in_scope": {},
            "sealed": {},
            "summary": {},
            "drift_dates": [],
            "drift": [],
            "missing_seals": [],
            "gaps": [],
            "not_preopen_plans": [],
            "blocked": "lock_manifest.json missing" if m is None else None,
            "lock_problems": [],
            "notes": FIRST_SEAL_NOTE,
        }, problems or ["lock_manifest.json missing"])
        emit_report(report, json_path)
        return 1
    _cols, rows, by_key = parsed
    report = finalize_report(build_report(m, rows, by_key, mode, today), problems)
    can_seal = seal and not report["drift"] and not report.get("blocked") and not report["lock_problems"]
    if can_seal and report["missing_seals"]:
        ts_s = now_utc().strftime("%Y-%m-%dT%H:%M:%SZ")
        scope, err = sealed_scope(m, rows, today)
        if err or scope is None:
            report["blocked"] = err or "could not enumerate seals"
            report["seal_refused"] = "manifest not written"
            report = finalize_report(report, problems)
        else:
            n_plans, n_logs = apply_scope_seals(m, scope, ts_s)
            if n_plans or n_logs:
                m.setdefault("pin_runs", []).append({
                    "at_utc": ts_s,
                    "first_seals": {"plans": n_plans, "log_rows": n_logs},
                    "note": "first-seal fingerprints recorded; row content not rewritten",
                })
                write_manifest(m)
            problems2, m2, parsed2 = run_check(quiet=True)
            m2 = m2 or m
            rows2 = parsed2[1] if parsed2 else rows
            by2 = parsed2[2] if parsed2 else by_key
            report = finalize_report(build_report(m2, rows2, by2, mode, today), problems2)
            report["newly_sealed"] = {"plans": n_plans, "log_rows": n_logs}
    elif seal and not report["ok"]:
        report["seal_refused"] = "manifest not written"
    elif seal:
        report["newly_sealed"] = {"plans": 0, "log_rows": 0}
    emit_report(report, json_path)
    return 0 if report.get("ok") else 1


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
    au = sp.add_parser("audit", help="fail-closed first-seal audit of sealed plans and closed LOCKED/CLEAN rows")
    au.add_argument("--seal", action="store_true",
                    help="append missing first-seal fingerprints; never rewrite a seal or a row")
    au.add_argument("--json", default=None, metavar="PATH",
                    help="write the summary JSON here, or - for JSON only on stdout")
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
    if a.cmd == "audit":
        return run_audit(seal=a.seal, json_path=a.json)


if __name__ == "__main__":
    sys.exit(main())
