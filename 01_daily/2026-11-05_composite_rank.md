# Composite residual rank — **2026-11-05**

Generated: 2026-11-05T17:00:48.029573-05:00
Prior snapshot (for returns): **2026-11-04**

## Y snapshot (v1 — breadth only)

- **p_risk_on:** 0.0 (from % names up)
- **pct_up:** 0.1591
- **median_ret:** -2.91%
- **conviction:** 1.0
- **n:** 11757
- note: price_derived breadth only (v1)

## Method (deliberately simple)

- **residual** = stock return − median stock return (same pair window)
- **composites:** SPEC_DURATION, QUALITY_DEFENSIVE, CROWDING, SIZE_TILT
- **pressure** = conviction × prior effects of composites given p_risk_on
- Ranking is **cross-sectional residual bias**, not an absolute SPY call
- Hand priors only — replace with audit weights later

CSV: `data/composite/2026-11-05_composite_rank.csv`

## Top 20 by residual pressure (favor when risk-on / current Y)

| Ticker | Sector | pressure | SPEC | QUAL | CROWD | SIZE | resid | beta | short |
|--------|--------|----------|------|------|-------|------|-------|------|-------|
| ABT | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.25% | low | low |
| NEM | Basic Materials | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +4.26% | low | low |
| RY | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.03% | low | low |
| UL | Consumer Defensive | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +4.09% | low | low |
| MFG | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -1.28% | low | low |
| SYK | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.56% | low | low |
| WMT | Consumer Defensive | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.78% | low | low |
| SMFG | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -1.76% | low | low |
| AZN | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.76% | low | low |
| CB | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +2.23% | low | low |
| TD | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -1.08% | low | low |
| HDB | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +4.43% | low | low |
| DHR | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.75% | low | low |
| MA | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.42% | low | low |
| SAN | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +2.41% | low | low |
| VZ | Communication Serv | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +2.80% | low | low |
| BP | Energy | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.91% | low | low |
| ADP | Technology | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +4.09% | low | low |
| PDD | Consumer Cyclical | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +5.10% | low | low |
| AMGN | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.90% | low | low |

## Bottom 15 (lowest pressure)

| Ticker | Sector | pressure | SPEC | QUAL | resid | beta |
|--------|--------|----------|------|------|-------|------|
| NMRA | Healthcare | -1.730 | 0.95 | 0.00 | -11.13% | high |
| DTIL | Healthcare | -1.730 | 0.95 | 0.00 | +24.46% | high |
| AMTX | Basic Materials | -1.730 | 0.95 | 0.00 | +41.31% | high |
| ACH | Healthcare | -1.730 | 0.95 | 0.00 | +10.05% | high |
| FOA | Financial | -1.730 | 0.95 | 0.00 | +9.91% | high |
| ANGI | Communication Serv | -1.730 | 0.95 | 0.00 | +9.92% | high |
| CRMT | Consumer Cyclical | -1.690 | 0.85 | 0.00 | +23.54% | high |
| WKHS | Consumer Cyclical | -1.690 | 0.85 | 0.00 | -2.53% | high |
| INO | Healthcare | -1.690 | 0.85 | 0.00 | -7.59% | high |
| TDOC | Healthcare | -1.670 | 0.95 | 0.00 | -0.08% | high |
| EVGO | Consumer Cyclical | -1.670 | 0.95 | 0.00 | -0.41% | high |
| ARRY | Technology | -1.670 | 0.95 | 0.00 | +2.34% | high |
| BMBL | Communication Serv | -1.670 | 0.95 | 0.00 | +2.57% | high |
| DNUT | Consumer Defensive | -1.670 | 0.95 | 0.00 | +33.59% | high |
| ARCT | Healthcare | -1.630 | 0.85 | 0.00 | -10.98% | high |

## Sector median pressure

| Sector | n | median pressure | median resid |
|--------|---|-----------------|--------------|
| Utilities | 107 | -0.030 | +1.72% |
| Energy | 252 | -0.225 | -1.02% |
| Financial | 7270 | -0.415 | +0.43% |
| Consumer Defensive | 240 | -0.475 | +0.71% |
| Real Estate | 248 | -0.505 | +0.87% |
| Consumer Cyclical | 522 | -0.570 | -0.46% |
| Basic Materials | 298 | -0.605 | -0.05% |
| Industrials | 712 | -0.625 | -1.75% |
| Communication Services | 252 | -0.705 | +0.44% |
| Technology | 802 | -0.745 | -4.18% |
| Healthcare | 1054 | -0.935 | -2.65% |

## Composite averages by size

| size | n | SPEC | QUAL | pressure |
|------|---|------|------|----------|
| large | 750 | 0.17 | 0.79 | +0.265 |
| mega | 160 | 0.14 | 0.83 | +0.471 |
| micro | 2281 | 0.52 | 0.27 | -0.950 |
| mid | 1108 | 0.36 | 0.51 | -0.351 |
| small | 1600 | 0.49 | 0.39 | -0.735 |
| unknown | 5858 | 0.32 | 0.23 | -0.395 |
