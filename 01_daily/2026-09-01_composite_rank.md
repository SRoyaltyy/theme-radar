# Composite residual rank — **2026-09-01**

Generated: 2026-09-01T19:21:51.503109-04:00
Prior snapshot (for returns): **2026-08-31**

## Y snapshot (v1 — breadth only)

- **p_risk_on:** 0.0 (from % names up)
- **pct_up:** 0.1991
- **median_ret:** -0.74%
- **conviction:** 1.0
- **n:** 11635
- note: price_derived breadth only (v1)

## Method (deliberately simple)

- **residual** = stock return − median stock return (same pair window)
- **composites:** SPEC_DURATION, QUALITY_DEFENSIVE, CROWDING, SIZE_TILT
- **pressure** = conviction × prior effects of composites given p_risk_on
- Ranking is **cross-sectional residual bias**, not an absolute SPY call
- Hand priors only — replace with audit weights later

CSV: `data/composite/2026-09-01_composite_rank.csv`

## Top 20 by residual pressure (favor when risk-on / current Y)

| Ticker | Sector | pressure | SPEC | QUAL | CROWD | SIZE | resid | beta | short |
|--------|--------|----------|------|------|-------|------|-------|------|-------|
| ABT | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.55% | low | low |
| ABBV | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +2.13% | low | low |
| HDB | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.84% | low | low |
| MDT | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +2.28% | low | low |
| MFG | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.68% | low | low |
| SYK | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -1.23% | low | low |
| LMT | Industrials | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -2.24% | low | low |
| VZ | Communication Serv | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.30% | low | low |
| HSBC | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.99% | low | low |
| RIO | Basic Materials | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.12% | low | low |
| IBM | Technology | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.31% | low | low |
| NVO | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.28% | low | low |
| BMY | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.91% | low | low |
| V | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -1.02% | low | low |
| AMGN | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +2.66% | low | low |
| EQNR | Energy | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +4.08% | low | low |
| RTX | Industrials | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.50% | low | low |
| IBN | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.18% | low | low |
| NVS | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +6.79% | low | low |
| WMT | Consumer Defensive | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.74% | low | low |

## Bottom 15 (lowest pressure)

| Ticker | Sector | pressure | SPEC | QUAL | resid | beta |
|--------|--------|----------|------|------|-------|------|
| GPRO | Technology | -1.790 | 0.95 | 0.00 | +40.51% | high |
| YYGH | Industrials | -1.690 | 0.85 | 0.00 | +12.11% | high |
| WCT | Technology | -1.690 | 0.85 | 0.00 | +7.04% | high |
| ARCT | Healthcare | -1.670 | 0.95 | 0.00 | +10.70% | high |
| INBX | Healthcare | -1.670 | 0.95 | 0.00 | -0.87% | high |
| NVAX | Healthcare | -1.670 | 0.95 | 0.00 | +8.75% | high |
| RCEL | Healthcare | -1.630 | 0.85 | 0.00 | +0.44% | high |
| CHAI | Communication Serv | -1.630 | 0.85 | 0.00 | -9.78% | high |
| SSM | Consumer Cyclical | -1.630 | 0.85 | 0.00 | +78.35% | high |
| SST | Industrials | -1.630 | 0.85 | 0.00 | +27.53% | high |
| TROO | Financial | -1.630 | 0.85 | 0.00 | +3.83% | high |
| TJGC | Communication Serv | -1.630 | 0.85 | 0.00 | +0.15% | high |
| ATOM | Technology | -1.630 | 0.85 | 0.00 | -4.55% | high |
| NCPL | Financial | -1.630 | 0.85 | 0.00 | +10.46% | high |
| DPRO | Technology | -1.630 | 0.85 | 0.00 | +0.00% | high |

## Sector median pressure

| Sector | n | median pressure | median resid |
|--------|---|-----------------|--------------|
| Utilities | 109 | +0.045 | +0.87% |
| Energy | 252 | -0.180 | +1.58% |
| Financial | 7137 | -0.415 | +0.08% |
| Consumer Defensive | 242 | -0.450 | +0.21% |
| Real Estate | 250 | -0.505 | +0.39% |
| Industrials | 712 | -0.530 | -0.92% |
| Basic Materials | 288 | -0.542 | -1.87% |
| Consumer Cyclical | 532 | -0.552 | -0.80% |
| Communication Services | 256 | -0.700 | -0.57% |
| Technology | 794 | -0.700 | -1.70% |
| Healthcare | 1063 | -0.840 | +0.36% |

## Composite averages by size

| size | n | SPEC | QUAL | pressure |
|------|---|------|------|----------|
| large | 777 | 0.16 | 0.80 | +0.294 |
| mega | 167 | 0.14 | 0.85 | +0.489 |
| micro | 2175 | 0.51 | 0.30 | -0.913 |
| mid | 1178 | 0.35 | 0.51 | -0.334 |
| small | 1617 | 0.48 | 0.41 | -0.708 |
| unknown | 5721 | 0.32 | 0.24 | -0.375 |
