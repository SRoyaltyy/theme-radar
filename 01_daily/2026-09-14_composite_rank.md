# Composite residual rank — **2026-09-14**

Generated: 2026-09-14T19:54:19.325890-04:00
Prior snapshot (for returns): **2026-09-11**

## Y snapshot (v1 — breadth only)

- **p_risk_on:** 0.0 (from % names up)
- **pct_up:** 0.3388
- **median_ret:** -0.20%
- **conviction:** 1.0
- **n:** 11616
- note: price_derived breadth only (v1)

## Method (deliberately simple)

- **residual** = stock return − median stock return (same pair window)
- **composites:** SPEC_DURATION, QUALITY_DEFENSIVE, CROWDING, SIZE_TILT
- **pressure** = conviction × prior effects of composites given p_risk_on
- Ranking is **cross-sectional residual bias**, not an absolute SPY call
- Hand priors only — replace with audit weights later

CSV: `data/composite/2026-09-14_composite_rank.csv`

## Top 20 by residual pressure (favor when risk-on / current Y)

| Ticker | Sector | pressure | SPEC | QUAL | CROWD | SIZE | resid | beta | short |
|--------|--------|----------|------|------|-------|------|-------|------|-------|
| T | Communication Serv | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.93% | low | low |
| NVS | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.54% | low | low |
| NVO | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.09% | low | low |
| SYK | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +2.49% | low | low |
| NEM | Basic Materials | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -2.74% | low | low |
| XOM | Energy | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.34% | low | low |
| NEE | Utilities | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.62% | low | low |
| PEP | Consumer Defensive | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.22% | low | low |
| BABA | Consumer Cyclical | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.14% | low | low |
| HSBC | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -1.09% | low | low |
| ENB | Energy | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.04% | low | low |
| IBM | Technology | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +2.59% | low | low |
| TTE | Energy | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.61% | low | low |
| IBN | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.24% | low | low |
| SMFG | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.02% | low | low |
| MO | Consumer Defensive | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +2.57% | low | low |
| BUD | Consumer Defensive | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +2.24% | low | low |
| TMUS | Communication Serv | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.52% | low | low |
| AEM | Basic Materials | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -1.20% | low | low |
| RIO | Basic Materials | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -2.12% | low | low |

## Bottom 15 (lowest pressure)

| Ticker | Sector | pressure | SPEC | QUAL | resid | beta |
|--------|--------|----------|------|------|-------|------|
| VERI | Technology | -1.790 | 0.95 | 0.00 | +10.78% | high |
| CRDF | Healthcare | -1.690 | 0.85 | 0.00 | +8.47% | high |
| GPRO | Technology | -1.630 | 0.85 | 0.00 | -1.97% | high |
| TJGC | Communication Serv | -1.630 | 0.85 | 0.00 | +3.24% | high |
| FGI | Consumer Cyclical | -1.630 | 0.85 | 0.00 | +7.91% | high |
| NCRA | Consumer Defensive | -1.630 | 0.85 | 0.00 | +2.89% | high |
| FLWS | Consumer Cyclical | -1.630 | 0.85 | 0.00 | +1.53% | high |
| KLC | Consumer Defensive | -1.630 | 0.85 | 0.00 | +0.63% | high |
| GAME | Communication Serv | -1.630 | 0.85 | 0.00 | -1.97% | high |
| ACVA | Consumer Cyclical | -1.610 | 0.95 | 0.00 | +0.20% | high |
| CRBP | Healthcare | -1.570 | 0.85 | 0.00 | -0.29% | high |
| NMRA | Healthcare | -1.570 | 0.85 | 0.00 | -3.64% | high |
| CNTX | Healthcare | -1.570 | 0.85 | 0.00 | +0.20% | high |
| LODE | Basic Materials | -1.570 | 0.85 | 0.00 | -4.76% | high |
| FHTX | Healthcare | -1.570 | 0.85 | 0.00 | -1.15% | high |

## Sector median pressure

| Sector | n | median pressure | median resid |
|--------|---|-----------------|--------------|
| Utilities | 107 | +0.045 | -0.62% |
| Energy | 251 | -0.180 | -0.86% |
| Financial | 7127 | -0.415 | +0.00% |
| Consumer Defensive | 242 | -0.440 | +0.54% |
| Real Estate | 248 | -0.480 | -0.07% |
| Industrials | 717 | -0.530 | -0.82% |
| Consumer Cyclical | 528 | -0.552 | +0.20% |
| Basic Materials | 291 | -0.580 | -1.91% |
| Communication Services | 256 | -0.700 | +0.91% |
| Technology | 794 | -0.700 | -0.54% |
| Healthcare | 1055 | -0.840 | +0.73% |

## Composite averages by size

| size | n | SPEC | QUAL | pressure |
|------|---|------|------|----------|
| large | 774 | 0.17 | 0.80 | +0.286 |
| mega | 167 | 0.14 | 0.85 | +0.494 |
| micro | 2167 | 0.51 | 0.30 | -0.918 |
| mid | 1162 | 0.36 | 0.51 | -0.334 |
| small | 1626 | 0.48 | 0.40 | -0.712 |
| unknown | 5720 | 0.32 | 0.24 | -0.378 |
