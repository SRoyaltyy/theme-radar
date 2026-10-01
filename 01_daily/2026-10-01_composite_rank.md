# Composite residual rank — **2026-10-01**

Generated: 2026-10-01T17:36:10.927743-04:00
Prior snapshot (for returns): **2026-09-30**

## Y snapshot (v1 — breadth only)

- **p_risk_on:** 0.4137 (from % names up)
- **pct_up:** 0.5155
- **median_ret:** 0.04%
- **conviction:** 0.1727
- **n:** 11706
- note: price_derived breadth only (v1)

## Method (deliberately simple)

- **residual** = stock return − median stock return (same pair window)
- **composites:** SPEC_DURATION, QUALITY_DEFENSIVE, CROWDING, SIZE_TILT
- **pressure** = conviction × prior effects of composites given p_risk_on
- Ranking is **cross-sectional residual bias**, not an absolute SPY call
- Hand priors only — replace with audit weights later

CSV: `data/composite/2026-10-01_composite_rank.csv`

## Top 20 by residual pressure (favor when risk-on / current Y)

| Ticker | Sector | pressure | SPEC | QUAL | CROWD | SIZE | resid | beta | short |
|--------|--------|----------|------|------|-------|------|-------|------|-------|
| WMT | Consumer Defensive | +0.022 | 0.00 | 1.00 | 0.00 | 0.00 | +0.29% | low | low |
| AZN | Healthcare | +0.022 | 0.00 | 1.00 | 0.00 | 0.00 | -2.37% | low | low |
| CB | Financial | +0.022 | 0.00 | 1.00 | 0.00 | 0.00 | +1.82% | low | low |
| VLO | Energy | +0.022 | 0.00 | 1.00 | 0.00 | 0.00 | +5.34% | low | low |
| BTI | Consumer Defensive | +0.022 | 0.00 | 1.00 | 0.00 | 0.00 | -2.26% | low | low |
| BRK-B | Financial | +0.022 | 0.00 | 1.00 | 0.00 | 0.00 | +0.47% | low | low |
| BRK-A | Financial | +0.022 | 0.00 | 1.00 | 0.00 | 0.00 | +0.59% | low | low |
| BP | Energy | +0.022 | 0.00 | 1.00 | 0.00 | 0.00 | +1.12% | low | low |
| BMY | Healthcare | +0.022 | 0.00 | 1.00 | 0.00 | 0.00 | -1.55% | low | low |
| ABBV | Healthcare | +0.022 | 0.00 | 1.00 | 0.00 | 0.00 | -0.67% | low | low |
| CVX | Energy | +0.022 | 0.00 | 1.00 | 0.00 | 0.00 | +1.38% | low | low |
| DHR | Healthcare | +0.022 | 0.00 | 1.00 | 0.00 | 0.00 | -4.46% | low | low |
| UL | Consumer Defensive | +0.022 | 0.00 | 1.00 | 0.00 | 0.00 | -1.93% | low | low |
| TTE | Energy | +0.022 | 0.00 | 1.00 | 0.00 | 0.00 | -1.20% | low | low |
| EQNR | Energy | +0.022 | 0.00 | 1.00 | 0.00 | 0.00 | +1.33% | low | low |
| TM | Consumer Cyclical | +0.022 | 0.00 | 1.00 | 0.00 | 0.00 | +0.09% | low | low |
| TMUS | Communication Serv | +0.022 | 0.00 | 1.00 | 0.00 | 0.00 | -0.87% | low | low |
| UNH | Healthcare | +0.022 | 0.00 | 1.00 | 0.00 | 0.00 | -0.55% | low | low |
| COP | Energy | +0.022 | 0.00 | 1.00 | 0.00 | 0.00 | +1.49% | low | low |
| V | Financial | +0.022 | 0.00 | 1.00 | 0.00 | 0.00 | +0.10% | low | low |

## Bottom 15 (lowest pressure)

| Ticker | Sector | pressure | SPEC | QUAL | resid | beta |
|--------|--------|----------|------|------|-------|------|
| HRTX | Healthcare | -0.053 | 0.95 | 0.00 | +16.09% | high |
| DMRC | Technology | -0.052 | 0.95 | 0.00 | +16.11% | high |
| TNON | Healthcare | -0.050 | 0.85 | 0.00 | -1.26% | high |
| BIRD | Technology | -0.050 | 0.85 | 0.00 | +33.68% | high |
| PACB | Healthcare | -0.050 | 0.95 | 0.00 | +5.87% | high |
| EYPT | Healthcare | -0.049 | 0.85 | 0.00 | -1.26% | high |
| TDUP | Consumer Cyclical | -0.049 | 0.85 | 0.00 | +0.43% | high |
| HUCK | Technology | -0.049 | 0.85 | 0.00 | -2.74% | high |
| VERI | Technology | -0.049 | 0.85 | 0.00 | -37.01% | high |
| CRBP | Healthcare | -0.049 | 0.85 | 0.00 | -7.08% | high |
| XOS | Industrials | -0.049 | 0.85 | 0.00 | -0.98% | high |
| NXH | Consumer Cyclical | -0.049 | 0.85 | 0.00 | -3.78% | high |
| NCPL | Financial | -0.049 | 0.85 | 0.00 | +24.96% | high |
| AIRS | Healthcare | -0.049 | 0.85 | 0.00 | -3.45% | high |
| TNXP | Healthcare | -0.049 | 0.85 | 0.00 | -5.28% | high |

## Sector median pressure

| Sector | n | median pressure | median resid |
|--------|---|-----------------|--------------|
| Utilities | 107 | +0.001 | +0.05% |
| Energy | 252 | -0.006 | +1.08% |
| Financial | 7214 | -0.012 | +0.04% |
| Consumer Defensive | 241 | -0.013 | -0.46% |
| Real Estate | 247 | -0.015 | -0.39% |
| Industrials | 719 | -0.016 | +0.42% |
| Consumer Cyclical | 529 | -0.017 | +0.14% |
| Basic Materials | 294 | -0.017 | -0.47% |
| Communication Services | 255 | -0.021 | -0.89% |
| Technology | 795 | -0.021 | +0.68% |
| Healthcare | 1053 | -0.026 | -1.95% |

## Composite averages by size

| size | n | SPEC | QUAL | pressure |
|------|---|------|------|----------|
| large | 766 | 0.17 | 0.79 | +0.008 |
| mega | 154 | 0.14 | 0.84 | +0.015 |
| micro | 2202 | 0.51 | 0.29 | -0.028 |
| mid | 1140 | 0.35 | 0.51 | -0.010 |
| small | 1643 | 0.48 | 0.40 | -0.021 |
| unknown | 5801 | 0.32 | 0.23 | -0.012 |
