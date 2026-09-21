# Composite residual rank — **2026-09-21**

Generated: 2026-09-21T16:57:22.679143-04:00
Prior snapshot (for returns): **2026-09-18**

## Y snapshot (v1 — breadth only)

- **p_risk_on:** 0.768 (from % names up)
- **pct_up:** 0.6572
- **median_ret:** 0.44%
- **conviction:** 0.5359
- **n:** 11642
- note: price_derived breadth only (v1)

## Method (deliberately simple)

- **residual** = stock return − median stock return (same pair window)
- **composites:** SPEC_DURATION, QUALITY_DEFENSIVE, CROWDING, SIZE_TILT
- **pressure** = conviction × prior effects of composites given p_risk_on
- Ranking is **cross-sectional residual bias**, not an absolute SPY call
- Hand priors only — replace with audit weights later

CSV: `data/composite/2026-09-21_composite_rank.csv`

## Top 20 by residual pressure (favor when risk-on / current Y)

| Ticker | Sector | pressure | SPEC | QUAL | CROWD | SIZE | resid | beta | short |
|--------|--------|----------|------|------|-------|------|-------|------|-------|
| VUZI | Technology | +0.514 | 0.95 | 0.00 | 0.80 | 1.00 | +10.10% | high | very_high |
| EAF | Industrials | +0.497 | 0.95 | 0.00 | 0.60 | 1.00 | +13.42% | high | elevated |
| LTRX | Technology | +0.497 | 0.95 | 0.00 | 0.60 | 1.00 | +5.20% | high | elevated |
| DAIC | Technology | +0.485 | 0.85 | 0.00 | 0.80 | 1.00 | +0.96% | high | very_high |
| KAZR | Industrials | +0.485 | 0.85 | 0.00 | 0.80 | 1.00 | +8.08% | high | very_high |
| CRDF | Healthcare | +0.485 | 0.85 | 0.00 | 0.80 | 1.00 | -0.44% | high | very_high |
| GRML | Basic Materials | +0.485 | 0.85 | 0.00 | 0.80 | 1.00 | +230.08% | high | very_high |
| NCPL | Financial | +0.485 | 0.85 | 0.00 | 0.80 | 1.00 | +36.04% | high | very_high |
| GEMI | Financial | +0.480 | 0.95 | 0.00 | 0.80 | 0.80 | +2.65% | high | very_high |
| BBNX | Healthcare | +0.480 | 0.95 | 0.00 | 0.80 | 0.80 | +0.24% | high | very_high |
| CRML | Basic Materials | +0.480 | 0.95 | 0.00 | 0.80 | 0.80 | +38.19% | high | very_high |
| ABSI | Healthcare | +0.480 | 0.95 | 0.00 | 0.80 | 0.80 | +1.32% | high | very_high |
| LVWR | Consumer Cyclical | +0.480 | 0.95 | 0.00 | 0.80 | 0.80 | -6.58% | high | very_high |
| CHOW | Technology | +0.468 | 0.85 | 0.00 | 0.60 | 1.00 | -8.38% | high | elevated |
| SRFM | Industrials | +0.468 | 0.85 | 0.00 | 0.60 | 1.00 | -4.73% | high | elevated |
| IMCC | Healthcare | +0.468 | 0.85 | 0.00 | 0.60 | 1.00 | -27.40% | high | elevated |
| FLWS | Consumer Cyclical | +0.468 | 0.85 | 0.00 | 0.60 | 1.00 | +3.18% | high | very_high |
| SKIL | Consumer Defensive | +0.468 | 0.85 | 0.00 | 0.60 | 1.00 | -4.48% | high | elevated |
| EXOD | Technology | +0.468 | 0.85 | 0.00 | 0.60 | 1.00 | +17.98% | high | elevated |
| CAN | Technology | +0.468 | 0.85 | 0.00 | 0.60 | 1.00 | +13.07% | high | elevated |

## Bottom 15 (lowest pressure)

| Ticker | Sector | pressure | SPEC | QUAL | resid | beta |
|--------|--------|----------|------|------|-------|------|
| ABT | Healthcare | -0.215 | 0.00 | 1.00 | -0.08% | low |
| PM | Consumer Defensive | -0.215 | 0.00 | 1.00 | -1.05% | low |
| BMY | Healthcare | -0.215 | 0.00 | 1.00 | -1.14% | low |
| MPC | Energy | -0.215 | 0.00 | 1.00 | -5.74% | low |
| SAN | Financial | -0.215 | 0.00 | 1.00 | +1.72% | low |
| AMGN | Healthcare | -0.215 | 0.00 | 1.00 | +1.50% | low |
| PDD | Consumer Cyclical | -0.215 | 0.00 | 1.00 | +0.05% | low |
| KO | Consumer Defensive | -0.215 | 0.00 | 1.00 | -1.73% | low |
| CB | Financial | -0.215 | 0.00 | 1.00 | -1.44% | low |
| BP | Energy | -0.215 | 0.00 | 1.00 | -3.63% | low |
| BRK-B | Financial | -0.215 | 0.00 | 1.00 | -1.97% | low |
| BRK-A | Financial | -0.215 | 0.00 | 1.00 | -1.94% | low |
| MCK | Healthcare | -0.215 | 0.00 | 1.00 | +0.91% | low |
| PSX | Energy | -0.215 | 0.00 | 1.00 | -4.61% | low |
| CVX | Energy | -0.215 | 0.00 | 1.00 | -3.23% | low |

## Sector median pressure

| Sector | n | median pressure | median resid |
|--------|---|-----------------|--------------|
| Healthcare | 1052 | +0.241 | -0.44% |
| Technology | 793 | +0.201 | +1.00% |
| Communication Services | 255 | +0.201 | +0.46% |
| Basic Materials | 291 | +0.162 | -0.56% |
| Consumer Cyclical | 528 | +0.159 | -0.07% |
| Industrials | 717 | +0.152 | -0.21% |
| Real Estate | 247 | +0.145 | -0.05% |
| Consumer Defensive | 242 | +0.126 | -0.59% |
| Financial | 7160 | +0.119 | +0.07% |
| Energy | 251 | +0.044 | -1.97% |
| Utilities | 106 | -0.013 | -0.69% |

## Composite averages by size

| size | n | SPEC | QUAL | pressure |
|------|---|------|------|----------|
| large | 770 | 0.17 | 0.80 | -0.080 |
| mega | 164 | 0.14 | 0.84 | -0.140 |
| micro | 2171 | 0.51 | 0.30 | +0.263 |
| mid | 1166 | 0.36 | 0.51 | +0.098 |
| small | 1624 | 0.48 | 0.41 | +0.204 |
| unknown | 5747 | 0.32 | 0.24 | +0.111 |
