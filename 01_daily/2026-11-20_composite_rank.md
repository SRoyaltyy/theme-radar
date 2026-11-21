# Composite residual rank — **2026-11-20**

Generated: 2026-11-20T21:26:35.757760-05:00
Prior snapshot (for returns): **2026-11-19**

## Y snapshot (v1 — breadth only)

- **p_risk_on:** 0.0 (from % names up)
- **pct_up:** 0.1669
- **median_ret:** -2.34%
- **conviction:** 1.0
- **n:** 11771
- note: price_derived breadth only (v1)

## Method (deliberately simple)

- **residual** = stock return − median stock return (same pair window)
- **composites:** SPEC_DURATION, QUALITY_DEFENSIVE, CROWDING, SIZE_TILT
- **pressure** = conviction × prior effects of composites given p_risk_on
- Ranking is **cross-sectional residual bias**, not an absolute SPY call
- Hand priors only — replace with audit weights later

CSV: `data/composite/2026-11-20_composite_rank.csv`

## Top 20 by residual pressure (favor when risk-on / current Y)

| Ticker | Sector | pressure | SPEC | QUAL | CROWD | SIZE | resid | beta | short |
|--------|--------|----------|------|------|-------|------|-------|------|-------|
| TMUS | Communication Serv | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +4.23% | low | low |
| TJX | Consumer Cyclical | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +2.49% | low | low |
| BRK-A | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.87% | low | low |
| BRK-B | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.98% | low | low |
| CVS | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +3.34% | low | low |
| T | Communication Serv | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +4.44% | low | low |
| CVX | Energy | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +3.24% | low | low |
| ADP | Technology | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +2.51% | low | low |
| PM | Consumer Defensive | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.08% | low | low |
| VZ | Communication Serv | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +3.96% | low | low |
| DUK | Utilities | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +3.05% | low | low |
| WMT | Consumer Defensive | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +3.85% | low | low |
| BMY | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +3.13% | low | low |
| PDD | Consumer Cyclical | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.36% | low | low |
| CB | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +2.75% | low | low |
| MRK | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +3.02% | low | low |
| PEP | Consumer Defensive | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +3.45% | low | low |
| PFE | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.83% | low | low |
| PGR | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +2.96% | low | low |
| MFG | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -2.67% | low | low |

## Bottom 15 (lowest pressure)

| Ticker | Sector | pressure | SPEC | QUAL | resid | beta |
|--------|--------|----------|------|------|-------|------|
| LVWR | Consumer Cyclical | -1.790 | 0.95 | 0.00 | +54.64% | high |
| GLSI | Healthcare | -1.790 | 0.95 | 0.00 | -0.39% | high |
| BMBL | Communication Serv | -1.670 | 0.95 | 0.00 | +2.00% | high |
| ABEO | Healthcare | -1.630 | 0.85 | 0.00 | +1.11% | high |
| GEMI | Financial | -1.630 | 0.85 | 0.00 | -7.02% | high |
| INSG | Technology | -1.630 | 0.85 | 0.00 | -9.17% | high |
| ABAT | Industrials | -1.630 | 0.85 | 0.00 | -6.86% | high |
| ABR | Real Estate | -1.630 | 0.85 | 0.00 | -4.87% | high |
| EDIT | Healthcare | -1.630 | 0.85 | 0.00 | -1.76% | high |
| PDYN | Technology | -1.630 | 0.85 | 0.00 | -10.21% | high |
| KYTX | Healthcare | -1.630 | 0.85 | 0.00 | -0.18% | high |
| BRUN | Technology | -1.630 | 0.85 | 0.00 | -12.50% | high |
| SLNH | Financial | -1.630 | 0.85 | 0.00 | -5.16% | high |
| VUZI | Technology | -1.630 | 0.85 | 0.00 | -6.83% | high |
| SERV | Industrials | -1.630 | 0.85 | 0.00 | -8.58% | high |

## Sector median pressure

| Sector | n | median pressure | median resid |
|--------|---|-----------------|--------------|
| Utilities | 104 | +0.087 | +1.90% |
| Energy | 252 | -0.225 | +0.04% |
| Consumer Defensive | 240 | -0.458 | +0.88% |
| Financial | 7289 | -0.470 | +0.27% |
| Real Estate | 246 | -0.530 | +1.47% |
| Consumer Cyclical | 520 | -0.565 | -0.07% |
| Industrials | 716 | -0.575 | -1.42% |
| Basic Materials | 298 | -0.680 | -2.46% |
| Communication Services | 252 | -0.700 | -0.33% |
| Technology | 800 | -0.770 | -3.45% |
| Healthcare | 1054 | -0.955 | -0.49% |

## Composite averages by size

| size | n | SPEC | QUAL | pressure |
|------|---|------|------|----------|
| large | 732 | 0.15 | 0.81 | +0.313 |
| mega | 150 | 0.13 | 0.82 | +0.481 |
| micro | 2373 | 0.52 | 0.26 | -0.969 |
| mid | 1083 | 0.34 | 0.53 | -0.307 |
| small | 1553 | 0.49 | 0.39 | -0.730 |
| unknown | 5880 | 0.32 | 0.20 | -0.417 |
