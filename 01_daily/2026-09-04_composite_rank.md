# Composite residual rank — **2026-09-04**

Generated: 2026-09-04T19:05:06.405202-04:00
Prior snapshot (for returns): **2026-09-03**

## Y snapshot (v1 — breadth only)

- **p_risk_on:** 0.2494 (from % names up)
- **pct_up:** 0.4498
- **median_ret:** 0.00%
- **conviction:** 0.5012
- **n:** 11646
- note: price_derived breadth only (v1)

## Method (deliberately simple)

- **residual** = stock return − median stock return (same pair window)
- **composites:** SPEC_DURATION, QUALITY_DEFENSIVE, CROWDING, SIZE_TILT
- **pressure** = conviction × prior effects of composites given p_risk_on
- Ranking is **cross-sectional residual bias**, not an absolute SPY call
- Hand priors only — replace with audit weights later

CSV: `data/composite/2026-09-04_composite_rank.csv`

## Top 20 by residual pressure (favor when risk-on / current Y)

| Ticker | Sector | pressure | SPEC | QUAL | CROWD | SIZE | resid | beta | short |
|--------|--------|----------|------|------|-------|------|-------|------|-------|
| BP | Energy | +0.188 | 0.00 | 1.00 | 0.00 | 0.00 | +0.53% | low | low |
| PM | Consumer Defensive | +0.188 | 0.00 | 1.00 | 0.00 | 0.00 | -1.96% | low | low |
| ABT | Healthcare | +0.188 | 0.00 | 1.00 | 0.00 | 0.00 | -0.42% | low | low |
| VRTX | Healthcare | +0.188 | 0.00 | 1.00 | 0.00 | 0.00 | -2.12% | low | low |
| RY | Financial | +0.188 | 0.00 | 1.00 | 0.00 | 0.00 | -0.70% | low | low |
| RIO | Basic Materials | +0.188 | 0.00 | 1.00 | 0.00 | 0.00 | +0.42% | low | low |
| DHR | Healthcare | +0.188 | 0.00 | 1.00 | 0.00 | 0.00 | -1.60% | low | low |
| RTX | Industrials | +0.188 | 0.00 | 1.00 | 0.00 | 0.00 | -0.66% | low | low |
| PDD | Consumer Cyclical | +0.188 | 0.00 | 1.00 | 0.00 | 0.00 | +0.71% | low | low |
| PEP | Consumer Defensive | +0.188 | 0.00 | 1.00 | 0.00 | 0.00 | -1.71% | low | low |
| PFE | Healthcare | +0.188 | 0.00 | 1.00 | 0.00 | 0.00 | -1.25% | low | low |
| PG | Consumer Defensive | +0.188 | 0.00 | 1.00 | 0.00 | 0.00 | -0.33% | low | low |
| PGR | Financial | +0.188 | 0.00 | 1.00 | 0.00 | 0.00 | -2.20% | low | low |
| AMGN | Healthcare | +0.188 | 0.00 | 1.00 | 0.00 | 0.00 | -1.55% | low | low |
| ENB | Energy | +0.188 | 0.00 | 1.00 | 0.00 | 0.00 | -0.85% | low | low |
| SAN | Financial | +0.188 | 0.00 | 1.00 | 0.00 | 0.00 | -0.80% | low | low |
| SCHW | Financial | +0.188 | 0.00 | 1.00 | 0.00 | 0.00 | -0.99% | low | low |
| EQNR | Energy | +0.188 | 0.00 | 1.00 | 0.00 | 0.00 | -1.34% | low | low |
| JNJ | Healthcare | +0.188 | 0.00 | 1.00 | 0.00 | 0.00 | -1.15% | low | low |
| HSBC | Financial | +0.188 | 0.00 | 1.00 | 0.00 | 0.00 | +0.61% | low | unknown |

## Bottom 15 (lowest pressure)

| Ticker | Sector | pressure | SPEC | QUAL | resid | beta |
|--------|--------|----------|------|------|-------|------|
| CHPT | Consumer Cyclical | -0.450 | 0.95 | 0.00 | +8.92% | high |
| WCT | Technology | -0.424 | 0.85 | 0.00 | +5.11% | high |
| INO | Healthcare | -0.424 | 0.85 | 0.00 | +5.15% | high |
| NVAX | Healthcare | -0.419 | 0.95 | 0.00 | -1.16% | high |
| PROK | Healthcare | -0.419 | 0.95 | 0.00 | +4.69% | high |
| GPRO | Technology | -0.419 | 0.95 | 0.00 | +22.30% | high |
| ARCT | Healthcare | -0.419 | 0.95 | 0.00 | +1.67% | high |
| RCEL | Healthcare | -0.409 | 0.85 | 0.00 | +2.38% | high |
| NAKA | Financial | -0.409 | 0.85 | 0.00 | -2.17% | high |
| DH | Healthcare | -0.409 | 0.85 | 0.00 | +0.96% | high |
| DPRO | Technology | -0.409 | 0.85 | 0.00 | -4.82% | high |
| SST | Industrials | -0.409 | 0.85 | 0.00 | +1.86% | high |
| XHLD | Communication Serv | -0.409 | 0.85 | 0.00 | +0.11% | high |
| ADIL | Healthcare | -0.409 | 0.85 | 0.00 | +6.91% | high |
| TJGC | Communication Serv | -0.409 | 0.85 | 0.00 | +5.58% | high |

## Sector median pressure

| Sector | n | median pressure | median resid |
|--------|---|-----------------|--------------|
| Utilities | 109 | +0.014 | +0.00% |
| Energy | 252 | -0.042 | -0.39% |
| Financial | 7147 | -0.104 | -0.02% |
| Consumer Defensive | 242 | -0.115 | -0.06% |
| Real Estate | 250 | -0.127 | +0.05% |
| Consumer Cyclical | 532 | -0.133 | +0.52% |
| Industrials | 713 | -0.133 | +0.75% |
| Basic Materials | 288 | -0.139 | -0.36% |
| Communication Services | 256 | -0.176 | -0.53% |
| Technology | 794 | -0.176 | +0.00% |
| Healthcare | 1063 | -0.210 | +0.00% |

## Composite averages by size

| size | n | SPEC | QUAL | pressure |
|------|---|------|------|----------|
| large | 783 | 0.17 | 0.80 | +0.073 |
| mega | 171 | 0.14 | 0.85 | +0.123 |
| micro | 2163 | 0.51 | 0.30 | -0.229 |
| mid | 1179 | 0.36 | 0.51 | -0.084 |
| small | 1624 | 0.49 | 0.41 | -0.178 |
| unknown | 5726 | 0.32 | 0.25 | -0.094 |
