# Composite residual rank — **2026-10-29**

Generated: 2026-10-29T16:53:14.760366-04:00
Prior snapshot (for returns): **2026-10-28**

## Y snapshot (v1 — breadth only)

- **p_risk_on:** 0.4675 (from % names up)
- **pct_up:** 0.537
- **median_ret:** 0.10%
- **conviction:** 0.0649
- **n:** 11780
- note: price_derived breadth only (v1)

## Method (deliberately simple)

- **residual** = stock return − median stock return (same pair window)
- **composites:** SPEC_DURATION, QUALITY_DEFENSIVE, CROWDING, SIZE_TILT
- **pressure** = conviction × prior effects of composites given p_risk_on
- Ranking is **cross-sectional residual bias**, not an absolute SPY call
- Hand priors only — replace with audit weights later

CSV: `data/composite/2026-10-29_composite_rank.csv`

## Top 20 by residual pressure (favor when risk-on / current Y)

| Ticker | Sector | pressure | SPEC | QUAL | CROWD | SIZE | resid | beta | short |
|--------|--------|----------|------|------|-------|------|-------|------|-------|
| ABBV | Healthcare | +0.007 | 0.00 | 1.00 | 0.00 | 0.00 | +1.58% | low | low |
| ABT | Healthcare | +0.007 | 0.00 | 1.00 | 0.00 | 0.00 | +1.78% | low | low |
| COP | Energy | +0.007 | 0.00 | 1.00 | 0.00 | 0.00 | +0.55% | low | low |
| NEM | Basic Materials | +0.007 | 0.00 | 1.00 | 0.00 | 0.00 | -1.96% | low | low |
| NEE | Utilities | +0.007 | 0.00 | 1.00 | 0.00 | 0.00 | +1.29% | low | low |
| MRK | Healthcare | +0.007 | 0.00 | 1.00 | 0.00 | 0.00 | +3.74% | low | low |
| MCK | Healthcare | +0.007 | 0.00 | 1.00 | 0.00 | 0.00 | +2.02% | low | low |
| MUFG | Financial | +0.007 | 0.00 | 1.00 | 0.00 | 0.00 | +2.14% | low | low |
| BP | Energy | +0.007 | 0.00 | 1.00 | 0.00 | 0.00 | +1.03% | low | low |
| MCD | Consumer Cyclical | +0.007 | 0.00 | 1.00 | 0.00 | 0.00 | +2.65% | low | low |
| MPC | Energy | +0.007 | 0.00 | 1.00 | 0.00 | 0.00 | -1.97% | low | low |
| PSX | Energy | +0.007 | 0.00 | 1.00 | 0.00 | 0.00 | -0.15% | low | low |
| IBN | Financial | +0.007 | 0.00 | 1.00 | 0.00 | 0.00 | +1.40% | low | low |
| TM | Consumer Cyclical | +0.007 | 0.00 | 1.00 | 0.00 | 0.00 | +0.82% | low | low |
| TJX | Consumer Cyclical | +0.007 | 0.00 | 1.00 | 0.00 | 0.00 | +2.07% | low | low |
| BMY | Healthcare | +0.007 | 0.00 | 1.00 | 0.00 | 0.00 | +1.26% | low | low |
| BRK-A | Financial | +0.007 | 0.00 | 1.00 | 0.00 | 0.00 | +0.59% | low | low |
| ENB | Energy | +0.007 | 0.00 | 1.00 | 0.00 | 0.00 | +1.39% | low | low |
| EQNR | Energy | +0.007 | 0.00 | 1.00 | 0.00 | 0.00 | -0.26% | low | low |
| BRK-B | Financial | +0.007 | 0.00 | 1.00 | 0.00 | 0.00 | +0.20% | low | low |

## Bottom 15 (lowest pressure)

| Ticker | Sector | pressure | SPEC | QUAL | resid | beta |
|--------|--------|----------|------|------|-------|------|
| AIRS | Healthcare | -0.018 | 0.95 | 0.00 | +15.88% | high |
| SLNH | Financial | -0.018 | 0.95 | 0.00 | -2.87% | high |
| GLSI | Healthcare | -0.018 | 0.95 | 0.00 | +3.67% | high |
| KRRO | Healthcare | -0.018 | 0.95 | 0.00 | +2.36% | high |
| INGN | Healthcare | -0.017 | 0.95 | 0.00 | +0.04% | high |
| DMRC | Technology | -0.017 | 0.95 | 0.00 | +1.53% | high |
| MRLN | Industrials | -0.017 | 0.85 | 0.00 | -7.99% | high |
| CRIS | Healthcare | -0.017 | 0.85 | 0.00 | +22.13% | high |
| PRME | Healthcare | -0.016 | 0.95 | 0.00 | -2.33% | high |
| TDOC | Healthcare | -0.016 | 0.95 | 0.00 | +26.79% | high |
| EVGO | Consumer Cyclical | -0.016 | 0.95 | 0.00 | -0.90% | high |
| BBAI | Technology | -0.016 | 0.95 | 0.00 | +8.44% | high |
| ULCC | Industrials | -0.016 | 0.95 | 0.00 | +4.93% | high |
| BETR | Financial | -0.016 | 0.95 | 0.00 | +6.45% | high |
| CRML | Basic Materials | -0.016 | 0.95 | 0.00 | +1.96% | high |

## Sector median pressure

| Sector | n | median pressure | median resid |
|--------|---|-----------------|--------------|
| Utilities | 107 | -0.000 | +0.84% |
| Energy | 252 | -0.002 | -0.25% |
| Financial | 7290 | -0.004 | -0.03% |
| Consumer Defensive | 240 | -0.004 | +0.31% |
| Real Estate | 248 | -0.005 | +1.55% |
| Basic Materials | 297 | -0.006 | -1.08% |
| Consumer Cyclical | 524 | -0.006 | +1.81% |
| Industrials | 714 | -0.006 | +1.03% |
| Communication Services | 254 | -0.007 | +0.65% |
| Technology | 801 | -0.007 | -0.68% |
| Healthcare | 1053 | -0.009 | -0.10% |

## Composite averages by size

| size | n | SPEC | QUAL | pressure |
|------|---|------|------|----------|
| large | 765 | 0.18 | 0.79 | +0.003 |
| mega | 164 | 0.14 | 0.84 | +0.005 |
| micro | 2250 | 0.52 | 0.28 | -0.009 |
| mid | 1134 | 0.36 | 0.51 | -0.003 |
| small | 1585 | 0.49 | 0.41 | -0.007 |
| unknown | 5882 | 0.32 | 0.24 | -0.004 |
