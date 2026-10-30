#!/usr/bin/env python3
"""Fill shadow-log outcomes from theme-radar's own data/labels files.

Stdlib only. This is the method the 2026-10-30 evening run used after the box
wipe removed the old evening scoring scripts (commits 8a01175 / 53fda8d).

For a row with entry date E and hold_days N, using data/labels/E_fwd.csv:
  exit_date            = label_date_N of the row's ticker
  short_ret            = short_fwd_Nd of the row's ticker (after-close E -> after-close exit)
  short_ret_fee_only   = short_ret - 0.0015   (15bp fee)
  short_ret_fee_borrow = short_ret - 0.0045   (fee + 0.3% borrow)
  tape                 = "up" if the median fwd_1d across the whole E_fwd.csv
                         universe is > 0, else "down"
Values are written as repr(round(x, 16)), matching the existing log.

Safety: only rows whose outcome fields are ALL empty are touched. Already
filled (sealed) rows are never rewritten. Rows whose label is not out yet
stay empty. Default is a dry run; pass --write to update log.csv.
Run shadow_log_lock.py check / pin afterwards as usual.
"""
import argparse, csv, os, statistics, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
LOG = os.path.join(HERE, "log.csv")
LABELS = os.path.join(REPO, "data", "labels")
FEE = 0.0015
BORROW = 0.003
OUTCOME = ["exit_date", "short_ret", "short_ret_fee_only", "short_ret_fee_borrow", "tape"]

_cache = {}


def load_labels(date, labels_dir=LABELS):
    key = (labels_dir, date)
    if key not in _cache:
        p = os.path.join(labels_dir, f"{date}_fwd.csv")
        if not os.path.exists(p):
            _cache[key] = None
        else:
            with open(p, newline="") as fh:
                _cache[key] = {r["Ticker"]: r for r in csv.DictReader(fh)}
    return _cache[key]


def tape_for(date, labels_dir=LABELS):
    lab = load_labels(date, labels_dir)
    if not lab:
        return None
    v = [float(r["fwd_1d"]) for r in lab.values() if r.get("fwd_1d")]
    if not v:
        return None
    return "up" if statistics.median(v) > 0 else "down"


def fmt(x):
    return repr(round(x, 16))


def outcome_for(row, labels_dir=LABELS):
    """Return the outcome dict for a row, or None if its label isn't out yet."""
    lab = load_labels(row["entry"], labels_dir)
    if not lab or row["ticker"] not in lab:
        return None
    h = int(float(row["hold_days"]))
    x = lab[row["ticker"]]
    sr, ex = x.get(f"short_fwd_{h}d"), x.get(f"label_date_{h}")
    tape = tape_for(row["entry"], labels_dir)
    if not sr or not ex or tape is None:
        return None
    sr = float(sr)
    return {"exit_date": ex, "short_ret": fmt(sr), "short_ret_fee_only": fmt(sr - FEE),
            "short_ret_fee_borrow": fmt(sr - FEE - BORROW), "tape": tape}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--log", default=LOG)
    ap.add_argument("--labels", default=LABELS)
    ap.add_argument("--write", action="store_true", help="write log.csv (default: dry run)")
    a = ap.parse_args(argv)
    with open(a.log, newline="") as fh:
        rd = csv.DictReader(fh)
        fields, rows = rd.fieldnames, list(rd)
    filled = 0
    for r in rows:
        if any(r[k] for k in OUTCOME):
            continue  # sealed / already scored: never touch
        o = outcome_for(r, a.labels)
        if o:
            r.update(o)
            filled += 1
            print("fill", r["cell"], r["date"], r["ticker"], o["exit_date"], o["short_ret"], o["tape"])
    print(f"{filled} row(s) fillable", "(written)" if a.write else "(dry run)")
    if a.write and filled:
        tmp = a.log + ".tmp"
        with open(tmp, "w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=fields, lineterminator="\n")
            w.writeheader()
            w.writerows(rows)
        os.replace(tmp, a.log)
    return 0


if __name__ == "__main__":
    sys.exit(main())
