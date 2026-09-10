# Composite residual rank — **2026-09-10**

Generated: 2026-09-10T19:14:28.492577-04:00
Prior snapshot (for returns): **2026-09-09**

## Y snapshot (v1 — breadth only)

- **p_risk_on:** 0.0 (from % names up)
- **pct_up:** 0.1967
- **median_ret:** -0.68%
- **conviction:** 1.0
- **n:** 11629
- note: price_derived breadth only (v1)

## Method (deliberately simple)

- **residual** = stock return − median stock return (same pair window)
- **composites:** SPEC_DURATION, QUALITY_DEFENSIVE, CROWDING, SIZE_TILT
- **pressure** = conviction × prior effects of composites given p_risk_on
- Ranking is **cross-sectional residual bias**, not an absolute SPY call
- Hand priors only — replace with audit weights later

CSV: `data/composite/2026-09-10_composite_rank.csv`

## Top 20 by residual pressure (favor when risk-on / current Y)

| Ticker | Sector | pressure | SPEC | QUAL | CROWD | SIZE | resid | beta | short |
|--------|--------|----------|------|------|-------|------|-------|------|-------|
| SHEL | Energy | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.06% | low | low |
| XOM | Energy | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.29% | low | low |
| ABBV | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +2.31% | low | low |
| BMY | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.34% | low | low |
| PFE | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.22% | low | low |
| SO | Utilities | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.02% | low | low |
| ABT | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -1.09% | low | low |
| VZ | Communication Serv | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.15% | low | low |
| VRTX | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.57% | low | low |
| SNY | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.38% | low | low |
| IBN | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.10% | low | low |
| IBM | Technology | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -1.78% | low | low |
| SMFG | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.60% | low | low |
| HSBC | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.66% | low | low |
| KO | Consumer Defensive | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.00% | low | low |
| LMT | Industrials | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.76% | low | low |
| LLY | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.58% | low | low |
| SCHW | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.43% | low | low |
| SAN | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.34% | low | low |
| RY | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.28% | low | low |

## Bottom 15 (lowest pressure)

| Ticker | Sector | pressure | SPEC | QUAL | resid | beta |
|--------|--------|----------|------|------|-------|------|
| CHPT | Consumer Cyclical | -1.790 | 0.95 | 0.00 | +0.46% | high |
| XHLD | Communication Serv | -1.630 | 0.85 | 0.00 | +3.82% | high |
| DH | Healthcare | -1.630 | 0.85 | 0.00 | +0.68% | high |
| SST | Industrials | -1.630 | 0.85 | 0.00 | -12.24% | high |
| SLE | Communication Serv | -1.630 | 0.85 | 0.00 | +0.90% | high |
| FGI | Consumer Cyclical | -1.630 | 0.85 | 0.00 | +10.13% | high |
| FLWS | Consumer Cyclical | -1.630 | 0.85 | 0.00 | -12.21% | high |
| TJGC | Communication Serv | -1.630 | 0.85 | 0.00 | +1.53% | high |
| KLC | Consumer Defensive | -1.630 | 0.85 | 0.00 | -0.50% | high |
| APPS | Technology | -1.610 | 0.95 | 0.00 | +7.37% | high |
| NMRA | Healthcare | -1.570 | 0.85 | 0.00 | -4.32% | high |
| DMRC | Technology | -1.570 | 0.85 | 0.00 | -2.06% | high |
| STRO | Healthcare | -1.570 | 0.85 | 0.00 | -2.15% | high |
| ACH | Healthcare | -1.570 | 0.85 | 0.00 | +1.62% | high |
| ELTX | Healthcare | -1.570 | 0.85 | 0.00 | -2.53% | high |

## Sector median pressure

| Sector | n | median pressure | median resid |
|--------|---|-----------------|--------------|
| Utilities | 107 | +0.045 | -0.33% |
| Energy | 253 | -0.180 | +0.44% |
| Financial | 7138 | -0.415 | +0.06% |
| Consumer Defensive | 242 | -0.440 | +0.23% |
| Real Estate | 248 | -0.505 | -0.20% |
| Industrials | 715 | -0.530 | -0.51% |
| Consumer Cyclical | 528 | -0.565 | -0.13% |
| Basic Materials | 291 | -0.580 | -1.58% |
| Communication Services | 257 | -0.700 | +0.68% |
| Technology | 792 | -0.700 | -0.30% |
| Healthcare | 1058 | -0.840 | -0.85% |

## Composite averages by size

| size | n | SPEC | QUAL | pressure |
|------|---|------|------|----------|
| large | 773 | 0.17 | 0.79 | +0.282 |
| mega | 167 | 0.14 | 0.84 | +0.490 |
| micro | 2175 | 0.51 | 0.30 | -0.917 |
| mid | 1163 | 0.35 | 0.51 | -0.333 |
| small | 1626 | 0.48 | 0.40 | -0.711 |
| unknown | 5725 | 0.32 | 0.24 | -0.380 |
