# Composite residual rank — **2026-10-07**

Generated: 2026-10-07T16:50:38.477415-04:00
Prior snapshot (for returns): **2026-10-06**

## Y snapshot (v1 — breadth only)

- **p_risk_on:** 0.0 (from % names up)
- **pct_up:** 0.213
- **median_ret:** -0.60%
- **conviction:** 1.0
- **n:** 11716
- note: price_derived breadth only (v1)

## Method (deliberately simple)

- **residual** = stock return − median stock return (same pair window)
- **composites:** SPEC_DURATION, QUALITY_DEFENSIVE, CROWDING, SIZE_TILT
- **pressure** = conviction × prior effects of composites given p_risk_on
- Ranking is **cross-sectional residual bias**, not an absolute SPY call
- Hand priors only — replace with audit weights later

CSV: `data/composite/2026-10-07_composite_rank.csv`

## Top 20 by residual pressure (favor when risk-on / current Y)

| Ticker | Sector | pressure | SPEC | QUAL | CROWD | SIZE | resid | beta | short |
|--------|--------|----------|------|------|-------|------|-------|------|-------|
| NVO | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +2.54% | low | low |
| ABBV | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +2.35% | low | low |
| PFE | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +2.41% | low | low |
| PGR | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.57% | low | low |
| TD | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -3.05% | low | low |
| MRK | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.20% | low | low |
| WMT | Consumer Defensive | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.49% | low | low |
| HSBC | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -3.37% | low | low |
| BUD | Consumer Defensive | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.73% | low | low |
| JNJ | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +2.04% | low | low |
| BRK-B | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.74% | low | low |
| UNH | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.51% | low | low |
| BMY | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.78% | low | low |
| PSX | Energy | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.27% | low | low |
| COP | Energy | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.98% | low | low |
| MCK | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.63% | low | low |
| AMGN | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +3.20% | low | low |
| T | Communication Serv | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.76% | low | low |
| PDD | Consumer Cyclical | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.72% | low | low |
| PG | Consumer Defensive | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.20% | low | low |

## Bottom 15 (lowest pressure)

| Ticker | Sector | pressure | SPEC | QUAL | resid | beta |
|--------|--------|----------|------|------|-------|------|
| HRTX | Healthcare | -1.790 | 0.95 | 0.00 | +15.75% | high |
| PACB | Healthcare | -1.670 | 0.95 | 0.00 | +1.34% | high |
| PRME | Healthcare | -1.670 | 0.95 | 0.00 | +12.03% | high |
| HTZ | Industrials | -1.670 | 0.95 | 0.00 | +1.08% | high |
| ATOS | Healthcare | -1.630 | 0.85 | 0.00 | +1.00% | high |
| QTEX | Technology | -1.630 | 0.85 | 0.00 | +5.00% | high |
| HUCK | Technology | -1.630 | 0.85 | 0.00 | +0.28% | high |
| NCPL | Financial | -1.630 | 0.85 | 0.00 | +46.47% | high |
| IPSC | Healthcare | -1.630 | 0.85 | 0.00 | -2.43% | high |
| OM | Healthcare | -1.630 | 0.85 | 0.00 | +2.29% | high |
| IPDN | Industrials | -1.630 | 0.85 | 0.00 | -5.91% | high |
| CRBP | Healthcare | -1.630 | 0.85 | 0.00 | -4.42% | high |
| BYRN | Industrials | -1.630 | 0.85 | 0.00 | +10.35% | high |
| VERI | Technology | -1.630 | 0.85 | 0.00 | -7.40% | high |
| PDSB | Healthcare | -1.630 | 0.85 | 0.00 | +3.48% | high |

## Sector median pressure

| Sector | n | median pressure | median resid |
|--------|---|-----------------|--------------|
| Utilities | 107 | +0.045 | +0.26% |
| Energy | 251 | -0.180 | -0.26% |
| Financial | 7225 | -0.415 | +0.10% |
| Consumer Defensive | 241 | -0.450 | +0.60% |
| Real Estate | 247 | -0.505 | -0.75% |
| Industrials | 716 | -0.550 | -1.20% |
| Basic Materials | 294 | -0.560 | -1.89% |
| Consumer Cyclical | 528 | -0.565 | -0.29% |
| Communication Services | 256 | -0.700 | +0.60% |
| Technology | 798 | -0.700 | -0.58% |
| Healthcare | 1053 | -0.905 | +0.11% |

## Composite averages by size

| size | n | SPEC | QUAL | pressure |
|------|---|------|------|----------|
| large | 768 | 0.17 | 0.79 | +0.271 |
| mega | 159 | 0.15 | 0.83 | +0.473 |
| micro | 2209 | 0.51 | 0.29 | -0.930 |
| mid | 1133 | 0.36 | 0.52 | -0.334 |
| small | 1638 | 0.49 | 0.40 | -0.720 |
| unknown | 5809 | 0.32 | 0.24 | -0.385 |
