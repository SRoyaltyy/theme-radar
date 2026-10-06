# Pre-open plans

One file per entry day: `plan_<entry date>.csv`, committed **before 09:30 America/New_York** on that day. Built by `../plan_build.py` (via `../plan_run.sh`) and pinned by `../shadow_log_lock.py plan-pin`.

Columns: `cell,signal_date,ticker,entry_date,hold_days,rules_sha256,source`. After the rows come `#` lines: `# status=fires|no_fires ...`, the build time, and the inputs used (with sha256s). A header-only file with `# status=no_fires` means the rules fired nothing that day. A missing file means **no plan**.

Append-only: never edit, overwrite or delete a plan. `letters_<entry date>.csv` is the Excel CLEAR letter input behind the plan's DCP rows (only written when there were DCP candidates).
