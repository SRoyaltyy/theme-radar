# Composite residual rank — **2026-09-29**

Generated: 2026-09-29T16:53:34.053729-04:00
Prior snapshot (for returns): **2026-09-28**

## Y snapshot (v1 — breadth only)

- **p_risk_on:** 0.03 (from % names up)
- **pct_up:** 0.362
- **median_ret:** -0.12%
- **conviction:** 0.94
- **n:** 11685
- note: price_derived breadth only (v1)

## Method (deliberately simple)

- **residual** = stock return − median stock return (same pair window)
- **composites:** SPEC_DURATION, QUALITY_DEFENSIVE, CROWDING, SIZE_TILT
- **pressure** = conviction × prior effects of composites given p_risk_on
- Ranking is **cross-sectional residual bias**, not an absolute SPY call
- Hand priors only — replace with audit weights later

CSV: `data/composite/2026-09-29_composite_rank.csv`

## Top 20 by residual pressure (favor when risk-on / current Y)

| Ticker | Sector | pressure | SPEC | QUAL | CROWD | SIZE | resid | beta | short |
|--------|--------|----------|------|------|-------|------|-------|------|-------|
| ABBV | Healthcare | +0.663 | 0.00 | 1.00 | 0.00 | 0.00 | -1.00% | low | low |
| ABT | Healthcare | +0.663 | 0.00 | 1.00 | 0.00 | 0.00 | +0.09% | low | low |
| CVS | Healthcare | +0.663 | 0.00 | 1.00 | 0.00 | 0.00 | -0.74% | low | low |
| CVX | Energy | +0.663 | 0.00 | 1.00 | 0.00 | 0.00 | -0.85% | low | low |
| VLO | Energy | +0.663 | 0.00 | 1.00 | 0.00 | 0.00 | -0.36% | low | low |
| XOM | Energy | +0.663 | 0.00 | 1.00 | 0.00 | 0.00 | -0.60% | low | low |
| BMY | Healthcare | +0.663 | 0.00 | 1.00 | 0.00 | 0.00 | -1.48% | low | low |
| T | Communication Serv | +0.663 | 0.00 | 1.00 | 0.00 | 0.00 | -1.57% | low | low |
| SYK | Healthcare | +0.663 | 0.00 | 1.00 | 0.00 | 0.00 | +1.38% | low | low |
| SHEL | Energy | +0.663 | 0.00 | 1.00 | 0.00 | 0.00 | -1.26% | low | low |
| SMFG | Financial | +0.663 | 0.00 | 1.00 | 0.00 | 0.00 | -1.43% | low | low |
| VRTX | Healthcare | +0.663 | 0.00 | 1.00 | 0.00 | 0.00 | -0.06% | low | low |
| NEM | Basic Materials | +0.663 | 0.00 | 1.00 | 0.00 | 0.00 | +1.01% | low | low |
| NVS | Healthcare | +0.663 | 0.00 | 1.00 | 0.00 | 0.00 | -0.68% | low | low |
| BUD | Consumer Defensive | +0.663 | 0.00 | 1.00 | 0.00 | 0.00 | -3.53% | low | low |
| SCHW | Financial | +0.663 | 0.00 | 1.00 | 0.00 | 0.00 | +0.93% | low | low |
| BRK-B | Financial | +0.663 | 0.00 | 1.00 | 0.00 | 0.00 | -0.03% | low | low |
| BP | Energy | +0.663 | 0.00 | 1.00 | 0.00 | 0.00 | -1.93% | low | low |
| MA | Financial | +0.663 | 0.00 | 1.00 | 0.00 | 0.00 | -0.71% | low | low |
| SAN | Financial | +0.663 | 0.00 | 1.00 | 0.00 | 0.00 | -0.09% | low | low |

## Bottom 15 (lowest pressure)

| Ticker | Sector | pressure | SPEC | QUAL | resid | beta |
|--------|--------|----------|------|------|-------|------|
| KAZR | Industrials | -1.493 | 0.85 | 0.00 | +4.98% | high |
| PACB | Healthcare | -1.476 | 0.95 | 0.00 | +7.14% | high |
| SXTP | Healthcare | -1.440 | 0.85 | 0.00 | +0.12% | high |
| BETR | Financial | -1.440 | 0.85 | 0.00 | +1.61% | high |
| TNXP | Healthcare | -1.440 | 0.85 | 0.00 | -2.41% | high |
| QSI | Healthcare | -1.440 | 0.85 | 0.00 | +20.12% | high |
| RENX | Real Estate | -1.440 | 0.85 | 0.00 | -4.10% | high |
| SRFM | Industrials | -1.440 | 0.85 | 0.00 | +0.96% | high |
| TRAW | Healthcare | -1.440 | 0.85 | 0.00 | +8.74% | high |
| CRBP | Healthcare | -1.440 | 0.85 | 0.00 | -4.07% | high |
| NCPL | Financial | -1.440 | 0.85 | 0.00 | +13.08% | high |
| NXH | Consumer Cyclical | -1.440 | 0.85 | 0.00 | -3.12% | high |
| ONFO | Communication Serv | -1.440 | 0.85 | 0.00 | -2.71% | high |
| TDUP | Consumer Cyclical | -1.440 | 0.85 | 0.00 | -0.34% | high |
| IPSC | Healthcare | -1.440 | 0.85 | 0.00 | -1.08% | high |

## Sector median pressure

| Sector | n | median pressure | median resid |
|--------|---|-----------------|--------------|
| Utilities | 107 | +0.040 | +0.89% |
| Energy | 252 | -0.137 | -1.14% |
| Financial | 7197 | -0.367 | +0.02% |
| Consumer Defensive | 241 | -0.398 | -0.41% |
| Real Estate | 247 | -0.446 | -0.05% |
| Industrials | 718 | -0.486 | -0.25% |
| Consumer Cyclical | 529 | -0.499 | -0.13% |
| Basic Materials | 292 | -0.515 | -0.43% |
| Communication Services | 255 | -0.619 | -0.11% |
| Technology | 795 | -0.619 | +0.12% |
| Healthcare | 1052 | -0.773 | -0.24% |

## Composite averages by size

| size | n | SPEC | QUAL | pressure |
|------|---|------|------|----------|
| large | 767 | 0.17 | 0.79 | +0.250 |
| mega | 159 | 0.14 | 0.84 | +0.427 |
| micro | 2201 | 0.51 | 0.29 | -0.815 |
| mid | 1136 | 0.35 | 0.51 | -0.296 |
| small | 1638 | 0.48 | 0.40 | -0.637 |
| unknown | 5784 | 0.32 | 0.23 | -0.342 |
