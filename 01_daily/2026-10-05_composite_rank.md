# Composite residual rank — **2026-10-05**

Generated: 2026-10-05T17:02:49.969816-04:00
Prior snapshot (for returns): **2026-10-02**

## Y snapshot (v1 — breadth only)

- **p_risk_on:** 0.6039 (from % names up)
- **pct_up:** 0.5916
- **median_ret:** 0.18%
- **conviction:** 0.2078
- **n:** 11703
- note: price_derived breadth only (v1)

## Method (deliberately simple)

- **residual** = stock return − median stock return (same pair window)
- **composites:** SPEC_DURATION, QUALITY_DEFENSIVE, CROWDING, SIZE_TILT
- **pressure** = conviction × prior effects of composites given p_risk_on
- Ranking is **cross-sectional residual bias**, not an absolute SPY call
- Hand priors only — replace with audit weights later

CSV: `data/composite/2026-10-05_composite_rank.csv`

## Top 20 by residual pressure (favor when risk-on / current Y)

| Ticker | Sector | pressure | SPEC | QUAL | CROWD | SIZE | resid | beta | short |
|--------|--------|----------|------|------|-------|------|-------|------|-------|
| HRTX | Healthcare | +0.077 | 0.95 | 0.00 | 0.80 | 1.00 | +5.53% | high | very_high |
| DMRC | Technology | +0.075 | 0.95 | 0.00 | 0.60 | 1.00 | -4.27% | high | elevated |
| TNON | Healthcare | +0.073 | 0.85 | 0.00 | 0.80 | 1.00 | -0.18% | high | very_high |
| BIRD | Technology | +0.073 | 0.85 | 0.00 | 0.80 | 1.00 | +1.00% | high | very_high |
| ABSI | Healthcare | +0.072 | 0.95 | 0.00 | 0.80 | 0.80 | +3.97% | high | very_high |
| PACB | Healthcare | +0.072 | 0.95 | 0.00 | 0.80 | 0.80 | +12.81% | high | very_high |
| WOLF | Technology | +0.072 | 0.95 | 0.00 | 0.80 | 0.80 | -5.14% | high | very_high |
| CERT | Healthcare | +0.072 | 0.95 | 0.00 | 0.80 | 0.80 | +7.40% | high | very_high |
| SXTP | Healthcare | +0.070 | 0.85 | 0.00 | 0.60 | 1.00 | +3.41% | high | elevated |
| TEAD | Communication Serv | +0.070 | 0.85 | 0.00 | 0.60 | 1.00 | +1.60% | high | elevated |
| HUCK | Technology | +0.070 | 0.85 | 0.00 | 0.60 | 1.00 | -0.50% | high | very_high |
| QSI | Healthcare | +0.070 | 0.85 | 0.00 | 0.60 | 1.00 | -17.60% | high | elevated |
| EYPT | Healthcare | +0.070 | 0.85 | 0.00 | 0.60 | 1.00 | -3.26% | high | very_high |
| TNXP | Healthcare | +0.070 | 0.85 | 0.00 | 0.60 | 1.00 | -9.61% | high | very_high |
| OM | Healthcare | +0.070 | 0.85 | 0.00 | 0.60 | 1.00 | +3.35% | high | elevated |
| CRBP | Healthcare | +0.070 | 0.85 | 0.00 | 0.60 | 1.00 | -4.75% | high | very_high |
| NXH | Consumer Cyclical | +0.070 | 0.85 | 0.00 | 0.60 | 1.00 | -25.55% | high | very_high |
| ORGO | Healthcare | +0.070 | 0.85 | 0.00 | 0.60 | 1.00 | -3.19% | high | very_high |
| IPSC | Healthcare | +0.070 | 0.85 | 0.00 | 0.60 | 1.00 | -3.45% | high | very_high |
| QTEX | Technology | +0.070 | 0.85 | 0.00 | 0.60 | 1.00 | +39.82% | high | elevated |

## Bottom 15 (lowest pressure)

| Ticker | Sector | pressure | SPEC | QUAL | resid | beta |
|--------|--------|----------|------|------|-------|------|
| ABBV | Healthcare | -0.032 | 0.00 | 1.00 | +0.94% | low |
| TJX | Consumer Cyclical | -0.032 | 0.00 | 1.00 | +1.12% | low |
| CVX | Energy | -0.032 | 0.00 | 1.00 | -0.29% | low |
| TM | Consumer Cyclical | -0.032 | 0.00 | 1.00 | +1.27% | low |
| TMUS | Communication Serv | -0.032 | 0.00 | 1.00 | +0.43% | low |
| MFG | Financial | -0.032 | 0.00 | 1.00 | +1.10% | low |
| MDT | Healthcare | -0.032 | 0.00 | 1.00 | +1.66% | low |
| PGR | Financial | -0.032 | 0.00 | 1.00 | +0.92% | low |
| PG | Consumer Defensive | -0.032 | 0.00 | 1.00 | +0.53% | low |
| VZ | Communication Serv | -0.032 | 0.00 | 1.00 | -0.34% | low |
| PFE | Healthcare | -0.032 | 0.00 | 1.00 | -1.59% | low |
| PDD | Consumer Cyclical | -0.032 | 0.00 | 1.00 | +3.16% | low |
| MCK | Healthcare | -0.032 | 0.00 | 1.00 | +1.28% | low |
| VRTX | Healthcare | -0.032 | 0.00 | 1.00 | -0.43% | low |
| DHR | Healthcare | -0.032 | 0.00 | 1.00 | +3.16% | low |

## Sector median pressure

| Sector | n | median pressure | median resid |
|--------|---|-----------------|--------------|
| Healthcare | 1052 | +0.040 | +0.23% |
| Technology | 797 | +0.030 | -0.18% |
| Communication Services | 255 | +0.030 | +0.16% |
| Consumer Cyclical | 528 | +0.024 | -0.43% |
| Basic Materials | 293 | +0.024 | +0.17% |
| Industrials | 716 | +0.024 | -0.36% |
| Real Estate | 247 | +0.022 | -0.98% |
| Consumer Defensive | 241 | +0.019 | -0.18% |
| Financial | 7216 | +0.018 | +0.03% |
| Energy | 251 | +0.009 | +0.88% |
| Utilities | 107 | -0.002 | -0.42% |

## Composite averages by size

| size | n | SPEC | QUAL | pressure |
|------|---|------|------|----------|
| large | 774 | 0.17 | 0.79 | -0.011 |
| mega | 159 | 0.15 | 0.83 | -0.020 |
| micro | 2202 | 0.52 | 0.29 | +0.040 |
| mid | 1136 | 0.36 | 0.51 | +0.015 |
| small | 1631 | 0.49 | 0.40 | +0.031 |
| unknown | 5801 | 0.32 | 0.24 | +0.017 |
