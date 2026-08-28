# Composite residual rank — **2026-08-28**

Generated: 2026-08-28T01:27:43.554746-04:00
Prior snapshot (for returns): **2026-08-26**

## Y snapshot (v1 — breadth only)

- **p_risk_on:** 0.3853 (from % names up)
- **pct_up:** 0.5041
- **median_ret:** 0.02%
- **conviction:** 0.2294
- **n:** 11654
- note: price_derived breadth only (v1)

## Method (deliberately simple)

- **residual** = stock return − median stock return (same pair window)
- **composites:** SPEC_DURATION, QUALITY_DEFENSIVE, CROWDING, SIZE_TILT
- **pressure** = conviction × prior effects of composites given p_risk_on
- Ranking is **cross-sectional residual bias**, not an absolute SPY call
- Hand priors only — replace with audit weights later

CSV: `data/composite/2026-08-28_composite_rank.csv`

## Top 20 by residual pressure (favor when risk-on / current Y)

| Ticker | Sector | pressure | SPEC | QUAL | CROWD | SIZE | resid | beta | short |
|--------|--------|----------|------|------|-------|------|-------|------|-------|
| MUFG | Financial | +0.040 | 0.00 | 1.00 | 0.00 | 0.00 | -0.02% | low | low |
| SO | Utilities | +0.040 | 0.00 | 1.00 | 0.00 | 0.00 | -0.82% | low | low |
| KO | Consumer Defensive | +0.040 | 0.00 | 1.00 | 0.00 | 0.00 | -1.16% | low | low |
| UL | Consumer Defensive | +0.040 | 0.00 | 1.00 | 0.00 | 0.00 | -0.86% | low | low |
| ABBV | Healthcare | +0.040 | 0.00 | 1.00 | 0.00 | 0.00 | -1.83% | low | low |
| MCK | Healthcare | +0.040 | 0.00 | 1.00 | 0.00 | 0.00 | -0.71% | low | low |
| MCD | Consumer Cyclical | +0.040 | 0.00 | 1.00 | 0.00 | 0.00 | -2.60% | low | low |
| WMT | Consumer Defensive | +0.040 | 0.00 | 1.00 | 0.00 | 0.00 | -1.66% | low | low |
| T | Communication Serv | +0.040 | 0.00 | 1.00 | 0.00 | 0.00 | -1.73% | low | low |
| BTI | Consumer Defensive | +0.040 | 0.00 | 1.00 | 0.00 | 0.00 | -2.04% | low | low |
| RIO | Basic Materials | +0.040 | 0.00 | 1.00 | 0.00 | 0.00 | +0.05% | low | low |
| PGR | Financial | +0.040 | 0.00 | 1.00 | 0.00 | 0.00 | -2.21% | low | low |
| PM | Consumer Defensive | +0.040 | 0.00 | 1.00 | 0.00 | 0.00 | -1.89% | low | low |
| GD | Industrials | +0.040 | 0.00 | 1.00 | 0.00 | 0.00 | -0.54% | low | low |
| BMY | Healthcare | +0.040 | 0.00 | 1.00 | 0.00 | 0.00 | -0.94% | low | low |
| SNY | Healthcare | +0.040 | 0.00 | 1.00 | 0.00 | 0.00 | -1.30% | low | low |
| VRTX | Healthcare | +0.040 | 0.00 | 1.00 | 0.00 | 0.00 | +0.02% | low | low |
| PG | Consumer Defensive | +0.040 | 0.00 | 1.00 | 0.00 | 0.00 | -1.31% | low | low |
| CB | Financial | +0.040 | 0.00 | 1.00 | 0.00 | 0.00 | -1.61% | low | low |
| TD | Financial | +0.040 | 0.00 | 1.00 | 0.00 | 0.00 | +1.37% | low | low |

## Bottom 15 (lowest pressure)

| Ticker | Sector | pressure | SPEC | QUAL | resid | beta |
|--------|--------|----------|------|------|-------|------|
| SPRB | Healthcare | -0.094 | 0.95 | 0.00 | +2.94% | high |
| GLSI | Healthcare | -0.094 | 0.95 | 0.00 | +2.72% | high |
| LVWR | Consumer Cyclical | -0.094 | 0.95 | 0.00 | -0.75% | high |
| BETR | Financial | -0.094 | 0.95 | 0.00 | +8.77% | high |
| ARMP | Healthcare | -0.091 | 0.95 | 0.00 | -0.39% | high |
| YYGH | Industrials | -0.089 | 0.85 | 0.00 | -9.93% | high |
| LASE | Industrials | -0.089 | 0.85 | 0.00 | +12.74% | high |
| BTCT | Technology | -0.089 | 0.85 | 0.00 | +16.00% | high |
| BIRD | Technology | -0.089 | 0.85 | 0.00 | +16.36% | high |
| METC | Basic Materials | -0.088 | 0.95 | 0.00 | +9.50% | high |
| CRML | Basic Materials | -0.088 | 0.95 | 0.00 | +0.60% | high |
| SGMT | Healthcare | -0.088 | 0.95 | 0.00 | -1.04% | high |
| CABA | Healthcare | -0.088 | 0.95 | 0.00 | +3.98% | high |
| PACB | Healthcare | -0.088 | 0.95 | 0.00 | -0.67% | high |
| SBET | Financial | -0.088 | 0.95 | 0.00 | +6.71% | high |

## Sector median pressure

| Sector | n | median pressure | median resid |
|--------|---|-----------------|--------------|
| Utilities | 109 | +0.002 | -0.69% |
| Energy | 252 | -0.008 | +0.91% |
| Financial | 7155 | -0.022 | +0.05% |
| Consumer Defensive | 243 | -0.024 | -1.05% |
| Real Estate | 251 | -0.027 | -0.75% |
| Industrials | 711 | -0.028 | -0.20% |
| Consumer Cyclical | 533 | -0.028 | -1.15% |
| Basic Materials | 287 | -0.029 | +0.47% |
| Communication Services | 258 | -0.037 | -0.74% |
| Technology | 791 | -0.037 | +1.60% |
| Healthcare | 1064 | -0.045 | -0.51% |

## Composite averages by size

| size | n | SPEC | QUAL | pressure |
|------|---|------|------|----------|
| large | 790 | 0.17 | 0.80 | +0.015 |
| mega | 169 | 0.14 | 0.84 | +0.025 |
| micro | 2156 | 0.51 | 0.30 | -0.048 |
| mid | 1185 | 0.36 | 0.51 | -0.018 |
| small | 1616 | 0.49 | 0.40 | -0.038 |
| unknown | 5738 | 0.32 | 0.24 | -0.020 |
