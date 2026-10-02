# Composite residual rank — **2026-10-02**

Generated: 2026-10-02T16:53:06.135998-04:00
Prior snapshot (for returns): **2026-10-01**

## Y snapshot (v1 — breadth only)

- **p_risk_on:** 0.6905 (from % names up)
- **pct_up:** 0.6262
- **median_ret:** 0.36%
- **conviction:** 0.3809
- **n:** 11709
- note: price_derived breadth only (v1)

## Method (deliberately simple)

- **residual** = stock return − median stock return (same pair window)
- **composites:** SPEC_DURATION, QUALITY_DEFENSIVE, CROWDING, SIZE_TILT
- **pressure** = conviction × prior effects of composites given p_risk_on
- Ranking is **cross-sectional residual bias**, not an absolute SPY call
- Hand priors only — replace with audit weights later

CSV: `data/composite/2026-10-02_composite_rank.csv`

## Top 20 by residual pressure (favor when risk-on / current Y)

| Ticker | Sector | pressure | SPEC | QUAL | CROWD | SIZE | resid | beta | short |
|--------|--------|----------|------|------|-------|------|-------|------|-------|
| DMRC | Technology | +0.251 | 0.95 | 0.00 | 0.60 | 1.00 | -6.28% | high | elevated |
| BIRD | Technology | +0.245 | 0.85 | 0.00 | 0.80 | 1.00 | -3.80% | high | very_high |
| PACB | Healthcare | +0.242 | 0.95 | 0.00 | 0.80 | 0.80 | +0.83% | high | very_high |
| WOLF | Technology | +0.242 | 0.95 | 0.00 | 0.80 | 0.80 | +12.82% | high | very_high |
| HUCK | Technology | +0.237 | 0.85 | 0.00 | 0.60 | 1.00 | -1.60% | high | very_high |
| TEAD | Communication Serv | +0.237 | 0.85 | 0.00 | 0.60 | 1.00 | +3.34% | high | elevated |
| TDUP | Consumer Cyclical | +0.237 | 0.85 | 0.00 | 0.60 | 1.00 | +1.52% | high | very_high |
| NXH | Consumer Cyclical | +0.237 | 0.85 | 0.00 | 0.60 | 1.00 | -2.84% | high | very_high |
| VERI | Technology | +0.237 | 0.85 | 0.00 | 0.60 | 1.00 | -0.36% | high | very_high |
| IPSC | Healthcare | +0.237 | 0.85 | 0.00 | 0.60 | 1.00 | -5.33% | high | very_high |
| QTEX | Technology | +0.237 | 0.85 | 0.00 | 0.60 | 1.00 | +40.66% | high | elevated |
| EYPT | Healthcare | +0.237 | 0.85 | 0.00 | 0.60 | 1.00 | +0.26% | high | very_high |
| CRBP | Healthcare | +0.237 | 0.85 | 0.00 | 0.60 | 1.00 | -3.67% | high | very_high |
| OM | Healthcare | +0.237 | 0.85 | 0.00 | 0.60 | 1.00 | +5.24% | high | elevated |
| ATOS | Healthcare | +0.237 | 0.85 | 0.00 | 0.60 | 1.00 | +2.72% | high | elevated |
| XOS | Industrials | +0.237 | 0.85 | 0.00 | 0.60 | 1.00 | +4.40% | high | elevated |
| TNXP | Healthcare | +0.237 | 0.85 | 0.00 | 0.60 | 1.00 | -3.83% | high | very_high |
| CD | Financial | +0.234 | 0.95 | 0.00 | 0.60 | 0.80 | -0.36% | high | elevated |
| ACVA | Consumer Cyclical | +0.234 | 0.95 | 0.00 | 0.60 | 0.80 | -0.36% | high | elevated |
| AZTA | Healthcare | +0.234 | 0.95 | 0.00 | 0.60 | 0.80 | +12.02% | high | elevated |

## Bottom 15 (lowest pressure)

| Ticker | Sector | pressure | SPEC | QUAL | resid | beta |
|--------|--------|----------|------|------|-------|------|
| NEM | Basic Materials | -0.109 | 0.00 | 1.00 | +0.41% | low |
| SAN | Financial | -0.109 | 0.00 | 1.00 | +0.24% | low |
| UL | Consumer Defensive | -0.109 | 0.00 | 1.00 | -0.16% | low |
| VRTX | Healthcare | -0.109 | 0.00 | 1.00 | -0.76% | low |
| DHR | Healthcare | -0.109 | 0.00 | 1.00 | +0.72% | low |
| SHEL | Energy | -0.109 | 0.00 | 1.00 | +0.29% | low |
| TM | Consumer Cyclical | -0.109 | 0.00 | 1.00 | -1.37% | low |
| WMT | Consumer Defensive | -0.109 | 0.00 | 1.00 | -0.36% | low |
| BRK-B | Financial | -0.109 | 0.00 | 1.00 | +0.07% | low |
| CVX | Energy | -0.109 | 0.00 | 1.00 | -0.56% | low |
| TMUS | Communication Serv | -0.109 | 0.00 | 1.00 | +0.82% | low |
| AMGN | Healthcare | -0.109 | 0.00 | 1.00 | -1.40% | low |
| MPC | Energy | -0.109 | 0.00 | 1.00 | +0.16% | low |
| KO | Consumer Defensive | -0.109 | 0.00 | 1.00 | -0.88% | low |
| TTE | Energy | -0.109 | 0.00 | 1.00 | -0.49% | low |

## Sector median pressure

| Sector | n | median pressure | median resid |
|--------|---|-----------------|--------------|
| Healthcare | 1053 | +0.131 | -0.36% |
| Technology | 795 | +0.102 | -0.19% |
| Communication Services | 256 | +0.102 | -0.36% |
| Consumer Cyclical | 529 | +0.082 | -0.33% |
| Basic Materials | 294 | +0.082 | +0.20% |
| Industrials | 719 | +0.080 | +0.52% |
| Real Estate | 247 | +0.073 | -0.10% |
| Consumer Defensive | 241 | +0.065 | +0.08% |
| Financial | 7216 | +0.060 | +0.02% |
| Energy | 252 | +0.030 | +0.26% |
| Utilities | 107 | -0.006 | +0.32% |

## Composite averages by size

| size | n | SPEC | QUAL | pressure |
|------|---|------|------|----------|
| large | 764 | 0.17 | 0.79 | -0.040 |
| mega | 159 | 0.15 | 0.83 | -0.068 |
| micro | 2201 | 0.51 | 0.29 | +0.135 |
| mid | 1143 | 0.36 | 0.52 | +0.049 |
| small | 1641 | 0.49 | 0.40 | +0.105 |
| unknown | 5801 | 0.32 | 0.23 | +0.056 |
