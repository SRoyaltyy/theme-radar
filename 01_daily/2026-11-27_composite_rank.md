# Composite residual rank — **2026-11-27**

Generated: 2026-11-27T22:23:09.877358-05:00
Prior snapshot (for returns): **2026-11-25**

## Y snapshot (v1 — breadth only)

- **p_risk_on:** 1.0 (from % names up)
- **pct_up:** 0.7663
- **median_ret:** 1.09%
- **conviction:** 1.0
- **n:** 11788
- note: price_derived breadth only (v1)

## Method (deliberately simple)

- **residual** = stock return − median stock return (same pair window)
- **composites:** SPEC_DURATION, QUALITY_DEFENSIVE, CROWDING, SIZE_TILT
- **pressure** = conviction × prior effects of composites given p_risk_on
- Ranking is **cross-sectional residual bias**, not an absolute SPY call
- Hand priors only — replace with audit weights later

CSV: `data/composite/2026-11-27_composite_rank.csv`

## Top 20 by residual pressure (favor when risk-on / current Y)

| Ticker | Sector | pressure | SPEC | QUAL | CROWD | SIZE | resid | beta | short |
|--------|--------|----------|------|------|-------|------|-------|------|-------|
| STRO | Healthcare | +1.790 | 0.95 | 0.00 | 0.80 | 1.00 | +2.60% | high | very_high |
| IPSC | Healthcare | +1.790 | 0.95 | 0.00 | 0.80 | 1.00 | +2.03% | high | very_high |
| HRTX | Healthcare | +1.790 | 0.95 | 0.00 | 0.80 | 1.00 | -4.12% | high | very_high |
| ASPI | Basic Materials | +1.790 | 0.95 | 0.00 | 0.80 | 1.00 | +8.91% | high | very_high |
| CRBP | Healthcare | +1.790 | 0.95 | 0.00 | 0.80 | 1.00 | +1.65% | high | very_high |
| ZNTL | Healthcare | +1.730 | 0.95 | 0.00 | 0.60 | 1.00 | -0.49% | high | elevated |
| AVXL | Healthcare | +1.730 | 0.95 | 0.00 | 0.60 | 1.00 | +0.04% | high | elevated |
| WETO | Technology | +1.690 | 0.85 | 0.00 | 0.80 | 1.00 | +29.10% | high | very_high |
| FIRY | Communication Serv | +1.690 | 0.85 | 0.00 | 0.80 | 1.00 | +16.22% | high | very_high |
| STIM | Healthcare | +1.690 | 0.85 | 0.00 | 0.80 | 1.00 | +15.02% | high | very_high |
| CCCC | Healthcare | +1.670 | 0.95 | 0.00 | 0.80 | 0.80 | +7.50% | high | very_high |
| FLNC | Industrials | +1.670 | 0.95 | 0.00 | 0.80 | 0.80 | +8.87% | high | very_high |
| ALTG | Industrials | +1.655 | 0.95 | 0.00 | 0.35 | 1.00 | +0.84% | high | low |
| GEMI | Financial | +1.630 | 0.85 | 0.00 | 0.60 | 1.00 | +1.05% | high | very_high |
| PTHS | Healthcare | +1.630 | 0.85 | 0.00 | 0.60 | 1.00 | +3.65% | high | elevated |
| PUSA | Industrials | +1.630 | 0.85 | 0.00 | 0.60 | 1.00 | +24.36% | high | elevated |
| JELD | Industrials | +1.630 | 0.85 | 0.00 | 0.60 | 1.00 | +8.21% | high | elevated |
| DPRO | Industrials | +1.630 | 0.85 | 0.00 | 0.60 | 1.00 | +11.06% | high | elevated |
| CGTX | Healthcare | +1.630 | 0.85 | 0.00 | 0.60 | 1.00 | -12.20% | high | elevated |
| RCAT | Industrials | +1.630 | 0.85 | 0.00 | 0.60 | 1.00 | +5.73% | high | very_high |

## Bottom 15 (lowest pressure)

| Ticker | Sector | pressure | SPEC | QUAL | resid | beta |
|--------|--------|----------|------|------|-------|------|
| COP | Energy | -0.750 | 0.00 | 1.00 | +0.23% | low |
| LIN | Basic Materials | -0.750 | 0.00 | 1.00 | +0.43% | low |
| SHEL | Energy | -0.750 | 0.00 | 1.00 | +0.33% | low |
| TTE | Energy | -0.750 | 0.00 | 1.00 | -0.81% | low |
| T | Communication Serv | -0.750 | 0.00 | 1.00 | -0.05% | low |
| BMY | Healthcare | -0.750 | 0.00 | 1.00 | -1.81% | low |
| UL | Consumer Defensive | -0.750 | 0.00 | 1.00 | -1.74% | low |
| V | Financial | -0.750 | 0.00 | 1.00 | +0.13% | low |
| DHR | Healthcare | -0.750 | 0.00 | 1.00 | -0.41% | low |
| SO | Utilities | -0.750 | 0.00 | 1.00 | -1.05% | low |
| BRK-A | Financial | -0.750 | 0.00 | 1.00 | -0.79% | low |
| REGN | Healthcare | -0.750 | 0.00 | 1.00 | -0.05% | low |
| BRK-B | Financial | -0.750 | 0.00 | 1.00 | -0.84% | low |
| ADP | Technology | -0.750 | 0.00 | 1.00 | -0.24% | low |
| CVX | Energy | -0.750 | 0.00 | 1.00 | -0.38% | low |

## Sector median pressure

| Sector | n | median pressure | median resid |
|--------|---|-----------------|--------------|
| Healthcare | 1054 | +0.935 | -0.00% |
| Technology | 799 | +0.725 | +1.87% |
| Communication Services | 252 | +0.700 | +0.29% |
| Basic Materials | 298 | +0.605 | +2.54% |
| Consumer Cyclical | 520 | +0.530 | +0.21% |
| Industrials | 715 | +0.530 | +0.66% |
| Consumer Defensive | 240 | +0.505 | -0.50% |
| Real Estate | 244 | +0.505 | -0.68% |
| Financial | 7309 | +0.415 | -0.14% |
| Energy | 252 | +0.198 | +0.33% |
| Utilities | 105 | -0.120 | -0.74% |

## Composite averages by size

| size | n | SPEC | QUAL | pressure |
|------|---|------|------|----------|
| large | 753 | 0.16 | 0.82 | -0.308 |
| mega | 162 | 0.14 | 0.85 | -0.495 |
| micro | 2309 | 0.53 | 0.27 | +0.965 |
| mid | 1100 | 0.34 | 0.54 | +0.306 |
| small | 1560 | 0.49 | 0.41 | +0.714 |
| unknown | 5904 | 0.32 | 0.25 | +0.374 |
