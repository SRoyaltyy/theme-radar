#!/usr/bin/env bash
# Build, pin, commit and push the pre-open plan for one entry date (research box only).
# usage: plan_run.sh [ENTRY_DATE]   (default: today ET if before 09:30 ET on a trading day, else next trading day)
# exit: 0 plan committed pre-open (or already there), 3 inputs not landed yet, 4 builder refused,
#       5 plan landed but NOT before 09:30 ET, 1 check/git failure
set -uo pipefail
REPO=${REPO:-/workspace/theme-radar-shadowlock}
SL=$REPO/research/shadow_log
export TR_ROOT=${TR_ROOT:-/tmp/tr_latest}
export GIT_AUTHOR_NAME=Theme-Radar-Bot GIT_AUTHOR_EMAIL=bot@users.noreply.github.com
export GIT_COMMITTER_NAME=Theme-Radar-Bot GIT_COMMITTER_EMAIL=bot@users.noreply.github.com
cd "$REPO" || exit 1
if [ -n "$(git status --porcelain -- research/shadow_log)" ]; then
  echo "ABORT: uncommitted changes under research/shadow_log; commit or report them first"; git status --short -- research/shadow_log; exit 1
fi
git pull --ff-only -q || { echo "ABORT: git pull --ff-only failed"; exit 1; }
[ -d "$TR_ROOT/.git" ] || git clone -q --filter=blob:none https://github.com/SRoyaltyy/theme-radar.git "$TR_ROOT" || exit 1
git -C "$TR_ROOT" pull --ff-only -q || { echo "ABORT: could not update $TR_ROOT"; exit 1; }
D=${1:-$(python3 - <<'PY'
import sys, datetime as dt, os
sys.path.insert(0, os.environ["TR_ROOT"])
from src import trading_calendar as tc
now = dt.datetime.now(tc.ET)
d = now.date()
print((d if tc.is_trading_day(d) and (now.hour, now.minute) < (9, 30) else tc.next_trading_day(d)).isoformat())
PY
)}
echo "entry date $D (now $(TZ=America/New_York date '+%F %H:%M ET'))"
python3 "$SL/shadow_log_lock.py" check || { echo "ABORT: lock check failed - report, do not build"; exit 1; }
if [ -f "$SL/plans/plan_$D.csv" ]; then
  echo "plan_$D.csv already in the repo (append-only; not rebuilt)"
  python3 "$SL/shadow_log_lock.py" plan-status "$D"; rc=$?
  [ $rc -eq 0 ] && exit 0 || exit 5
fi
python3 "$SL/plan_build.py" --plan-for "$D"; rc=$?
[ $rc -eq 0 ] || { echo "plan NOT written (rc=$rc)"; exit $rc; }
python3 "$SL/shadow_log_lock.py" plan-pin || exit 1
python3 "$SL/shadow_log_lock.py" check || exit 1
git add "$SL/plans/plan_$D.csv" "$SL/lock_manifest.json"
[ -f "$SL/plans/letters_$D.csv" ] && git add "$SL/plans/letters_$D.csv"
git commit -q -m "shadow_log: pre-open plan for $D" || exit 1
for i in 1 2 3 4 5; do
  git push -q origin HEAD:main && break
  echo "push rejected (attempt $i); rebasing on origin/main"; git pull --rebase -q || exit 1
done
git fetch -q origin && [ "$(git rev-parse HEAD)" = "$(git rev-parse origin/main)" ] || { echo "ABORT: push did not land"; exit 1; }
python3 "$SL/shadow_log_lock.py" plan-status "$D"; rc=$?
[ $rc -eq 0 ] && { echo "OK: plan_$D.csv committed + pushed before 09:30 ET ($(git rev-parse --short HEAD))"; exit 0; }
echo "WARNING: plan_$D.csv landed but NOT before 09:30 ET - its rows will be no_preopen_plan"; exit 5
