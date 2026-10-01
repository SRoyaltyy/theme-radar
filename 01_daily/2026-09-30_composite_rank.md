# Composite residual rank — **2026-09-30**

Generated: 2026-09-30T20:37:32.742376-04:00
Prior snapshot (for returns): **2026-09-29**

## Y snapshot (v1 — breadth only)

- **p_risk_on:** 0.0 (from % names up)
- **pct_up:** 0.3197
- **median_ret:** -0.23%
- **conviction:** 1.0
- **n:** 11694
- note: price_derived breadth only (v1)

## Method (deliberately simple)

- **residual** = stock return − median stock return (same pair window)
- **composites:** SPEC_DURATION, QUALITY_DEFENSIVE, CROWDING, SIZE_TILT
- **pressure** = conviction × prior effects of composites given p_risk_on
- Ranking is **cross-sectional residual bias**, not an absolute SPY call
- Hand priors only — replace with audit weights later

CSV: `data/composite/2026-09-30_composite_rank.csv`

## Top 20 by residual pressure (favor when risk-on / current Y)

| Ticker | Sector | pressure | SPEC | QUAL | CROWD | SIZE | resid | beta | short |
|--------|--------|----------|------|------|-------|------|-------|------|-------|
| ABBV | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.41% | low | low |
| WMT | Consumer Defensive | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -2.46% | low | low |
| AZN | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -1.44% | low | low |
| BRK-B | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.64% | low | low |
| BRK-A | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.61% | low | low |
| BP | Energy | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.31% | low | low |
| BMY | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.50% | low | low |
| BTI | Consumer Defensive | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.59% | low | low |
| UNH | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -1.86% | low | low |
| TTE | Energy | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -2.29% | low | low |
| UL | Consumer Defensive | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.60% | low | low |
| CVS | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -1.39% | low | low |
| V | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -1.56% | low | low |
| CVX | Energy | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.15% | low | low |
| DHR | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -1.78% | low | low |
| COP | Energy | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.00% | low | low |
| VRTX | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.51% | low | low |
| VZ | Communication Serv | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.01% | low | low |
| VLO | Energy | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.20% | low | low |
| SYK | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.98% | low | low |

## Bottom 15 (lowest pressure)

| Ticker | Sector | pressure | SPEC | QUAL | resid | beta |
|--------|--------|----------|------|------|-------|------|
| TNON | Healthcare | -1.690 | 0.85 | 0.00 | +50.05% | high |
| PACB | Healthcare | -1.670 | 0.95 | 0.00 | +29.74% | high |
| FLWS | Consumer Cyclical | -1.630 | 0.85 | 0.00 | -3.61% | high |
| ONFO | Communication Serv | -1.630 | 0.85 | 0.00 | -4.62% | high |
| EYPT | Healthcare | -1.630 | 0.85 | 0.00 | -4.15% | high |
| LDI | Financial | -1.630 | 0.85 | 0.00 | -3.05% | high |
| TNXP | Healthcare | -1.630 | 0.85 | 0.00 | +1.16% | high |
| SRFM | Industrials | -1.630 | 0.85 | 0.00 | +0.23% | high |
| PALI | Healthcare | -1.630 | 0.85 | 0.00 | -6.66% | high |
| XOS | Industrials | -1.630 | 0.85 | 0.00 | +13.40% | high |
| AIRS | Healthcare | -1.630 | 0.85 | 0.00 | -1.99% | high |
| QSI | Healthcare | -1.630 | 0.85 | 0.00 | +11.69% | high |
| NXH | Consumer Cyclical | -1.630 | 0.85 | 0.00 | -1.44% | high |
| LXEO | Healthcare | -1.630 | 0.85 | 0.00 | -0.94% | high |
| TDUP | Consumer Cyclical | -1.630 | 0.85 | 0.00 | -2.96% | high |

## Sector median pressure

| Sector | n | median pressure | median resid |
|--------|---|-----------------|--------------|
| Utilities | 107 | +0.045 | -0.14% |
| Energy | 252 | -0.185 | +0.19% |
| Financial | 7205 | -0.415 | +0.06% |
| Consumer Defensive | 241 | -0.450 | -0.54% |
| Real Estate | 247 | -0.505 | -0.88% |
| Industrials | 719 | -0.550 | -0.65% |
| Consumer Cyclical | 529 | -0.565 | -0.65% |
| Basic Materials | 292 | -0.583 | -0.82% |
| Communication Services | 255 | -0.700 | -0.14% |
| Technology | 795 | -0.700 | +0.27% |
| Healthcare | 1052 | -0.875 | -0.05% |

## Composite averages by size

| size | n | SPEC | QUAL | pressure |
|------|---|------|------|----------|
| large | 770 | 0.17 | 0.79 | +0.279 |
| mega | 154 | 0.14 | 0.83 | +0.482 |
| micro | 2198 | 0.51 | 0.29 | -0.924 |
| mid | 1132 | 0.35 | 0.51 | -0.336 |
| small | 1650 | 0.48 | 0.40 | -0.722 |
| unknown | 5790 | 0.32 | 0.23 | -0.389 |
