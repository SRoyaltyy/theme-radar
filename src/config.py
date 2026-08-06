"""Shared config for Theme Radar. All credentials come from env (same names as fullscan)."""
from __future__ import annotations
import os
from pathlib import Path

# --- credentials (never hardcode; strip to survive trailing newlines from GH secrets) ---
DEEPSEEK_API_KEY = os.environ.get("DEEPSEEK_API_KEY", "").strip()
SEARXNG_URL = os.environ.get("SEARXNG_URL", "").strip().rstrip("/")
FRED_API_KEY = os.environ.get("FRED_API_KEY", "").strip()

# --- DeepSeek ---
MODEL_PREDICT = os.environ.get("MODEL_PREDICT", "deepseek-chat").strip()
DEEPSEEK_BASE_URL = os.environ.get("DEEPSEEK_BASE_URL", "https://api.deepseek.com").strip()
MAX_TOOL_ROUNDS = 12

# --- paths ---
ROOT = Path(__file__).resolve().parent.parent
GROUNDING = ROOT / "00_grounding"
DAILY = ROOT / "01_daily"
LESSONS_ACTIVE = ROOT / "02_lessons" / "active"
SCOREBOARD_DIR = ROOT / "03_scoreboard"
ARCHIVE = ROOT / "04_archive"
DATA = ROOT / "data"
CONSOLIDATED_MEMORY = ARCHIVE / "consolidated_memory.md"

TOPIC = "theme_radar"
MEMORY_WINDOW_DAYS = 12
TZ = "America/New_York"

# Finviz
FINVIZ_CSV = DATA / "finviz_universe.csv"

# Mapping thresholds
MIN_OVERALL_TO_MAP = 6.0
MIN_CONFIDENCE_TO_MAP = 0.55
