# Composite residual rank — **2026-10-14**

Generated: 2026-10-14T16:56:44.558786-04:00
Prior snapshot (for returns): **2026-10-13**

## Y snapshot (v1 — breadth only)

- **p_risk_on:** 0.0 (from % names up)
- **pct_up:** 0.1963
- **median_ret:** -1.00%
- **conviction:** 1.0
- **n:** 11738
- note: price_derived breadth only (v1)

## Method (deliberately simple)

- **residual** = stock return − median stock return (same pair window)
- **composites:** SPEC_DURATION, QUALITY_DEFENSIVE, CROWDING, SIZE_TILT
- **pressure** = conviction × prior effects of composites given p_risk_on
- Ranking is **cross-sectional residual bias**, not an absolute SPY call
- Hand priors only — replace with audit weights later

CSV: `data/composite/2026-10-14_composite_rank.csv`

## Top 20 by residual pressure (favor when risk-on / current Y)

| Ticker | Sector | pressure | SPEC | QUAL | CROWD | SIZE | resid | beta | short |
|--------|--------|----------|------|------|-------|------|-------|------|-------|
| PFE | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +3.96% | low | low |
| PEP | Consumer Defensive | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +2.54% | low | low |
| PDD | Consumer Cyclical | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.37% | low | low |
| PM | Consumer Defensive | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +4.15% | low | low |
| BUD | Consumer Defensive | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +2.12% | low | low |
| BTI | Consumer Defensive | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +2.81% | low | low |
| CME | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +3.72% | low | low |
| ABT | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.35% | low | low |
| WMT | Consumer Defensive | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +4.45% | low | low |
| NEE | Utilities | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.19% | low | low |
| VZ | Communication Serv | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +3.04% | low | low |
| NEM | Basic Materials | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -2.49% | low | low |
| NVO | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.15% | low | low |
| NVS | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +4.14% | low | low |
| MRK | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +4.79% | low | low |
| CVS | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +4.24% | low | low |
| MFG | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -2.21% | low | low |
| RIO | Basic Materials | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.95% | low | low |
| DHR | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.83% | low | low |
| MCD | Consumer Cyclical | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +2.06% | low | low |

## Bottom 15 (lowest pressure)

| Ticker | Sector | pressure | SPEC | QUAL | resid | beta |
|--------|--------|----------|------|------|-------|------|
| CRMT | Consumer Cyclical | -1.690 | 0.85 | 0.00 | -6.49% | high |
| USGO | Basic Materials | -1.630 | 0.85 | 0.00 | -5.76% | high |
| ATOM | Technology | -1.630 | 0.85 | 0.00 | -7.16% | high |
| HUCK | Technology | -1.630 | 0.85 | 0.00 | -1.25% | high |
| SPRB | Healthcare | -1.630 | 0.85 | 0.00 | -2.40% | high |
| AIRS | Healthcare | -1.630 | 0.85 | 0.00 | -11.35% | high |
| YMAT | Basic Materials | -1.630 | 0.85 | 0.00 | -14.51% | high |
| AIRO | Industrials | -1.630 | 0.85 | 0.00 | -3.24% | high |
| WATT | Technology | -1.630 | 0.85 | 0.00 | -6.07% | high |
| CLPT | Healthcare | -1.630 | 0.85 | 0.00 | -4.81% | high |
| LFMD | Healthcare | -1.630 | 0.85 | 0.00 | -3.05% | high |
| CABA | Healthcare | -1.630 | 0.85 | 0.00 | -3.15% | high |
| BETR | Financial | -1.630 | 0.85 | 0.00 | -8.48% | high |
| EU | Energy | -1.630 | 0.85 | 0.00 | -5.60% | high |
| TNXP | Healthcare | -1.630 | 0.85 | 0.00 | +5.40% | high |

## Sector median pressure

| Sector | n | median pressure | median resid |
|--------|---|-----------------|--------------|
| Utilities | 107 | +0.045 | +0.53% |
| Energy | 252 | -0.205 | -1.05% |
| Financial | 7248 | -0.415 | +0.23% |
| Consumer Defensive | 241 | -0.465 | +0.97% |
| Real Estate | 248 | -0.525 | -0.27% |
| Industrials | 717 | -0.550 | -1.11% |
| Basic Materials | 293 | -0.580 | -2.48% |
| Consumer Cyclical | 526 | -0.580 | -0.24% |
| Communication Services | 254 | -0.700 | -0.50% |
| Technology | 799 | -0.700 | -2.45% |
| Healthcare | 1053 | -0.935 | -0.36% |

## Composite averages by size

| size | n | SPEC | QUAL | pressure |
|------|---|------|------|----------|
| large | 759 | 0.17 | 0.80 | +0.274 |
| mega | 162 | 0.15 | 0.84 | +0.467 |
| micro | 2245 | 0.51 | 0.28 | -0.942 |
| mid | 1116 | 0.35 | 0.51 | -0.339 |
| small | 1620 | 0.48 | 0.40 | -0.724 |
| unknown | 5836 | 0.32 | 0.24 | -0.379 |
