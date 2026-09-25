"""Append-only / fill-once guard for past-dated records (stdlib only).

IRONCLAD rule: records dated in the past are append-only. A new day adds rows;
it never overwrites or re-picks an earlier day. Outcomes that mature later
(forward returns graded on a later snapshot) may be filled in ONCE when they
mature; a filled value never changes afterwards.

Two layers use this module:

1. In-code writers (label_backfill, attribution, suggestion_check,
   composite_rank, segments, run_predict, the Clock-B oppset builder) call the
   helpers here so a nightly rerun keeps an existing past record instead of
   rewriting it.
2. scripts/check_history_hashes.py verifies/records row-level fingerprints in
   sibling manifests of data/snapshots/HASHES.json:
     data/snapshots/ROWS.json                  labels, suggestion checks,
                                               attribution pointers
     research/oppset_clock_b/FINGERPRINTS.json Clock-B oppset (written only by
                                               the oppset builder)

Fingerprints are over the literal CSV cell strings (csv module, no float
re-parsing), sorted, so re-serialising identical rows is a no-op while any
changed cell, added/removed row, or removed day fails.

Each fingerprint "part" carries an ``asof`` date: the latest snapshot date the
part depends on. A part may be replaced only when ``asof == today`` (ET) — the
same-day rerun exception that HASHES.json already has for files dated today
(e.g. the ~23:00 UTC cron re-fetch of today's snapshot). Anything older is
strict.
"""
from __future__ import annotations

import csv
import hashlib
import io
import json
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

ROWS_REL = "data/snapshots/ROWS.json"
OPPSET_FP_REL = "research/oppset_clock_b/FINGERPRINTS.json"

csv.field_size_limit(1 << 30)

DATE_RE = re.compile(r"(\d{4}-\d{2}-\d{2})")


def today_et() -> str:
    return datetime.now(ZoneInfo("America/New_York")).date().isoformat()


def is_past(date_str: str, today: str | None = None) -> bool:
    return str(date_str) < (today or today_et())


def keep_existing_past(paths, date_str: str, what: str,
                       today: str | None = None) -> bool:
    """True (and log) when any output exists for a past date -> caller must skip.

    Past dates are write-once: a rerun for a date before today never replaces
    an existing record. Today's outputs may be replaced (same-day rerun).
    """
    today = today or today_et()
    if not is_past(date_str, today):
        return False
    existing = [str(p) for p in paths if Path(p).exists()]
    if existing:
        print(f"[history] {what} {date_str}: past date already recorded "
              f"({', '.join(Path(e).name for e in existing)}); keeping it "
              f"(append-only; today={today})")
        return True
    return False


# ---------------------------------------------------------------- csv helpers

def read_csv_text(text: str) -> tuple[list[str], list[list[str]]]:
    rdr = csv.reader(io.StringIO(text))
    try:
        header = next(rdr)
    except StopIteration:
        return [], []
    return header, [r for r in rdr]


def read_csv_path(path: Path) -> tuple[list[str], list[list[str]]]:
    with open(path, newline="", encoding="utf-8") as fh:
        return read_csv_text(fh.read())


def _sha_rows(header: list[str], rows: list[list[str]], cols: list[str]) -> str:
    idx = [header.index(c) if c in header else None for c in cols]
    lines = sorted("\x1f".join((r[i] if (i is not None and i < len(r)) else "")
                               for i in idx) for r in rows)
    h = hashlib.sha256()
    h.update("\x1f".join(cols).encode())
    for ln in lines:
        h.update(b"\n")
        h.update(ln.encode())
    h.update(f"\nrows={len(rows)}".encode())
    return h.hexdigest()


def _mode(vals) -> str:
    vals = [v for v in vals if v]
    return Counter(vals).most_common(1)[0][0] if vals else ""


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


# ---------------------------------------------------------- fingerprinters
# Each returns {group: {part: {"sha": str, "asof": "YYYY-MM-DD" | ""}}}

LABEL_BASE = ["Ticker", "scan_date", "signal_asof", "entry_price", "price_T"]


def label_part_cols(k: int) -> list[str]:
    cols = ["Ticker", f"prediction_day_{k}d", f"label_date_{k}",
            f"exit_price_{k}d", f"price_T{k}", f"fwd_{k}d", f"short_fwd_{k}d"]
    if k == 3:
        cols += ["up_3d", "down_3d"]
    return cols


def fp_labels(header, rows, file_date: str) -> dict:
    parts = {"base": {"sha": _sha_rows(header, rows, LABEL_BASE), "asof": file_date}}
    for k in (1, 2, 3):
        c = f"prediction_day_{k}d"
        if c not in header:
            continue
        i = header.index(c)
        asof = _mode(r[i] for r in rows if i < len(r))
        if asof:
            parts[f"{k}d"] = {"sha": _sha_rows(header, rows, label_part_cols(k)),
                              "asof": asof}
    return {"all": parts}


LABEL_META_GROWING = ("prediction_days", "forward_snapshots", "n_fwd_3d_valid")


def fp_label_meta(meta: dict) -> dict:
    days = list(meta.get("prediction_days") or [])
    static = {k: v for k, v in meta.items() if k not in LABEL_META_GROWING}
    parts = {}
    if days:
        parts["first"] = {"sha": hashlib.sha256(json.dumps(
            static, sort_keys=True).encode()).hexdigest(), "asof": days[0]}
    if len(days) >= 3:
        parts["final"] = {"sha": hashlib.sha256(json.dumps(
            meta, sort_keys=True).encode()).hexdigest(), "asof": days[2]}
    return {"all": parts}


def fp_grouped(header, rows, key: str, asof_col: str | None,
               base_cols: list[str] | None = None) -> dict:
    """Group rows by ``key``; one 'rows' part per group over ``base_cols``
    (default: all columns). Columns outside base_cols are fill-once grade
    columns: one part per column, recorded the first time any cell is set."""
    if key not in header:
        return {}
    ki = header.index(key)
    ai = header.index(asof_col) if asof_col and asof_col in header else None
    base = [c for c in (base_cols or header)]
    extra = [c for c in header if base_cols and c not in base_cols]
    groups: dict[str, list] = {}
    for r in rows:
        groups.setdefault(r[ki] if ki < len(r) else "", []).append(r)
    out = {}
    for g, rs in groups.items():
        asof = _mode(r[ai] for r in rs) if ai is not None else ""
        parts = {"rows": {"sha": _sha_rows(header, rs, base), "asof": asof}}
        idx_key = [c for c in ("ticker", "Ticker") if c in header][:1]
        for c in extra:
            ci = header.index(c)
            if any(ci < len(r) and r[ci] != "" for r in rs):
                parts[f"grade:{c}"] = {"sha": _sha_rows(header, rs, idx_key + [c]),
                                       "asof": ""}
        out[g] = parts
    return out


def horizon_of(label: str) -> int:
    m = re.search(r"(\d+)d", label or "")
    return int(m.group(1)) if m else 0


def fp_attr_pointer(root: Path, summary_rel: str) -> dict:
    """Upgrade-only pointer: data/attribution/D_summary.json (+ D_ic.csv,
    01_daily/D_attribution.md). Group = label;
    a label's content never changes once recorded; the label may only move to a
    longer matured horizon (1d -> 2d -> 3d). Every horizon's record is also kept
    immutably in data/attribution/by_horizon/ (HASHES.json)."""
    p = root / summary_rel
    d = json.loads(p.read_text(encoding="utf-8"))
    date = DATE_RE.search(p.name).group(1)
    h = hashlib.sha256()
    for rel in attr_pointer_files(date):
        f = root / rel
        h.update(f"{rel}={sha256_file(f) if f.exists() else '-'}\n".encode())
    return {str(d.get("label", "")): {"files": {
        "sha": h.hexdigest(), "asof": str(d.get("prediction_day") or "")}}}


def attr_pointer_files(date: str) -> list[str]:
    return [f"data/attribution/{date}_summary.json",
            f"data/attribution/{date}_ic.csv",
            f"01_daily/{date}_attribution.md"]
    # 02_lessons/candidate/D_lesson.md is deliberately excluded: the weekly
    # promote job flips its status field (candidate -> promoted).


# ------------------------------------------------------------------- specs

OPPSET_BASE_COLS = [
    "join_morning", "finviz_asof", "ticker", "sector",
    "price", "avg_vol", "mcap", "rvol",
    "change_pct", "chg_open_pct", "gap_pct", "ah_change_pct", "pweek",
    "flag_rvol_ge_2", "flag_rvol_ge_3", "flag_rvol_ge_5",
    "flag_abs_chg_ge_5", "flag_abs_chg_ge_8", "flag_abs_chg_ge_10",
    "flag_abs_gap_ge_3", "flag_abs_gap_ge_5",
    "flag_abs_ah_chg_ge_2", "flag_abs_ah_chg_ge_5",
    "flag_pweek_ge_15", "flag_pweek_ge_40",
    "any_opp",
]

ROWS_SPECS = [
    ("data/labels", re.compile(r"^\d{4}-\d{2}-\d{2}_fwd\.csv$"), "labels"),
    ("data/labels", re.compile(r"^\d{4}-\d{2}-\d{2}_fwd\.meta\.json$"), "label_meta"),
    ("data/attribution", re.compile(r"^\d{4}-\d{2}-\d{2}_suggestion_check\.csv$"), "suggestion"),
    ("data/attribution", re.compile(r"^\d{4}-\d{2}-\d{2}_summary\.json$"), "attr_pointer"),
]

OPPSET_SPECS = [
    ("research/oppset_clock_b", re.compile(r"^oppset_(all|flagged|0916_0918)\.csv$"), "oppset"),
]


def discover(root: Path, specs) -> dict[str, str]:
    out = {}
    for d, rx, kind in specs:
        dd = root / d
        if dd.is_dir():
            for p in sorted(dd.iterdir()):
                if p.is_file() and rx.match(p.name):
                    out[f"{d}/{p.name}"] = kind
    return out


def fingerprint(root: Path, rel: str, kind: str) -> dict:
    p = root / rel
    date_m = DATE_RE.search(p.name)
    if kind == "labels":
        h, rows = read_csv_path(p)
        return fp_labels(h, rows, date_m.group(1))
    if kind == "label_meta":
        return fp_label_meta(json.loads(p.read_text(encoding="utf-8")))
    if kind == "suggestion":
        h, rows = read_csv_path(p)
        return fp_grouped(h, rows, "horizon", "prediction_day")
    if kind == "attr_pointer":
        return fp_attr_pointer(root, rel)
    if kind == "oppset":
        h, rows = read_csv_path(p)
        return fp_grouped(h, rows, "join_morning", "finviz_asof", OPPSET_BASE_COLS)
    raise ValueError(kind)


# ---------------------------------------------------------------- compare

def compare(kind: str, recorded: dict, current: dict | None, today: str | None,
            allow_today: bool) -> tuple[list[str], dict]:
    """Return (problems, merged_groups). ``current`` None = file deleted."""
    probs: list[str] = []
    merged = json.loads(json.dumps(recorded))
    if current is None:
        return ["file deleted"], merged
    if kind == "attr_pointer":
        (cur_label, cur_parts), = current.items() if current else ((None, {}),)
        hi = max((horizon_of(g) for g in recorded), default=0)
        if horizon_of(cur_label) < hi:
            probs.append(f"downgraded to {cur_label} after {hi}d was recorded")
        rec = recorded.get(cur_label)
        if rec is None:
            merged[cur_label] = _stamp(cur_parts, today)
            return probs, merged
        for part, ent in cur_parts.items():
            if rec.get(part, {}).get("sha") != ent["sha"]:
                if allow_today and rec.get(part, {}).get("asof") == today:
                    merged[cur_label][part] = _stamp({part: ent}, today)[part]
                else:
                    probs.append(f"{cur_label}/{part} changed")
        return probs, merged
    for g, parts in recorded.items():
        for part, ent in parts.items():
            cur = (current.get(g) or {}).get(part)
            if cur is not None and cur["sha"] == ent["sha"]:
                continue
            same_day = allow_today and ent.get("asof") and ent.get("asof") == today
            if same_day:
                if cur is None:
                    merged[g].pop(part, None)
                else:
                    merged[g][part] = _stamp({part: cur}, today)[part]
                continue
            probs.append(f"{g}/{part} {'removed' if cur is None else 'changed'}")
    for g, parts in current.items():
        for part, ent in parts.items():
            if part not in merged.get(g, {}):
                merged.setdefault(g, {})[part] = _stamp({part: ent}, today)[part]
    merged = {g: p for g, p in merged.items() if p}
    return probs, merged


def _stamp(parts: dict, today: str | None) -> dict:
    return {k: {"sha": v["sha"], "asof": v.get("asof", ""),
                "first_recorded": today or ""} for k, v in parts.items()}


# ---------------------------------------------------------------- manifests

def load_rows_manifest(root: Path, rel: str) -> dict:
    p = root / rel
    if not p.exists():
        return {"version": 1, "tables": {}}
    return json.loads(p.read_text(encoding="utf-8"))


def save_rows_manifest(root: Path, rel: str, man: dict) -> None:
    man["tables"] = {k: man["tables"][k] for k in sorted(man["tables"])}
    p = root / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(man, indent=1) + "\n", encoding="utf-8")


def table_for(root: Path, rel: str) -> tuple[str, str, str] | None:
    """(manifest_rel, table_rel, kind) of the row manifest covering ``rel``.

    Attribution pointer members (D_ic.csv, 01_daily/D_attribution.md) map to
    their D_summary.json table."""
    for man_rel, specs in ((ROWS_REL, ROWS_SPECS), (OPPSET_FP_REL, OPPSET_SPECS)):
        kind = discover(root, specs).get(rel)
        if kind:
            return man_rel, rel, kind
        if rel in load_rows_manifest(root, man_rel)["tables"]:
            return man_rel, rel, load_rows_manifest(root, man_rel)["tables"][rel]["kind"]
    m = DATE_RE.search(rel.rsplit("/", 1)[-1])
    if m and rel in attr_pointer_files(m.group(1)):
        summ = attr_pointer_files(m.group(1))[0]
        if (root / summ).exists():
            return ROWS_REL, summ, "attr_pointer"
    return None


def restate_table(root: Path, man: dict, frel: str, kind: str,
                  today: str | None) -> None:
    """Deliberate restatement (logged by check_history_hashes.py --restate):
    re-fingerprint one table to its current contents. Unchanged parts keep
    their record; changed/new parts get ``restated``. Attribution pointers keep
    the history of other labels (upgrade-only check still applies)."""
    tables = man["tables"]
    old = (tables.get(frel) or {}).get("groups", {})
    cur = fingerprint(root, frel, kind) if (root / frel).exists() else {}
    new = json.loads(json.dumps(old)) if kind == "attr_pointer" else {}
    for g, parts in cur.items():
        for part, ent in parts.items():
            prev = (old.get(g) or {}).get(part)
            if prev and prev.get("sha") == ent["sha"]:
                new.setdefault(g, {})[part] = prev
                continue
            st = _stamp({part: ent}, today)[part]
            if prev:
                st["first_recorded"] = prev.get("first_recorded", "")
            st["restated"] = today or ""
            new.setdefault(g, {})[part] = st
    if cur or kind == "attr_pointer":
        tables[frel] = {"kind": kind, "groups": {g: p for g, p in new.items() if p}}
    else:
        tables.pop(frel, None)


def check_manifest(root: Path, rel: str, specs, today: str | None,
                   update: bool, restate=()) -> tuple[list[str], dict]:
    """Verify (update=False) or verify+merge new parts (update=True).

    ``restate``: table paths deliberately re-fingerprinted first (logged by the
    caller). Returns (problems, new_manifest). Callers save only when
    problems == []."""
    man = load_rows_manifest(root, rel)
    tables = man["tables"]
    found = discover(root, specs)
    for frel in restate:
        kind = found.get(frel) or (tables.get(frel) or {}).get("kind")
        if kind:
            restate_table(root, man, frel, kind, today)
    probs: list[str] = []
    for frel, ent in list(tables.items()):
        kind = ent["kind"]
        cur = fingerprint(root, frel, kind) if (root / frel).exists() else None
        p, merged = compare(kind, ent["groups"], cur, today, allow_today=update)
        probs += [f"{frel}: {x}" for x in p]
        ent["groups"] = merged
    if update:
        for frel, kind in found.items():
            if frel not in tables:
                cur = fingerprint(root, frel, kind)
                tables[frel] = {"kind": kind, "groups": {
                    g: _stamp(parts, today) for g, parts in cur.items() if parts}}
    return probs, man


def now_utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
