# Composite residual rank — **2026-09-17**

Generated: 2026-09-17T16:42:00.965684-04:00
Prior snapshot (for returns): **2026-09-16**

## Y snapshot (v1 — breadth only)

- **p_risk_on:** 0.9705 (from % names up)
- **pct_up:** 0.7382
- **median_ret:** 0.63%
- **conviction:** 0.941
- **n:** 11650
- note: price_derived breadth only (v1)

## Method (deliberately simple)

- **residual** = stock return − median stock return (same pair window)
- **composites:** SPEC_DURATION, QUALITY_DEFENSIVE, CROWDING, SIZE_TILT
- **pressure** = conviction × prior effects of composites given p_risk_on
- Ranking is **cross-sectional residual bias**, not an absolute SPY call
- Hand priors only — replace with audit weights later

CSV: `data/composite/2026-09-17_composite_rank.csv`

## Top 20 by residual pressure (favor when risk-on / current Y)

| Ticker | Sector | pressure | SPEC | QUAL | CROWD | SIZE | resid | beta | short |
|--------|--------|----------|------|------|-------|------|-------|------|-------|
| GLSI | Healthcare | +1.585 | 0.95 | 0.00 | 0.80 | 1.00 | +17.02% | high | very_high |
| CHPT | Consumer Cyclical | +1.585 | 0.95 | 0.00 | 0.80 | 1.00 | +10.70% | high | very_high |
| LVWR | Consumer Cyclical | +1.585 | 0.95 | 0.00 | 0.80 | 1.00 | +18.69% | high | very_high |
| VERI | Technology | +1.585 | 0.95 | 0.00 | 0.80 | 1.00 | -1.55% | high | very_high |
| EAF | Industrials | +1.532 | 0.95 | 0.00 | 0.60 | 1.00 | -1.99% | high | elevated |
| NCPL | Financial | +1.496 | 0.85 | 0.00 | 0.80 | 1.00 | +32.70% | high | very_high |
| DAIC | Technology | +1.496 | 0.85 | 0.00 | 0.80 | 1.00 | +163.05% | high | very_high |
| YFOR | Industrials | +1.496 | 0.85 | 0.00 | 0.80 | 1.00 | +6.34% | high | very_high |
| AEMD | Healthcare | +1.496 | 0.85 | 0.00 | 0.80 | 1.00 | +373.49% | high | very_high |
| BBNX | Healthcare | +1.479 | 0.95 | 0.00 | 0.80 | 0.80 | -4.01% | high | very_high |
| RXT | Technology | +1.479 | 0.95 | 0.00 | 0.80 | 0.80 | +12.01% | high | very_high |
| ARCT | Healthcare | +1.479 | 0.95 | 0.00 | 0.80 | 0.80 | +7.89% | high | very_high |
| SKIL | Consumer Defensive | +1.443 | 0.85 | 0.00 | 0.60 | 1.00 | +3.14% | high | elevated |
| CUE | Healthcare | +1.443 | 0.85 | 0.00 | 0.60 | 1.00 | +10.11% | high | elevated |
| KLC | Consumer Defensive | +1.443 | 0.85 | 0.00 | 0.60 | 1.00 | +0.22% | high | very_high |
| PLAY | Communication Serv | +1.443 | 0.85 | 0.00 | 0.60 | 1.00 | -5.30% | high | very_high |
| FLWS | Consumer Cyclical | +1.443 | 0.85 | 0.00 | 0.60 | 1.00 | -4.69% | high | very_high |
| AGPU | Technology | +1.443 | 0.85 | 0.00 | 0.60 | 1.00 | +16.93% | high | elevated |
| LASE | Industrials | +1.443 | 0.85 | 0.00 | 0.60 | 1.00 | +10.62% | high | elevated |
| RCEL | Healthcare | +1.443 | 0.85 | 0.00 | 0.60 | 1.00 | +6.74% | high | elevated |

## Bottom 15 (lowest pressure)

| Ticker | Sector | pressure | SPEC | QUAL | resid | beta |
|--------|--------|----------|------|------|-------|------|
| ABBV | Healthcare | -0.664 | 0.00 | 1.00 | -0.06% | low |
| CB | Financial | -0.664 | 0.00 | 1.00 | -0.53% | low |
| MO | Consumer Defensive | -0.664 | 0.00 | 1.00 | -1.20% | low |
| DHR | Healthcare | -0.664 | 0.00 | 1.00 | +1.35% | low |
| BUD | Consumer Defensive | -0.664 | 0.00 | 1.00 | -2.05% | low |
| V | Financial | -0.664 | 0.00 | 1.00 | -0.90% | low |
| HDB | Financial | -0.664 | 0.00 | 1.00 | +0.62% | low |
| TMUS | Communication Serv | -0.664 | 0.00 | 1.00 | -6.20% | low |
| SMFG | Financial | -0.664 | 0.00 | 1.00 | +1.00% | low |
| WMT | Consumer Defensive | -0.664 | 0.00 | 1.00 | -1.29% | low |
| BABA | Consumer Cyclical | -0.664 | 0.00 | 1.00 | +0.55% | low |
| LMT | Industrials | -0.664 | 0.00 | 1.00 | -0.48% | low |
| LLY | Healthcare | -0.664 | 0.00 | 1.00 | +0.65% | low |
| COP | Energy | -0.664 | 0.00 | 1.00 | -0.14% | low |
| KO | Consumer Defensive | -0.664 | 0.00 | 1.00 | -0.42% | low |

## Sector median pressure

| Sector | n | median pressure | median resid |
|--------|---|-----------------|--------------|
| Healthcare | 1055 | +0.766 | +0.45% |
| Technology | 794 | +0.620 | +0.60% |
| Communication Services | 256 | +0.620 | -1.07% |
| Basic Materials | 291 | +0.514 | +1.31% |
| Consumer Cyclical | 528 | +0.500 | -0.42% |
| Industrials | 717 | +0.469 | -0.04% |
| Real Estate | 248 | +0.447 | -0.37% |
| Consumer Defensive | 242 | +0.390 | -0.63% |
| Financial | 7161 | +0.367 | -0.00% |
| Energy | 251 | +0.181 | -0.33% |
| Utilities | 107 | -0.040 | +0.14% |

## Composite averages by size

| size | n | SPEC | QUAL | pressure |
|------|---|------|------|----------|
| large | 772 | 0.17 | 0.79 | -0.248 |
| mega | 165 | 0.14 | 0.84 | -0.432 |
| micro | 2177 | 0.51 | 0.30 | +0.814 |
| mid | 1163 | 0.36 | 0.51 | +0.301 |
| small | 1624 | 0.48 | 0.41 | +0.628 |
| unknown | 5749 | 0.32 | 0.25 | +0.329 |
