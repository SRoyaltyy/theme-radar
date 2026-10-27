# Composite residual rank — **2026-10-27**

Generated: 2026-10-27T16:56:09.803426-04:00
Prior snapshot (for returns): **2026-10-26**

## Y snapshot (v1 — breadth only)

- **p_risk_on:** 0.7837 (from % names up)
- **pct_up:** 0.6635
- **median_ret:** 0.39%
- **conviction:** 0.5675
- **n:** 11774
- note: price_derived breadth only (v1)

## Method (deliberately simple)

- **residual** = stock return − median stock return (same pair window)
- **composites:** SPEC_DURATION, QUALITY_DEFENSIVE, CROWDING, SIZE_TILT
- **pressure** = conviction × prior effects of composites given p_risk_on
- Ranking is **cross-sectional residual bias**, not an absolute SPY call
- Hand priors only — replace with audit weights later

CSV: `data/composite/2026-10-27_composite_rank.csv`

## Top 20 by residual pressure (favor when risk-on / current Y)

| Ticker | Sector | pressure | SPEC | QUAL | CROWD | SIZE | resid | beta | short |
|--------|--------|----------|------|------|-------|------|-------|------|-------|
| LDI | Financial | +0.576 | 0.95 | 0.00 | 0.80 | 1.00 | +13.41% | high | very_high |
| KRRO | Healthcare | +0.576 | 0.95 | 0.00 | 0.80 | 1.00 | +10.26% | high | very_high |
| TBCH | Technology | +0.576 | 0.95 | 0.00 | 0.80 | 1.00 | +0.83% | high | very_high |
| INGN | Healthcare | +0.557 | 0.95 | 0.00 | 0.60 | 1.00 | +0.32% | high | elevated |
| CRML | Basic Materials | +0.538 | 0.95 | 0.00 | 0.80 | 0.80 | +27.04% | high | very_high |
| BETR | Financial | +0.538 | 0.95 | 0.00 | 0.80 | 0.80 | +17.00% | high | very_high |
| BMBL | Communication Serv | +0.538 | 0.95 | 0.00 | 0.80 | 0.80 | -0.22% | high | very_high |
| PACB | Healthcare | +0.538 | 0.95 | 0.00 | 0.80 | 0.80 | +8.50% | high | very_high |
| ENVX | Industrials | +0.538 | 0.95 | 0.00 | 0.80 | 0.80 | +24.61% | high | very_high |
| CERT | Healthcare | +0.538 | 0.95 | 0.00 | 0.80 | 0.80 | +2.82% | high | very_high |
| ONL | Real Estate | +0.533 | 0.95 | 0.00 | 0.35 | 1.00 | +10.73% | high | low |
| GPUS | Industrials | +0.525 | 0.85 | 0.00 | 0.60 | 1.00 | +16.28% | high | elevated |
| TROO | Financial | +0.525 | 0.85 | 0.00 | 0.60 | 1.00 | -1.27% | high | elevated |
| YHC | Consumer Defensive | +0.525 | 0.85 | 0.00 | 0.60 | 1.00 | +1.66% | high | elevated |
| CRBP | Healthcare | +0.525 | 0.85 | 0.00 | 0.60 | 1.00 | +3.62% | high | very_high |
| LFMD | Healthcare | +0.525 | 0.85 | 0.00 | 0.60 | 1.00 | +1.54% | high | very_high |
| BKKT | Technology | +0.525 | 0.85 | 0.00 | 0.60 | 1.00 | +5.88% | high | very_high |
| NXH | Consumer Cyclical | +0.525 | 0.85 | 0.00 | 0.60 | 1.00 | +0.88% | high | very_high |
| PAL | Industrials | +0.525 | 0.85 | 0.00 | 0.60 | 1.00 | -4.70% | high | very_high |
| ORGO | Healthcare | +0.525 | 0.85 | 0.00 | 0.60 | 1.00 | -4.64% | high | very_high |

## Bottom 15 (lowest pressure)

| Ticker | Sector | pressure | SPEC | QUAL | resid | beta |
|--------|--------|----------|------|------|-------|------|
| TD | Financial | -0.241 | 0.00 | 1.00 | -0.02% | low |
| MRK | Healthcare | -0.241 | 0.00 | 1.00 | +0.47% | low |
| MUFG | Financial | -0.241 | 0.00 | 1.00 | +1.46% | low |
| NEE | Utilities | -0.241 | 0.00 | 1.00 | +0.08% | low |
| MO | Consumer Defensive | -0.241 | 0.00 | 1.00 | -0.56% | low |
| MPC | Energy | -0.241 | 0.00 | 1.00 | -7.75% | low |
| NEM | Basic Materials | -0.241 | 0.00 | 1.00 | +1.65% | low |
| CB | Financial | -0.241 | 0.00 | 1.00 | -0.52% | low |
| TM | Consumer Cyclical | -0.241 | 0.00 | 1.00 | -0.93% | low |
| PSX | Energy | -0.241 | 0.00 | 1.00 | -7.42% | low |
| WMT | Consumer Defensive | -0.241 | 0.00 | 1.00 | -1.19% | low |
| JNJ | Healthcare | -0.241 | 0.00 | 1.00 | +0.53% | low |
| RIO | Basic Materials | -0.241 | 0.00 | 1.00 | +2.03% | low |
| IBN | Financial | -0.241 | 0.00 | 1.00 | -1.62% | low |
| IBM | Technology | -0.241 | 0.00 | 1.00 | -1.64% | low |

## Sector median pressure

| Sector | n | median pressure | median resid |
|--------|---|-----------------|--------------|
| Healthcare | 1053 | +0.288 | +1.02% |
| Technology | 801 | +0.225 | +0.84% |
| Communication Services | 254 | +0.225 | -0.39% |
| Basic Materials | 297 | +0.187 | +2.28% |
| Consumer Cyclical | 524 | +0.182 | -0.05% |
| Industrials | 714 | +0.177 | +0.68% |
| Real Estate | 248 | +0.163 | -0.52% |
| Consumer Defensive | 240 | +0.145 | -0.89% |
| Financial | 7284 | +0.134 | -0.05% |
| Energy | 252 | +0.066 | -0.68% |
| Utilities | 107 | -0.015 | +0.13% |

## Composite averages by size

| size | n | SPEC | QUAL | pressure |
|------|---|------|------|----------|
| large | 762 | 0.17 | 0.80 | -0.089 |
| mega | 164 | 0.14 | 0.84 | -0.157 |
| micro | 2250 | 0.52 | 0.28 | +0.302 |
| mid | 1131 | 0.36 | 0.52 | +0.111 |
| small | 1590 | 0.49 | 0.41 | +0.232 |
| unknown | 5877 | 0.32 | 0.25 | +0.121 |
