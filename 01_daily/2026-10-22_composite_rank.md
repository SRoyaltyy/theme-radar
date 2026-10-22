# Composite residual rank — **2026-10-22**

Generated: 2026-10-22T16:53:44.066303-04:00
Prior snapshot (for returns): **2026-10-21**

## Y snapshot (v1 — breadth only)

- **p_risk_on:** 0.1486 (from % names up)
- **pct_up:** 0.4094
- **median_ret:** -0.28%
- **conviction:** 0.7028
- **n:** 11772
- note: price_derived breadth only (v1)

## Method (deliberately simple)

- **residual** = stock return − median stock return (same pair window)
- **composites:** SPEC_DURATION, QUALITY_DEFENSIVE, CROWDING, SIZE_TILT
- **pressure** = conviction × prior effects of composites given p_risk_on
- Ranking is **cross-sectional residual bias**, not an absolute SPY call
- Hand priors only — replace with audit weights later

CSV: `data/composite/2026-10-22_composite_rank.csv`

## Top 20 by residual pressure (favor when risk-on / current Y)

| Ticker | Sector | pressure | SPEC | QUAL | CROWD | SIZE | resid | beta | short |
|--------|--------|----------|------|------|-------|------|-------|------|-------|
| ABBV | Healthcare | +0.370 | 0.00 | 1.00 | 0.00 | 0.00 | +0.42% | low | low |
| VRTX | Healthcare | +0.370 | 0.00 | 1.00 | 0.00 | 0.00 | +2.31% | low | low |
| PDD | Consumer Cyclical | +0.370 | 0.00 | 1.00 | 0.00 | 0.00 | +0.85% | low | low |
| BP | Energy | +0.370 | 0.00 | 1.00 | 0.00 | 0.00 | +0.68% | low | low |
| PM | Consumer Defensive | +0.370 | 0.00 | 1.00 | 0.00 | 0.00 | +2.45% | low | low |
| PGR | Financial | +0.370 | 0.00 | 1.00 | 0.00 | 0.00 | +4.02% | low | low |
| EQNR | Energy | +0.370 | 0.00 | 1.00 | 0.00 | 0.00 | +0.93% | low | low |
| HSBC | Financial | +0.370 | 0.00 | 1.00 | 0.00 | 0.00 | -1.86% | low | low |
| PEP | Consumer Defensive | +0.370 | 0.00 | 1.00 | 0.00 | 0.00 | +3.35% | low | low |
| GSK | Healthcare | +0.370 | 0.00 | 1.00 | 0.00 | 0.00 | +2.66% | low | low |
| SCHW | Financial | +0.370 | 0.00 | 1.00 | 0.00 | 0.00 | +0.06% | low | low |
| NVO | Healthcare | +0.370 | 0.00 | 1.00 | 0.00 | 0.00 | +1.23% | low | low |
| SAN | Financial | +0.370 | 0.00 | 1.00 | 0.00 | 0.00 | -2.65% | low | low |
| AMGN | Healthcare | +0.370 | 0.00 | 1.00 | 0.00 | 0.00 | +2.32% | low | low |
| BMY | Healthcare | +0.370 | 0.00 | 1.00 | 0.00 | 0.00 | +3.36% | low | low |
| RTX | Industrials | +0.370 | 0.00 | 1.00 | 0.00 | 0.00 | +1.90% | low | low |
| ENB | Energy | +0.370 | 0.00 | 1.00 | 0.00 | 0.00 | +0.28% | low | low |
| AZN | Healthcare | +0.370 | 0.00 | 1.00 | 0.00 | 0.00 | +2.73% | low | low |
| BABA | Consumer Cyclical | +0.370 | 0.00 | 1.00 | 0.00 | 0.00 | -2.20% | low | low |
| MPC | Energy | +0.370 | 0.00 | 1.00 | 0.00 | 0.00 | -1.58% | low | low |

## Bottom 15 (lowest pressure)

| Ticker | Sector | pressure | SPEC | QUAL | resid | beta |
|--------|--------|----------|------|------|-------|------|
| KRRO | Healthcare | -0.884 | 0.95 | 0.00 | +29.99% | high |
| TBCH | Technology | -0.884 | 0.95 | 0.00 | +1.26% | high |
| INGN | Healthcare | -0.855 | 0.95 | 0.00 | +5.83% | high |
| LHSW | Technology | -0.835 | 0.85 | 0.00 | -32.07% | high |
| SGMT | Healthcare | -0.825 | 0.95 | 0.00 | -0.12% | high |
| BMBL | Communication Serv | -0.825 | 0.95 | 0.00 | +0.11% | high |
| BETR | Financial | -0.825 | 0.95 | 0.00 | +6.70% | high |
| YMAT | Basic Materials | -0.805 | 0.85 | 0.00 | -14.76% | high |
| ADIL | Healthcare | -0.805 | 0.85 | 0.00 | +2.96% | high |
| OCGN | Healthcare | -0.805 | 0.85 | 0.00 | -3.38% | high |
| ATOM | Technology | -0.805 | 0.85 | 0.00 | +2.27% | high |
| XHLD | Communication Serv | -0.805 | 0.85 | 0.00 | -12.91% | high |
| EYPT | Healthcare | -0.805 | 0.85 | 0.00 | +0.28% | high |
| ABAT | Industrials | -0.805 | 0.85 | 0.00 | -4.51% | high |
| WATT | Technology | -0.805 | 0.85 | 0.00 | +0.17% | high |

## Sector median pressure

| Sector | n | median pressure | median resid |
|--------|---|-----------------|--------------|
| Utilities | 107 | +0.022 | +2.30% |
| Energy | 252 | -0.101 | -0.95% |
| Financial | 7282 | -0.205 | -0.03% |
| Consumer Defensive | 240 | -0.236 | +2.17% |
| Real Estate | 248 | -0.249 | +2.64% |
| Industrials | 716 | -0.277 | -0.59% |
| Consumer Cyclical | 524 | -0.281 | +1.53% |
| Basic Materials | 295 | -0.299 | -3.02% |
| Communication Services | 255 | -0.346 | +0.28% |
| Technology | 800 | -0.351 | -1.67% |
| Healthcare | 1053 | -0.447 | +0.16% |

## Composite averages by size

| size | n | SPEC | QUAL | pressure |
|------|---|------|------|----------|
| large | 753 | 0.18 | 0.79 | +0.122 |
| mega | 164 | 0.16 | 0.82 | +0.212 |
| micro | 2261 | 0.51 | 0.28 | -0.462 |
| mid | 1131 | 0.36 | 0.51 | -0.175 |
| small | 1590 | 0.49 | 0.40 | -0.358 |
| unknown | 5873 | 0.32 | 0.24 | -0.189 |
