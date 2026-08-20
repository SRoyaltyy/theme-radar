# Composite residual rank — **2026-08-20**

Generated: 2026-08-20T17:47:38.382884-04:00
Prior snapshot (for returns): **2026-08-19**

## Y snapshot (v1 — breadth only)

- **p_risk_on:** 0.0 (from % names up)
- **pct_up:** 0.2852
- **median_ret:** -0.37%
- **conviction:** 1.0
- **n:** 11612
- note: price_derived breadth only (v1)

## Method (deliberately simple)

- **residual** = stock return − median stock return (same pair window)
- **composites:** SPEC_DURATION, QUALITY_DEFENSIVE, CROWDING, SIZE_TILT
- **pressure** = conviction × prior effects of composites given p_risk_on
- Ranking is **cross-sectional residual bias**, not an absolute SPY call
- Hand priors only — replace with audit weights later

CSV: `data/composite/2026-08-20_composite_rank.csv`

## Top 20 by residual pressure (favor when risk-on / current Y)

| Ticker | Sector | pressure | SPEC | QUAL | CROWD | SIZE | resid | beta | short |
|--------|--------|----------|------|------|-------|------|-------|------|-------|
| GD | Industrials | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -1.22% | low | low |
| TTE | Energy | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.30% | low | low |
| SAN | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.66% | low | low |
| NEE | Utilities | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.65% | low | low |
| BMY | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -2.79% | low | low |
| MO | Consumer Defensive | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.75% | low | low |
| TMUS | Communication Serv | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.25% | low | low |
| SNY | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -1.11% | low | low |
| RTX | Industrials | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -3.28% | low | low |
| SO | Utilities | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.45% | low | low |
| BRK-B | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.18% | low | low |
| CVX | Energy | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.38% | low | low |
| CVS | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.37% | low | low |
| HSBC | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.40% | low | low |
| MFG | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.28% | low | low |
| BRK-A | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.37% | low | low |
| HDB | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.15% | low | low |
| TD | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.89% | low | low |
| BP | Energy | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +3.60% | low | low |
| RIO | Basic Materials | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +2.10% | low | low |

## Bottom 15 (lowest pressure)

| Ticker | Sector | pressure | SPEC | QUAL | resid | beta |
|--------|--------|----------|------|------|-------|------|
| GDC | Communication Serv | -1.730 | 0.95 | 0.00 | +13.56% | high |
| BTCT | Technology | -1.690 | 0.85 | 0.00 | +75.37% | high |
| INO | Healthcare | -1.690 | 0.85 | 0.00 | -6.55% | high |
| SBET | Financial | -1.670 | 0.95 | 0.00 | +7.58% | high |
| CERT | Healthcare | -1.670 | 0.95 | 0.00 | +4.80% | high |
| FDMT | Healthcare | -1.670 | 0.95 | 0.00 | -3.56% | high |
| ARCT | Healthcare | -1.670 | 0.95 | 0.00 | +7.28% | high |
| EBS | Healthcare | -1.630 | 0.85 | 0.00 | -1.06% | high |
| BTCS | Financial | -1.630 | 0.85 | 0.00 | +4.34% | high |
| AGPU | Technology | -1.630 | 0.85 | 0.00 | -1.55% | high |
| NAKA | Financial | -1.630 | 0.85 | 0.00 | +4.33% | high |
| VERI | Technology | -1.630 | 0.85 | 0.00 | -13.03% | high |
| AIRS | Healthcare | -1.630 | 0.85 | 0.00 | -4.61% | high |
| AIRO | Industrials | -1.630 | 0.85 | 0.00 | -3.70% | high |
| HRTX | Healthcare | -1.630 | 0.85 | 0.00 | +0.37% | high |

## Sector median pressure

| Sector | n | median pressure | median resid |
|--------|---|-----------------|--------------|
| Utilities | 110 | +0.045 | -0.08% |
| Energy | 253 | -0.180 | +0.58% |
| Financial | 7111 | -0.415 | +0.09% |
| Real Estate | 252 | -0.453 | +0.32% |
| Consumer Defensive | 244 | -0.485 | +0.10% |
| Industrials | 709 | -0.505 | -0.93% |
| Consumer Cyclical | 533 | -0.555 | -0.80% |
| Basic Materials | 287 | -0.580 | +0.05% |
| Communication Services | 258 | -0.700 | -0.42% |
| Technology | 791 | -0.700 | -0.46% |
| Healthcare | 1064 | -0.840 | -1.47% |

## Composite averages by size

| size | n | SPEC | QUAL | pressure |
|------|---|------|------|----------|
| large | 799 | 0.17 | 0.79 | +0.268 |
| mega | 166 | 0.15 | 0.84 | +0.473 |
| micro | 2146 | 0.51 | 0.30 | -0.918 |
| mid | 1174 | 0.36 | 0.51 | -0.343 |
| small | 1623 | 0.49 | 0.40 | -0.716 |
| unknown | 5704 | 0.32 | 0.24 | -0.383 |
