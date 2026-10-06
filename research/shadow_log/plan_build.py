#!/usr/bin/env python3
"""Pre-open plan builder for the research-only shadow shorts (never traded).

Runs on the research box only (needs pandas, the theme-radar clone at /tmp/tr_latest,
the read-only fullscan sparse clone used by the Excel CLEAR letters, and Yahoo).
CI never runs this file; CI only runs shadow_log_lock.py.

For entry date D (a trading day) the signal date is T = previous trading day. The fires
are computed with the SAME code the daily routine used to build the log rows:
  * FPE  (fpe_delta_t3_earn_today_3d): verbatim logic of shadow_log/work/repro_fpe.py
         Forward P/E on features/{T}_1d.csv minus features/{T-3 snapshot}_1d.csv > 0,
         gated by fullscan membership {D}_membership.csv earn in {today,tomorrow,this_week}.
  * DCP  (fresh_dcp_t1_*): verbatim logic of shadow_log/work/repro_dcp.py
         fresh_cat_data_center_power 0 on the prior snapshot and 1 on snapshot T,
         then Excel CLEAR letters for D built by shadow_log/work/build_letters_fwd.py
         (bars strictly before D, universe = membership D | liquid), EP >= 0.03 / AH >= 1.
Inputs used: theme-radar snapshots/features dated <= T, Yahoo daily bars dated <= T, and
fullscan's membership file for D, which fullscan lands pre-market on D (~04:25-04:35 ET).
That membership file is the one input not available the evening of T, so a plan for D can
be built only after it lands and must be committed before 09:30 ET on D.

usage:
  plan_build.py --plan-for D [--dry-run] [--membership PATH] [--letters PATH] [--accept-skips]
  plan_build.py --append-log D        # append log rows for every plan_D row missing from log.csv
"""
import argparse, ast, csv, datetime as dt, hashlib, io, json, os, shutil, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
PLANS = os.path.join(HERE, "plans")
LOG = os.path.join(HERE, "log.csv")
RULES = os.path.join(HERE, "rules_frozen.json")
RULES_SHA = "e66cac9b7208117611466f5606e1ba218a9540b64756629ea8cfe21f64402ba6"
TR_ROOT = os.environ.get("TR_ROOT", "/tmp/tr_latest")
TR = os.path.join(TR_ROOT, "data")
BOX_SL = "/workspace/stale-news-rejoin/shadow_log"
LETTERS_SCRIPT = os.path.join(BOX_SL, "work", "build_letters_fwd.py")
FS_CACHE = os.path.join(BOX_SL, "work")
FSU_LOCAL = "/workspace/fullscan/data/universe"
CELLS = ["fpe_delta_t3_earn_today_3d", "fresh_dcp_t1_ep_ge03_2d", "fresh_dcp_t1_avoid_ah_3d"]
HOLD = {"fpe_delta_t3_earn_today_3d": 3, "fresh_dcp_t1_ep_ge03_2d": 2, "fresh_dcp_t1_avoid_ah_3d": 3}
PLAN_COLUMNS = ["cell", "signal_date", "ticker", "entry_date", "hold_days", "rules_sha256", "source"]
LOG_COLUMNS = ["cell", "date", "ticker", "entry", "hold_days", "exit_date", "short_ret", "short_ret_fee_only",
               "short_ret_fee_borrow", "tape", "feature_date", "source", "meta"]

sys.path.insert(0, TR_ROOT)


def sha_bytes(b):
    return hashlib.sha256(b).hexdigest()


def sha_file(p):
    with open(p, "rb") as f:
        return sha_bytes(f.read())


def rule_shas():
    if sha_file(RULES) != RULES_SHA:
        sys.exit(f"ABORT: rules_frozen.json sha256 is not the pinned {RULES_SHA}")
    rules = json.load(open(RULES, encoding="utf-8"))["rules"]
    out = {r["cell"]: r["sha256"] for r in rules}
    assert set(out) == set(CELLS), out
    for r in rules:
        assert int(r["hold_days"]) == HOLD[r["cell"]], r
    return out


# ------------------------------------------------------------------ rule code (verbatim)
def snaps_list():
    return sorted(p[:10] for p in os.listdir(TR + '/features') if p.endswith('_1d.csv'))


def fpe_fires(T, t1, membership_path):
    """repro_fpe.py, unchanged logic: T = signal date, t1 = entry date."""
    import pandas as pd
    snaps = snaps_list()

    def lvl(d):
        f = pd.read_csv(f'{TR}/features/{d}_1d.csv', usecols=['Ticker', 'Forward P/E'], low_memory=False)
        f['Ticker'] = f.Ticker.astype(str); return f.drop_duplicates('Ticker').set_index('Ticker')['Forward P/E'].pipe(pd.to_numeric, errors='coerce')
    i = snaps.index(T); P = snaps[i - 3]
    fT, fP = lvl(T), lvl(P); both = fT.index.intersection(fP.index)
    d = (fT[both] - fP[both]); sig = set(d[d > 0].index)
    mc = pd.read_csv(membership_path, usecols=['Ticker', 'earn'])
    g = set(mc.loc[mc.earn.astype(str).isin(['today', 'tomorrow', 'this_week']), 'Ticker'].astype(str))
    return sorted(sig & g), {"fpe_prior_snapshot": P, "fpe_signal_n": len(sig), "earn_gate_n": len(g)}


def dcp_appear(T):
    """repro_dcp.py, unchanged logic: names whose fresh_cat_data_center_power goes 0 -> 1 at T."""
    import pandas as pd, pathlib
    from src import finviz_delta as fd

    def fresh(d):
        f = pd.read_csv(f'{TR}/features/{d}_1d.csv', usecols=['Ticker', 'cat_data_center_power'], low_memory=False)
        f['Ticker'] = f.Ticker.astype(str).str.upper(); f = f.drop_duplicates('Ticker').set_index('Ticker')
        s = fd._add_catalyst_flags(fd.load_snapshot(pathlib.Path(f'{TR}/snapshots/{d}.csv'))).drop_duplicates('Ticker').set_index('Ticker')
        return s['fresh_cat_data_center_power'].astype(float).reindex(f.index).fillna(0.0)
    snaps = snaps_list()
    P = snaps[snaps.index(T) - 1]
    fT, fP = fresh(T), fresh(P)
    both = fT.index.intersection(fP.index)
    app = set(both[((fP[both] == 0) & (fT[both] == 1)).values])
    return sorted(app), {"dcp_prior_snapshot": P}


def build_letters(t1, membership_path, cands, out_csv):
    """build_letters_fwd.py, invoked exactly as the daily routine does."""
    r = subprocess.run([sys.executable, LETTERS_SCRIPT, t1, membership_path, ",".join(cands), out_csv],
                       capture_output=True, text=True)
    sys.stderr.write(r.stdout[-4000:] + r.stderr[-4000:])
    if r.returncode != 0:
        sys.exit(f"ABORT: build_letters_fwd.py failed (rc {r.returncode})")
    info = {}
    for line in r.stdout.splitlines():
        if line.startswith("rows "):
            # "rows N skipped {...} FAILS [...]"
            info["letters_log"] = line.strip()
            info["skipped"] = line.split("skipped", 1)[1].split("FAILS", 1)[0].strip()
            info["fails"] = line.split("FAILS", 1)[1].strip()
        if " cand " in line and "universe" in line:
            info["universe_log"] = line.strip()
    return info


def dcp_fires(letters_csv):
    import pandas as pd
    let = pd.read_csv(letters_csv)
    return sorted(let[let.EP >= 0.03].ticker), sorted(let[let.AH >= 1].ticker)


# ------------------------------------------------------------------ inputs
def calendar():
    from src import trading_calendar as tc
    return tc


def resolve_membership(D, override):
    if override:
        return override, f"file:{os.path.basename(override)} sha256={sha_file(override)}"
    q = subprocess.run(["gh", "api", f"repos/SRoyaltyy/fullscan/commits?path=data/universe/{D}_membership.csv&per_page=1",
                        "--jq", ".[0] | \"\\(.sha) \\(.commit.committer.date)\""], capture_output=True, text=True)
    line = q.stdout.strip()
    if q.returncode != 0 or not line or line.startswith("null"):
        return None, f"fullscan membership {D} not landed yet (gh rc={q.returncode} {q.stderr.strip()[:200]})"
    sha, when = line.split()
    path = os.path.join(FS_CACHE, f"fs_{D}_membership_{sha[:9]}.csv")
    if not os.path.exists(path):
        b = subprocess.run(["gh", "api", f"repos/SRoyaltyy/fullscan/contents/data/universe/{D}_membership.csv?ref={sha}",
                            "-H", "Accept: application/vnd.github.raw"], capture_output=True)
        if b.returncode != 0 or not b.stdout:
            return None, f"could not download fullscan membership {D}@{sha[:9]}"
        with open(path + ".tmp", "wb") as f:
            f.write(b.stdout)
        os.replace(path + ".tmp", path)
    return path, f"fullscan@{sha[:9]} (committed {when}) sha256={sha_file(path)}"


def compute(D, membership=None, letters_out=None, letters_in=None):
    tc = calendar()
    d = dt.date.fromisoformat(D)
    if not tc.is_trading_day(d):
        sys.exit(f"ABORT: {D} is not an NYSE trading day")
    T = tc.previous_trading_day(d).isoformat()
    snaps = snaps_list()
    if T not in snaps or not os.path.exists(f"{TR}/snapshots/{T}.csv"):
        return None, {"status": "pending", "why": f"theme-radar snapshot/features for signal date {T} not landed in {TR} (git -C {TR_ROOT} pull?)"}
    later = [s for s in snaps if s > T]
    mpath, mdesc = resolve_membership(D, membership)
    if mpath is None:
        return None, {"status": "pending", "why": mdesc}
    meta = {"signal_date": T, "entry_date": D, "membership": mdesc,
            "tr_head": subprocess.run(["git", "-C", TR_ROOT, "rev-parse", "--short=9", "HEAD"], capture_output=True, text=True).stdout.strip(),
            "features_T_sha256": sha_file(f"{TR}/features/{T}_1d.csv"),
            "snapshot_T_sha256": sha_file(f"{TR}/snapshots/{T}.csv"),
            "snapshots_after_T_ignored": later}
    fpe, m1 = fpe_fires(T, D, mpath); meta.update(m1)
    app, m2 = dcp_appear(T); meta.update(m2)
    meta["dcp_candidates"] = app
    if app:
        if letters_in:
            lp = letters_in
        else:
            lp = letters_out
            meta.update(build_letters(D, mpath, app, lp))
        ep, ah = dcp_fires(lp)
        meta["letters_sha256"] = sha_file(lp)
        with open(lp, newline="") as f:
            meta["letters_rows"] = sum(1 for _ in csv.DictReader(f))
    else:
        ep, ah = [], []
        meta["letters_rows"] = 0
    fires = {"fpe_delta_t3_earn_today_3d": fpe, "fresh_dcp_t1_ep_ge03_2d": ep, "fresh_dcp_t1_avoid_ah_3d": ah}
    return fires, meta


# ------------------------------------------------------------------ plan file
def plan_path(D):
    return os.path.join(PLANS, f"plan_{D}.csv")


def write_plan(D, fires, meta, shas):
    p = plan_path(D)
    if os.path.exists(p):
        sys.exit(f"REFUSED: {p} already exists (plans are append-only; never overwritten)")
    os.makedirs(PLANS, exist_ok=True)
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(PLAN_COLUMNS)
    n = 0
    for c in CELLS:
        for tk in fires[c]:
            w.writerow([c, meta["signal_date"], tk, D, HOLD[c], shas[c], f"preopen_plan_{D}"])
            n += 1
    ts = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).strftime("%Y-%m-%dT%H:%M:%SZ")
    counts = " ".join(f"{c}={len(fires[c])}" for c in CELLS)
    buf.write(f"# status={'fires' if n else 'no_fires'} rows={n} {counts}\n")
    buf.write(f"# built_at_utc={ts} signal_date={meta['signal_date']} entry_date={D} builder_sha256={sha_file(os.path.abspath(__file__))}\n")
    buf.write("# inputs: " + json.dumps({k: v for k, v in meta.items() if k not in ("signal_date", "entry_date")},
                                       separators=(",", ":"), sort_keys=True) + "\n")
    with open(p + ".tmp", "w", encoding="utf-8", newline="") as f:
        f.write(buf.getvalue())
    os.replace(p + ".tmp", p)
    return p, n


def read_plan(D):
    p = plan_path(D)
    with open(p, newline="", encoding="utf-8") as f:
        lines = [l for l in f if not l.startswith("#")]
    return list(csv.DictReader(lines))


def append_log(D):
    plan = read_plan(D)
    with open(LOG, newline="", encoding="utf-8") as f:
        rd = csv.DictReader(f); cols = rd.fieldnames; rows = list(rd)
    assert cols == LOG_COLUMNS, cols
    have = {(r["cell"], r["date"], r["ticker"]) for r in rows}
    new = []
    for r in plan:
        k = (r["cell"], r["entry_date"], r["ticker"])
        if k in have:
            continue
        new.append({"cell": r["cell"], "date": r["entry_date"], "ticker": r["ticker"], "entry": r["entry_date"],
                    "hold_days": str(int(r["hold_days"])), "exit_date": "", "short_ret": "", "short_ret_fee_only": "",
                    "short_ret_fee_borrow": "", "tape": "", "feature_date": r["signal_date"],
                    "source": f"shadow_{r['entry_date']}", "meta": f"plan_{D}.csv"})
    extra = [r for r in rows if r["date"] == D and (r["cell"], r["ticker"]) not in {(p["cell"], p["ticker"]) for p in plan}]
    if new:
        with open(LOG, "a", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=LOG_COLUMNS, lineterminator="\n")
            for r in new:
                w.writerow(r)
    print(f"append-log {D}: plan rows {len(plan)}, appended {len(new)}, already present {len(plan) - len(new)}"
          + (f"; WARNING {len(extra)} log row(s) for {D} not in the plan (never LOCKED): "
             + ",".join(r['cell'] + ':' + r['ticker'] for r in extra) if extra else ""))
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--plan-for", metavar="ENTRY_DATE")
    g.add_argument("--append-log", metavar="ENTRY_DATE")
    ap.add_argument("--dry-run", action="store_true", help="compute and print fires; write no plan (letters go to a temp dir)")
    ap.add_argument("--membership", help="explicit fullscan membership CSV for the entry date (default: latest from GitHub)")
    ap.add_argument("--letters", help="reuse an existing letters CSV for the entry date instead of rebuilding")
    ap.add_argument("--accept-skips", action="store_true", help="write the plan even if some letter candidates were skipped")
    a = ap.parse_args()
    if a.append_log:
        return append_log(a.append_log)
    D = a.plan_for
    shas = rule_shas()
    if not a.dry_run and os.path.exists(plan_path(D)):
        print(f"plan already exists: {plan_path(D)} (append-only; nothing to do)")
        return 0
    tmpd = tempfile.mkdtemp(prefix=f"plan_{D}_")
    letters_out = os.path.join(tmpd, f"letters_{D}.csv")  # copied next to the plan only when the plan is written
    fires, meta = compute(D, a.membership, letters_out, a.letters)
    if fires is None:
        print(f"PENDING {D}: {meta['why']}")
        return 3
    print(json.dumps({"entry_date": D, "signal_date": meta["signal_date"], "fires": fires}, indent=1))
    print(json.dumps(meta, indent=1, default=str), file=sys.stderr)
    probs = []
    if meta.get("fails") not in (None, "[]"):
        probs.append(f"Yahoo fetch failures in letters: {meta['fails']}")
    try:
        n_skipped = sum(ast.literal_eval(meta.get("skipped") or "{}").values())
    except Exception:  # noqa
        n_skipped = -1
    if n_skipped != 0 and not a.accept_skips:
        probs.append(f"letter candidates skipped (stale/short history?): {meta['skipped']}")
    if meta["snapshots_after_T_ignored"]:
        print(f"note: snapshots after T present and ignored: {meta['snapshots_after_T_ignored']}", file=sys.stderr)
    if a.dry_run:
        if meta.get("dcp_candidates") and not a.letters:
            print(f"dry-run letters: {letters_out}")
        if probs:
            print("WOULD REFUSE: " + "; ".join(probs))
        return 0
    if probs:
        print("REFUSED to write plan: " + "; ".join(probs) + " (re-run, or --accept-skips after checking)")
        return 4
    if meta.get("dcp_candidates") and not a.letters:
        dst = os.path.join(PLANS, f"letters_{D}.csv")
        if os.path.exists(dst) and sha_file(dst) != meta["letters_sha256"]:
            sys.exit(f"REFUSED: {dst} exists with different content (append-only)")
        os.makedirs(PLANS, exist_ok=True)
        shutil.copyfile(letters_out, dst)
    p, n = write_plan(D, fires, meta, shas)
    print(f"wrote {p} ({n} row(s){'' if n else ', status=no_fires'})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
