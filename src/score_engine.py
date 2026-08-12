"""Theme Radar score engine — bootstrap known-good core, then explicit scan.md.

Core implementation is loaded from commit 64eafa9 (stable scoring).
scan_report.brief overrides the old brief so daily scan.md is layman-explicit.
"""
from __future__ import annotations

import urllib.request
from pathlib import Path

_FALLBACK_URL = (
    "https://raw.githubusercontent.com/SRoyaltyy/theme-radar/"
    "64eafa9/src/score_engine.py"
)
_CACHE = Path(__file__).resolve().parent / "_score_engine_cache.py"


def _ensure() -> str:
    if _CACHE.exists() and _CACHE.stat().st_size > 1000:
        return _CACHE.read_text(encoding="utf-8")
    try:
        text = urllib.request.urlopen(_FALLBACK_URL, timeout=60).read().decode()
        if "def snapshot_dates" in text and "def main" in text:
            _CACHE.write_text(text, encoding="utf-8")
            return text
    except Exception as e:
        raise RuntimeError(f"score_engine bootstrap failed: {e}") from e
    raise RuntimeError("score_engine bootstrap: invalid payload")


exec(compile(_ensure(), str(_CACHE), "exec"), globals())

# Override human report with explicit pair / Ret% / driver wording
from .scan_report import brief as brief  # noqa: E402, F811
