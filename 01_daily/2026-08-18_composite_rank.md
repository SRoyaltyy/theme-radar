# Composite residual rank — **2026-08-18**

Generated: 2026-08-18T17:42:46.533310-04:00
Prior snapshot (for returns): **2026-08-17**

## Y snapshot (v1 — breadth only)

- **p_risk_on:** 0.0 (from % names up)
- **pct_up:** 0.2973
- **median_ret:** -0.41%
- **conviction:** 1.0
- **n:** 11584
- note: price_derived breadth only (v1)

## Method (deliberately simple)

- **residual** = stock return − median stock return (same pair window)
- **composites:** SPEC_DURATION, QUALITY_DEFENSIVE, CROWDING, SIZE_TILT
- **pressure** = conviction × prior effects of composites given p_risk_on
- Ranking is **cross-sectional residual bias**, not an absolute SPY call
- Hand priors only — replace with audit weights later

CSV: `data/composite/2026-08-18_composite_rank.csv`

## Top 20 by residual pressure (favor when risk-on / current Y)

| Ticker | Sector | pressure | SPEC | QUAL | CROWD | SIZE | resid | beta | short |
|--------|--------|----------|------|------|-------|------|-------|------|-------|
| SHEL | Energy | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.83% | low | low |
| HDB | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.49% | low | low |
| NEM | Basic Materials | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -3.21% | low | low |
| CVX | Energy | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.91% | low | low |
| CVS | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.36% | low | low |
| KO | Consumer Defensive | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +2.52% | low | low |
| PFE | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.82% | low | low |
| AZN | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +2.45% | low | low |
| V | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.91% | low | low |
| BABA | Consumer Cyclical | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +3.16% | low | low |
| LIN | Basic Materials | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.33% | low | low |
| RY | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -1.07% | low | low |
| SAN | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -1.99% | low | low |
| SMFG | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -1.23% | low | low |
| HSBC | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.19% | low | low |
| SO | Utilities | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.17% | low | low |
| SNY | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.67% | low | low |
| UNH | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.02% | low | low |
| PGR | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +2.07% | low | low |
| PG | Consumer Defensive | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.64% | low | low |

## Bottom 15 (lowest pressure)

| Ticker | Sector | pressure | SPEC | QUAL | resid | beta |
|--------|--------|----------|------|------|-------|------|
| ZENA | Technology | -1.790 | 0.95 | 0.00 | -0.08% | high |
| ARCT | Healthcare | -1.790 | 0.95 | 0.00 | +1.27% | high |
| INO | Healthcare | -1.690 | 0.85 | 0.00 | +4.75% | high |
| SGMT | Healthcare | -1.670 | 0.95 | 0.00 | +1.84% | high |
| FDMT | Healthcare | -1.670 | 0.95 | 0.00 | +1.57% | high |
| ACHV | Healthcare | -1.670 | 0.95 | 0.00 | +0.67% | high |
| TNDM | Healthcare | -1.670 | 0.95 | 0.00 | +7.06% | high |
| RCEL | Healthcare | -1.630 | 0.85 | 0.00 | +25.09% | high |
| PFSA | Healthcare | -1.630 | 0.85 | 0.00 | +507.03% | high |
| HRTX | Healthcare | -1.630 | 0.85 | 0.00 | -5.84% | high |
| AGPU | Technology | -1.630 | 0.85 | 0.00 | -2.32% | high |
| IVF | Healthcare | -1.630 | 0.85 | 0.00 | -6.13% | high |
| SST | Industrials | -1.630 | 0.85 | 0.00 | -7.29% | high |
| RRGB | Consumer Cyclical | -1.630 | 0.85 | 0.00 | -3.18% | high |
| VERI | Technology | -1.630 | 0.85 | 0.00 | -7.85% | high |

## Sector median pressure

| Sector | n | median pressure | median resid |
|--------|---|-----------------|--------------|
| Utilities | 110 | +0.045 | +0.13% |
| Energy | 253 | -0.160 | +0.41% |
| Financial | 7086 | -0.415 | +0.06% |
| Consumer Defensive | 244 | -0.450 | +0.65% |
| Real Estate | 252 | -0.455 | +0.17% |
| Industrials | 708 | -0.505 | -1.35% |
| Basic Materials | 286 | -0.565 | -2.12% |
| Consumer Cyclical | 533 | -0.565 | -0.49% |
| Technology | 790 | -0.693 | -1.15% |
| Communication Services | 258 | -0.700 | -0.05% |
| Healthcare | 1064 | -0.850 | +0.41% |

## Composite averages by size

| size | n | SPEC | QUAL | pressure |
|------|---|------|------|----------|
| large | 801 | 0.17 | 0.80 | +0.271 |
| mega | 171 | 0.15 | 0.84 | +0.472 |
| micro | 2145 | 0.51 | 0.30 | -0.919 |
| mid | 1170 | 0.36 | 0.51 | -0.337 |
| small | 1614 | 0.48 | 0.41 | -0.710 |
| unknown | 5683 | 0.32 | 0.25 | -0.373 |
