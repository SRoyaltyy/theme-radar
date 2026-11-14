# Composite residual rank — **2026-11-13**

Generated: 2026-11-13T20:31:01.140038-05:00
Prior snapshot (for returns): **2026-11-12**

## Y snapshot (v1 — breadth only)

- **p_risk_on:** 0.0249 (from % names up)
- **pct_up:** 0.36
- **median_ret:** -0.16%
- **conviction:** 0.9501
- **n:** 11762
- note: price_derived breadth only (v1)

## Method (deliberately simple)

- **residual** = stock return − median stock return (same pair window)
- **composites:** SPEC_DURATION, QUALITY_DEFENSIVE, CROWDING, SIZE_TILT
- **pressure** = conviction × prior effects of composites given p_risk_on
- Ranking is **cross-sectional residual bias**, not an absolute SPY call
- Hand priors only — replace with audit weights later

CSV: `data/composite/2026-11-13_composite_rank.csv`

## Top 20 by residual pressure (favor when risk-on / current Y)

| Ticker | Sector | pressure | SPEC | QUAL | CROWD | SIZE | resid | beta | short |
|--------|--------|----------|------|------|-------|------|-------|------|-------|
| ABT | Healthcare | +0.677 | 0.00 | 1.00 | 0.00 | 0.00 | +1.34% | low | low |
| ABBV | Healthcare | +0.677 | 0.00 | 1.00 | 0.00 | 0.00 | +0.36% | low | low |
| TM | Consumer Cyclical | +0.677 | 0.00 | 1.00 | 0.00 | 0.00 | +1.47% | low | low |
| TJX | Consumer Cyclical | +0.677 | 0.00 | 1.00 | 0.00 | 0.00 | -1.03% | low | low |
| TD | Financial | +0.677 | 0.00 | 1.00 | 0.00 | 0.00 | +0.13% | low | low |
| T | Communication Serv | +0.677 | 0.00 | 1.00 | 0.00 | 0.00 | +0.16% | low | low |
| ENB | Energy | +0.677 | 0.00 | 1.00 | 0.00 | 0.00 | -0.76% | low | low |
| JNJ | Healthcare | +0.677 | 0.00 | 1.00 | 0.00 | 0.00 | +0.95% | low | low |
| SYK | Healthcare | +0.677 | 0.00 | 1.00 | 0.00 | 0.00 | -0.72% | low | low |
| BABA | Consumer Cyclical | +0.677 | 0.00 | 1.00 | 0.00 | 0.00 | +0.18% | low | low |
| AZN | Healthcare | +0.677 | 0.00 | 1.00 | 0.00 | 0.00 | +0.20% | low | low |
| VLO | Energy | +0.677 | 0.00 | 1.00 | 0.00 | 0.00 | +1.46% | low | low |
| MFG | Financial | +0.677 | 0.00 | 1.00 | 0.00 | 0.00 | +2.33% | low | low |
| MO | Consumer Defensive | +0.677 | 0.00 | 1.00 | 0.00 | 0.00 | +1.08% | low | low |
| MRK | Healthcare | +0.677 | 0.00 | 1.00 | 0.00 | 0.00 | +0.71% | low | low |
| MCD | Consumer Cyclical | +0.677 | 0.00 | 1.00 | 0.00 | 0.00 | -0.45% | low | low |
| MUFG | Financial | +0.677 | 0.00 | 1.00 | 0.00 | 0.00 | +0.53% | low | low |
| MPC | Energy | +0.677 | 0.00 | 1.00 | 0.00 | 0.00 | +0.59% | low | low |
| CVX | Energy | +0.677 | 0.00 | 1.00 | 0.00 | 0.00 | +1.80% | low | low |
| CVS | Healthcare | +0.677 | 0.00 | 1.00 | 0.00 | 0.00 | -0.33% | low | low |

## Bottom 15 (lowest pressure)

| Ticker | Sector | pressure | SPEC | QUAL | resid | beta |
|--------|--------|----------|------|------|-------|------|
| HUCK | Technology | -1.616 | 0.95 | 0.00 | +0.45% | high |
| AIRS | Healthcare | -1.616 | 0.95 | 0.00 | +16.83% | high |
| WSHP | Communication Serv | -1.616 | 0.95 | 0.00 | +7.51% | high |
| TDUP | Consumer Cyclical | -1.562 | 0.95 | 0.00 | +5.49% | high |
| NCPL | Financial | -1.526 | 0.85 | 0.00 | -6.13% | high |
| INLF | Industrials | -1.526 | 0.85 | 0.00 | +24.55% | high |
| MRLN | Industrials | -1.526 | 0.85 | 0.00 | +17.87% | high |
| NUAI | Technology | -1.508 | 0.95 | 0.00 | +17.81% | high |
| BMBL | Communication Serv | -1.508 | 0.95 | 0.00 | -0.17% | high |
| REAL | Consumer Cyclical | -1.508 | 0.95 | 0.00 | +1.70% | high |
| AP | Industrials | -1.494 | 0.95 | 0.00 | -4.01% | high |
| FTFT | Technology | -1.472 | 0.85 | 0.00 | +1.64% | high |
| NXH | Consumer Cyclical | -1.472 | 0.85 | 0.00 | +0.16% | high |
| ONFO | Communication Serv | -1.472 | 0.85 | 0.00 | +126.63% | high |
| TNXP | Healthcare | -1.472 | 0.85 | 0.00 | -6.94% | high |

## Sector median pressure

| Sector | n | median pressure | median resid |
|--------|---|-----------------|--------------|
| Utilities | 104 | +0.045 | +0.42% |
| Energy | 252 | -0.151 | +0.82% |
| Financial | 7276 | -0.375 | +0.02% |
| Consumer Defensive | 240 | -0.413 | +0.53% |
| Real Estate | 247 | -0.456 | +0.39% |
| Consumer Cyclical | 521 | -0.510 | +0.26% |
| Industrials | 716 | -0.515 | -0.51% |
| Basic Materials | 298 | -0.535 | -0.98% |
| Communication Services | 252 | -0.632 | +0.57% |
| Technology | 800 | -0.632 | -1.22% |
| Healthcare | 1056 | -0.835 | -0.60% |

## Composite averages by size

| size | n | SPEC | QUAL | pressure |
|------|---|------|------|----------|
| large | 748 | 0.16 | 0.81 | +0.264 |
| mega | 166 | 0.14 | 0.85 | +0.439 |
| micro | 2280 | 0.52 | 0.28 | -0.859 |
| mid | 1117 | 0.35 | 0.53 | -0.295 |
| small | 1589 | 0.49 | 0.41 | -0.649 |
| unknown | 5862 | 0.32 | 0.25 | -0.340 |
