# Composite residual rank — **2026-10-08**

Generated: 2026-10-08T17:41:10.244972-04:00
Prior snapshot (for returns): **2026-10-07**

## Y snapshot (v1 — breadth only)

- **p_risk_on:** 0.2454 (from % names up)
- **pct_up:** 0.4482
- **median_ret:** -0.03%
- **conviction:** 0.5092
- **n:** 11717
- note: price_derived breadth only (v1)

## Method (deliberately simple)

- **residual** = stock return − median stock return (same pair window)
- **composites:** SPEC_DURATION, QUALITY_DEFENSIVE, CROWDING, SIZE_TILT
- **pressure** = conviction × prior effects of composites given p_risk_on
- Ranking is **cross-sectional residual bias**, not an absolute SPY call
- Hand priors only — replace with audit weights later

CSV: `data/composite/2026-10-08_composite_rank.csv`

## Top 20 by residual pressure (favor when risk-on / current Y)

| Ticker | Sector | pressure | SPEC | QUAL | CROWD | SIZE | resid | beta | short |
|--------|--------|----------|------|------|-------|------|-------|------|-------|
| BUD | Consumer Defensive | +0.195 | 0.00 | 1.00 | 0.00 | 0.00 | +3.77% | low | low |
| BTI | Consumer Defensive | +0.195 | 0.00 | 1.00 | 0.00 | 0.00 | +2.87% | low | low |
| SAN | Financial | +0.195 | 0.00 | 1.00 | 0.00 | 0.00 | -1.29% | low | low |
| SCHW | Financial | +0.195 | 0.00 | 1.00 | 0.00 | 0.00 | +1.38% | low | low |
| BRK-A | Financial | +0.195 | 0.00 | 1.00 | 0.00 | 0.00 | +0.95% | low | low |
| ABT | Healthcare | +0.195 | 0.00 | 1.00 | 0.00 | 0.00 | -0.21% | low | low |
| BRK-B | Financial | +0.195 | 0.00 | 1.00 | 0.00 | 0.00 | +0.98% | low | low |
| JNJ | Healthcare | +0.195 | 0.00 | 1.00 | 0.00 | 0.00 | -0.73% | low | low |
| RTX | Industrials | +0.195 | 0.00 | 1.00 | 0.00 | 0.00 | +2.28% | low | low |
| SHEL | Energy | +0.195 | 0.00 | 1.00 | 0.00 | 0.00 | +3.49% | low | low |
| VRTX | Healthcare | +0.195 | 0.00 | 1.00 | 0.00 | 0.00 | -0.44% | low | low |
| VZ | Communication Serv | +0.195 | 0.00 | 1.00 | 0.00 | 0.00 | +1.30% | low | low |
| BP | Energy | +0.195 | 0.00 | 1.00 | 0.00 | 0.00 | +4.19% | low | low |
| PDD | Consumer Cyclical | +0.195 | 0.00 | 1.00 | 0.00 | 0.00 | -0.27% | low | low |
| BABA | Consumer Cyclical | +0.195 | 0.00 | 1.00 | 0.00 | 0.00 | -1.18% | low | low |
| PM | Consumer Defensive | +0.195 | 0.00 | 1.00 | 0.00 | 0.00 | +4.09% | low | low |
| MUFG | Financial | +0.195 | 0.00 | 1.00 | 0.00 | 0.00 | -0.72% | low | low |
| PEP | Consumer Defensive | +0.195 | 0.00 | 1.00 | 0.00 | 0.00 | +3.76% | low | low |
| NEM | Basic Materials | +0.195 | 0.00 | 1.00 | 0.00 | 0.00 | +1.80% | low | low |
| IBM | Technology | +0.195 | 0.00 | 1.00 | 0.00 | 0.00 | +2.80% | low | low |

## Bottom 15 (lowest pressure)

| Ticker | Sector | pressure | SPEC | QUAL | resid | beta |
|--------|--------|----------|------|------|-------|------|
| ADCT | Healthcare | -0.449 | 0.95 | 0.00 | +12.00% | high |
| RC | Real Estate | -0.449 | 0.95 | 0.00 | +7.35% | high |
| CRMT | Consumer Cyclical | -0.438 | 0.85 | 0.00 | +11.64% | high |
| PDSB | Healthcare | -0.423 | 0.85 | 0.00 | -4.64% | high |
| IPDN | Industrials | -0.423 | 0.85 | 0.00 | -2.29% | high |
| UNCY | Healthcare | -0.423 | 0.85 | 0.00 | -2.60% | high |
| NXH | Consumer Cyclical | -0.423 | 0.85 | 0.00 | -2.79% | high |
| VERI | Technology | -0.423 | 0.85 | 0.00 | -14.46% | high |
| BYRN | Industrials | -0.423 | 0.85 | 0.00 | +16.82% | high |
| TNXP | Healthcare | -0.423 | 0.85 | 0.00 | -3.54% | high |
| HUCK | Technology | -0.423 | 0.85 | 0.00 | -0.61% | high |
| QTEX | Technology | -0.423 | 0.85 | 0.00 | +1.84% | high |
| CRBP | Healthcare | -0.423 | 0.85 | 0.00 | -3.97% | high |
| CHPT | Consumer Cyclical | -0.423 | 0.85 | 0.00 | -1.06% | high |
| ACVA | Consumer Cyclical | -0.417 | 0.95 | 0.00 | +0.03% | high |

## Sector median pressure

| Sector | n | median pressure | median resid |
|--------|---|-----------------|--------------|
| Utilities | 107 | +0.012 | +0.29% |
| Energy | 251 | -0.053 | +1.54% |
| Financial | 7226 | -0.108 | -0.01% |
| Consumer Defensive | 241 | -0.117 | +0.94% |
| Real Estate | 247 | -0.131 | +0.70% |
| Industrials | 716 | -0.137 | -0.08% |
| Basic Materials | 294 | -0.143 | +0.13% |
| Consumer Cyclical | 528 | -0.146 | +0.36% |
| Communication Services | 256 | -0.181 | +0.03% |
| Technology | 798 | -0.181 | -1.03% |
| Healthcare | 1053 | -0.235 | -0.85% |

## Composite averages by size

| size | n | SPEC | QUAL | pressure |
|------|---|------|------|----------|
| large | 776 | 0.17 | 0.80 | +0.072 |
| mega | 159 | 0.14 | 0.84 | +0.125 |
| micro | 2211 | 0.51 | 0.29 | -0.241 |
| mid | 1124 | 0.36 | 0.52 | -0.086 |
| small | 1637 | 0.49 | 0.40 | -0.187 |
| unknown | 5810 | 0.32 | 0.25 | -0.098 |
