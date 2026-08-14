# Composite residual rank — **2026-08-14**

Generated: 2026-08-14T17:44:21.920787-04:00
Prior snapshot (for returns): **2026-08-13**

## Y snapshot (v1 — breadth only)

- **p_risk_on:** 0.2408 (from % names up)
- **pct_up:** 0.4463
- **median_ret:** 0.00%
- **conviction:** 0.5184
- **n:** 11586
- note: price_derived breadth only (v1)

## Method (deliberately simple)

- **residual** = stock return − median stock return (same pair window)
- **composites:** SPEC_DURATION, QUALITY_DEFENSIVE, CROWDING, SIZE_TILT
- **pressure** = conviction × prior effects of composites given p_risk_on
- Ranking is **cross-sectional residual bias**, not an absolute SPY call
- Hand priors only — replace with audit weights later

CSV: `data/composite/2026-08-14_composite_rank.csv`

## Top 20 by residual pressure (favor when risk-on / current Y)

| Ticker | Sector | pressure | SPEC | QUAL | CROWD | SIZE | resid | beta | short |
|--------|--------|----------|------|------|-------|------|-------|------|-------|
| BMY | Healthcare | +0.202 | 0.00 | 1.00 | 0.00 | 0.00 | -1.27% | low | low |
| ABBV | Healthcare | +0.202 | 0.00 | 1.00 | 0.00 | 0.00 | -0.54% | low | low |
| IBN | Financial | +0.202 | 0.00 | 1.00 | 0.00 | 0.00 | +0.88% | low | low |
| IBM | Technology | +0.202 | 0.00 | 1.00 | 0.00 | 0.00 | -1.19% | low | low |
| VRTX | Healthcare | +0.202 | 0.00 | 1.00 | 0.00 | 0.00 | -2.07% | low | low |
| XOM | Energy | +0.202 | 0.00 | 1.00 | 0.00 | 0.00 | +0.94% | low | low |
| GD | Industrials | +0.202 | 0.00 | 1.00 | 0.00 | 0.00 | +0.72% | low | low |
| SNY | Healthcare | +0.202 | 0.00 | 1.00 | 0.00 | 0.00 | -0.14% | low | low |
| MA | Financial | +0.202 | 0.00 | 1.00 | 0.00 | 0.00 | +0.40% | low | low |
| TMUS | Communication Serv | +0.202 | 0.00 | 1.00 | 0.00 | 0.00 | -0.42% | low | low |
| VZ | Communication Serv | +0.202 | 0.00 | 1.00 | 0.00 | 0.00 | +0.54% | low | low |
| PGR | Financial | +0.202 | 0.00 | 1.00 | 0.00 | 0.00 | +0.35% | low | low |
| PG | Consumer Defensive | +0.202 | 0.00 | 1.00 | 0.00 | 0.00 | +0.20% | low | low |
| MO | Consumer Defensive | +0.202 | 0.00 | 1.00 | 0.00 | 0.00 | +0.95% | low | low |
| BABA | Consumer Cyclical | +0.202 | 0.00 | 1.00 | 0.00 | 0.00 | +1.35% | low | low |
| HSBC | Financial | +0.202 | 0.00 | 1.00 | 0.00 | 0.00 | -0.25% | low | low |
| SHEL | Energy | +0.202 | 0.00 | 1.00 | 0.00 | 0.00 | +0.61% | low | low |
| V | Financial | +0.202 | 0.00 | 1.00 | 0.00 | 0.00 | -0.36% | low | low |
| TD | Financial | +0.202 | 0.00 | 1.00 | 0.00 | 0.00 | +1.02% | low | low |
| PFE | Healthcare | +0.202 | 0.00 | 1.00 | 0.00 | 0.00 | -0.04% | low | low |

## Bottom 15 (lowest pressure)

| Ticker | Sector | pressure | SPEC | QUAL | resid | beta |
|--------|--------|----------|------|------|-------|------|
| ZENA | Technology | -0.481 | 0.95 | 0.00 | +0.47% | high |
| ARCT | Healthcare | -0.481 | 0.95 | 0.00 | +4.71% | high |
| PROP | Energy | -0.454 | 0.85 | 0.00 | +19.05% | high |
| INO | Healthcare | -0.454 | 0.85 | 0.00 | +21.11% | high |
| LASE | Industrials | -0.454 | 0.85 | 0.00 | +8.03% | high |
| SGMT | Healthcare | -0.449 | 0.95 | 0.00 | +13.69% | high |
| RCAT | Industrials | -0.449 | 0.95 | 0.00 | +8.80% | high |
| CARL | Healthcare | -0.449 | 0.95 | 0.00 | +2.36% | high |
| ACHV | Healthcare | -0.449 | 0.95 | 0.00 | +4.69% | high |
| UMAC | Technology | -0.449 | 0.95 | 0.00 | +25.04% | high |
| JBIO | Healthcare | -0.449 | 0.95 | 0.00 | +3.78% | high |
| SMRT | Technology | -0.445 | 0.95 | 0.00 | +3.47% | high |
| SST | Industrials | -0.438 | 0.85 | 0.00 | +38.24% | high |
| RRGB | Consumer Cyclical | -0.438 | 0.85 | 0.00 | +2.42% | high |
| RCEL | Healthcare | -0.438 | 0.85 | 0.00 | -2.00% | high |

## Sector median pressure

| Sector | n | median pressure | median resid |
|--------|---|-----------------|--------------|
| Utilities | 109 | +0.012 | +0.22% |
| Energy | 253 | -0.048 | +1.55% |
| Financial | 7085 | -0.112 | -0.03% |
| Real Estate | 253 | -0.122 | -0.10% |
| Consumer Defensive | 244 | -0.123 | +0.00% |
| Industrials | 708 | -0.142 | +0.19% |
| Consumer Cyclical | 533 | -0.152 | +0.00% |
| Basic Materials | 288 | -0.156 | +0.69% |
| Communication Services | 259 | -0.188 | +0.11% |
| Technology | 790 | -0.188 | -0.30% |
| Healthcare | 1064 | -0.233 | +0.00% |

## Composite averages by size

| size | n | SPEC | QUAL | pressure |
|------|---|------|------|----------|
| large | 808 | 0.18 | 0.79 | +0.072 |
| mega | 169 | 0.15 | 0.83 | +0.124 |
| micro | 2145 | 0.51 | 0.30 | -0.247 |
| mid | 1175 | 0.36 | 0.51 | -0.093 |
| small | 1613 | 0.49 | 0.40 | -0.193 |
| unknown | 5676 | 0.32 | 0.24 | -0.105 |
