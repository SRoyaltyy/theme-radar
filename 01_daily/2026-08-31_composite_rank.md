# Composite residual rank — **2026-08-31**

Generated: 2026-08-31T20:40:08.701011-04:00
Prior snapshot (for returns): **2026-08-28**

## Y snapshot (v1 — breadth only)

- **p_risk_on:** 0.0 (from % names up)
- **pct_up:** 0.3231
- **median_ret:** -0.20%
- **conviction:** 1.0
- **n:** 11631
- note: price_derived breadth only (v1)

## Method (deliberately simple)

- **residual** = stock return − median stock return (same pair window)
- **composites:** SPEC_DURATION, QUALITY_DEFENSIVE, CROWDING, SIZE_TILT
- **pressure** = conviction × prior effects of composites given p_risk_on
- Ranking is **cross-sectional residual bias**, not an absolute SPY call
- Hand priors only — replace with audit weights later

CSV: `data/composite/2026-08-31_composite_rank.csv`

## Top 20 by residual pressure (favor when risk-on / current Y)

| Ticker | Sector | pressure | SPEC | QUAL | CROWD | SIZE | resid | beta | short |
|--------|--------|----------|------|------|-------|------|-------|------|-------|
| V | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.38% | low | low |
| ENB | Energy | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.94% | low | low |
| MDT | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.43% | low | low |
| NEE | Utilities | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.81% | low | low |
| NEM | Basic Materials | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -1.30% | low | low |
| DHR | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.96% | low | low |
| BP | Energy | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.91% | low | low |
| AMGN | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.38% | low | low |
| MO | Consumer Defensive | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.04% | low | low |
| MA | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.80% | low | low |
| LLY | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -1.32% | low | low |
| MRK | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.19% | low | low |
| IBN | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.81% | low | low |
| GD | Industrials | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -1.90% | low | low |
| JNJ | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.61% | low | low |
| PGR | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.05% | low | low |
| HDB | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -1.44% | low | low |
| ABT | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -1.67% | low | low |
| RIO | Basic Materials | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.57% | low | low |
| EQNR | Energy | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +3.61% | low | low |

## Bottom 15 (lowest pressure)

| Ticker | Sector | pressure | SPEC | QUAL | resid | beta |
|--------|--------|----------|------|------|-------|------|
| GPRO | Technology | -1.790 | 0.95 | 0.00 | +46.87% | high |
| ADCT | Healthcare | -1.730 | 0.95 | 0.00 | +2.83% | high |
| BTCT | Technology | -1.690 | 0.85 | 0.00 | +8.45% | high |
| WCT | Technology | -1.690 | 0.85 | 0.00 | +16.72% | high |
| INBX | Healthcare | -1.670 | 0.95 | 0.00 | +2.87% | high |
| ARCT | Healthcare | -1.670 | 0.95 | 0.00 | -2.63% | high |
| TROO | Financial | -1.630 | 0.85 | 0.00 | +5.78% | high |
| CHAI | Communication Serv | -1.630 | 0.85 | 0.00 | -4.80% | high |
| DH | Healthcare | -1.630 | 0.85 | 0.00 | +18.95% | high |
| NCPL | Financial | -1.630 | 0.85 | 0.00 | +4.55% | high |
| LPSN | Technology | -1.630 | 0.85 | 0.00 | +10.13% | high |
| XHLD | Communication Serv | -1.630 | 0.85 | 0.00 | -2.06% | high |
| DAIC | Technology | -1.630 | 0.85 | 0.00 | -24.80% | high |
| RCEL | Healthcare | -1.630 | 0.85 | 0.00 | -2.21% | high |
| DPRO | Technology | -1.630 | 0.85 | 0.00 | +21.46% | high |

## Sector median pressure

| Sector | n | median pressure | median resid |
|--------|---|-----------------|--------------|
| Utilities | 109 | +0.045 | +0.03% |
| Energy | 252 | -0.170 | +1.62% |
| Financial | 7134 | -0.415 | +0.04% |
| Consumer Defensive | 242 | -0.458 | -0.64% |
| Real Estate | 250 | -0.505 | -0.54% |
| Industrials | 712 | -0.505 | -0.48% |
| Basic Materials | 288 | -0.530 | -0.57% |
| Consumer Cyclical | 532 | -0.535 | -1.06% |
| Communication Services | 256 | -0.700 | -0.52% |
| Technology | 793 | -0.700 | -0.05% |
| Healthcare | 1063 | -0.835 | -0.29% |

## Composite averages by size

| size | n | SPEC | QUAL | pressure |
|------|---|------|------|----------|
| large | 784 | 0.16 | 0.80 | +0.290 |
| mega | 168 | 0.14 | 0.85 | +0.487 |
| micro | 2164 | 0.51 | 0.30 | -0.912 |
| mid | 1181 | 0.36 | 0.51 | -0.339 |
| small | 1614 | 0.48 | 0.41 | -0.706 |
| unknown | 5720 | 0.32 | 0.25 | -0.377 |
