# Composite residual rank — **2026-11-19**

Generated: 2026-11-19T21:24:35.462253-05:00
Prior snapshot (for returns): **2026-11-18**

## Y snapshot (v1 — breadth only)

- **p_risk_on:** 0.0 (from % names up)
- **pct_up:** 0.1555
- **median_ret:** -1.57%
- **conviction:** 1.0
- **n:** 11759
- note: price_derived breadth only (v1)

## Method (deliberately simple)

- **residual** = stock return − median stock return (same pair window)
- **composites:** SPEC_DURATION, QUALITY_DEFENSIVE, CROWDING, SIZE_TILT
- **pressure** = conviction × prior effects of composites given p_risk_on
- Ranking is **cross-sectional residual bias**, not an absolute SPY call
- Hand priors only — replace with audit weights later

CSV: `data/composite/2026-11-19_composite_rank.csv`

## Top 20 by residual pressure (favor when risk-on / current Y)

| Ticker | Sector | pressure | SPEC | QUAL | CROWD | SIZE | resid | beta | short |
|--------|--------|----------|------|------|-------|------|-------|------|-------|
| SNY | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.68% | low | low |
| PG | Consumer Defensive | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.14% | low | low |
| PFE | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.28% | low | low |
| UL | Consumer Defensive | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.24% | low | low |
| PEP | Consumer Defensive | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.45% | low | low |
| SMFG | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.08% | low | low |
| ADP | Technology | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.14% | low | low |
| NVO | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.15% | low | low |
| DUK | Utilities | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.66% | low | low |
| PDD | Consumer Cyclical | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +12.61% | low | low |
| LOW | Consumer Cyclical | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.06% | low | low |
| AMGN | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.43% | low | low |
| CB | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.33% | low | low |
| MO | Consumer Defensive | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.50% | low | low |
| HSBC | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.02% | low | low |
| VZ | Communication Serv | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.73% | low | low |
| PM | Consumer Defensive | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -1.70% | low | low |
| WMT | Consumer Defensive | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.54% | low | low |
| NVS | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -1.00% | low | low |
| MFG | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -1.42% | low | low |

## Bottom 15 (lowest pressure)

| Ticker | Sector | pressure | SPEC | QUAL | resid | beta |
|--------|--------|----------|------|------|-------|------|
| LVWR | Consumer Cyclical | -1.790 | 0.95 | 0.00 | +77.25% | high |
| GLSI | Healthcare | -1.790 | 0.95 | 0.00 | -2.27% | high |
| CRDF | Healthcare | -1.690 | 0.85 | 0.00 | +7.52% | high |
| BMBL | Communication Serv | -1.670 | 0.95 | 0.00 | +1.57% | high |
| SPCE | Industrials | -1.630 | 0.85 | 0.00 | -4.26% | high |
| ENVX | Industrials | -1.630 | 0.85 | 0.00 | -11.27% | high |
| SERV | Industrials | -1.630 | 0.85 | 0.00 | -3.01% | high |
| ASPI | Basic Materials | -1.630 | 0.85 | 0.00 | -6.56% | high |
| PALI | Healthcare | -1.630 | 0.85 | 0.00 | +0.51% | high |
| ATOM | Technology | -1.630 | 0.85 | 0.00 | -3.37% | high |
| CABA | Healthcare | -1.630 | 0.85 | 0.00 | -2.24% | high |
| AKAN | Healthcare | -1.630 | 0.85 | 0.00 | -13.32% | high |
| TNXP | Healthcare | -1.630 | 0.85 | 0.00 | -8.00% | high |
| ABEO | Healthcare | -1.630 | 0.85 | 0.00 | -8.68% | high |
| VELO | Technology | -1.630 | 0.85 | 0.00 | -1.01% | high |

## Sector median pressure

| Sector | n | median pressure | median resid |
|--------|---|-----------------|--------------|
| Utilities | 103 | +0.120 | +0.34% |
| Energy | 252 | -0.215 | +0.54% |
| Financial | 7279 | -0.415 | +0.18% |
| Consumer Defensive | 239 | -0.485 | -0.25% |
| Real Estate | 246 | -0.528 | -0.16% |
| Industrials | 716 | -0.550 | -0.47% |
| Consumer Cyclical | 520 | -0.565 | -1.38% |
| Basic Materials | 298 | -0.627 | -1.35% |
| Communication Services | 252 | -0.700 | -1.26% |
| Technology | 800 | -0.752 | -1.06% |
| Healthcare | 1054 | -0.935 | -0.39% |

## Composite averages by size

| size | n | SPEC | QUAL | pressure |
|------|---|------|------|----------|
| large | 735 | 0.15 | 0.82 | +0.313 |
| mega | 155 | 0.14 | 0.84 | +0.491 |
| micro | 2348 | 0.52 | 0.26 | -0.962 |
| mid | 1098 | 0.34 | 0.53 | -0.304 |
| small | 1554 | 0.49 | 0.40 | -0.722 |
| unknown | 5869 | 0.32 | 0.23 | -0.387 |
