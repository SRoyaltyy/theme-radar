"""US equity trading-day helpers (America/New_York).

Finviz/score jobs must gate on ET trading days — not HKT weekdays and not
all Mon–Fri (NYSE holidays).
"""
from __future__ import annotations

from datetime import date, datetime, timedelta
from zoneinfo import ZoneInfo

ET = ZoneInfo("America/New_York")

# NYSE full closures 2026–2027 (observed dates). Extend yearly.
NYSE_HOLIDAYS = {
    # 2026
    date(2026, 1, 1),   # New Year's Day
    date(2026, 1, 19),  # MLK
    date(2026, 2, 16),  # Presidents
    date(2026, 4, 3),   # Good Friday
    date(2026, 5, 25),  # Memorial
    date(2026, 6, 19),  # Juneteenth
    date(2026, 7, 3),   # Independence (observed)
    date(2026, 9, 7),   # Labor
    date(2026, 11, 26), # Thanksgiving
    date(2026, 12, 25), # Christmas
    # 2027
    date(2027, 1, 1),
    date(2027, 1, 18),
    date(2027, 2, 15),
    date(2027, 3, 26),
    date(2027, 5, 31),
    date(2027, 6, 18),
    date(2027, 7, 5),
    date(2027, 9, 6),
    date(2027, 11, 25),
    date(2027, 12, 24),  # Christmas observed if needed — verify yearly
    date(2027, 12, 31),
}


def today_et() -> date:
    return datetime.now(ET).date()


def is_trading_day(d: date | None = None) -> bool:
    d = d or today_et()
    if d.weekday() >= 5:
        return False
    if d in NYSE_HOLIDAYS:
        return False
    return True


def next_trading_day(d: date) -> date:
    x = d + timedelta(days=1)
    while not is_trading_day(x):
        x += timedelta(days=1)
    return x


def add_trading_days(d: date, n: int) -> date:
    """Move n trading sessions forward (n>=0)."""
    x = d
    for _ in range(n):
        x = next_trading_day(x)
    return x


def trading_days_between(start: date, end: date) -> list[date]:
    """Inclusive list of trading days from start to end."""
    out = []
    x = start
    if not is_trading_day(x):
        x = next_trading_day(x)
    while x <= end:
        if is_trading_day(x):
            out.append(x)
        x += timedelta(days=1)
    return out
