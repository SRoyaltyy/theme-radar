#!/usr/bin/env python3
"""Reproduction check: every already-logged outcome in log.csv must be
reproduced from data/labels by fill_outcomes_from_labels.py.
Run: python3 research/shadow_log/test_fill_outcomes_from_labels.py
Exits non-zero on any mismatch."""
import csv, os, sys, unittest
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fill_outcomes_from_labels as F

TOL = 1e-12  # log values are stored rounded to 16 decimals


class Reproduce(unittest.TestCase):
    def test_all_logged_outcomes(self):
        with open(F.LOG, newline="") as fh:
            rows = [r for r in csv.DictReader(fh) if r["short_ret"]]
        self.assertGreater(len(rows), 0)
        bad = []
        for r in rows:
            o = F.outcome_for(r)
            key = (r["cell"], r["date"], r["ticker"], r["hold_days"])
            if o is None:
                bad.append((key, "no label")); continue
            for k in ("exit_date", "tape"):
                if o[k] != r[k]:
                    bad.append((key, k, r[k], o[k]))
            for k in ("short_ret", "short_ret_fee_only", "short_ret_fee_borrow"):
                if abs(float(o[k]) - float(r[k])) > TOL:
                    bad.append((key, k, r[k], o[k]))
        print(f"checked {len(rows)} logged rows, {len(bad)} mismatch(es)")
        self.assertEqual(bad, [], "\n".join(map(str, bad[:50])))


if __name__ == "__main__":
    unittest.main(verbosity=2)
