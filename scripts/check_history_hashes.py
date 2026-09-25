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
             * --restate FILE --reason "..." replaces one past entry and
               logs it to data/snapshots/RESTATEMENTS.log.
           Any other changed/deleted past entry -> exit 1, manifest untouched.

Usage
  python scripts/check_history_hashes.py verify
  python scripts/check_history_hashes.py add-new [--today YYYY-MM-DD]
  python scripts/check_history_hashes.py add-new --restate data/scores/X.csv --reason "why"
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
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


def rows_problems(root: Path, today: str | None, update: bool):
    """Check the sibling row manifests. Returns (problems, rows_manifest)."""
    probs, rows_man = hg.check_manifest(root, hg.ROWS_REL, hg.ROWS_SPECS,
                                        today, update=update)
    # Oppset fingerprints are only ever written by the oppset builder.
    p2, _ = hg.check_manifest(root, hg.OPPSET_FP_REL, hg.OPPSET_SPECS,
                              today, update=False)
    return probs + p2, rows_man


def cmd_verify(root: Path) -> int:
    man = load_manifest(root)
    bad = problems(root, man)
    for rel, why in bad.items():
        print(f"[history] FAIL {why}: {rel}", file=sys.stderr)
    rprobs, rows_man = rows_problems(root, None, update=False)
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


def cmd_add_new(root: Path, today: str, restate: str | None,
                reason: str | None) -> int:
    man = load_manifest(root)
    files = man["files"]
    bad = problems(root, man)
    log_lines: list[str] = []
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    if restate:
        if not reason or not reason.strip():
            print("[history] --restate requires a non-empty --reason", file=sys.stderr)
            return 2
        rel = Path(restate).as_posix()
        if Path(restate).is_absolute():
            rel = Path(restate).resolve().relative_to(root).as_posix()
        if rel not in files:
            print(f"[history] --restate: {rel} is not in the manifest", file=sys.stderr)
            return 2
        old = files[rel]["sha256"]
        p = root / rel
        if p.exists():
            new = sha256_file(p)
            files[rel] = {"sha256": new, "first_recorded": files[rel]["first_recorded"],
                          "restated": now[:10]}
        else:
            new = "DELETED"
            del files[rel]
        bad.pop(rel, None)
        log_lines.append(f"{now}\t{rel}\t{old}\t{new}\t{reason.strip()}")

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

    rprobs, rows_man = rows_problems(root, today, update=True)
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
    if log_lines:
        with open(root / RESTATE_LOG_REL, "a", encoding="utf-8") as fh:
            fh.write("\n".join(log_lines) + "\n")
        print(f"[history] restated {restate} (logged to {RESTATE_LOG_REL})")
    print(f"[history] added {added} new file(s); manifest now {len(files)} files")
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("mode", choices=["verify", "add-new"])
    ap.add_argument("--root", default=str(ROOT), help=argparse.SUPPRESS)
    ap.add_argument("--today", default=None,
                    help="Run date whose entries may be replaced (default: ET today)")
    ap.add_argument("--restate", default=None, help="Past file to deliberately re-hash")
    ap.add_argument("--reason", default=None, help="Required with --restate")
    a = ap.parse_args(argv)
    root = Path(a.root).resolve()
    if a.mode == "verify":
        if a.restate:
            ap.error("--restate is only valid with add-new")
        return cmd_verify(root)
    return cmd_add_new(root, a.today or et_today(), a.restate, a.reason)


if __name__ == "__main__":
    sys.exit(main())
