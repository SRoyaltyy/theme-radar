# Composite residual rank — **2026-08-24**

Generated: 2026-08-24T17:47:24.236464-04:00
Prior snapshot (for returns): **2026-08-21**

## Y snapshot (v1 — breadth only)

- **p_risk_on:** 0.0831 (from % names up)
- **pct_up:** 0.3832
- **median_ret:** -0.14%
- **conviction:** 0.8338
- **n:** 11617
- note: price_derived breadth only (v1)

## Method (deliberately simple)

- **residual** = stock return − median stock return (same pair window)
- **composites:** SPEC_DURATION, QUALITY_DEFENSIVE, CROWDING, SIZE_TILT
- **pressure** = conviction × prior effects of composites given p_risk_on
- Ranking is **cross-sectional residual bias**, not an absolute SPY call
- Hand priors only — replace with audit weights later

CSV: `data/composite/2026-08-24_composite_rank.csv`

## Top 20 by residual pressure (favor when risk-on / current Y)

| Ticker | Sector | pressure | SPEC | QUAL | CROWD | SIZE | resid | beta | short |
|--------|--------|----------|------|------|-------|------|-------|------|-------|
| CB | Financial | +0.521 | 0.00 | 1.00 | 0.00 | 0.00 | +1.56% | low | low |
| RIO | Basic Materials | +0.521 | 0.00 | 1.00 | 0.00 | 0.00 | -0.34% | low | low |
| BUD | Consumer Defensive | +0.521 | 0.00 | 1.00 | 0.00 | 0.00 | +0.62% | low | low |
| ABBV | Healthcare | +0.521 | 0.00 | 1.00 | 0.00 | 0.00 | -0.03% | low | low |
| CME | Financial | +0.521 | 0.00 | 1.00 | 0.00 | 0.00 | +1.66% | low | low |
| MUFG | Financial | +0.521 | 0.00 | 1.00 | 0.00 | 0.00 | -0.22% | low | low |
| SO | Utilities | +0.521 | 0.00 | 1.00 | 0.00 | 0.00 | +1.44% | low | low |
| XOM | Energy | +0.521 | 0.00 | 1.00 | 0.00 | 0.00 | -0.50% | low | low |
| SAN | Financial | +0.521 | 0.00 | 1.00 | 0.00 | 0.00 | +1.03% | low | unknown |
| PM | Consumer Defensive | +0.521 | 0.00 | 1.00 | 0.00 | 0.00 | +1.85% | low | low |
| UL | Consumer Defensive | +0.521 | 0.00 | 1.00 | 0.00 | 0.00 | +1.98% | low | low |
| CNQ | Energy | +0.521 | 0.00 | 1.00 | 0.00 | 0.00 | -1.26% | low | low |
| VRTX | Healthcare | +0.521 | 0.00 | 1.00 | 0.00 | 0.00 | +0.05% | low | low |
| WMT | Consumer Defensive | +0.521 | 0.00 | 1.00 | 0.00 | 0.00 | +2.83% | low | low |
| BMY | Healthcare | +0.521 | 0.00 | 1.00 | 0.00 | 0.00 | +0.54% | low | low |
| COP | Energy | +0.521 | 0.00 | 1.00 | 0.00 | 0.00 | -0.99% | low | low |
| V | Financial | +0.521 | 0.00 | 1.00 | 0.00 | 0.00 | +3.20% | low | low |
| PG | Consumer Defensive | +0.521 | 0.00 | 1.00 | 0.00 | 0.00 | +1.47% | low | low |
| NEE | Utilities | +0.521 | 0.00 | 1.00 | 0.00 | 0.00 | +0.68% | low | low |
| SMFG | Financial | +0.521 | 0.00 | 1.00 | 0.00 | 0.00 | -0.06% | low | low |

## Bottom 15 (lowest pressure)

| Ticker | Sector | pressure | SPEC | QUAL | resid | beta |
|--------|--------|----------|------|------|-------|------|
| USGO | Basic Materials | -1.244 | 0.95 | 0.00 | +3.67% | high |
| SPRB | Healthcare | -1.244 | 0.95 | 0.00 | +13.85% | high |
| BTCT | Technology | -1.175 | 0.85 | 0.00 | +52.77% | high |
| GOSS | Healthcare | -1.175 | 0.85 | 0.00 | +13.47% | high |
| AQST | Healthcare | -1.161 | 0.95 | 0.00 | +3.14% | high |
| ARCT | Healthcare | -1.161 | 0.95 | 0.00 | +6.76% | high |
| SBET | Financial | -1.161 | 0.95 | 0.00 | +4.69% | high |
| BEEM | Technology | -1.133 | 0.85 | 0.00 | -8.78% | high |
| PEPG | Healthcare | -1.133 | 0.85 | 0.00 | +1.73% | high |
| CAN | Technology | -1.133 | 0.85 | 0.00 | +3.00% | high |
| BTCS | Financial | -1.133 | 0.85 | 0.00 | +9.03% | high |
| RCEL | Healthcare | -1.133 | 0.85 | 0.00 | -1.35% | high |
| NAKA | Financial | -1.133 | 0.85 | 0.00 | +2.12% | high |
| JELD | Industrials | -1.133 | 0.85 | 0.00 | +8.40% | high |
| AIFC | Technology | -1.133 | 0.85 | 0.00 | -2.80% | high |

## Sector median pressure

| Sector | n | median pressure | median resid |
|--------|---|-----------------|--------------|
| Utilities | 109 | +0.031 | +0.88% |
| Energy | 252 | -0.118 | -0.94% |
| Financial | 7119 | -0.288 | +0.04% |
| Real Estate | 251 | -0.316 | +0.67% |
| Consumer Defensive | 243 | -0.351 | +0.88% |
| Consumer Cyclical | 533 | -0.368 | +0.07% |
| Industrials | 711 | -0.368 | -0.76% |
| Basic Materials | 287 | -0.403 | -0.39% |
| Communication Services | 258 | -0.487 | +0.19% |
| Technology | 790 | -0.487 | -1.28% |
| Healthcare | 1064 | -0.587 | -0.39% |

## Composite averages by size

| size | n | SPEC | QUAL | pressure |
|------|---|------|------|----------|
| large | 802 | 0.18 | 0.79 | +0.183 |
| mega | 166 | 0.14 | 0.84 | +0.329 |
| micro | 2146 | 0.51 | 0.30 | -0.640 |
| mid | 1173 | 0.36 | 0.51 | -0.242 |
| small | 1617 | 0.49 | 0.40 | -0.499 |
| unknown | 5713 | 0.32 | 0.24 | -0.270 |
