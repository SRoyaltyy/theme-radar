# Composite residual rank — **2026-08-19**

Generated: 2026-08-19T17:45:06.569581-04:00
Prior snapshot (for returns): **2026-08-18**

## Y snapshot (v1 — breadth only)

- **p_risk_on:** 0.6761 (from % names up)
- **pct_up:** 0.6204
- **median_ret:** 0.22%
- **conviction:** 0.3522
- **n:** 11600
- note: price_derived breadth only (v1)

## Method (deliberately simple)

- **residual** = stock return − median stock return (same pair window)
- **composites:** SPEC_DURATION, QUALITY_DEFENSIVE, CROWDING, SIZE_TILT
- **pressure** = conviction × prior effects of composites given p_risk_on
- Ranking is **cross-sectional residual bias**, not an absolute SPY call
- Hand priors only — replace with audit weights later

CSV: `data/composite/2026-08-19_composite_rank.csv`

## Top 20 by residual pressure (favor when risk-on / current Y)

| Ticker | Sector | pressure | SPEC | QUAL | CROWD | SIZE | resid | beta | short |
|--------|--------|----------|------|------|-------|------|-------|------|-------|
| ARCT | Healthcare | +0.222 | 0.95 | 0.00 | 0.80 | 1.00 | +24.99% | high | very_high |
| GDC | Communication Serv | +0.215 | 0.95 | 0.00 | 0.60 | 1.00 | +17.43% | high | elevated |
| INO | Healthcare | +0.210 | 0.85 | 0.00 | 0.80 | 1.00 | +8.11% | high | very_high |
| BTCT | Technology | +0.210 | 0.85 | 0.00 | 0.80 | 1.00 | +82.39% | high | very_high |
| MSS | Consumer Defensive | +0.210 | 0.85 | 0.00 | 0.80 | 1.00 | +18.25% | high | very_high |
| FDMT | Healthcare | +0.207 | 0.95 | 0.00 | 0.80 | 0.80 | +13.64% | high | very_high |
| ACHV | Healthcare | +0.207 | 0.95 | 0.00 | 0.80 | 0.80 | +13.21% | high | very_high |
| DSGN | Healthcare | +0.207 | 0.95 | 0.00 | 0.80 | 0.80 | +4.17% | high | very_high |
| SGMT | Healthcare | +0.207 | 0.95 | 0.00 | 0.80 | 0.80 | -0.22% | high | very_high |
| SDGR | Healthcare | +0.207 | 0.95 | 0.00 | 0.80 | 0.80 | +12.12% | high | very_high |
| HRTX | Healthcare | +0.202 | 0.85 | 0.00 | 0.60 | 1.00 | +3.11% | high | very_high |
| MYO | Healthcare | +0.202 | 0.85 | 0.00 | 0.60 | 1.00 | +10.49% | high | elevated |
| ADIL | Healthcare | +0.202 | 0.85 | 0.00 | 0.60 | 1.00 | +5.47% | high | elevated |
| AGPU | Technology | +0.202 | 0.85 | 0.00 | 0.60 | 1.00 | +5.30% | high | elevated |
| NAKA | Financial | +0.202 | 0.85 | 0.00 | 0.60 | 1.00 | +20.74% | high | elevated |
| XGN | Healthcare | +0.202 | 0.85 | 0.00 | 0.60 | 1.00 | +12.53% | high | elevated |
| AIFC | Technology | +0.202 | 0.85 | 0.00 | 0.60 | 1.00 | +10.42% | high | elevated |
| EXOD | Technology | +0.202 | 0.85 | 0.00 | 0.60 | 1.00 | +14.63% | high | elevated |
| VERI | Technology | +0.202 | 0.85 | 0.00 | 0.60 | 1.00 | -3.22% | high | very_high |
| PEPG | Healthcare | +0.202 | 0.85 | 0.00 | 0.60 | 1.00 | +4.59% | high | elevated |

## Bottom 15 (lowest pressure)

| Ticker | Sector | pressure | SPEC | QUAL | resid | beta |
|--------|--------|----------|------|------|-------|------|
| ABBV | Healthcare | -0.093 | 0.00 | 1.00 | +2.50% | low |
| T | Communication Serv | -0.093 | 0.00 | 1.00 | +0.66% | low |
| MUFG | Financial | -0.093 | 0.00 | 1.00 | -5.33% | low |
| SO | Utilities | -0.093 | 0.00 | 1.00 | -0.09% | low |
| SNY | Healthcare | -0.093 | 0.00 | 1.00 | +1.69% | low |
| SMFG | Financial | -0.093 | 0.00 | 1.00 | -5.02% | low |
| KO | Consumer Defensive | -0.093 | 0.00 | 1.00 | +1.50% | low |
| CVX | Energy | -0.093 | 0.00 | 1.00 | -0.21% | low |
| TM | Consumer Cyclical | -0.093 | 0.00 | 1.00 | +0.06% | low |
| VZ | Communication Serv | -0.093 | 0.00 | 1.00 | +1.47% | low |
| PDD | Consumer Cyclical | -0.093 | 0.00 | 1.00 | +3.14% | low |
| PEP | Consumer Defensive | -0.093 | 0.00 | 1.00 | +1.53% | low |
| SHEL | Energy | -0.093 | 0.00 | 1.00 | +0.61% | low |
| COP | Energy | -0.093 | 0.00 | 1.00 | +0.44% | low |
| CVS | Healthcare | -0.093 | 0.00 | 1.00 | -1.55% | low |

## Sector median pressure

| Sector | n | median pressure | median resid |
|--------|---|-----------------|--------------|
| Healthcare | 1064 | +0.108 | +1.87% |
| Technology | 791 | +0.087 | -0.28% |
| Communication Services | 258 | +0.087 | +0.55% |
| Basic Materials | 286 | +0.072 | +2.39% |
| Consumer Cyclical | 533 | +0.069 | +0.81% |
| Industrials | 708 | +0.063 | -0.51% |
| Consumer Defensive | 244 | +0.060 | +0.73% |
| Real Estate | 252 | +0.056 | +0.88% |
| Financial | 7101 | +0.051 | -0.06% |
| Energy | 253 | +0.022 | +0.08% |
| Utilities | 110 | -0.006 | -0.22% |

## Composite averages by size

| size | n | SPEC | QUAL | pressure |
|------|---|------|------|----------|
| large | 805 | 0.18 | 0.79 | -0.033 |
| mega | 168 | 0.15 | 0.84 | -0.058 |
| micro | 2137 | 0.51 | 0.30 | +0.114 |
| mid | 1175 | 0.36 | 0.51 | +0.043 |
| small | 1619 | 0.49 | 0.41 | +0.089 |
| unknown | 5696 | 0.32 | 0.25 | +0.047 |
