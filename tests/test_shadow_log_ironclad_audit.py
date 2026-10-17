"""Fail-closed first-seal audit for Theme Radar research shorts.

Run: python3 -m unittest tests.test_shadow_log_ironclad_audit
"""
from __future__ import annotations

import datetime as dt
import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "shadow_log_lock", _ROOT / "research" / "shadow_log" / "shadow_log_lock.py")
s = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(s)

FIELDS = ["cell", "signal_date", "ticker", "entry_date", "hold_days", "rules_sha256", "source"]
LOG_FIELDS = ["cell", "date", "ticker", "entry", "hold_days", "feature_date", "source",
              "exit_date", "short_ret", "short_ret_fee_only", "short_ret_fee_borrow", "tape"]


def _plan_row(hold="3"):
    vals = ["fpe_delta_t3_earn_today_3d", "2026-10-05", "AXIL", "2026-10-06", hold, "abc", "preopen"]
    return {"sha256": s.hash_values(vals), "values": vals}


class IroncladAuditTest(unittest.TestCase):
    def test_meta_note_is_add_only(self):
        self.assertTrue(s.meta_note_ok("plan_2026-10-06.csv", "plan_2026-10-06.csv"))
        self.assertTrue(s.meta_note_ok("plan_2026-10-06.csv", "plan_2026-10-06.csv | note: tape"))
        self.assertTrue(s.meta_note_ok("", "note: first note"))
        self.assertFalse(s.meta_note_ok("plan_2026-10-06.csv", "rewritten"))
        self.assertFalse(s.meta_note_ok("plan_2026-10-06.csv", "plan_2026-10-06.csvX"))

    def test_log_drift_names_the_field(self):
        row = {
            "cell": "fpe_delta_t3_earn_today_3d", "date": "2026-10-06", "ticker": "AXIL",
            "entry": "2026-10-06", "hold_days": "3", "feature_date": "2026-10-05",
            "source": "shadow", "exit_date": "2026-10-09", "short_ret": "0.1",
            "short_ret_fee_only": "0.08", "short_ret_fee_borrow": "0.05", "tape": "down",
            "meta": "plan_2026-10-06.csv",
        }
        snap = s.log_snapshot(row, "LOCKED", LOG_FIELDS)
        seal = dict(snap, sealed_at_utc="t")
        self.assertEqual(s.diff_log_seal("fpe_delta_t3_earn_today_3d|2026-10-06|AXIL", seal, row, LOG_FIELDS), [])
        noted = dict(row, meta="plan_2026-10-06.csv | note: ok")
        self.assertEqual(s.diff_log_seal("fpe_delta_t3_earn_today_3d|2026-10-06|AXIL", seal, noted, LOG_FIELDS), [])
        moved = dict(row, short_ret="0.9")
        drifts = s.diff_log_seal("fpe_delta_t3_earn_today_3d|2026-10-06|AXIL", seal, moved, LOG_FIELDS)
        self.assertEqual(len(drifts), 1)
        self.assertEqual(drifts[0]["date"], "2026-10-06")
        self.assertEqual(drifts[0]["what_changed"][0]["field"], "short_ret")
        self.assertEqual(drifts[0]["what_changed"][0]["current"], s.norm("short_ret", "0.9"))
        rewritten = dict(row, meta="rewritten")
        meta = s.diff_log_seal("k", seal, rewritten, LOG_FIELDS)
        self.assertEqual(meta[0]["what_changed"][0]["field"], "meta")
        gone = s.diff_log_seal("fpe_delta_t3_earn_today_3d|2026-10-06|AXIL", seal, None, LOG_FIELDS)
        self.assertEqual(gone[0]["what_changed"][0]["current"], "missing")

    def test_plan_drift_names_hold_and_ignores_matching_bytes(self):
        seal = {
            "file_sha256": "aaa",
            "status_lines": ["# status=fires"],
            "rows": {"fpe_delta_t3_earn_today_3d|AXIL": _plan_row("3")},
        }
        same = {
            "file_sha256": "aaa",
            "status_lines": ["# status=other"],
            "rows": {"fpe_delta_t3_earn_today_3d|AXIL": _plan_row("9")},
        }
        self.assertEqual(s.plan_content_drifts("2026-10-06", seal, same, FIELDS), [])
        moved = {
            "file_sha256": "bbb",
            "status_lines": ["# status=fires"],
            "rows": {"fpe_delta_t3_earn_today_3d|AXIL": _plan_row("9")},
        }
        drifts = s.plan_content_drifts("2026-10-06", seal, moved, FIELDS)
        kinds = [d["kind"] for d in drifts]
        self.assertIn("plan_file", kinds)
        row = next(d for d in drifts if d["kind"] == "plan_row")
        self.assertEqual(row["date"], "2026-10-06")
        self.assertEqual(row["key"], "fpe_delta_t3_earn_today_3d|AXIL")
        self.assertEqual(row["what_changed"][0]["field"], "hold_days")
        self.assertEqual(row["what_changed"][0]["sealed"], "3")
        self.assertEqual(row["what_changed"][0]["current"], "9")
        added = {
            "file_sha256": "ccc",
            "status_lines": ["# status=fires"],
            "rows": {
                "fpe_delta_t3_earn_today_3d|AXIL": _plan_row("3"),
                "fpe_delta_t3_earn_today_3d|ZZZ": _plan_row("3"),
            },
        }
        extra = s.plan_content_drifts("2026-10-06", seal, added, FIELDS)
        self.assertTrue(any(d["key"] == "fpe_delta_t3_earn_today_3d|ZZZ" for d in extra))
        missing = s.plan_content_drifts("2026-10-06", seal, None, FIELDS)
        self.assertEqual(missing[0]["what_changed"][0]["current"], "missing")

    def test_seals_are_append_only(self):
        old = {"first_seals": {
            "strategy": s.STRATEGY, "note": "n", "fingerprint_method": "m",
            "log_fields": ["cell"], "plan_fields": ["cell"],
            "plans": {"2026-10-06": {"file_sha256": "old"}},
            "log_rows": {"a|b|c": {"sha256": "old"}},
        }}
        added = json.loads(json.dumps(old))
        added["first_seals"]["log_rows"]["d|e|f"] = {"sha256": "new"}
        self.assertEqual(s.first_seal_superset_problems(old, added, "test"), [])
        changed = json.loads(json.dumps(old))
        changed["first_seals"]["plans"]["2026-10-06"]["file_sha256"] = "new"
        bad = s.first_seal_superset_problems(old, changed, "test")
        self.assertTrue(any("2026-10-06" in x for x in bad))
        dropped = json.loads(json.dumps(old))
        dropped["first_seals"] = None
        # None is not a block; treat missing block as removal
        dropped["first_seals"] = {}
        bad2 = s.first_seal_superset_problems(old, dropped, "test")
        self.assertTrue(bad2)
        self.assertEqual(s.first_seal_superset_problems({}, {"first_seals": old["first_seals"]}, "test"), [])

    def test_apply_scope_seals_does_not_rewrite(self):
        m = {"first_seals": {
            "strategy": s.STRATEGY,
            "note": s.FIRST_SEAL_NOTE,
            "fingerprint_method": s.FINGERPRINT_METHOD,
            "log_fields": list(s.SEAL_LOG_FIELDS),
            "plan_fields": list(s.SEAL_PLAN_FIELDS),
            "plans": {"2026-10-06": {"file_sha256": "keep", "rows": {}}},
            "log_rows": {"k": {"sha256": "keep"}},
        }}
        scope = {
            "plans": {"2026-10-06": {
                "entry": "2026-10-06", "file": "plans/plan_2026-10-06.csv",
                "file_sha256": "changed", "status_lines": [], "rows": {},
            }},
            "log_rows": {
                "k": {"bucket": "LOCKED", "signal_date": "2026-10-06", "entry": "2026-10-06",
                      "sha256": "changed", "values": ["x"], "meta": ""},
                "new|2026-10-07|ZZ": {"bucket": "CLEAN", "signal_date": "2026-10-07",
                                      "entry": "2026-10-07", "sha256": "n", "values": ["y"], "meta": ""},
            },
        }
        n_plans, n_logs = s.apply_scope_seals(m, scope, "2026-10-17T00:00:00Z")
        self.assertEqual((n_plans, n_logs), (0, 1))
        self.assertEqual(m["first_seals"]["plans"]["2026-10-06"]["file_sha256"], "keep")
        self.assertEqual(m["first_seals"]["log_rows"]["k"]["sha256"], "keep")
        self.assertIn("new|2026-10-07|ZZ", m["first_seals"]["log_rows"])

    def test_buckets_match_scorecard_rules(self):
        m = {
            "pre_lock": {"keys": [
                "fpe_delta_t3_earn_today_3d|2026-09-28|AYI",
                "fpe_delta_t3_earn_today_3d|2026-09-14|EPM",
            ]},
            "rows": {"fpe_delta_t3_earn_today_3d|2026-10-06|AXIL": {"status": "locked", "signal": {"sha256": "x"}}},
        }
        pidx = {"2026-10-06": {
            "rows": {("fpe_delta_t3_earn_today_3d", "AXIL", "2026-10-06", 3)},
            "timing": {"preopen": True},
        }}
        locked = {
            "cell": "fpe_delta_t3_earn_today_3d", "date": "2026-10-06", "ticker": "AXIL",
            "entry": "2026-10-06", "hold_days": "3", "short_ret": "0.1",
        }
        self.assertEqual(s.row_bucket(locked, m, pidx), "LOCKED")
        open_row = dict(locked, short_ret="")
        self.assertIsNone(s.row_bucket(open_row, m, pidx))
        late = {"2026-10-06": {"rows": set(), "timing": {"preopen": False, "reason": "late"}}}
        self.assertIsNone(s.row_bucket(locked, m, late))
        clean = {
            "cell": "fpe_delta_t3_earn_today_3d", "date": "2026-09-28", "ticker": "AYI",
            "entry": "2026-09-28", "hold_days": "3", "short_ret": "0.1",
        }
        self.assertEqual(s.row_bucket(clean, m, {}), "CLEAN")
        mixed = {
            "cell": "fpe_delta_t3_earn_today_3d", "date": "2026-09-14", "ticker": "EPM",
            "entry": "2026-09-14", "hold_days": "3", "short_ret": "0.1",
        }
        self.assertIsNone(s.row_bucket(mixed, m, {}))

    def test_gaps_stay_missing_and_do_not_fail(self):
        gaps = s.plan_gap_dates("2026-10-12", {"2026-10-06", "2026-10-07", "2026-10-08", "2026-10-09"})
        dates = [g["date"] for g in gaps]
        self.assertNotIn("2026-10-10", dates)  # Saturday
        self.assertNotIn("2026-10-11", dates)  # Sunday
        self.assertNotIn("2026-10-12", dates)  # today is not a past gap
        self.assertEqual(dates, [])
        missing_friday = s.plan_gap_dates("2026-10-13", {"2026-10-06"})
        self.assertIn("2026-10-09", [g["date"] for g in missing_friday])
        report = s.finalize_report({
            "drift": [], "missing_seals": [], "gaps": [{"date": "2026-10-10", "reason": "no plan file"}],
            "blocked": None,
        }, [])
        self.assertTrue(report["ok"])
        self.assertEqual(report["summary"]["gaps"], 1)

    def test_slot_is_1830_et(self):
        self.assertTrue(s.audit_slot_due(dt.datetime(2026, 10, 16, 18, 30), "schedule")[0])
        self.assertFalse(s.audit_slot_due(dt.datetime(2026, 10, 16, 19, 30), "schedule")[0])
        self.assertFalse(s.audit_slot_due(dt.datetime(2026, 12, 15, 17, 30), "schedule")[0])
        self.assertTrue(s.audit_slot_due(dt.datetime(2026, 12, 15, 18, 30), "schedule")[0])
        self.assertTrue(s.audit_slot_due(dt.datetime(2026, 10, 17, 11, 0), "workflow_dispatch")[0])
        # 22:30 UTC in October is 18:30 EDT
        oct_2230 = dt.datetime(2026, 10, 16, 22, 30, tzinfo=dt.timezone.utc)
        self.assertTrue(s.audit_slot_due(s.to_et(oct_2230), "schedule")[0])
        dec_2230 = dt.datetime(2026, 12, 15, 22, 30, tzinfo=dt.timezone.utc)
        self.assertFalse(s.audit_slot_due(s.to_et(dec_2230), "schedule")[0])
        dec_2330 = dt.datetime(2026, 12, 15, 23, 30, tzinfo=dt.timezone.utc)
        self.assertTrue(s.audit_slot_due(s.to_et(dec_2330), "schedule")[0])

    def test_live_audit_passes(self):
        proc = subprocess.run(
            [sys.executable, str(_ROOT / "research" / "shadow_log" / "shadow_log_lock.py"),
             "audit", "--json", "-"],
            cwd=_ROOT, capture_output=True, text=True, check=False)
        self.assertEqual(proc.returncode, 0, proc.stderr + proc.stdout)
        report = json.loads(proc.stdout)
        self.assertEqual(report["strategy"], "theme_radar_research_shorts")
        self.assertTrue(report["ok"])
        self.assertEqual(report["drift"], [])
        self.assertEqual(report["missing_seals"], [])
        self.assertGreaterEqual(report["sealed"]["plans"], 9)
        self.assertGreaterEqual(report["sealed"]["log_rows"], 232)


if __name__ == "__main__":
    unittest.main()
