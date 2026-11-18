# Composite residual rank — **2026-11-17**

Generated: 2026-11-17T21:59:08.222281-05:00
Prior snapshot (for returns): **2026-11-16**

## Y snapshot (v1 — breadth only)

- **p_risk_on:** 0.0 (from % names up)
- **pct_up:** 0.1976
- **median_ret:** -0.99%
- **conviction:** 1.0
- **n:** 11751
- note: price_derived breadth only (v1)

## Method (deliberately simple)

- **residual** = stock return − median stock return (same pair window)
- **composites:** SPEC_DURATION, QUALITY_DEFENSIVE, CROWDING, SIZE_TILT
- **pressure** = conviction × prior effects of composites given p_risk_on
- Ranking is **cross-sectional residual bias**, not an absolute SPY call
- Hand priors only — replace with audit weights later

CSV: `data/composite/2026-11-17_composite_rank.csv`

## Top 20 by residual pressure (favor when risk-on / current Y)

| Ticker | Sector | pressure | SPEC | QUAL | CROWD | SIZE | resid | beta | short |
|--------|--------|----------|------|------|-------|------|-------|------|-------|
| TMUS | Communication Serv | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.25% | low | low |
| TM | Consumer Cyclical | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.65% | low | low |
| TJX | Consumer Cyclical | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.05% | low | low |
| TD | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.72% | low | low |
| T | Communication Serv | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.68% | low | low |
| SYK | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +3.19% | low | low |
| AZN | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.04% | low | low |
| SO | Utilities | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.11% | low | low |
| SNY | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.79% | low | low |
| SMFG | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -2.44% | low | low |
| SHEL | Energy | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.51% | low | low |
| UL | Consumer Defensive | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -1.25% | low | low |
| SCHW | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.19% | low | low |
| SAN | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.09% | low | low |
| BMY | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -1.52% | low | low |
| RY | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.57% | low | low |
| UNH | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -4.43% | low | low |
| RTX | Industrials | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +2.59% | low | low |
| ABT | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -1.56% | low | low |
| BP | Energy | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.84% | low | low |

## Bottom 15 (lowest pressure)

| Ticker | Sector | pressure | SPEC | QUAL | resid | beta |
|--------|--------|----------|------|------|-------|------|
| NCPL | Financial | -1.690 | 0.85 | 0.00 | +20.09% | high |
| BMBL | Communication Serv | -1.670 | 0.95 | 0.00 | +0.83% | high |
| ABEO | Healthcare | -1.630 | 0.85 | 0.00 | +0.99% | high |
| SLNH | Financial | -1.630 | 0.85 | 0.00 | -9.88% | high |
| KRUS | Consumer Cyclical | -1.630 | 0.85 | 0.00 | -1.43% | high |
| ASPI | Basic Materials | -1.630 | 0.85 | 0.00 | -10.05% | high |
| HRTX | Healthcare | -1.630 | 0.85 | 0.00 | +0.99% | high |
| ABAT | Industrials | -1.630 | 0.85 | 0.00 | -4.89% | high |
| VELO | Technology | -1.630 | 0.85 | 0.00 | -7.18% | high |
| KRRO | Healthcare | -1.630 | 0.85 | 0.00 | -2.08% | high |
| LVWR | Consumer Cyclical | -1.630 | 0.85 | 0.00 | +28.58% | high |
| ABR | Real Estate | -1.630 | 0.85 | 0.00 | -1.57% | high |
| PAL | Industrials | -1.630 | 0.85 | 0.00 | -3.24% | high |
| ARTV | Healthcare | -1.630 | 0.85 | 0.00 | -1.53% | high |
| DDD | Technology | -1.630 | 0.85 | 0.00 | -1.14% | high |

## Sector median pressure

| Sector | n | median pressure | median resid |
|--------|---|-----------------|--------------|
| Utilities | 103 | +0.120 | -0.47% |
| Energy | 252 | -0.205 | -0.06% |
| Financial | 7273 | -0.415 | +0.12% |
| Consumer Defensive | 239 | -0.465 | -0.18% |
| Industrials | 715 | -0.530 | -0.36% |
| Real Estate | 246 | -0.532 | -0.30% |
| Consumer Cyclical | 520 | -0.565 | -0.73% |
| Basic Materials | 298 | -0.573 | -0.09% |
| Communication Services | 252 | -0.700 | -0.67% |
| Technology | 799 | -0.710 | -0.89% |
| Healthcare | 1054 | -0.935 | -0.40% |

## Composite averages by size

| size | n | SPEC | QUAL | pressure |
|------|---|------|------|----------|
| large | 740 | 0.15 | 0.82 | +0.308 |
| mega | 159 | 0.13 | 0.85 | +0.499 |
| micro | 2313 | 0.52 | 0.27 | -0.958 |
| mid | 1100 | 0.34 | 0.53 | -0.309 |
| small | 1574 | 0.49 | 0.41 | -0.719 |
| unknown | 5865 | 0.32 | 0.25 | -0.377 |
