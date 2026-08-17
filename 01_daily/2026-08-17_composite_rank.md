# Composite residual rank — **2026-08-17**

Generated: 2026-08-17T17:44:50.457918-04:00
Prior snapshot (for returns): **2026-08-14**

## Y snapshot (v1 — breadth only)

- **p_risk_on:** 0.0 (from % names up)
- **pct_up:** 0.3248
- **median_ret:** -0.22%
- **conviction:** 1.0
- **n:** 11573
- note: price_derived breadth only (v1)

## Method (deliberately simple)

- **residual** = stock return − median stock return (same pair window)
- **composites:** SPEC_DURATION, QUALITY_DEFENSIVE, CROWDING, SIZE_TILT
- **pressure** = conviction × prior effects of composites given p_risk_on
- Ranking is **cross-sectional residual bias**, not an absolute SPY call
- Hand priors only — replace with audit weights later

CSV: `data/composite/2026-08-17_composite_rank.csv`

## Top 20 by residual pressure (favor when risk-on / current Y)

| Ticker | Sector | pressure | SPEC | QUAL | CROWD | SIZE | resid | beta | short |
|--------|--------|----------|------|------|-------|------|-------|------|-------|
| TTE | Energy | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.56% | low | low |
| LMT | Industrials | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -2.24% | low | low |
| TJX | Consumer Cyclical | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.61% | low | low |
| PEP | Consumer Defensive | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -1.60% | low | low |
| MDT | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.52% | low | low |
| RY | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.04% | low | low |
| LLY | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.47% | low | low |
| MFG | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.15% | low | low |
| PM | Consumer Defensive | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -2.87% | low | low |
| COP | Energy | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.83% | low | low |
| HSBC | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.23% | low | low |
| UL | Consumer Defensive | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -1.17% | low | low |
| RTX | Industrials | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.38% | low | low |
| T | Communication Serv | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.63% | low | low |
| VRTX | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +2.15% | low | low |
| HDB | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.73% | low | low |
| SAN | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.94% | low | low |
| SYK | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -2.00% | low | low |
| GSK | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.75% | low | low |
| MCK | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.83% | low | low |

## Bottom 15 (lowest pressure)

| Ticker | Sector | pressure | SPEC | QUAL | resid | beta |
|--------|--------|----------|------|------|-------|------|
| ZENA | Technology | -1.790 | 0.95 | 0.00 | -3.99% | high |
| CD | Financial | -1.730 | 0.95 | 0.00 | -10.90% | high |
| INO | Healthcare | -1.690 | 0.85 | 0.00 | +5.72% | high |
| LASE | Industrials | -1.690 | 0.85 | 0.00 | -1.81% | high |
| WYFI | Technology | -1.670 | 0.95 | 0.00 | +3.03% | high |
| BTBT | Financial | -1.670 | 0.95 | 0.00 | +2.13% | high |
| MRAM | Technology | -1.670 | 0.95 | 0.00 | +5.35% | high |
| SGMT | Healthcare | -1.670 | 0.95 | 0.00 | -0.92% | high |
| FDMT | Healthcare | -1.670 | 0.95 | 0.00 | +19.58% | high |
| INDI | Technology | -1.670 | 0.95 | 0.00 | +0.22% | high |
| VELO | Technology | -1.670 | 0.95 | 0.00 | -3.25% | high |
| METC | Basic Materials | -1.670 | 0.95 | 0.00 | +0.05% | high |
| ACHV | Healthcare | -1.670 | 0.95 | 0.00 | -0.97% | high |
| SMRT | Technology | -1.655 | 0.95 | 0.00 | -0.46% | high |
| AGPU | Technology | -1.630 | 0.85 | 0.00 | +28.63% | high |

## Sector median pressure

| Sector | n | median pressure | median resid |
|--------|---|-----------------|--------------|
| Utilities | 110 | +0.045 | -0.42% |
| Energy | 253 | -0.160 | +0.99% |
| Financial | 7075 | -0.415 | +0.06% |
| Real Estate | 252 | -0.455 | -0.52% |
| Consumer Defensive | 244 | -0.485 | -1.33% |
| Industrials | 708 | -0.530 | -0.47% |
| Basic Materials | 286 | -0.555 | +0.22% |
| Consumer Cyclical | 533 | -0.565 | -1.04% |
| Communication Services | 258 | -0.700 | -1.12% |
| Technology | 790 | -0.700 | -1.42% |
| Healthcare | 1064 | -0.835 | -0.05% |

## Composite averages by size

| size | n | SPEC | QUAL | pressure |
|------|---|------|------|----------|
| large | 803 | 0.18 | 0.79 | +0.264 |
| mega | 170 | 0.15 | 0.84 | +0.470 |
| micro | 2142 | 0.51 | 0.30 | -0.921 |
| mid | 1174 | 0.36 | 0.51 | -0.340 |
| small | 1609 | 0.49 | 0.41 | -0.712 |
| unknown | 5675 | 0.32 | 0.25 | -0.381 |
