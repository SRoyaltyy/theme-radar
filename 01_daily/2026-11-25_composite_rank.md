# Composite residual rank — **2026-11-25**

Generated: 2026-11-25T22:40:41.740846-05:00
Prior snapshot (for returns): **2026-11-24**

## Y snapshot (v1 — breadth only)

- **p_risk_on:** 0.6811 (from % names up)
- **pct_up:** 0.6224
- **median_ret:** 0.29%
- **conviction:** 0.3622
- **n:** 11786
- note: price_derived breadth only (v1)

## Method (deliberately simple)

- **residual** = stock return − median stock return (same pair window)
- **composites:** SPEC_DURATION, QUALITY_DEFENSIVE, CROWDING, SIZE_TILT
- **pressure** = conviction × prior effects of composites given p_risk_on
- Ranking is **cross-sectional residual bias**, not an absolute SPY call
- Hand priors only — replace with audit weights later

CSV: `data/composite/2026-11-25_composite_rank.csv`

## Top 20 by residual pressure (favor when risk-on / current Y)

| Ticker | Sector | pressure | SPEC | QUAL | CROWD | SIZE | resid | beta | short |
|--------|--------|----------|------|------|-------|------|-------|------|-------|
| STRO | Healthcare | +0.235 | 0.95 | 0.00 | 0.80 | 1.00 | +2.56% | high | very_high |
| HRTX | Healthcare | +0.235 | 0.95 | 0.00 | 0.80 | 1.00 | +6.16% | high | very_high |
| AVXL | Healthcare | +0.227 | 0.95 | 0.00 | 0.60 | 1.00 | +8.35% | high | elevated |
| IVVD | Healthcare | +0.227 | 0.95 | 0.00 | 0.60 | 1.00 | +8.97% | high | elevated |
| ZNTL | Healthcare | +0.227 | 0.95 | 0.00 | 0.60 | 1.00 | +0.32% | high | elevated |
| GOSS | Healthcare | +0.222 | 0.85 | 0.00 | 0.80 | 1.00 | +7.86% | high | very_high |
| CCCC | Healthcare | +0.219 | 0.95 | 0.00 | 0.80 | 0.80 | +4.87% | high | very_high |
| ALTG | Industrials | +0.217 | 0.95 | 0.00 | 0.35 | 1.00 | +1.01% | high | low |
| ENVX | Industrials | +0.214 | 0.85 | 0.00 | 0.60 | 1.00 | +3.35% | high | very_high |
| GEMI | Financial | +0.214 | 0.85 | 0.00 | 0.60 | 1.00 | +6.58% | high | very_high |
| DDD | Technology | +0.214 | 0.85 | 0.00 | 0.60 | 1.00 | +1.16% | high | very_high |
| CNSY | Healthcare | +0.214 | 0.85 | 0.00 | 0.60 | 1.00 | +8.35% | high | elevated |
| CGTX | Healthcare | +0.214 | 0.85 | 0.00 | 0.60 | 1.00 | +30.15% | high | elevated |
| CUE | Healthcare | +0.214 | 0.85 | 0.00 | 0.60 | 1.00 | +22.63% | high | elevated |
| ABR | Real Estate | +0.214 | 0.85 | 0.00 | 0.60 | 1.00 | +14.26% | high | very_high |
| WYFI | Technology | +0.214 | 0.85 | 0.00 | 0.60 | 1.00 | -3.85% | high | very_high |
| TNXP | Healthcare | +0.214 | 0.85 | 0.00 | 0.60 | 1.00 | +4.47% | high | very_high |
| TNYA | Healthcare | +0.214 | 0.85 | 0.00 | 0.60 | 1.00 | +9.24% | high | elevated |
| SEGG | Consumer Cyclical | +0.214 | 0.85 | 0.00 | 0.60 | 1.00 | -12.19% | high | elevated |
| SPCE | Industrials | +0.214 | 0.85 | 0.00 | 0.60 | 1.00 | +8.71% | high | very_high |

## Bottom 15 (lowest pressure)

| Ticker | Sector | pressure | SPEC | QUAL | resid | beta |
|--------|--------|----------|------|------|-------|------|
| SMFG | Financial | -0.098 | 0.00 | 1.00 | +0.25% | low |
| BMY | Healthcare | -0.098 | 0.00 | 1.00 | -1.03% | low |
| LIN | Basic Materials | -0.098 | 0.00 | 1.00 | +1.22% | low |
| NEM | Basic Materials | -0.098 | 0.00 | 1.00 | +1.47% | low |
| NEE | Utilities | -0.098 | 0.00 | 1.00 | +0.69% | low |
| AMGN | Healthcare | -0.098 | 0.00 | 1.00 | -1.28% | low |
| BUD | Consumer Defensive | -0.098 | 0.00 | 1.00 | -0.40% | low |
| VZ | Communication Serv | -0.098 | 0.00 | 1.00 | -0.03% | low |
| TMUS | Communication Serv | -0.098 | 0.00 | 1.00 | -0.92% | low |
| TM | Consumer Cyclical | -0.098 | 0.00 | 1.00 | +2.48% | low |
| HSBC | Financial | -0.098 | 0.00 | 1.00 | -0.56% | low |
| BTI | Consumer Defensive | -0.098 | 0.00 | 1.00 | +3.47% | low |
| VRTX | Healthcare | -0.098 | 0.00 | 1.00 | -0.25% | low |
| REGN | Healthcare | -0.098 | 0.00 | 1.00 | -0.82% | low |
| T | Communication Serv | -0.098 | 0.00 | 1.00 | +0.11% | low |

## Sector median pressure

| Sector | n | median pressure | median resid |
|--------|---|-----------------|--------------|
| Healthcare | 1054 | +0.125 | -0.29% |
| Technology | 799 | +0.092 | +0.54% |
| Communication Services | 252 | +0.092 | -0.10% |
| Basic Materials | 298 | +0.081 | +2.17% |
| Consumer Cyclical | 520 | +0.070 | +0.60% |
| Industrials | 714 | +0.070 | +0.76% |
| Consumer Defensive | 240 | +0.066 | +0.39% |
| Real Estate | 244 | +0.066 | +0.63% |
| Financial | 7309 | +0.054 | -0.09% |
| Energy | 252 | +0.027 | +0.99% |
| Utilities | 104 | -0.016 | +0.28% |

## Composite averages by size

| size | n | SPEC | QUAL | pressure |
|------|---|------|------|----------|
| large | 753 | 0.15 | 0.82 | -0.041 |
| mega | 158 | 0.14 | 0.85 | -0.065 |
| micro | 2340 | 0.53 | 0.27 | +0.126 |
| mid | 1085 | 0.34 | 0.54 | +0.040 |
| small | 1547 | 0.49 | 0.41 | +0.093 |
| unknown | 5903 | 0.32 | 0.24 | +0.050 |
