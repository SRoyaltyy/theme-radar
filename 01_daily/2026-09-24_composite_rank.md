# Composite residual rank — **2026-09-24**

Generated: 2026-09-24T19:55:04.552887-04:00
Prior snapshot (for returns): **2026-09-23**

## Y snapshot (v1 — breadth only)

- **p_risk_on:** 0.0 (from % names up)
- **pct_up:** 0.3355
- **median_ret:** -0.21%
- **conviction:** 1.0
- **n:** 11672
- note: price_derived breadth only (v1)

## Method (deliberately simple)

- **residual** = stock return − median stock return (same pair window)
- **composites:** SPEC_DURATION, QUALITY_DEFENSIVE, CROWDING, SIZE_TILT
- **pressure** = conviction × prior effects of composites given p_risk_on
- Ranking is **cross-sectional residual bias**, not an absolute SPY call
- Hand priors only — replace with audit weights later

CSV: `data/composite/2026-09-24_composite_rank.csv`

## Top 20 by residual pressure (favor when risk-on / current Y)

| Ticker | Sector | pressure | SPEC | QUAL | CROWD | SIZE | resid | beta | short |
|--------|--------|----------|------|------|-------|------|-------|------|-------|
| ABT | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -2.13% | low | low |
| VLO | Energy | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +2.07% | low | low |
| TTE | Energy | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.45% | low | low |
| TM | Consumer Cyclical | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -1.71% | low | low |
| HSBC | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.13% | low | low |
| TJX | Consumer Cyclical | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.24% | low | low |
| TMUS | Communication Serv | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.02% | low | low |
| MUFG | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.89% | low | low |
| JNJ | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.77% | low | low |
| MDT | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.68% | low | low |
| MFG | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -1.47% | low | low |
| MO | Consumer Defensive | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.10% | low | low |
| MPC | Energy | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.87% | low | low |
| MRK | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.14% | low | low |
| DHR | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.20% | low | low |
| NEM | Basic Materials | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -1.62% | low | low |
| VZ | Communication Serv | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.93% | low | low |
| BABA | Consumer Cyclical | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.05% | low | low |
| AZN | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.96% | low | low |
| PDD | Consumer Cyclical | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -1.06% | low | low |

## Bottom 15 (lowest pressure)

| Ticker | Sector | pressure | SPEC | QUAL | resid | beta |
|--------|--------|----------|------|------|-------|------|
| EU | Energy | -1.790 | 0.95 | 0.00 | +0.21% | high |
| VERI | Technology | -1.790 | 0.95 | 0.00 | +3.31% | high |
| EAF | Industrials | -1.730 | 0.95 | 0.00 | -6.75% | high |
| ADCT | Healthcare | -1.730 | 0.95 | 0.00 | -1.32% | high |
| FIRY | Communication Serv | -1.690 | 0.85 | 0.00 | -2.54% | high |
| QCLS | Technology | -1.690 | 0.85 | 0.00 | +16.12% | high |
| KAZR | Industrials | -1.690 | 0.85 | 0.00 | +0.57% | high |
| TJGC | Communication Serv | -1.690 | 0.85 | 0.00 | +21.34% | high |
| LHSW | Technology | -1.690 | 0.85 | 0.00 | -1.09% | high |
| GRML | Basic Materials | -1.690 | 0.85 | 0.00 | +33.27% | high |
| MRAM | Technology | -1.670 | 0.95 | 0.00 | +4.83% | high |
| BKKT | Technology | -1.670 | 0.95 | 0.00 | +3.27% | high |
| GEMI | Financial | -1.670 | 0.95 | 0.00 | +0.56% | high |
| CAN | Technology | -1.630 | 0.85 | 0.00 | +0.21% | high |
| SLMT | Technology | -1.630 | 0.85 | 0.00 | -2.64% | high |

## Sector median pressure

| Sector | n | median pressure | median resid |
|--------|---|-----------------|--------------|
| Utilities | 106 | +0.045 | -0.71% |
| Energy | 251 | -0.155 | +0.31% |
| Financial | 7188 | -0.415 | +0.04% |
| Consumer Defensive | 242 | -0.450 | -0.02% |
| Real Estate | 247 | -0.505 | -0.15% |
| Industrials | 718 | -0.550 | -0.48% |
| Basic Materials | 292 | -0.565 | -1.15% |
| Consumer Cyclical | 528 | -0.565 | -0.05% |
| Communication Services | 255 | -0.700 | +0.21% |
| Technology | 793 | -0.700 | -0.39% |
| Healthcare | 1052 | -0.875 | -0.32% |

## Composite averages by size

| size | n | SPEC | QUAL | pressure |
|------|---|------|------|----------|
| large | 772 | 0.17 | 0.79 | +0.275 |
| mega | 161 | 0.14 | 0.84 | +0.480 |
| micro | 2192 | 0.51 | 0.29 | -0.924 |
| mid | 1145 | 0.36 | 0.51 | -0.343 |
| small | 1628 | 0.48 | 0.40 | -0.719 |
| unknown | 5774 | 0.32 | 0.23 | -0.389 |
