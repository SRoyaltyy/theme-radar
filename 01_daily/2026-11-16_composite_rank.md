# Composite residual rank — **2026-11-16**

Generated: 2026-11-16T23:00:51.025448-05:00
Prior snapshot (for returns): **2026-11-13**

## Y snapshot (v1 — breadth only)

- **p_risk_on:** 0.0 (from % names up)
- **pct_up:** 0.1745
- **median_ret:** -1.34%
- **conviction:** 1.0
- **n:** 11739
- note: price_derived breadth only (v1)

## Method (deliberately simple)

- **residual** = stock return − median stock return (same pair window)
- **composites:** SPEC_DURATION, QUALITY_DEFENSIVE, CROWDING, SIZE_TILT
- **pressure** = conviction × prior effects of composites given p_risk_on
- Ranking is **cross-sectional residual bias**, not an absolute SPY call
- Hand priors only — replace with audit weights later

CSV: `data/composite/2026-11-16_composite_rank.csv`

## Top 20 by residual pressure (favor when risk-on / current Y)

| Ticker | Sector | pressure | SPEC | QUAL | CROWD | SIZE | resid | beta | short |
|--------|--------|----------|------|------|-------|------|-------|------|-------|
| ABT | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.36% | low | low |
| ABBV | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.18% | low | low |
| UNH | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +2.46% | low | low |
| ADP | Technology | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +2.47% | low | low |
| VZ | Communication Serv | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.30% | low | low |
| MO | Consumer Defensive | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.67% | low | low |
| PM | Consumer Defensive | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.12% | low | low |
| PDD | Consumer Cyclical | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.25% | low | low |
| HSBC | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.30% | low | low |
| JNJ | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.22% | low | low |
| NVO | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.27% | low | low |
| SO | Utilities | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +2.47% | low | low |
| MPC | Energy | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -1.66% | low | low |
| VRTX | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.19% | low | low |
| MRK | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.89% | low | low |
| T | Communication Serv | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +2.15% | low | low |
| SYK | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.69% | low | low |
| PEP | Consumer Defensive | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +2.02% | low | low |
| XOM | Energy | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.84% | low | low |
| PFE | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.24% | low | low |

## Bottom 15 (lowest pressure)

| Ticker | Sector | pressure | SPEC | QUAL | resid | beta |
|--------|--------|----------|------|------|-------|------|
| INLF | Industrials | -1.690 | 0.85 | 0.00 | -22.19% | high |
| NUAI | Technology | -1.670 | 0.95 | 0.00 | -1.47% | high |
| BMBL | Communication Serv | -1.670 | 0.95 | 0.00 | +1.51% | high |
| SPCE | Industrials | -1.630 | 0.85 | 0.00 | -13.87% | high |
| VUZI | Technology | -1.630 | 0.85 | 0.00 | -9.77% | high |
| ABAT | Industrials | -1.630 | 0.85 | 0.00 | -8.39% | high |
| OCGN | Healthcare | -1.630 | 0.85 | 0.00 | -5.89% | high |
| NXH | Consumer Cyclical | -1.630 | 0.85 | 0.00 | -6.59% | high |
| GPRO | Technology | -1.630 | 0.85 | 0.00 | -1.83% | high |
| CABA | Healthcare | -1.630 | 0.85 | 0.00 | -11.94% | high |
| PAL | Industrials | -1.630 | 0.85 | 0.00 | +0.58% | high |
| XRX | Industrials | -1.630 | 0.85 | 0.00 | +1.34% | high |
| EU | Energy | -1.630 | 0.85 | 0.00 | -5.93% | high |
| GEMI | Financial | -1.630 | 0.85 | 0.00 | -6.64% | high |
| ONFO | Communication Serv | -1.630 | 0.85 | 0.00 | +6.54% | high |

## Sector median pressure

| Sector | n | median pressure | median resid |
|--------|---|-----------------|--------------|
| Utilities | 103 | +0.045 | +1.04% |
| Energy | 252 | -0.205 | -1.62% |
| Financial | 7262 | -0.415 | +0.19% |
| Consumer Defensive | 239 | -0.465 | +0.77% |
| Real Estate | 246 | -0.528 | +0.74% |
| Industrials | 715 | -0.550 | -0.68% |
| Consumer Cyclical | 520 | -0.565 | +0.07% |
| Basic Materials | 297 | -0.605 | -2.27% |
| Communication Services | 252 | -0.700 | +0.28% |
| Technology | 799 | -0.710 | -1.97% |
| Healthcare | 1054 | -0.925 | -1.36% |

## Composite averages by size

| size | n | SPEC | QUAL | pressure |
|------|---|------|------|----------|
| large | 746 | 0.16 | 0.81 | +0.291 |
| mega | 162 | 0.14 | 0.85 | +0.486 |
| micro | 2293 | 0.52 | 0.27 | -0.955 |
| mid | 1104 | 0.35 | 0.53 | -0.322 |
| small | 1578 | 0.49 | 0.40 | -0.723 |
| unknown | 5856 | 0.32 | 0.25 | -0.376 |
