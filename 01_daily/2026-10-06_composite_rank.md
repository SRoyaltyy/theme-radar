# Composite residual rank — **2026-10-06**

Generated: 2026-10-06T17:03:44.773158-04:00
Prior snapshot (for returns): **2026-10-05**

## Y snapshot (v1 — breadth only)

- **p_risk_on:** 0.6344 (from % names up)
- **pct_up:** 0.6037
- **median_ret:** 0.20%
- **conviction:** 0.2687
- **n:** 11707
- note: price_derived breadth only (v1)

## Method (deliberately simple)

- **residual** = stock return − median stock return (same pair window)
- **composites:** SPEC_DURATION, QUALITY_DEFENSIVE, CROWDING, SIZE_TILT
- **pressure** = conviction × prior effects of composites given p_risk_on
- Ranking is **cross-sectional residual bias**, not an absolute SPY call
- Hand priors only — replace with audit weights later

CSV: `data/composite/2026-10-06_composite_rank.csv`

## Top 20 by residual pressure (favor when risk-on / current Y)

| Ticker | Sector | pressure | SPEC | QUAL | CROWD | SIZE | resid | beta | short |
|--------|--------|----------|------|------|-------|------|-------|------|-------|
| DMRC | Technology | +0.125 | 0.95 | 0.00 | 0.60 | 1.00 | +1.11% | high | elevated |
| BIRD | Technology | +0.122 | 0.85 | 0.00 | 0.80 | 1.00 | -7.24% | high | very_high |
| TNON | Healthcare | +0.122 | 0.85 | 0.00 | 0.80 | 1.00 | +0.07% | high | very_high |
| HTZ | Industrials | +0.121 | 0.95 | 0.00 | 0.80 | 0.80 | +14.88% | high | very_high |
| PACB | Healthcare | +0.121 | 0.95 | 0.00 | 0.80 | 0.80 | -6.12% | high | very_high |
| FCEL | Industrials | +0.121 | 0.95 | 0.00 | 0.80 | 0.80 | +14.08% | high | very_high |
| TDUP | Consumer Cyclical | +0.118 | 0.85 | 0.00 | 0.60 | 1.00 | -0.66% | high | very_high |
| VERI | Technology | +0.118 | 0.85 | 0.00 | 0.60 | 1.00 | +2.54% | high | very_high |
| IPSC | Healthcare | +0.118 | 0.85 | 0.00 | 0.60 | 1.00 | -11.01% | high | very_high |
| TNXP | Healthcare | +0.118 | 0.85 | 0.00 | 0.60 | 1.00 | -4.78% | high | very_high |
| NXH | Consumer Cyclical | +0.118 | 0.85 | 0.00 | 0.60 | 1.00 | -11.37% | high | very_high |
| IPDN | Industrials | +0.118 | 0.85 | 0.00 | 0.60 | 1.00 | +48.51% | high | elevated |
| EYPT | Healthcare | +0.118 | 0.85 | 0.00 | 0.60 | 1.00 | +0.43% | high | very_high |
| OM | Healthcare | +0.118 | 0.85 | 0.00 | 0.60 | 1.00 | +0.78% | high | elevated |
| CRBP | Healthcare | +0.118 | 0.85 | 0.00 | 0.60 | 1.00 | -1.40% | high | very_high |
| QTEX | Technology | +0.118 | 0.85 | 0.00 | 0.60 | 1.00 | +3.05% | high | elevated |
| PDSB | Healthcare | +0.118 | 0.85 | 0.00 | 0.60 | 1.00 | -13.53% | high | elevated |
| ATOS | Healthcare | +0.118 | 0.85 | 0.00 | 0.60 | 1.00 | -0.20% | high | elevated |
| HUCK | Technology | +0.118 | 0.85 | 0.00 | 0.60 | 1.00 | -2.39% | high | very_high |
| QSI | Healthcare | +0.118 | 0.85 | 0.00 | 0.60 | 1.00 | -4.89% | high | elevated |

## Bottom 15 (lowest pressure)

| Ticker | Sector | pressure | SPEC | QUAL | resid | beta |
|--------|--------|----------|------|------|-------|------|
| SCHW | Financial | -0.054 | 0.00 | 1.00 | -1.38% | low |
| SAN | Financial | -0.054 | 0.00 | 1.00 | +0.59% | low |
| BTI | Consumer Defensive | -0.054 | 0.00 | 1.00 | +0.05% | low |
| SHEL | Energy | -0.054 | 0.00 | 1.00 | +0.94% | low |
| CVX | Energy | -0.054 | 0.00 | 1.00 | +0.34% | low |
| CVS | Healthcare | -0.054 | 0.00 | 1.00 | -0.87% | low |
| RIO | Basic Materials | -0.054 | 0.00 | 1.00 | +0.05% | low |
| RY | Financial | -0.054 | 0.00 | 1.00 | +0.66% | low |
| UL | Consumer Defensive | -0.054 | 0.00 | 1.00 | +1.17% | low |
| TTE | Energy | -0.054 | 0.00 | 1.00 | -0.66% | low |
| PM | Consumer Defensive | -0.054 | 0.00 | 1.00 | +0.26% | low |
| PSX | Energy | -0.054 | 0.00 | 1.00 | -0.17% | low |
| AMGN | Healthcare | -0.054 | 0.00 | 1.00 | -0.29% | low |
| ABBV | Healthcare | -0.054 | 0.00 | 1.00 | +0.15% | low |
| CB | Financial | -0.054 | 0.00 | 1.00 | +0.93% | low |

## Sector median pressure

| Sector | n | median pressure | median resid |
|--------|---|-----------------|--------------|
| Healthcare | 1052 | +0.067 | -1.73% |
| Technology | 797 | +0.051 | -0.22% |
| Communication Services | 255 | +0.051 | -0.17% |
| Consumer Cyclical | 528 | +0.041 | +0.08% |
| Basic Materials | 294 | +0.039 | +0.06% |
| Industrials | 716 | +0.038 | -0.05% |
| Real Estate | 247 | +0.036 | +0.20% |
| Consumer Defensive | 241 | +0.033 | +0.19% |
| Financial | 7219 | +0.030 | +0.04% |
| Energy | 251 | +0.013 | +0.05% |
| Utilities | 107 | +0.002 | +1.16% |

## Composite averages by size

| size | n | SPEC | QUAL | pressure |
|------|---|------|------|----------|
| large | 773 | 0.17 | 0.79 | -0.020 |
| mega | 163 | 0.15 | 0.83 | -0.033 |
| micro | 2203 | 0.52 | 0.29 | +0.067 |
| mid | 1129 | 0.36 | 0.52 | +0.024 |
| small | 1635 | 0.49 | 0.40 | +0.052 |
| unknown | 5804 | 0.32 | 0.24 | +0.028 |
