# Composite residual rank — **2026-10-21**

Generated: 2026-10-21T17:03:46.415787-04:00
Prior snapshot (for returns): **2026-10-20**

## Y snapshot (v1 — breadth only)

- **p_risk_on:** 0.6157 (from % names up)
- **pct_up:** 0.5963
- **median_ret:** 0.16%
- **conviction:** 0.2314
- **n:** 11768
- note: price_derived breadth only (v1)

## Method (deliberately simple)

- **residual** = stock return − median stock return (same pair window)
- **composites:** SPEC_DURATION, QUALITY_DEFENSIVE, CROWDING, SIZE_TILT
- **pressure** = conviction × prior effects of composites given p_risk_on
- Ranking is **cross-sectional residual bias**, not an absolute SPY call
- Hand priors only — replace with audit weights later

CSV: `data/composite/2026-10-21_composite_rank.csv`

## Top 20 by residual pressure (favor when risk-on / current Y)

| Ticker | Sector | pressure | SPEC | QUAL | CROWD | SIZE | resid | beta | short |
|--------|--------|----------|------|------|-------|------|-------|------|-------|
| CHPT | Consumer Cyclical | +0.096 | 0.95 | 0.00 | 0.80 | 1.00 | +6.99% | high | very_high |
| BETR | Financial | +0.096 | 0.95 | 0.00 | 0.80 | 1.00 | +29.99% | high | very_high |
| VENU | Consumer Cyclical | +0.093 | 0.95 | 0.00 | 0.60 | 1.00 | +14.84% | high | elevated |
| BDTX | Healthcare | +0.093 | 0.95 | 0.00 | 0.60 | 1.00 | +0.32% | high | elevated |
| DMRC | Technology | +0.093 | 0.95 | 0.00 | 0.60 | 1.00 | -3.53% | high | elevated |
| LHSW | Technology | +0.090 | 0.85 | 0.00 | 0.80 | 1.00 | +39.56% | high | very_high |
| SGMT | Healthcare | +0.089 | 0.95 | 0.00 | 0.80 | 0.80 | +2.40% | high | very_high |
| BMBL | Communication Serv | +0.089 | 0.95 | 0.00 | 0.80 | 0.80 | -0.16% | high | very_high |
| CDZI | Industrials | +0.089 | 0.95 | 0.00 | 0.80 | 0.80 | -0.91% | high | very_high |
| PRME | Healthcare | +0.089 | 0.95 | 0.00 | 0.80 | 0.80 | -2.97% | high | very_high |
| MAZE | Healthcare | +0.089 | 0.95 | 0.00 | 0.80 | 0.80 | +0.24% | high | very_high |
| CCCC | Healthcare | +0.089 | 0.95 | 0.00 | 0.80 | 0.80 | +0.15% | high | very_high |
| SLNH | Financial | +0.087 | 0.85 | 0.00 | 0.60 | 1.00 | -3.61% | high | very_high |
| UPLD | Technology | +0.087 | 0.85 | 0.00 | 0.60 | 1.00 | +9.45% | high | elevated |
| PDYN | Technology | +0.087 | 0.85 | 0.00 | 0.60 | 1.00 | +2.34% | high | very_high |
| OCGN | Healthcare | +0.087 | 0.85 | 0.00 | 0.60 | 1.00 | +1.07% | high | very_high |
| OLOX | Industrials | +0.087 | 0.85 | 0.00 | 0.60 | 1.00 | +36.32% | high | elevated |
| ORGO | Healthcare | +0.087 | 0.85 | 0.00 | 0.60 | 1.00 | -3.11% | high | very_high |
| WATT | Technology | +0.087 | 0.85 | 0.00 | 0.60 | 1.00 | +1.44% | high | very_high |
| PAL | Industrials | +0.087 | 0.85 | 0.00 | 0.60 | 1.00 | -3.36% | high | very_high |

## Bottom 15 (lowest pressure)

| Ticker | Sector | pressure | SPEC | QUAL | resid | beta |
|--------|--------|----------|------|------|-------|------|
| ABBV | Healthcare | -0.040 | 0.00 | 1.00 | -1.64% | low |
| BABA | Consumer Cyclical | -0.040 | 0.00 | 1.00 | -4.03% | low |
| NEE | Utilities | -0.040 | 0.00 | 1.00 | -0.90% | low |
| NEM | Basic Materials | -0.040 | 0.00 | 1.00 | +0.15% | low |
| BTI | Consumer Defensive | -0.040 | 0.00 | 1.00 | -0.52% | low |
| PFE | Healthcare | -0.040 | 0.00 | 1.00 | -1.03% | low |
| BUD | Consumer Defensive | -0.040 | 0.00 | 1.00 | -1.41% | low |
| LMT | Industrials | -0.040 | 0.00 | 1.00 | +0.35% | low |
| VZ | Communication Serv | -0.040 | 0.00 | 1.00 | -2.36% | low |
| ENB | Energy | -0.040 | 0.00 | 1.00 | +0.09% | low |
| AZN | Healthcare | -0.040 | 0.00 | 1.00 | -0.38% | low |
| KO | Consumer Defensive | -0.040 | 0.00 | 1.00 | -1.03% | low |
| TJX | Consumer Cyclical | -0.040 | 0.00 | 1.00 | -1.16% | low |
| RTX | Industrials | -0.040 | 0.00 | 1.00 | -1.06% | low |
| T | Communication Serv | -0.040 | 0.00 | 1.00 | -6.61% | low |

## Sector median pressure

| Sector | n | median pressure | median resid |
|--------|---|-----------------|--------------|
| Healthcare | 1053 | +0.050 | -0.29% |
| Technology | 799 | +0.037 | +0.92% |
| Communication Services | 255 | +0.037 | -0.61% |
| Basic Materials | 295 | +0.031 | -0.07% |
| Consumer Cyclical | 524 | +0.030 | -1.02% |
| Industrials | 716 | +0.029 | +0.52% |
| Real Estate | 248 | +0.028 | -0.87% |
| Consumer Defensive | 240 | +0.025 | -1.02% |
| Financial | 7279 | +0.022 | +0.04% |
| Energy | 252 | +0.011 | +0.15% |
| Utilities | 107 | -0.002 | -0.16% |

## Composite averages by size

| size | n | SPEC | QUAL | pressure |
|------|---|------|------|----------|
| large | 766 | 0.17 | 0.80 | -0.015 |
| mega | 162 | 0.15 | 0.84 | -0.025 |
| micro | 2267 | 0.52 | 0.28 | +0.050 |
| mid | 1119 | 0.36 | 0.52 | +0.018 |
| small | 1582 | 0.49 | 0.40 | +0.039 |
| unknown | 5872 | 0.32 | 0.25 | +0.020 |
