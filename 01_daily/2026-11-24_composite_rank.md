# Composite residual rank — **2026-11-24**

Generated: 2026-11-24T23:20:15.476760-05:00
Prior snapshot (for returns): **2026-11-23**

## Y snapshot (v1 — breadth only)

- **p_risk_on:** 0.2144 (from % names up)
- **pct_up:** 0.4358
- **median_ret:** -0.04%
- **conviction:** 0.5711
- **n:** 11786
- note: price_derived breadth only (v1)

## Method (deliberately simple)

- **residual** = stock return − median stock return (same pair window)
- **composites:** SPEC_DURATION, QUALITY_DEFENSIVE, CROWDING, SIZE_TILT
- **pressure** = conviction × prior effects of composites given p_risk_on
- Ranking is **cross-sectional residual bias**, not an absolute SPY call
- Hand priors only — replace with audit weights later

CSV: `data/composite/2026-11-24_composite_rank.csv`

## Top 20 by residual pressure (favor when risk-on / current Y)

| Ticker | Sector | pressure | SPEC | QUAL | CROWD | SIZE | resid | beta | short |
|--------|--------|----------|------|------|-------|------|-------|------|-------|
| LIN | Basic Materials | +0.245 | 0.00 | 1.00 | 0.00 | 0.00 | +0.01% | low | low |
| VZ | Communication Serv | +0.245 | 0.00 | 1.00 | 0.00 | 0.00 | +1.57% | low | low |
| AZN | Healthcare | +0.245 | 0.00 | 1.00 | 0.00 | 0.00 | +3.53% | low | low |
| BABA | Consumer Cyclical | +0.245 | 0.00 | 1.00 | 0.00 | 0.00 | -1.33% | low | low |
| HSBC | Financial | +0.245 | 0.00 | 1.00 | 0.00 | 0.00 | -1.14% | low | low |
| BRK-A | Financial | +0.245 | 0.00 | 1.00 | 0.00 | 0.00 | +0.78% | low | low |
| BRK-B | Financial | +0.245 | 0.00 | 1.00 | 0.00 | 0.00 | +0.89% | low | low |
| LLY | Healthcare | +0.245 | 0.00 | 1.00 | 0.00 | 0.00 | +3.19% | low | low |
| LMT | Industrials | +0.245 | 0.00 | 1.00 | 0.00 | 0.00 | +2.66% | low | low |
| SO | Utilities | +0.245 | 0.00 | 1.00 | 0.00 | 0.00 | +1.12% | low | low |
| NVS | Healthcare | +0.245 | 0.00 | 1.00 | 0.00 | 0.00 | +1.67% | low | low |
| CME | Financial | +0.245 | 0.00 | 1.00 | 0.00 | 0.00 | +1.63% | low | low |
| AMGN | Healthcare | +0.245 | 0.00 | 1.00 | 0.00 | 0.00 | +5.59% | low | low |
| SHEL | Energy | +0.245 | 0.00 | 1.00 | 0.00 | 0.00 | +0.59% | low | low |
| T | Communication Serv | +0.245 | 0.00 | 1.00 | 0.00 | 0.00 | +2.64% | low | low |
| MRSH | Financial | +0.245 | 0.00 | 1.00 | 0.00 | 0.00 | +2.97% | low | low |
| UNH | Healthcare | +0.245 | 0.00 | 1.00 | 0.00 | 0.00 | +1.77% | low | low |
| MUFG | Financial | +0.245 | 0.00 | 1.00 | 0.00 | 0.00 | +0.66% | low | low |
| PM | Consumer Defensive | +0.245 | 0.00 | 1.00 | 0.00 | 0.00 | +0.84% | low | low |
| TMUS | Communication Serv | +0.245 | 0.00 | 1.00 | 0.00 | 0.00 | +0.61% | low | low |

## Bottom 15 (lowest pressure)

| Ticker | Sector | pressure | SPEC | QUAL | resid | beta |
|--------|--------|----------|------|------|-------|------|
| ARMP | Healthcare | -0.564 | 0.95 | 0.00 | +27.74% | high |
| FIRY | Communication Serv | -0.551 | 0.85 | 0.00 | +6.83% | high |
| LVWR | Consumer Cyclical | -0.545 | 0.95 | 0.00 | +90.86% | high |
| ABSI | Healthcare | -0.545 | 0.95 | 0.00 | +8.18% | high |
| CCCC | Healthcare | -0.545 | 0.95 | 0.00 | +15.71% | high |
| LXEO | Healthcare | -0.545 | 0.95 | 0.00 | +16.66% | high |
| CNSY | Healthcare | -0.532 | 0.85 | 0.00 | +12.54% | high |
| ABEO | Healthcare | -0.532 | 0.85 | 0.00 | +4.11% | high |
| IBIO | Healthcare | -0.532 | 0.85 | 0.00 | +40.04% | high |
| ASPI | Basic Materials | -0.532 | 0.85 | 0.00 | -7.58% | high |
| ABR | Real Estate | -0.532 | 0.85 | 0.00 | -2.61% | high |
| ENVX | Industrials | -0.532 | 0.85 | 0.00 | -2.61% | high |
| RCAT | Industrials | -0.532 | 0.85 | 0.00 | -8.42% | high |
| LFMD | Healthcare | -0.532 | 0.85 | 0.00 | -5.44% | high |
| CUE | Healthcare | -0.532 | 0.85 | 0.00 | +19.17% | high |

## Sector median pressure

| Sector | n | median pressure | median resid |
|--------|---|-----------------|--------------|
| Utilities | 104 | +0.039 | +0.47% |
| Energy | 252 | -0.067 | +0.82% |
| Financial | 7309 | -0.135 | -0.06% |
| Consumer Defensive | 240 | -0.159 | +0.65% |
| Real Estate | 244 | -0.165 | +1.25% |
| Consumer Cyclical | 520 | -0.173 | +0.41% |
| Industrials | 714 | -0.173 | -0.98% |
| Basic Materials | 298 | -0.210 | -1.21% |
| Communication Services | 252 | -0.228 | +0.65% |
| Technology | 799 | -0.236 | -1.91% |
| Healthcare | 1054 | -0.311 | +2.81% |

## Composite averages by size

| size | n | SPEC | QUAL | pressure |
|------|---|------|------|----------|
| large | 744 | 0.15 | 0.82 | +0.102 |
| mega | 158 | 0.13 | 0.84 | +0.161 |
| micro | 2341 | 0.53 | 0.27 | -0.315 |
| mid | 1091 | 0.34 | 0.54 | -0.097 |
| small | 1548 | 0.49 | 0.41 | -0.233 |
| unknown | 5904 | 0.32 | 0.24 | -0.124 |
