# Shadow shorts log, under IRONCLAD lock (research only)

**Research only.** These three short ideas are never on James's buy/sell list and are never sent to Webull. Nothing here places or suggests a trade. The log exists for one reason: to show honestly how good each strategy really is, using results nobody can quietly edit afterwards.

Cyrus approved the lock on 2026-10-06 ("apply to every strat, not just h1"; "I need the strat to show how good it really is"). It covers all three cells:

| cell | rule | hold |
|---|---|---|
| `fpe_delta_t3_earn_today_3d` | Forward P/E delta > 0 at T-3, earnings today/tomorrow/this week, short | 3 days |
| `fresh_dcp_t1_ep_ge03_2d` | fresh data-center-power tag appears at T-1, EP >= 0.03, short | 2 days |
| `fresh_dcp_t1_avoid_ah_3d` | fresh data-center-power tag appears at T-1, AH >= 1, short | 3 days |

The exact frozen rules are in `rules_frozen.json` (sha256 `e66cac9b7208117611466f5606e1ba218a9540b64756629ea8cfe21f64402ba6`, copied byte-for-byte and pinned).

## Files

| file | what it is |
|---|---|
| `log.csv` | one row per shadow short: signal fields (`cell,date,ticker,entry,hold_days,feature_date,source`) and outcome fields (`exit_date,short_ret,short_ret_fee_only,short_ret_fee_borrow,tape`), plus `meta` |
| `rules_frozen.json` | frozen rule definitions. Must never change. Its hash is pinned |
| `lock_manifest.json` | the lock: pinned fingerprints, the list of pre_lock rows, the history of pin runs |
| `shadow_log_lock.py` | `check`, `pin`, `scorecard`, `plan-pin`, `plan-status` (Python stdlib only) |
| `plans/plan_<entry>.csv` | the pre-open plan for one entry day: `cell,signal_date,ticker,entry_date,hold_days,rules_sha256,source`, then `#` status/provenance lines. Append-only, never overwritten |
| `plans/letters_<entry>.csv` | the Excel CLEAR letters the plan's DCP fires came from (only when there were DCP candidates) |
| `plan_build.py`, `plan_run.sh` | build / pin / commit / push a plan (research box only; needs pandas and the box data). CI never runs them |
| `scorecard.md` | generated results per cell (LOCKED / CLEAN / MIXED). Don't edit it by hand |
| `iwm_daily.csv` | cached Yahoo IWM daily open/close (split-adjusted), used for the "vs shorting IWM" comparison |
| `summary.json`, `milestones_posted.json`, `letters/` | the daily routine's own state and the DCP letter inputs, copied as they were on 2026-10-06 |

Returns: `short_ret` is the raw short return from the after-close price on `entry` to the after-close price on `exit_date` (theme-radar labels, `short_fwd_Nd`). `short_ret_fee_only` subtracts the 15bp fee. `short_ret_fee_borrow` also subtracts 0.3% borrow. **The scorecard uses `short_ret_fee_borrow`.**

### Correction: `milestones_posted.json`

`milestones_posted.json` wrongly records a forward P/E milestone posted on 2026-10-02 (`fpe_delta_t3_earn_today_3d`, n=122, hit 57.3%). That number came from **mixed** totals (reconstructed history plus live shadow rows), and mixed totals can never clear the bar. **The forward P/E cell has NOT cleared the bar.** The file is kept unchanged as a record of what was posted. It is not a verdict.

## What the lock does

Every row has a key: `cell|date|ticker`. The lock records a **fingerprint** (sha256) of a row's fields at the moment they become known. Any later edit to those fields changes the fingerprint, and `check` fails.

- **Signal fingerprint**: taken from `cell,date,ticker,entry,hold_days,feature_date,source` on the **same run that appends the row**, before the outcome can be known.
- **Outcome fingerprint**: taken from `exit_date,short_ret,short_ret_fee_only,short_ret_fee_borrow,tape` on the **run that scores the row**.
- **Rules hash**: the sha256 of `rules_frozen.json`.

Pins are append-only. `pin` refuses to change or remove an existing pin. CI (`.github/workflows/shadow_log_lock.yml`) runs `check` on every push or PR that touches `research/shadow_log/**`, and also when run by hand. On a push or PR it also checks that the new `lock_manifest.json` contains every entry from the previous commit's manifest, unchanged.

The fingerprint normalises numbers (`hold_days` to an int, returns to `repr(float)`), so a harmless pandas read/write round-trip doesn't break it. Any real change to a value does.

`check` fails (exit 1) and prints what broke if:
- a pinned signal or outcome fingerprint no longer matches;
- a pinned row, or a pre_lock row, is missing from `log.csv`;
- a key is duplicated, or the columns changed;
- the `rules_frozen.json` hash changed;
- (with `--against-git REF`) any manifest entry from REF was removed or modified.

## pre_lock vs locked

- **pre_lock**: the 196 rows that were already in `log.csv` on 2026-10-06, when the lock started. They were built before the lock, so they are **not fingerprinted**. Fingerprinting them now would only prove they haven't changed since today, not that they were never edited earlier. Git history from the lock commit is their only record. Only their keys are listed in the manifest, so `check` can tell them apart from new rows and catch a deleted row.
  - 27 of them were still open (unscored) at lock time (`pre_lock.open_at_lock`). When one of them is scored, its **outcome** is pinned on that run. That is a new fact recorded going forward, not a backfill. Its signal stays unpinned.
- **locked**: a row appended on or after 2026-10-06 whose signal fingerprint was pinned on the run that appended it. From entry date 2026-10-06 on it must **also** match a pre-09:30 plan (next section) to count as LOCKED in the scorecard.
- **late_append**: a new row that `pin` sees for the first time but that can't be trusted as forward. Either its signal date is before the lock start, it was first pinned more than 5 days after its signal date, or it was already scored when first seen. It is still pinned (so it can't change), but it is **never** counted as LOCKED. The reason is recorded in `late_reason`.

## Pre-open plans (the shorts are fixed before the open)

The log is written in the evening, after the entry day's open has already happened. So the log alone can't prove a short was chosen before the market opened. The plan files fix that.

- **Every trading day, before 09:30 New York time, the day's shorts are committed to git** as `plans/plan_<entry date>.csv`. It is built with the same code and the same frozen rules as the log rows, from data dated up to the previous session plus fullscan's universe file for the entry day, which lands around 04:30 ET.
  - Normal run: as soon as the inputs have landed (the previous evening's theme-radar snapshot and Yahoo closes, plus fullscan's pre-market universe file). In practice that means from about 04:45 ET on the entry day.
  - Backstop: by 09:00 ET a second run checks the plan is there and builds and commits it if not (`plan_run.sh`).
- A plan with no shorts is still committed. It has just the header and `# status=no_fires`, so **"no fires"** looks different from **"no plan"**.
- **A day with no plan file reads "no plan".** Its rows can never be LOCKED.
- **Only log rows that match a pre-09:30 plan count as LOCKED.** A match means the same cell, ticker, entry date and hold. The time that counts is when the plan file was *first* committed (`git log --diff-filter=A --format=%cI`). It has to be before 09:30 America/New_York on the entry date.
- Rows with entry on or after 2026-10-06 that have no such plan, or that differ from their plan, get the status **`no_preopen_plan`** and are never LOCKED. The first plan is `plan_2026-10-06.csv`, committed at 06:20 ET on 2026-10-06 (commit `ecdb627`), before that day's open.
- Every plan row needs a log row. If one is missing, the scorecard lists it under **MISSING log rows**. Append it. Don't skip it.
- Plans are append-only. `plan-pin` records each plan file's sha256 in `lock_manifest.json`. `check` fails if a pinned plan changed or was deleted, or if a plan differs from the version first committed. With `--against-git`, `check` also fails if a plan file that existed at that commit was modified or deleted (adding new plans is fine).
- The commit-time test needs full git history. CI checks out with `fetch-depth: 0`. In a shallow checkout, or with no git at all, plan times can't be checked, so the scorecard counts nothing from plan days as LOCKED and says so.
- One limit: git commit times are written by the machine that makes the commit. The plan's own `# built_at_utc`, the manifest's `pinned_at_utc` and GitHub's push/CI times are the cross-checks.

## Scorecard buckets and the bar

- **LOCKED**: rows whose signal was pinned when they were appended **and**, from entry 2026-10-06 on, that match a plan committed before 09:30 ET on the entry day (first plan: 2026-10-06).
- **CLEAN pre-lock**: pre_lock rows with signal date >= 2026-09-28, the live shadow days.
- **CLEAN+LOCKED**: both together, i.e. every forward row since 2026-09-28.
- **MIXED**: every scored row, including reconstructed history. Context only.

**The bar:** closed n >= 60 over >= 12 distinct signal dates, win rate > 55%, and mean > 0 after fee and borrow. It is counted on LOCKED or CLEAN rows only. **MIXED can never clear it.** Fewer than 30 closed trades means too few for any verdict.

The scorecard also shows: the mean without the single best trade; the mean return of shorting IWM over the same entry/exit days (gross, Yahoo split-adjusted close); and the per-trade excess over that IWM short.

## Daily routine (must follow this order)

Pre-open (research box; normal run from ~04:45 ET once fullscan's universe file for the day has landed, backstop by 09:00 ET):

```
research/shadow_log/plan_run.sh            # builds, plan-pins, commits and pushes plans/plan_<today>.csv; exit 0 = committed before 09:30 ET
#   exit 3 = inputs not landed yet (retry later), 4 = builder refused (Yahoo/letter problem, report), 5 = plan landed after 09:30 ET
```

Evening (after the entry day's close):

```
git pull --ff-only                                   # repo copy is the source of truth
python research/shadow_log/shadow_log_lock.py check  # FAIL -> stop, report, do NOT append
python research/shadow_log/plan_build.py --append-log <asof>   # the day's new rows = the rows of plans/plan_<asof>.csv
#  ... (only if there is NO plan for <asof>: compute the day's rows exactly as before; they will read no_preopen_plan)
#  ... fill outcomes for rows whose hold closed, exactly as before (only fill blank outcome fields)
python research/shadow_log/shadow_log_lock.py pin        # pins new signals + new outcomes
python research/shadow_log/shadow_log_lock.py scorecard  # regenerates scorecard.md
git add research/shadow_log && git commit -m "shadow_log: <asof>" && git push   # same run, never later
```

Rules for whoever runs it:
- Never edit, reorder or delete existing rows. Only append new rows and fill **blank** outcome fields.
- Never edit `lock_manifest.json` or `rules_frozen.json` by hand.
- Append, pin and commit in the **same run**. A row that sits unpinned for days becomes `late_append`.
- If `check` fails, stop and report. Don't "fix" the log to make it pass.
