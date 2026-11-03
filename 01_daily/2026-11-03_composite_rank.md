# Composite residual rank — **2026-11-03**

Generated: 2026-11-03T17:20:13.229323-05:00
Prior snapshot (for returns): **2026-11-02**

## Y snapshot (v1 — breadth only)

- **p_risk_on:** 0.3177 (from % names up)
- **pct_up:** 0.4771
- **median_ret:** 0.00%
- **conviction:** 0.3647
- **n:** 11751
- note: price_derived breadth only (v1)

## Method (deliberately simple)

- **residual** = stock return − median stock return (same pair window)
- **composites:** SPEC_DURATION, QUALITY_DEFENSIVE, CROWDING, SIZE_TILT
- **pressure** = conviction × prior effects of composites given p_risk_on
- Ranking is **cross-sectional residual bias**, not an absolute SPY call
- Hand priors only — replace with audit weights later

CSV: `data/composite/2026-11-03_composite_rank.csv`

## Top 20 by residual pressure (favor when risk-on / current Y)

| Ticker | Sector | pressure | SPEC | QUAL | CROWD | SIZE | resid | beta | short |
|--------|--------|----------|------|------|-------|------|-------|------|-------|
| ABBV | Healthcare | +0.100 | 0.00 | 1.00 | 0.00 | 0.00 | -0.98% | low | low |
| V | Financial | +0.100 | 0.00 | 1.00 | 0.00 | 0.00 | -1.20% | low | low |
| AMGN | Healthcare | +0.100 | 0.00 | 1.00 | 0.00 | 0.00 | -0.90% | low | low |
| RY | Financial | +0.100 | 0.00 | 1.00 | 0.00 | 0.00 | -0.47% | low | low |
| BMY | Healthcare | +0.100 | 0.00 | 1.00 | 0.00 | 0.00 | -2.08% | low | low |
| RTX | Industrials | +0.100 | 0.00 | 1.00 | 0.00 | 0.00 | +0.51% | low | low |
| SO | Utilities | +0.100 | 0.00 | 1.00 | 0.00 | 0.00 | -0.91% | low | low |
| DHR | Healthcare | +0.100 | 0.00 | 1.00 | 0.00 | 0.00 | +0.94% | low | low |
| UL | Consumer Defensive | +0.100 | 0.00 | 1.00 | 0.00 | 0.00 | -2.45% | low | low |
| MCD | Consumer Cyclical | +0.100 | 0.00 | 1.00 | 0.00 | 0.00 | -0.98% | low | low |
| MCK | Healthcare | +0.100 | 0.00 | 1.00 | 0.00 | 0.00 | +0.12% | low | low |
| XOM | Energy | +0.100 | 0.00 | 1.00 | 0.00 | 0.00 | -1.23% | low | low |
| UNH | Healthcare | +0.100 | 0.00 | 1.00 | 0.00 | 0.00 | +1.00% | low | low |
| MA | Financial | +0.100 | 0.00 | 1.00 | 0.00 | 0.00 | -1.66% | low | low |
| BP | Energy | +0.100 | 0.00 | 1.00 | 0.00 | 0.00 | -0.61% | low | low |
| T | Communication Serv | +0.100 | 0.00 | 1.00 | 0.00 | 0.00 | -0.23% | low | low |
| BABA | Consumer Cyclical | +0.100 | 0.00 | 1.00 | 0.00 | 0.00 | -1.12% | low | low |
| HDB | Financial | +0.100 | 0.00 | 1.00 | 0.00 | 0.00 | +1.54% | low | low |
| MFG | Financial | +0.100 | 0.00 | 1.00 | 0.00 | 0.00 | -0.73% | low | low |
| BUD | Consumer Defensive | +0.100 | 0.00 | 1.00 | 0.00 | 0.00 | -3.36% | low | low |

## Bottom 15 (lowest pressure)

| Ticker | Sector | pressure | SPEC | QUAL | resid | beta |
|--------|--------|----------|------|------|-------|------|
| AIRS | Healthcare | -0.238 | 0.95 | 0.00 | -1.80% | high |
| KRRO | Healthcare | -0.238 | 0.95 | 0.00 | +0.06% | high |
| PAL | Industrials | -0.238 | 0.95 | 0.00 | -0.34% | high |
| CHPT | Consumer Cyclical | -0.238 | 0.95 | 0.00 | +9.21% | high |
| ACH | Healthcare | -0.230 | 0.95 | 0.00 | +7.69% | high |
| UPB | Healthcare | -0.230 | 0.95 | 0.00 | +1.19% | high |
| NMRA | Healthcare | -0.230 | 0.95 | 0.00 | +14.00% | high |
| INO | Healthcare | -0.225 | 0.85 | 0.00 | -12.17% | high |
| VCIG | Industrials | -0.225 | 0.85 | 0.00 | -30.27% | high |
| CRMT | Consumer Cyclical | -0.225 | 0.85 | 0.00 | +32.97% | high |
| WKHS | Consumer Cyclical | -0.225 | 0.85 | 0.00 | +10.14% | high |
| EVGO | Consumer Cyclical | -0.222 | 0.95 | 0.00 | -1.08% | high |
| REAL | Consumer Cyclical | -0.222 | 0.95 | 0.00 | -2.46% | high |
| TDOC | Healthcare | -0.222 | 0.95 | 0.00 | +3.01% | high |
| BMBL | Communication Serv | -0.222 | 0.95 | 0.00 | +0.17% | high |

## Sector median pressure

| Sector | n | median pressure | median resid |
|--------|---|-----------------|--------------|
| Utilities | 107 | +0.006 | -0.75% |
| Energy | 252 | -0.026 | -0.47% |
| Financial | 7264 | -0.055 | +0.00% |
| Consumer Defensive | 240 | -0.064 | -1.00% |
| Real Estate | 248 | -0.067 | -0.58% |
| Industrials | 712 | -0.073 | +0.16% |
| Consumer Cyclical | 522 | -0.075 | -1.08% |
| Basic Materials | 298 | -0.079 | -1.31% |
| Communication Services | 252 | -0.093 | +0.21% |
| Technology | 802 | -0.093 | +0.50% |
| Healthcare | 1054 | -0.124 | +0.69% |

## Composite averages by size

| size | n | SPEC | QUAL | pressure |
|------|---|------|------|----------|
| large | 761 | 0.17 | 0.80 | +0.037 |
| mega | 162 | 0.13 | 0.85 | +0.066 |
| micro | 2271 | 0.52 | 0.28 | -0.125 |
| mid | 1116 | 0.36 | 0.52 | -0.045 |
| small | 1589 | 0.49 | 0.41 | -0.096 |
| unknown | 5852 | 0.32 | 0.25 | -0.050 |
