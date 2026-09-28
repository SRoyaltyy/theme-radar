# Composite residual rank — **2026-09-28**

Generated: 2026-09-28T16:48:06.071723-04:00
Prior snapshot (for returns): **2026-09-25**

## Y snapshot (v1 — breadth only)

- **p_risk_on:** 0.0 (from % names up)
- **pct_up:** 0.1932
- **median_ret:** -0.67%
- **conviction:** 1.0
- **n:** 11680
- note: price_derived breadth only (v1)

## Method (deliberately simple)

- **residual** = stock return − median stock return (same pair window)
- **composites:** SPEC_DURATION, QUALITY_DEFENSIVE, CROWDING, SIZE_TILT
- **pressure** = conviction × prior effects of composites given p_risk_on
- Ranking is **cross-sectional residual bias**, not an absolute SPY call
- Hand priors only — replace with audit weights later

CSV: `data/composite/2026-09-28_composite_rank.csv`

## Top 20 by residual pressure (favor when risk-on / current Y)

| Ticker | Sector | pressure | SPEC | QUAL | CROWD | SIZE | resid | beta | short |
|--------|--------|----------|------|------|-------|------|-------|------|-------|
| MUFG | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.21% | low | low |
| EQNR | Energy | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.86% | low | low |
| ABT | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.37% | low | low |
| TTE | Energy | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.02% | low | low |
| VZ | Communication Serv | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.17% | low | low |
| COP | Energy | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.31% | low | low |
| SMFG | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.00% | low | low |
| VRTX | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.96% | low | low |
| MDT | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.65% | low | low |
| VLO | Energy | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.29% | low | low |
| WMT | Consumer Defensive | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.37% | low | low |
| AMGN | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.52% | low | low |
| LMT | Industrials | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.39% | low | low |
| LLY | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.79% | low | low |
| MFG | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.49% | low | low |
| LIN | Basic Materials | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.13% | low | low |
| CVX | Energy | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.61% | low | low |
| NVS | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.65% | low | low |
| NVO | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.44% | low | low |
| SYK | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.76% | low | low |

## Bottom 15 (lowest pressure)

| Ticker | Sector | pressure | SPEC | QUAL | resid | beta |
|--------|--------|----------|------|------|-------|------|
| TJGC | Communication Serv | -1.690 | 0.85 | 0.00 | +9.44% | high |
| GRML | Basic Materials | -1.690 | 0.85 | 0.00 | -18.49% | high |
| LHSW | Technology | -1.690 | 0.85 | 0.00 | -4.88% | high |
| PACB | Healthcare | -1.670 | 0.95 | 0.00 | +6.23% | high |
| SRFM | Industrials | -1.630 | 0.85 | 0.00 | +7.88% | high |
| TNXP | Healthcare | -1.630 | 0.85 | 0.00 | +1.08% | high |
| NXH | Consumer Cyclical | -1.630 | 0.85 | 0.00 | -4.83% | high |
| HUCK | Technology | -1.630 | 0.85 | 0.00 | -1.11% | high |
| LXEO | Healthcare | -1.630 | 0.85 | 0.00 | -4.46% | high |
| TDUP | Consumer Cyclical | -1.630 | 0.85 | 0.00 | -1.55% | high |
| AIRS | Healthcare | -1.630 | 0.85 | 0.00 | -3.41% | high |
| SXTP | Healthcare | -1.630 | 0.85 | 0.00 | +7.51% | high |
| CRBP | Healthcare | -1.630 | 0.85 | 0.00 | -2.41% | high |
| LDI | Financial | -1.630 | 0.85 | 0.00 | -8.28% | high |
| EYPT | Healthcare | -1.630 | 0.85 | 0.00 | -7.89% | high |

## Sector median pressure

| Sector | n | median pressure | median resid |
|--------|---|-----------------|--------------|
| Utilities | 107 | +0.045 | -0.10% |
| Energy | 252 | -0.155 | -0.06% |
| Financial | 7193 | -0.415 | +0.03% |
| Consumer Defensive | 241 | -0.450 | +0.38% |
| Real Estate | 247 | -0.505 | +0.07% |
| Consumer Cyclical | 529 | -0.550 | +0.09% |
| Industrials | 717 | -0.550 | -0.41% |
| Basic Materials | 292 | -0.573 | -1.46% |
| Communication Services | 255 | -0.700 | -0.31% |
| Technology | 795 | -0.700 | -0.74% |
| Healthcare | 1052 | -0.875 | +0.67% |

## Composite averages by size

| size | n | SPEC | QUAL | pressure |
|------|---|------|------|----------|
| large | 771 | 0.16 | 0.79 | +0.280 |
| mega | 158 | 0.14 | 0.84 | +0.481 |
| micro | 2202 | 0.51 | 0.29 | -0.923 |
| mid | 1140 | 0.35 | 0.51 | -0.335 |
| small | 1629 | 0.48 | 0.40 | -0.720 |
| unknown | 5780 | 0.32 | 0.23 | -0.386 |
