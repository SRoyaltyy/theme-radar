"""Theme Radar score engine — loads split source parts."""
from __future__ import annotations

from pathlib import Path

_dir = Path(__file__).resolve().parent
_src = (_dir / "_score_engine_a.txt").read_text(encoding="utf-8") + (
    _dir / "_score_engine_b.txt"
).read_text(encoding="utf-8")
exec(compile(_src, str(_dir / "score_engine_full.py"), "exec"), globals())
