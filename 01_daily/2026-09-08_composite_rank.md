# Composite residual rank — **2026-09-08**

Generated: 2026-09-08T19:26:29.526680-04:00
Prior snapshot (for returns): **2026-09-04**

## Y snapshot (v1 — breadth only)

- **p_risk_on:** 0.0 (from % names up)
- **pct_up:** 0.3022
- **median_ret:** -0.31%
- **conviction:** 1.0
- **n:** 11608
- note: price_derived breadth only (v1)

## Method (deliberately simple)

- **residual** = stock return − median stock return (same pair window)
- **composites:** SPEC_DURATION, QUALITY_DEFENSIVE, CROWDING, SIZE_TILT
- **pressure** = conviction × prior effects of composites given p_risk_on
- Ranking is **cross-sectional residual bias**, not an absolute SPY call
- Hand priors only — replace with audit weights later

CSV: `data/composite/2026-09-08_composite_rank.csv`

## Top 20 by residual pressure (favor when risk-on / current Y)

| Ticker | Sector | pressure | SPEC | QUAL | CROWD | SIZE | resid | beta | short |
|--------|--------|----------|------|------|-------|------|-------|------|-------|
| SMFG | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -1.55% | low | low |
| MA | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -1.12% | low | low |
| MCK | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -1.76% | low | low |
| MCD | Consumer Cyclical | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.36% | low | low |
| PG | Consumer Defensive | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.27% | low | low |
| MUFG | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -1.72% | low | low |
| DHR | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.86% | low | low |
| UNH | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.25% | low | low |
| UL | Consumer Defensive | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.71% | low | low |
| MDT | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -1.58% | low | low |
| SNY | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -2.15% | low | low |
| SO | Utilities | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.31% | low | low |
| NEE | Utilities | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.79% | low | low |
| NEM | Basic Materials | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.47% | low | low |
| SHEL | Energy | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +2.86% | low | unknown |
| XOM | Energy | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.06% | low | low |
| MFG | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.49% | low | low |
| RIO | Basic Materials | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.86% | low | low |
| TD | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.60% | low | low |
| CME | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.77% | low | low |

## Bottom 15 (lowest pressure)

| Ticker | Sector | pressure | SPEC | QUAL | resid | beta |
|--------|--------|----------|------|------|-------|------|
| CHPT | Consumer Cyclical | -1.790 | 0.95 | 0.00 | -4.94% | high |
| GPRO | Technology | -1.790 | 0.95 | 0.00 | -13.80% | high |
| INO | Healthcare | -1.690 | 0.85 | 0.00 | -0.39% | high |
| ARCT | Healthcare | -1.670 | 0.95 | 0.00 | -0.89% | high |
| EOSE | Industrials | -1.670 | 0.95 | 0.00 | +11.14% | high |
| XHLD | Communication Serv | -1.630 | 0.85 | 0.00 | +1.83% | high |
| DH | Healthcare | -1.630 | 0.85 | 0.00 | -2.54% | high |
| SST | Industrials | -1.630 | 0.85 | 0.00 | +30.86% | high |
| TJGC | Communication Serv | -1.630 | 0.85 | 0.00 | +1.27% | high |
| JANX | Healthcare | -1.610 | 0.95 | 0.00 | -0.67% | high |
| INGN | Healthcare | -1.570 | 0.85 | 0.00 | -3.19% | high |
| ACH | Healthcare | -1.570 | 0.85 | 0.00 | -8.78% | high |
| PBM | Healthcare | -1.555 | 0.85 | 0.00 | +4.72% | high |
| BRR | Financial | -1.555 | 0.85 | 0.00 | +2.95% | high |
| CTOR | Healthcare | -1.555 | 0.85 | 0.00 | +8.45% | high |

## Sector median pressure

| Sector | n | median pressure | median resid |
|--------|---|-----------------|--------------|
| Utilities | 107 | +0.045 | +1.09% |
| Energy | 253 | -0.180 | +1.25% |
| Financial | 7117 | -0.415 | +0.10% |
| Consumer Defensive | 242 | -0.458 | -0.80% |
| Real Estate | 248 | -0.505 | -0.25% |
| Consumer Cyclical | 528 | -0.530 | -1.60% |
| Industrials | 715 | -0.530 | -0.24% |
| Basic Materials | 291 | -0.565 | -0.30% |
| Communication Services | 257 | -0.700 | -0.50% |
| Technology | 792 | -0.700 | -0.53% |
| Healthcare | 1058 | -0.835 | -1.01% |

## Composite averages by size

| size | n | SPEC | QUAL | pressure |
|------|---|------|------|----------|
| large | 779 | 0.17 | 0.80 | +0.286 |
| mega | 170 | 0.14 | 0.84 | +0.488 |
| micro | 2156 | 0.51 | 0.30 | -0.913 |
| mid | 1185 | 0.36 | 0.51 | -0.334 |
| small | 1612 | 0.48 | 0.41 | -0.706 |
| unknown | 5706 | 0.32 | 0.25 | -0.376 |
