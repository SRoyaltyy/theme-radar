# Composite residual rank — **2026-11-11**

Generated: 2026-11-11T17:25:21.555241-05:00
Prior snapshot (for returns): **2026-11-10**

## Y snapshot (v1 — breadth only)

- **p_risk_on:** 0.7644 (from % names up)
- **pct_up:** 0.6557
- **median_ret:** 0.46%
- **conviction:** 0.5287
- **n:** 11753
- note: price_derived breadth only (v1)

## Method (deliberately simple)

- **residual** = stock return − median stock return (same pair window)
- **composites:** SPEC_DURATION, QUALITY_DEFENSIVE, CROWDING, SIZE_TILT
- **pressure** = conviction × prior effects of composites given p_risk_on
- Ranking is **cross-sectional residual bias**, not an absolute SPY call
- Hand priors only — replace with audit weights later

CSV: `data/composite/2026-11-11_composite_rank.csv`

## Top 20 by residual pressure (favor when risk-on / current Y)

| Ticker | Sector | pressure | SPEC | QUAL | CROWD | SIZE | resid | beta | short |
|--------|--------|----------|------|------|-------|------|-------|------|-------|
| ORGO | Healthcare | +0.500 | 0.95 | 0.00 | 0.80 | 1.00 | +11.24% | high | very_high |
| HRTX | Healthcare | +0.500 | 0.95 | 0.00 | 0.80 | 1.00 | -3.16% | high | very_high |
| UIS | Technology | +0.484 | 0.95 | 0.00 | 0.60 | 1.00 | +0.57% | high | elevated |
| ARMP | Healthcare | +0.484 | 0.95 | 0.00 | 0.60 | 1.00 | +3.27% | high | elevated |
| INLF | Industrials | +0.472 | 0.85 | 0.00 | 0.80 | 1.00 | +26.81% | high | very_high |
| NCPL | Financial | +0.472 | 0.85 | 0.00 | 0.80 | 1.00 | -6.04% | high | very_high |
| OPTT | Industrials | +0.472 | 0.85 | 0.00 | 0.80 | 1.00 | +32.10% | high | very_high |
| GCTS | Technology | +0.472 | 0.85 | 0.00 | 0.80 | 1.00 | +9.19% | high | very_high |
| KULR | Technology | +0.472 | 0.85 | 0.00 | 0.80 | 1.00 | +2.55% | high | very_high |
| WOLF | Technology | +0.467 | 0.95 | 0.00 | 0.80 | 0.80 | +5.07% | high | very_high |
| NRGV | Industrials | +0.467 | 0.95 | 0.00 | 0.80 | 0.80 | +9.17% | high | very_high |
| BKSY | Industrials | +0.467 | 0.95 | 0.00 | 0.80 | 0.80 | +0.63% | high | very_high |
| ANRO | Healthcare | +0.467 | 0.95 | 0.00 | 0.80 | 0.80 | +8.42% | high | very_high |
| VOYG | Industrials | +0.467 | 0.95 | 0.00 | 0.80 | 0.80 | +1.47% | high | very_high |
| REAL | Consumer Cyclical | +0.467 | 0.95 | 0.00 | 0.80 | 0.80 | -2.88% | high | very_high |
| EVGO | Consumer Cyclical | +0.467 | 0.95 | 0.00 | 0.80 | 0.80 | +0.64% | high | very_high |
| INDI | Technology | +0.467 | 0.95 | 0.00 | 0.80 | 0.80 | +0.42% | high | very_high |
| AEVA | Technology | +0.467 | 0.95 | 0.00 | 0.80 | 0.80 | +4.18% | high | very_high |
| FIP | Industrials | +0.467 | 0.95 | 0.00 | 0.80 | 0.80 | +13.60% | high | very_high |
| CHPT | Consumer Cyclical | +0.467 | 0.95 | 0.00 | 0.80 | 0.80 | +1.66% | high | very_high |

## Bottom 15 (lowest pressure)

| Ticker | Sector | pressure | SPEC | QUAL | resid | beta |
|--------|--------|----------|------|------|-------|------|
| ABBV | Healthcare | -0.210 | 0.00 | 1.00 | -0.09% | low |
| IBM | Technology | -0.210 | 0.00 | 1.00 | +1.05% | low |
| BABA | Consumer Cyclical | -0.210 | 0.00 | 1.00 | -1.63% | low |
| TM | Consumer Cyclical | -0.210 | 0.00 | 1.00 | -1.29% | low |
| TJX | Consumer Cyclical | -0.210 | 0.00 | 1.00 | -0.81% | low |
| AZN | Healthcare | -0.210 | 0.00 | 1.00 | -1.15% | low |
| SO | Utilities | -0.210 | 0.00 | 1.00 | -0.26% | low |
| TMUS | Communication Serv | -0.210 | 0.00 | 1.00 | +1.36% | low |
| PGR | Financial | -0.210 | 0.00 | 1.00 | +0.31% | low |
| PG | Consumer Defensive | -0.210 | 0.00 | 1.00 | -1.05% | low |
| MCD | Consumer Cyclical | -0.210 | 0.00 | 1.00 | -3.07% | low |
| CB | Financial | -0.210 | 0.00 | 1.00 | -0.13% | low |
| PFE | Healthcare | -0.210 | 0.00 | 1.00 | -0.15% | low |
| PEP | Consumer Defensive | -0.210 | 0.00 | 1.00 | -0.23% | low |
| MFG | Financial | -0.210 | 0.00 | 1.00 | +1.86% | low |

## Sector median pressure

| Sector | n | median pressure | median resid |
|--------|---|-----------------|--------------|
| Healthcare | 1053 | +0.259 | +0.02% |
| Technology | 800 | +0.196 | +1.51% |
| Communication Services | 252 | +0.196 | +0.35% |
| Industrials | 716 | +0.172 | +0.18% |
| Consumer Cyclical | 521 | +0.158 | -0.63% |
| Basic Materials | 298 | +0.154 | -1.16% |
| Consumer Defensive | 240 | +0.141 | -0.46% |
| Real Estate | 247 | +0.141 | -0.89% |
| Financial | 7270 | +0.116 | -0.00% |
| Energy | 252 | +0.057 | +1.45% |
| Utilities | 104 | -0.024 | -0.43% |

## Composite averages by size

| size | n | SPEC | QUAL | pressure |
|------|---|------|------|----------|
| large | 762 | 0.17 | 0.81 | -0.079 |
| mega | 168 | 0.14 | 0.84 | -0.133 |
| micro | 2238 | 0.52 | 0.28 | +0.265 |
| mid | 1124 | 0.36 | 0.52 | +0.095 |
| small | 1602 | 0.49 | 0.40 | +0.205 |
| unknown | 5859 | 0.32 | 0.25 | +0.105 |
