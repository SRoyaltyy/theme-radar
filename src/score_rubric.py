"""Theme Radar scoring rubric v1 — the rubric AS DATA, not prose.

Every rule row mirrors the brainstorm schema:
  field            Finviz column (or derived name: ret, d_<field>, upside_pct)
  kind             level | delta | ret        (how the raw value is computed)
  category         price | flow | technical | positioning | valuation |
                   fundamental | catalyst
  speed            fast | slow               (slow fields never vote on 1d)
  horizons         which horizons the rule may vote on
  weight           base points at stake
  polarity         + (up is good) | - (up is bad) | curve:<name> (custom level curve)
  deadzone         |value| below this -> signal 0 (noise floor)
  status_mode      none | momentum | rsi     (how status buckets modify the signal)
  note             caveat, in plain words (surfaced in outputs for auditability)

Tuning policy: change numbers HERE only. Every change is auditable in git
history, same discipline as fullscan's compute_scores constants.
"""
from __future__ import annotations

# --- horizon definitions (calendar-day windows for picking the prior snapshot)
HORIZON_WINDOWS = {
    "1d": (1, 3),     # nearest prior snapshot 1-3 days back
    "1w": (4, 8),     # ~5-7 calendar days back
    "1m": (18, 32),   # ~20-31 calendar days back
}

# --- status bucket thresholds (brainstorm: "thresholds are tunable; idea is
#     buckets, not one magic number")
STATUS = {
    "extreme_week_pct": 100.0,    # Performance (Week) above this -> EXTREME
    "extended_week_pct": 40.0,
    "extended_month_pct": 60.0,
    "extended_rsi": 75.0,
    "washed_month_pct": -25.0,
    "washed_rsi": 30.0,
    "high_short_pct": 25.0,
    "elevated_short_pct": 10.0,
    "far_above_50dma_pct": 40.0,  # extension via distance to 50-DMA
}

# --- deadzones for the true return, per horizon (|ret| below this -> 0)
RET_DEADZONE = {"1d": 0.015, "1w": 0.03, "1m": 0.05}

RUBRIC: list[dict] = [
    # ---------------------------------------------------------- price
    {"field": "Price", "kind": "ret", "category": "price", "speed": "fast",
     "horizons": ["1d", "1w", "1m"], "weight": 3.0, "polarity": "+",
     "deadzone": None,  # per-horizon RET_DEADZONE
     "status_mode": "momentum",
     "note": "true horizon return from Price pairs; EXTENDED flips/caps it"},
    {"field": "Performance (Month)", "kind": "delta", "category": "price",
     "speed": "fast", "horizons": ["1d", "1w", "1m"], "weight": 1.5,
     "polarity": "+", "deadzone": 1.5, "status_mode": "momentum",
     "note": "acceleration of the rolling month window, not the return itself"},

    # ---------------------------------------------------------- flow
    {"field": "Relative Volume", "kind": "level", "category": "flow",
     "speed": "fast", "horizons": ["1d", "1w"], "weight": 1.5,
     "polarity": "curve:rvol", "deadzone": 0.0, "status_mode": "none",
     "note": "hot tape confirms; quiet tape undercuts; sign set by ret direction"},
    {"field": "Average Volume", "kind": "delta", "category": "flow",
     "speed": "fast", "horizons": ["1w", "1m"], "weight": 0.8,
     "polarity": "pct:+", "deadzone": 0.10,
     "note": "liquidity/attention regime; 10% relative change floor"},

    # ---------------------------------------------------------- technical
    {"field": "Relative Strength Index (14)", "kind": "level",
     "category": "technical", "speed": "fast", "horizons": ["1d", "1w", "1m"],
     "weight": 1.0, "polarity": "curve:rsi", "deadzone": 0.0,
     "status_mode": "none",
     "note": "45-65 clean momentum; >75 overbuy risk; <30 washout"},
    {"field": "Relative Strength Index (14)", "kind": "delta",
     "category": "technical", "speed": "fast", "horizons": ["1d", "1w"],
     "weight": 0.5, "polarity": "+", "deadzone": 2.0, "status_mode": "rsi",
     "note": "rising RSI is good from neutral, bad into overbought"},
    {"field": "50-Day Simple Moving Average", "kind": "level",
     "category": "technical", "speed": "fast", "horizons": ["1w", "1m"],
     "weight": 1.0, "polarity": "curve:sma50", "deadzone": 0.0,
     "status_mode": "none",
     "note": "above = +; far above (>40%) = extension, flips negative"},
    {"field": "200-Day Simple Moving Average", "kind": "level",
     "category": "technical", "speed": "fast", "horizons": ["1m"],
     "weight": 1.0, "polarity": "curve:sma200", "deadzone": 0.0,
     "status_mode": "none", "note": "long-term regime line"},
    {"field": "Volatility (Month)", "kind": "level", "category": "technical",
     "speed": "fast", "horizons": ["1w", "1m"], "weight": 0.5,
     "polarity": "curve:vol", "deadzone": 0.0, "status_mode": "none",
     "note": "very high vol = unstable; very low = coiled (mild positive)"},

    # ---------------------------------------------------------- positioning
    {"field": "Short Float", "kind": "level", "category": "positioning",
     "speed": "slow", "horizons": ["1w", "1m"], "weight": 1.5,
     "polarity": "curve:short", "deadzone": 0.0, "status_mode": "none",
     "note": "dual: high short = bearish sponsorship; squeeze is a separate flag"},
    {"field": "Short Float", "kind": "delta", "category": "positioning",
     "speed": "slow", "horizons": ["1m"], "weight": 1.2, "polarity": "-",
     "deadzone": 1.0, "status_mode": "none",
     "note": "shorts adding = bears pressing; covering = relief"},
    {"field": "Institutional Transactions", "kind": "level",
     "category": "positioning", "speed": "slow", "horizons": ["1w", "1m"],
     "weight": 1.5, "polarity": "+", "deadzone": 0.5, "status_mode": "none",
     "note": "recent inst buying pressure vs distribution"},
    {"field": "Institutional Ownership", "kind": "delta",
     "category": "positioning", "speed": "slow", "horizons": ["1m"],
     "weight": 1.0, "polarity": "+", "deadzone": 1.0, "status_mode": "none",
     "note": "accumulation vs exit, monthly only"},
    {"field": "Insider Transactions", "kind": "level", "category": "positioning",
     "speed": "slow", "horizons": ["1w", "1m"], "weight": 1.0, "polarity": "+",
     "deadzone": 0.5, "status_mode": "none",
     "note": "net buying bullish when clearly positive"},

    # ---------------------------------------------------------- valuation
    {"field": "upside_pct", "kind": "level", "category": "valuation",
     "speed": "fast", "horizons": ["1d", "1w", "1m"], "weight": 1.0,
     "polarity": "curve:upside", "deadzone": 0.0, "status_mode": "none",
     "note": "room vs Street; <0 = extended vs target (kill-switch input)"},
    {"field": "Target Price", "kind": "delta", "category": "valuation",
     "speed": "slow", "horizons": ["1w", "1m"], "weight": 1.5,
     "polarity": "pct:+", "deadzone": 0.03, "status_mode": "none",
     "note": "target raises vs cuts; 3% relative floor"},
    {"field": "Analyst Recom", "kind": "delta", "category": "valuation",
     "speed": "slow", "horizons": ["1w", "1m"], "weight": 1.0, "polarity": "-",
     "deadzone": 0.15, "status_mode": "none",
     "note": "finviz scale: LOWER = stronger buy, so polarity is inverted"},

    # ---------------------------------------------------------- fundamental
    {"field": "Sales Growth Quarter Over Quarter", "kind": "level",
     "category": "fundamental", "speed": "slow", "horizons": ["1m"],
     "weight": 1.2, "polarity": "+", "deadzone": 2.0, "status_mode": "none",
     "note": "sequential top-line impulse"},
    {"field": "Sales Year Over Year TTM", "kind": "level",
     "category": "fundamental", "speed": "slow", "horizons": ["1m"],
     "weight": 1.0, "polarity": "+", "deadzone": 3.0, "status_mode": "none",
     "note": "top-line trend"},
    {"field": "Profit Margin", "kind": "delta", "category": "fundamental",
     "speed": "slow", "horizons": ["1m"], "weight": 1.0, "polarity": "+",
     "deadzone": 2.0, "status_mode": "none",
     "note": "margin repair vs pressure"},
    {"field": "EPS Surprise", "kind": "level", "category": "fundamental",
     "speed": "slow", "horizons": ["1w", "1m"], "weight": 1.0, "polarity": "+",
     "deadzone": 5.0, "status_mode": "none",
     "note": "last print's beat/miss; stale is level history, modest weight"},
    {"field": "Total Debt/Equity", "kind": "level", "category": "fundamental",
     "speed": "slow", "horizons": ["1m"], "weight": 0.5,
     "polarity": "curve:debt", "deadzone": 0.0, "status_mode": "none",
     "note": "high leverage = risk gate, monthly only"},

    # ---------------------------------------------------------- catalyst
    {"field": "n_catalysts", "kind": "level", "category": "catalyst",
     "speed": "fast", "horizons": ["1d", "1w"], "weight": 0.5,
     "polarity": "+", "deadzone": 0.0, "status_mode": "none",
     "note": "keyword hits in News Title + Digest + Description (0/1 per theme)"},
]

# --- interaction gates, evaluated IN ORDER after category sums -------------
# (brainstorm section 8: "gates and dampeners, not a second model")
INTERACTIONS = [
    {"id": "extension_cap",
     "when": "status_extension in ('EXTENDED',) and cat.price > 0",
     "do": "cat.price *= 0.25",
     "why": "extended momentum: chase risk, cap the price category"},
    {"id": "extreme_flip",
     "when": "status_extension == 'EXTREME' and cat.price > 0",
     "do": "cat.price = -abs(cat.price) * 0.5",
     "why": "parabolic week (+100%): take-profit risk, flip price bearish"},
    {"id": "downtrend_bounce_discount",
     "when": "status_trend == 'DOWNTREND' and horizon in ('1w','1m') and cat.price > 0",
     "do": "cat.price *= 0.5",
     "why": "bounce inside a downtrend is not trend confirmation"},
    {"id": "street_extended_discount",
     "when": "upside_pct < 0 and cat.price > 0",
     "do": "cat.price *= 0.5",
     "why": "price above Street target: no sponsorship headroom"},
    {"id": "squeeze_flag",
     "when": "status_short == 'HIGH_SHORT' and ret > 0.05 and rvol > 1.5",
     "do": "flags.append('SQUEEZE_SETUP')",
     "why": "crowded short + price impulse + volume: squeeze scenario (not base case)"},
    {"id": "unconfirmed_rally",
     "when": "inst_tx < 0 and ret > 0",
     "do": "confidence *= 0.8",
     "why": "price up while institutions distribute: lower confidence"},
    {"id": "capitulation_watch",
     "when": "status_extension == 'WASHED' and ret < -0.03 and rvol > 1.5",
     "do": "flags.append('CAPITULATION_WATCH')",
     "why": "washed-out + heavy down volume: possible flush, needs follow-through"},
]

# --- category normalization reference (max plausible |points| per category,
#     used only to render the -100..+100 display score)
CATEGORY_MAX = {
    "price": 4.5, "flow": 2.3, "technical": 3.5, "positioning": 5.2,
    "valuation": 3.5, "fundamental": 4.7, "catalyst": 1.5,
}
