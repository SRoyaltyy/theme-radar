# Composite residual rank — **2026-10-26**

Generated: 2026-10-26T20:33:36.268008-04:00
Prior snapshot (for returns): **2026-10-23**

## Y snapshot (v1 — breadth only)

- **p_risk_on:** 0.6066 (from % names up)
- **pct_up:** 0.5926
- **median_ret:** 0.19%
- **conviction:** 0.2132
- **n:** 11771
- note: price_derived breadth only (v1)

## Method (deliberately simple)

- **residual** = stock return − median stock return (same pair window)
- **composites:** SPEC_DURATION, QUALITY_DEFENSIVE, CROWDING, SIZE_TILT
- **pressure** = conviction × prior effects of composites given p_risk_on
- Ranking is **cross-sectional residual bias**, not an absolute SPY call
- Hand priors only — replace with audit weights later

CSV: `data/composite/2026-10-26_composite_rank.csv`

## Top 20 by residual pressure (favor when risk-on / current Y)

| Ticker | Sector | pressure | SPEC | QUAL | CROWD | SIZE | resid | beta | short |
|--------|--------|----------|------|------|-------|------|-------|------|-------|
| KRRO | Healthcare | +0.081 | 0.95 | 0.00 | 0.80 | 1.00 | +0.15% | high | very_high |
| EAF | Industrials | +0.079 | 0.95 | 0.00 | 0.60 | 1.00 | +24.96% | high | elevated |
| INGN | Healthcare | +0.079 | 0.95 | 0.00 | 0.60 | 1.00 | -0.47% | high | elevated |
| GPUS | Industrials | +0.077 | 0.85 | 0.00 | 0.80 | 1.00 | +5.69% | high | very_high |
| BETR | Financial | +0.076 | 0.95 | 0.00 | 0.80 | 0.80 | +5.79% | high | very_high |
| BMBL | Communication Serv | +0.076 | 0.95 | 0.00 | 0.80 | 0.80 | -0.02% | high | very_high |
| PACB | Healthcare | +0.076 | 0.95 | 0.00 | 0.80 | 0.80 | +6.45% | high | very_high |
| TBI | Industrials | +0.075 | 0.95 | 0.00 | 0.35 | 1.00 | +5.06% | high | low |
| CNDT | Technology | +0.075 | 0.95 | 0.00 | 0.35 | 1.00 | -5.22% | high | low |
| EU | Energy | +0.074 | 0.85 | 0.00 | 0.60 | 1.00 | +2.67% | high | very_high |
| EYPT | Healthcare | +0.074 | 0.85 | 0.00 | 0.60 | 1.00 | -7.69% | high | very_high |
| VELO | Technology | +0.074 | 0.85 | 0.00 | 0.60 | 1.00 | -2.45% | high | very_high |
| AIRO | Industrials | +0.074 | 0.85 | 0.00 | 0.60 | 1.00 | +2.97% | high | very_high |
| ORGO | Healthcare | +0.074 | 0.85 | 0.00 | 0.60 | 1.00 | -5.24% | high | very_high |
| OCGN | Healthcare | +0.074 | 0.85 | 0.00 | 0.60 | 1.00 | -4.24% | high | very_high |
| PAL | Industrials | +0.074 | 0.85 | 0.00 | 0.60 | 1.00 | -6.09% | high | very_high |
| CATX | Healthcare | +0.074 | 0.85 | 0.00 | 0.60 | 1.00 | -25.03% | high | very_high |
| ABAT | Industrials | +0.074 | 0.85 | 0.00 | 0.60 | 1.00 | -5.37% | high | very_high |
| CABA | Healthcare | +0.074 | 0.85 | 0.00 | 0.60 | 1.00 | -8.35% | high | very_high |
| PDYN | Technology | +0.074 | 0.85 | 0.00 | 0.60 | 1.00 | +4.41% | high | very_high |

## Bottom 15 (lowest pressure)

| Ticker | Sector | pressure | SPEC | QUAL | resid | beta |
|--------|--------|----------|------|------|-------|------|
| VZ | Communication Serv | -0.034 | 0.00 | 1.00 | -3.68% | low |
| AMGN | Healthcare | -0.034 | 0.00 | 1.00 | +1.03% | low |
| MO | Consumer Defensive | -0.034 | 0.00 | 1.00 | -1.12% | low |
| PM | Consumer Defensive | -0.034 | 0.00 | 1.00 | +1.01% | low |
| KO | Consumer Defensive | -0.034 | 0.00 | 1.00 | -0.20% | low |
| PFE | Healthcare | -0.034 | 0.00 | 1.00 | -0.99% | low |
| TTE | Energy | -0.034 | 0.00 | 1.00 | +0.87% | low |
| SYK | Healthcare | -0.034 | 0.00 | 1.00 | -0.52% | low |
| EQNR | Energy | -0.034 | 0.00 | 1.00 | -1.66% | low |
| RTX | Industrials | -0.034 | 0.00 | 1.00 | +3.20% | low |
| JNJ | Healthcare | -0.034 | 0.00 | 1.00 | +0.76% | low |
| RY | Financial | -0.034 | 0.00 | 1.00 | +0.46% | low |
| T | Communication Serv | -0.034 | 0.00 | 1.00 | -0.57% | low |
| PEP | Consumer Defensive | -0.034 | 0.00 | 1.00 | -0.42% | low |
| PDD | Consumer Cyclical | -0.034 | 0.00 | 1.00 | -1.34% | low |

## Sector median pressure

| Sector | n | median pressure | median resid |
|--------|---|-----------------|--------------|
| Healthcare | 1053 | +0.041 | -0.35% |
| Technology | 801 | +0.032 | -0.19% |
| Communication Services | 253 | +0.032 | -1.35% |
| Basic Materials | 297 | +0.028 | -0.19% |
| Consumer Cyclical | 524 | +0.026 | -0.22% |
| Industrials | 714 | +0.024 | -0.03% |
| Real Estate | 248 | +0.023 | -0.19% |
| Consumer Defensive | 240 | +0.021 | -0.72% |
| Financial | 7282 | +0.019 | +0.06% |
| Energy | 252 | +0.009 | +0.21% |
| Utilities | 107 | -0.002 | -0.29% |

## Composite averages by size

| size | n | SPEC | QUAL | pressure |
|------|---|------|------|----------|
| large | 744 | 0.17 | 0.80 | -0.012 |
| mega | 165 | 0.15 | 0.83 | -0.021 |
| micro | 2263 | 0.52 | 0.28 | +0.043 |
| mid | 1116 | 0.36 | 0.52 | +0.016 |
| small | 1600 | 0.49 | 0.40 | +0.033 |
| unknown | 5883 | 0.32 | 0.24 | +0.017 |
