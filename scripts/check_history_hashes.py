#!/usr/bin/env python3
"""Hash manifest that makes past dated history immutable-by-check.

Covers every dated file:
  data/snapshots/YYYY-MM-DD.csv and YYYY-MM-DD.raw.csv
      (NOT current.csv / previous.csv / manifest.json / archive/)
  data/features/YYYY-MM-DD*   data/scores/YYYY-MM-DD*
  data/composite/YYYY-MM-DD*  data/universe/YYYY-MM-DD*
  data/attribution/by_horizon/YYYY-MM-DD*   (write-once per-horizon records)
  01_daily/YYYY-MM-DD_{scan,universe,composite_rank}.md

Manifest: data/snapshots/HASHES.json  {path: {sha256, first_recorded}}

Sibling row-level manifests (src/history_guard.py; fill-once semantics for
outcomes that mature later, append-only for tables that grow by day):
  data/snapshots/ROWS.json                   labels (+meta), suggestion checks,
                                             attribution pointers (upgrade-only)
  research/oppset_clock_b/FINGERPRINTS.json  Clock-B oppset; verified here but
                                             only written by the oppset builder

Modes
  verify   exit 1 if any file already in the manifest changed or was deleted.
  add-new  append entries for new dated files only. Existing entries are
           never updated, except:
             * entries whose file date == --today (default: today in
               America/New_York) may be replaced (same-day rerun);
             * --restate FILE --reason "..." deliberately re-records one past
               file and logs it to data/snapshots/RESTATEMENTS.log. FILE may
               be a HASHES.json entry (or a new dated file restored from git),
               a row-fingerprinted table in ROWS.json / FINGERPRINTS.json
               (labels, suggestion checks, attribution pointer members
               D_summary.json / D_ic.csv / D_attribution.md, Clock-B oppset),
               or an untracked record (logged only, e.g. a lesson file).
               Repeat --restate/--reason pairs to restate several files in
               one run (one log line each; one --reason may cover all).
           Any other changed/deleted past entry -> exit 1, manifest untouched.

  note     append one line to RESTATEMENTS.log for a data correction whose
           kept record is already the manifest's record (nothing re-hashed,
           manifests untouched): --file F (repeatable) --old TEXT --new TEXT
           --reason TEXT. old/new describe the superseded and kept values.

Usage
  python scripts/check_history_hashes.py verify
  python scripts/check_history_hashes.py add-new [--today YYYY-MM-DD]
  python scripts/check_history_hashes.py add-new --restate data/scores/X.csv --reason "why"
  python scripts/check_history_hashes.py add-new \
      --restate research/oppset_clock_b/oppset_all.csv --reason "why A" \
      --restate data/labels/2026-08-06_fwd.csv --reason "why B"
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_REL = "data/snapshots/HASHES.json"
RESTATE_LOG_REL = "data/snapshots/RESTATEMENTS.log"

SNAP_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})(\.raw)?\.csv$")
DATED_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})[._]")
DATED_DIRS = ("data/features", "data/scores", "data/composite", "data/universe",
              "data/attribution/by_horizon")
DAILY_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})_(scan|universe|composite_rank)\.md$")

sys.path.insert(0, str(ROOT))
from src import history_guard as hg  # noqa: E402


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def file_date(rel: str) -> str | None:
    name = rel.rsplit("/", 1)[-1]
    m = SNAP_RE.match(name) or DATED_RE.match(name)
    return m.group(1) if m else None


def discover(root: Path) -> list[str]:
    out: list[str] = []
    snap = root / "data/snapshots"
    if snap.is_dir():
        out += [f"data/snapshots/{p.name}" for p in snap.iterdir()
                if p.is_file() and SNAP_RE.match(p.name)]
    for d in DATED_DIRS:
        dd = root / d
        if dd.is_dir():
            out += [f"{d}/{p.name}" for p in dd.iterdir()
                    if p.is_file() and DATED_RE.match(p.name)]
    daily = root / "01_daily"
    if daily.is_dir():
        out += [f"01_daily/{p.name}" for p in daily.iterdir()
                if p.is_file() and DAILY_RE.match(p.name)]
    return sorted(out)


def load_manifest(root: Path) -> dict:
    p = root / MANIFEST_REL
    if not p.exists():
        return {"version": 1, "algorithm": "sha256", "files": {}}
    return json.loads(p.read_text(encoding="utf-8"))


def save_manifest(root: Path, man: dict) -> None:
    man["files"] = dict(sorted(man["files"].items()))
    (root / MANIFEST_REL).write_text(
        json.dumps(man, indent=1, sort_keys=False) + "\n", encoding="utf-8")


def problems(root: Path, man: dict) -> dict[str, str]:
    """{rel: 'changed'|'deleted'} for manifest entries that no longer match."""
    bad: dict[str, str] = {}
    for rel, ent in man["files"].items():
        p = root / rel
        if not p.exists():
            bad[rel] = "deleted"
        elif sha256_file(p) != ent["sha256"]:
            bad[rel] = "changed"
    return bad


def et_today() -> str:
    return datetime.now(ZoneInfo("America/New_York")).date().isoformat()


def rows_problems(root: Path, today: str | None, update: bool,
                  restate: dict[str, set[str]] | None = None):
    """Check the sibling row manifests. Returns (problems, rows_manifest,
    oppset_manifest). ``restate`` = {manifest_rel: {table_rel}} re-fingerprinted
    first (deliberate, logged restatement)."""
    restate = restate or {}
    probs, rows_man = hg.check_manifest(root, hg.ROWS_REL, hg.ROWS_SPECS,
                                        today, update=update,
                                        restate=restate.get(hg.ROWS_REL, ()))
    # Oppset fingerprints are only written by the oppset builder, or here by a
    # logged --restate.
    p2, opp_man = hg.check_manifest(root, hg.OPPSET_FP_REL, hg.OPPSET_SPECS,
                                    today, update=False,
                                    restate=restate.get(hg.OPPSET_FP_REL, ()))
    return probs + p2, rows_man, opp_man


def head_sha(root: Path, rel: str) -> str:
    """sha256 of rel as committed at HEAD ('ABSENT' if not in HEAD / no git)."""
    try:
        r = subprocess.run(["git", "-C", str(root), "show", f"HEAD:{rel}"],
                           capture_output=True, check=False)
    except OSError:
        return "ABSENT"
    if r.returncode != 0:
        return "ABSENT"
    return hashlib.sha256(r.stdout).hexdigest()


def cmd_verify(root: Path) -> int:
    man = load_manifest(root)
    bad = problems(root, man)
    for rel, why in bad.items():
        print(f"[history] FAIL {why}: {rel}", file=sys.stderr)
    rprobs, rows_man, _ = rows_problems(root, None, update=False)
    for x in rprobs:
        print(f"[history] FAIL rows: {x}", file=sys.stderr)
    if rprobs and not bad:
        print(f"[history] {len(rprobs)} row fingerprint(s) no longer match. Past "
              "rows are append-only; matured grades are fill-once.", file=sys.stderr)
        return 1
    if bad:
        print(f"[history] {len(bad)} manifest entr(y/ies) no longer match. "
              "Past days are immutable; use add-new --restate FILE --reason ... "
              "only for a deliberate, logged restatement.", file=sys.stderr)
        return 1
    n_rows = len(rows_man["tables"]) + len(hg.load_rows_manifest(
        root, hg.OPPSET_FP_REL)["tables"])
    print(f"[history] OK: {len(man['files'])} files + {n_rows} row-fingerprinted "
          "tables verified")
    return 0


def cmd_add_new(root: Path, today: str, restate: list[str] | None,
                reason: list[str] | None) -> int:
    man = load_manifest(root)
    files = man["files"]
    bad = problems(root, man)
    log_lines: list[str] = []
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    restate = [restate] if isinstance(restate, str) else list(restate or [])
    reason = [reason] if isinstance(reason, str) else list(reason or [])
    rows_restate: dict[str, set[str]] = {}

    if restate:
        if not reason or any(not (r or "").strip() for r in reason):
            print("[history] --restate requires a non-empty --reason", file=sys.stderr)
            return 2
        if len(reason) not in (1, len(restate)):
            print("[history] give one --reason for all --restate files, or one each",
                  file=sys.stderr)
            return 2
        reasons = reason * len(restate) if len(reason) == 1 else reason
        discovered = set(discover(root))
        for raw, why in zip(restate, reasons):
            rel = Path(raw).as_posix()
            if Path(raw).is_absolute():
                rel = Path(raw).resolve().relative_to(root).as_posix()
            p = root / rel
            tab = hg.table_for(root, rel)
            in_hashes = rel in files or (rel in discovered and p.exists())
            if not in_hashes and tab is None and not p.exists():
                print(f"[history] --restate: {rel} is not in any manifest and does "
                      "not exist", file=sys.stderr)
                return 2
            old = files[rel]["sha256"] if rel in files else head_sha(root, rel)
            new = sha256_file(p) if p.exists() else "DELETED"
            if in_hashes:
                if p.exists():
                    first = files.get(rel, {}).get("first_recorded", today)
                    files[rel] = {"sha256": new, "first_recorded": first,
                                  "restated": now[:10]}
                else:
                    files.pop(rel, None)
                bad.pop(rel, None)
            if tab is not None:
                rows_restate.setdefault(tab[0], set()).add(tab[1])
            log_lines.append(f"{now}\t{rel}\t{old}\t{new}\t{why.strip()}")

    # Same-day rerun: today's entries may be replaced/removed.
    for rel in [r for r in bad if file_date(r) == today]:
        p = root / rel
        if p.exists():
            files[rel] = {"sha256": sha256_file(p), "first_recorded": today}
            print(f"[history] same-day rewrite allowed ({today}): {rel}")
        else:
            del files[rel]
            print(f"[history] same-day delete allowed ({today}): {rel}")
        bad.pop(rel)

    rprobs, rows_man, opp_man = rows_problems(root, today, update=True,
                                              restate=rows_restate)
    if bad or rprobs:
        for rel, why in bad.items():
            print(f"[history] FAIL past file {why}: {rel}", file=sys.stderr)
        for x in rprobs:
            print(f"[history] FAIL rows: {x}", file=sys.stderr)
        print("[history] refusing to update manifest; past dates are strict.",
              file=sys.stderr)
        return 1

    added = 0
    for rel in discover(root):
        if rel not in files:
            files[rel] = {"sha256": sha256_file(root / rel), "first_recorded": today}
            added += 1
    save_manifest(root, man)
    hg.save_rows_manifest(root, hg.ROWS_REL, rows_man)
    if rows_restate.get(hg.OPPSET_FP_REL):
        hg.save_rows_manifest(root, hg.OPPSET_FP_REL, opp_man)
    if log_lines:
        with open(root / RESTATE_LOG_REL, "a", encoding="utf-8") as fh:
            fh.write("\n".join(log_lines) + "\n")
        print(f"[history] restated {len(log_lines)} file(s): {', '.join(restate)} "
              f"(logged to {RESTATE_LOG_REL})")
    print(f"[history] added {added} new file(s); manifest now {len(files)} files")
    return 0


def cmd_note(root: Path, files: list[str] | None, old: str | None,
             new: str | None, reason: str | None) -> int:
    """Log-only entry (one-time data correction): no manifest is changed."""
    if not files or not all((x or "").strip() for x in (old, new, reason)):
        print("[history] note requires --file, --old, --new and --reason", file=sys.stderr)
        return 2
    missing = [f for f in files if not (root / f).exists()]
    if missing:
        print(f"[history] note: missing file(s) {missing}", file=sys.stderr)
        return 2
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    clean = [" ".join(x.split()) for x in (old, new, reason)]
    with open(root / RESTATE_LOG_REL, "a", encoding="utf-8") as fh:
        fh.write(f"{now}\t{';'.join(files)}\t{clean[0]}\t{clean[1]}\t{clean[2]}\n")
    print(f"[history] noted correction for {', '.join(files)} in {RESTATE_LOG_REL}")
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("mode", choices=["verify", "add-new", "note"])
    ap.add_argument("--root", default=str(ROOT), help=argparse.SUPPRESS)
    ap.add_argument("--today", default=None,
                    help="Run date whose entries may be replaced (default: ET today)")
    ap.add_argument("--restate", action="append", default=None,
                    help="Past file to deliberately re-record (repeatable)")
    ap.add_argument("--reason", action="append", default=None,
                    help="Required with --restate (one for all, or one per --restate)")
    ap.add_argument("--file", action="append", default=None, help="note: file(s) concerned")
    ap.add_argument("--old", default=None, help="note: superseded value(s)")
    ap.add_argument("--new", default=None, help="note: kept value(s)")
    a = ap.parse_args(argv)
    root = Path(a.root).resolve()
    if a.mode == "note":
        return cmd_note(root, a.file, a.old, a.new,
                        (a.reason or [None])[-1] if a.reason else None)
    if a.mode == "verify":
        if a.restate:
            ap.error("--restate is only valid with add-new")
        return cmd_verify(root)
    return cmd_add_new(root, a.today or et_today(), a.restate, a.reason)


if __name__ == "__main__":
    sys.exit(main())
