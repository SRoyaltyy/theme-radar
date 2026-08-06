"""Configuration for Theme Radar."""
from __future__ import annotations
import os
from pathlib import Path

# Paths
ROOT = Path(__file__).resolve().parent.parent
GROUNDING = ROOT / "00_grounding"
DAILY = ROOT / "01_daily"
LESSONS_ACTIVE = ROOT / "02_lessons" / "active"
SCOREBOARD_DIR = ROOT / "03_scoreboard"
ARCHIVE = ROOT / "04_archive"
DATA = ROOT / "data"

# Memory
CONSOLIDATED_MEMORY = ARCHIVE / "consolidated_memory.md"
MEMORY_WINDOW_DAYS = 15          # how many prior prediction cycles to inject
TOPIC = "theme_radar"

# Model
MODEL_PREDICT = os.environ.get("THEME_MODEL", "deepseek-chat")
DEEPSEEK_API_KEY = os.environ.get("DEEPSEEK_API_KEY", "")

# Timezone for daily runs
TZ = "America/New_York"

# Finviz universe
FINVIZ_CSV = DATA / "finviz_universe.csv"   # processed / lighter version
FINVIZ_FULL = DATA / "finviz_with_descriptions.csv"  # optional full dump

# Scoring thresholds (can be adjusted by reflection later)
MIN_OVERALL_TO_MAP = 6.0
MIN_CONFIDENCE_TO_MAP = 0.55
