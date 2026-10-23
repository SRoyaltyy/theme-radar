# Composite residual rank — **2026-10-23**

Generated: 2026-10-23T17:33:53.214912-04:00
Prior snapshot (for returns): **2026-10-22**

## Y snapshot (v1 — breadth only)

- **p_risk_on:** 0.0 (from % names up)
- **pct_up:** 0.3135
- **median_ret:** -0.26%
- **conviction:** 1.0
- **n:** 11782
- note: price_derived breadth only (v1)

## Method (deliberately simple)

- **residual** = stock return − median stock return (same pair window)
- **composites:** SPEC_DURATION, QUALITY_DEFENSIVE, CROWDING, SIZE_TILT
- **pressure** = conviction × prior effects of composites given p_risk_on
- Ranking is **cross-sectional residual bias**, not an absolute SPY call
- Hand priors only — replace with audit weights later

CSV: `data/composite/2026-10-23_composite_rank.csv`

## Top 20 by residual pressure (favor when risk-on / current Y)

| Ticker | Sector | pressure | SPEC | QUAL | CROWD | SIZE | resid | beta | short |
|--------|--------|----------|------|------|-------|------|-------|------|-------|
| MO | Consumer Defensive | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -2.06% | low | low |
| MCD | Consumer Cyclical | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -1.39% | low | low |
| HSBC | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -1.06% | low | low |
| PSX | Energy | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.25% | low | low |
| WMT | Consumer Defensive | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.76% | low | low |
| MPC | Energy | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.19% | low | low |
| SYK | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.28% | low | low |
| HDB | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -1.30% | low | low |
| UL | Consumer Defensive | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.89% | low | low |
| JNJ | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -1.16% | low | low |
| PFE | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -1.03% | low | low |
| PEP | Consumer Defensive | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -1.95% | low | low |
| MRK | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -1.08% | low | low |
| UNH | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -1.37% | low | low |
| TD | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.15% | low | low |
| PDD | Consumer Cyclical | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.09% | low | low |
| CB | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -2.17% | low | low |
| SCHW | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.68% | low | low |
| PGR | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.42% | low | low |
| PG | Consumer Defensive | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -2.50% | low | low |

## Bottom 15 (lowest pressure)

| Ticker | Sector | pressure | SPEC | QUAL | resid | beta |
|--------|--------|----------|------|------|-------|------|
| CHPT | Consumer Cyclical | -1.790 | 0.95 | 0.00 | +1.96% | high |
| TBCH | Technology | -1.790 | 0.95 | 0.00 | +0.44% | high |
| KRRO | Healthcare | -1.790 | 0.95 | 0.00 | -0.33% | high |
| INGN | Healthcare | -1.730 | 0.95 | 0.00 | +1.11% | high |
| ELTX | Healthcare | -1.730 | 0.95 | 0.00 | -1.81% | high |
| GPUS | Industrials | -1.690 | 0.85 | 0.00 | +31.03% | high |
| AVBP | Healthcare | -1.670 | 0.95 | 0.00 | +9.63% | high |
| PACB | Healthcare | -1.670 | 0.95 | 0.00 | +2.68% | high |
| BETR | Financial | -1.670 | 0.95 | 0.00 | +1.10% | high |
| BMBL | Communication Serv | -1.670 | 0.95 | 0.00 | +0.59% | high |
| CNDT | Technology | -1.655 | 0.95 | 0.00 | +20.39% | high |
| PDYN | Technology | -1.630 | 0.85 | 0.00 | +1.63% | high |
| CRBP | Healthcare | -1.630 | 0.85 | 0.00 | -1.68% | high |
| SLNH | Financial | -1.630 | 0.85 | 0.00 | +4.03% | high |
| ORGO | Healthcare | -1.630 | 0.85 | 0.00 | -3.63% | high |

## Sector median pressure

| Sector | n | median pressure | median resid |
|--------|---|-----------------|--------------|
| Utilities | 107 | +0.045 | -0.49% |
| Energy | 252 | -0.205 | +2.99% |
| Financial | 7290 | -0.415 | +0.05% |
| Consumer Defensive | 240 | -0.458 | -1.09% |
| Real Estate | 248 | -0.505 | +0.10% |
| Industrials | 716 | -0.550 | -0.07% |
| Consumer Cyclical | 524 | -0.565 | -1.14% |
| Basic Materials | 296 | -0.627 | -0.38% |
| Communication Services | 255 | -0.700 | -0.56% |
| Technology | 800 | -0.705 | +0.26% |
| Healthcare | 1054 | -0.935 | -0.92% |

## Composite averages by size

| size | n | SPEC | QUAL | pressure |
|------|---|------|------|----------|
| large | 751 | 0.17 | 0.80 | +0.271 |
| mega | 163 | 0.15 | 0.83 | +0.456 |
| micro | 2268 | 0.52 | 0.28 | -0.940 |
| mid | 1131 | 0.36 | 0.51 | -0.349 |
| small | 1586 | 0.49 | 0.40 | -0.729 |
| unknown | 5883 | 0.32 | 0.24 | -0.378 |
