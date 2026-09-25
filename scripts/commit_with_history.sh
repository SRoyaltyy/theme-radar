#!/usr/bin/env bash
# Commit workflow outputs, then record history hashes on top of the freshest
# main, then push. Used by score_delta / composite_rank / backtest.
#
#   scripts/commit_with_history.sh "<commit message>" <today YYYY-MM-DD> <paths...>
#
# Why the manifests are recorded AFTER `git pull --rebase`: several workflows
# append to data/snapshots/HASHES.json / ROWS.json and can overlap (cron delays).
# Recording on the rebased tree avoids manifest merge conflicts and re-checks
# every past entry against what is actually on main. If a past-dated record
# changed, add-new exits 1 and nothing is pushed.
set -euo pipefail
PY="$(command -v python || command -v python3)"
msg="$1"; today="$2"; shift 2
MANIFESTS=(data/snapshots/HASHES.json data/snapshots/ROWS.json data/snapshots/RESTATEMENTS.log)

# Manifests are regenerated after the rebase; drop any mid-run edits.
git checkout -- "${MANIFESTS[@]}" 2>/dev/null || true
for p in "$@"; do git add -- "$p" 2>/dev/null || true; done
git reset -q -- "${MANIFESTS[@]}" 2>/dev/null || true
git commit -m "$msg" || echo "No output changes"

for attempt in 1 2 3; do
  git pull --rebase --autostash origin main
  "$PY" scripts/check_history_hashes.py add-new --today "$today"
  git add -- "${MANIFESTS[@]}" 2>/dev/null || true
  git commit -m "auto: history manifest (${msg#auto: })" || echo "No manifest changes"
  if git push origin main; then
    exit 0
  fi
  echo "[commit] push rejected (attempt $attempt); re-recording on newer main"
  if git log -1 --format=%s | grep -q '^auto: history manifest'; then
    git reset -q --soft HEAD~1
  fi
  git reset -q -- "${MANIFESTS[@]}" 2>/dev/null || true
  git checkout -- "${MANIFESTS[@]}" 2>/dev/null || true
  sleep $((attempt * 5))
done
echo "[commit] giving up after 3 attempts" >&2
exit 1
