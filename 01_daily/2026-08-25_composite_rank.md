# Composite residual rank — **2026-08-25**

Generated: 2026-08-25T17:47:26.296908-04:00
Prior snapshot (for returns): **2026-08-24**

## Y snapshot (v1 — breadth only)

- **p_risk_on:** 0.743 (from % names up)
- **pct_up:** 0.6472
- **median_ret:** 0.25%
- **conviction:** 0.486
- **n:** 11624
- note: price_derived breadth only (v1)

## Method (deliberately simple)

- **residual** = stock return − median stock return (same pair window)
- **composites:** SPEC_DURATION, QUALITY_DEFENSIVE, CROWDING, SIZE_TILT
- **pressure** = conviction × prior effects of composites given p_risk_on
- Ranking is **cross-sectional residual bias**, not an absolute SPY call
- Hand priors only — replace with audit weights later

CSV: `data/composite/2026-08-25_composite_rank.csv`

## Top 20 by residual pressure (favor when risk-on / current Y)

| Ticker | Sector | pressure | SPEC | QUAL | CROWD | SIZE | resid | beta | short |
|--------|--------|----------|------|------|-------|------|-------|------|-------|
| SPRB | Healthcare | +0.423 | 0.95 | 0.00 | 0.80 | 1.00 | +7.85% | high | very_high |
| EBS | Healthcare | +0.423 | 0.95 | 0.00 | 0.80 | 1.00 | +8.63% | high | very_high |
| ARMP | Healthcare | +0.409 | 0.95 | 0.00 | 0.60 | 1.00 | +7.30% | high | elevated |
| CRBP | Healthcare | +0.409 | 0.95 | 0.00 | 0.60 | 1.00 | +5.55% | high | elevated |
| BTCT | Technology | +0.399 | 0.85 | 0.00 | 0.80 | 1.00 | +14.70% | high | very_high |
| PLCE | Consumer Cyclical | +0.399 | 0.85 | 0.00 | 0.80 | 1.00 | +2.82% | high | very_high |
| GOSS | Healthcare | +0.399 | 0.85 | 0.00 | 0.80 | 1.00 | +17.40% | high | very_high |
| WW | Healthcare | +0.399 | 0.85 | 0.00 | 0.80 | 1.00 | +10.14% | high | very_high |
| PACB | Healthcare | +0.394 | 0.95 | 0.00 | 0.80 | 0.80 | +18.50% | high | very_high |
| PROK | Healthcare | +0.394 | 0.95 | 0.00 | 0.80 | 0.80 | +7.21% | high | very_high |
| BKKT | Technology | +0.394 | 0.95 | 0.00 | 0.80 | 0.80 | +5.26% | high | very_high |
| AMCX | Communication Serv | +0.394 | 0.95 | 0.00 | 0.80 | 0.80 | +3.22% | high | very_high |
| ARCT | Healthcare | +0.394 | 0.95 | 0.00 | 0.80 | 0.80 | +7.42% | high | very_high |
| AQST | Healthcare | +0.394 | 0.95 | 0.00 | 0.80 | 0.80 | +5.59% | high | very_high |
| PRME | Healthcare | +0.394 | 0.95 | 0.00 | 0.80 | 0.80 | +13.91% | high | very_high |
| CDZI | Utilities | +0.394 | 0.95 | 0.00 | 0.80 | 0.80 | +9.57% | high | very_high |
| CRML | Basic Materials | +0.394 | 0.95 | 0.00 | 0.80 | 0.80 | +21.19% | high | very_high |
| INBX | Healthcare | +0.394 | 0.95 | 0.00 | 0.80 | 0.80 | +16.70% | high | very_high |
| FDMT | Healthcare | +0.394 | 0.95 | 0.00 | 0.80 | 0.80 | +1.90% | high | very_high |
| SBET | Financial | +0.394 | 0.95 | 0.00 | 0.80 | 0.80 | +0.72% | high | very_high |

## Bottom 15 (lowest pressure)

| Ticker | Sector | pressure | SPEC | QUAL | resid | beta |
|--------|--------|----------|------|------|-------|------|
| ABBV | Healthcare | -0.177 | 0.00 | 1.00 | +0.23% | low |
| VRTX | Healthcare | -0.177 | 0.00 | 1.00 | +0.71% | low |
| MO | Consumer Defensive | -0.177 | 0.00 | 1.00 | -0.83% | low |
| MFG | Financial | -0.177 | 0.00 | 1.00 | +1.51% | low |
| LIN | Basic Materials | -0.177 | 0.00 | 1.00 | -0.82% | low |
| BRK-B | Financial | -0.177 | 0.00 | 1.00 | -0.25% | low |
| BRK-A | Financial | -0.177 | 0.00 | 1.00 | -0.28% | low |
| HDB | Financial | -0.177 | 0.00 | 1.00 | +0.14% | low |
| DHR | Healthcare | -0.177 | 0.00 | 1.00 | +0.15% | low |
| SAN | Financial | -0.177 | 0.00 | 1.00 | -0.86% | low |
| SNY | Healthcare | -0.177 | 0.00 | 1.00 | +0.48% | low |
| NVO | Healthcare | -0.177 | 0.00 | 1.00 | +3.46% | low |
| PM | Consumer Defensive | -0.177 | 0.00 | 1.00 | +1.04% | low |
| NVS | Healthcare | -0.177 | 0.00 | 1.00 | +0.99% | low |
| JNJ | Healthcare | -0.177 | 0.00 | 1.00 | -0.21% | low |

## Sector median pressure

| Sector | n | median pressure | median resid |
|--------|---|-----------------|--------------|
| Healthcare | 1064 | +0.204 | +0.97% |
| Technology | 791 | +0.165 | +0.31% |
| Communication Services | 258 | +0.165 | +0.61% |
| Basic Materials | 287 | +0.137 | +0.94% |
| Consumer Cyclical | 533 | +0.130 | -0.47% |
| Industrials | 711 | +0.125 | -0.25% |
| Consumer Defensive | 243 | +0.116 | -0.45% |
| Real Estate | 251 | +0.107 | -0.25% |
| Financial | 7125 | +0.098 | -0.01% |
| Energy | 252 | +0.037 | -1.05% |
| Utilities | 109 | -0.011 | +0.17% |

## Composite averages by size

| size | n | SPEC | QUAL | pressure |
|------|---|------|------|----------|
| large | 797 | 0.17 | 0.79 | -0.063 |
| mega | 167 | 0.15 | 0.83 | -0.108 |
| micro | 2144 | 0.51 | 0.30 | +0.217 |
| mid | 1181 | 0.36 | 0.51 | +0.082 |
| small | 1620 | 0.49 | 0.40 | +0.170 |
| unknown | 5715 | 0.32 | 0.24 | +0.092 |
