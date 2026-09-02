# Composite residual rank — **2026-09-02**

Generated: 2026-09-02T19:21:56.789491-04:00
Prior snapshot (for returns): **2026-09-01**

## Y snapshot (v1 — breadth only)

- **p_risk_on:** 0.7934 (from % names up)
- **pct_up:** 0.6674
- **median_ret:** 0.30%
- **conviction:** 0.5868
- **n:** 11640
- note: price_derived breadth only (v1)

## Method (deliberately simple)

- **residual** = stock return − median stock return (same pair window)
- **composites:** SPEC_DURATION, QUALITY_DEFENSIVE, CROWDING, SIZE_TILT
- **pressure** = conviction × prior effects of composites given p_risk_on
- Ranking is **cross-sectional residual bias**, not an absolute SPY call
- Hand priors only — replace with audit weights later

CSV: `data/composite/2026-09-02_composite_rank.csv`

## Top 20 by residual pressure (favor when risk-on / current Y)

| Ticker | Sector | pressure | SPEC | QUAL | CROWD | SIZE | resid | beta | short |
|--------|--------|----------|------|------|-------|------|-------|------|-------|
| ADCT | Healthcare | +0.596 | 0.95 | 0.00 | 0.60 | 1.00 | +6.15% | high | elevated |
| WCT | Technology | +0.582 | 0.85 | 0.00 | 0.80 | 1.00 | -11.42% | high | very_high |
| NVAX | Healthcare | +0.575 | 0.95 | 0.00 | 0.80 | 0.80 | +1.67% | high | very_high |
| AQST | Healthcare | +0.575 | 0.95 | 0.00 | 0.80 | 0.80 | +2.37% | high | very_high |
| GPRO | Technology | +0.575 | 0.95 | 0.00 | 0.80 | 0.80 | +37.09% | high | very_high |
| ARCT | Healthcare | +0.575 | 0.95 | 0.00 | 0.80 | 0.80 | +2.84% | high | very_high |
| INBX | Healthcare | +0.575 | 0.95 | 0.00 | 0.80 | 0.80 | -0.06% | high | very_high |
| CHAI | Communication Serv | +0.561 | 0.85 | 0.00 | 0.60 | 1.00 | -6.19% | high | elevated |
| XHLD | Communication Serv | +0.561 | 0.85 | 0.00 | 0.60 | 1.00 | -2.22% | high | elevated |
| RCEL | Healthcare | +0.561 | 0.85 | 0.00 | 0.60 | 1.00 | +6.55% | high | elevated |
| TJGC | Communication Serv | +0.561 | 0.85 | 0.00 | 0.60 | 1.00 | -0.11% | high | elevated |
| SSM | Consumer Cyclical | +0.561 | 0.85 | 0.00 | 0.60 | 1.00 | +0.54% | high | elevated |
| DH | Healthcare | +0.561 | 0.85 | 0.00 | 0.60 | 1.00 | +15.25% | high | elevated |
| SST | Industrials | +0.561 | 0.85 | 0.00 | 0.60 | 1.00 | +5.68% | high | elevated |
| ATOM | Technology | +0.561 | 0.85 | 0.00 | 0.60 | 1.00 | +1.22% | high | very_high |
| DPRO | Technology | +0.561 | 0.85 | 0.00 | 0.60 | 1.00 | +5.46% | high | elevated |
| NCPL | Financial | +0.561 | 0.85 | 0.00 | 0.60 | 1.00 | +30.07% | high | elevated |
| CHOW | Technology | +0.561 | 0.85 | 0.00 | 0.60 | 1.00 | -8.30% | high | elevated |
| OPK | Healthcare | +0.554 | 0.95 | 0.00 | 0.60 | 0.80 | +10.88% | high | elevated |
| JANX | Healthcare | +0.554 | 0.95 | 0.00 | 0.60 | 0.80 | +3.98% | high | elevated |

## Bottom 15 (lowest pressure)

| Ticker | Sector | pressure | SPEC | QUAL | resid | beta |
|--------|--------|----------|------|------|-------|------|
| T | Communication Serv | -0.258 | 0.00 | 1.00 | -0.50% | low |
| ABBV | Healthcare | -0.258 | 0.00 | 1.00 | +0.36% | low |
| SAN | Financial | -0.258 | 0.00 | 1.00 | +2.27% | low |
| IBN | Financial | -0.258 | 0.00 | 1.00 | +0.99% | low |
| KO | Consumer Defensive | -0.258 | 0.00 | 1.00 | -0.03% | low |
| AEM | Basic Materials | -0.258 | 0.00 | 1.00 | +1.35% | low |
| IBM | Technology | -0.258 | 0.00 | 1.00 | -0.18% | low |
| PM | Consumer Defensive | -0.258 | 0.00 | 1.00 | +0.12% | low |
| RIO | Basic Materials | -0.258 | 0.00 | 1.00 | +0.57% | low |
| AMGN | Healthcare | -0.258 | 0.00 | 1.00 | +0.77% | low |
| MO | Consumer Defensive | -0.258 | 0.00 | 1.00 | -0.32% | low |
| CNQ | Energy | -0.258 | 0.00 | 1.00 | -0.30% | low |
| BP | Energy | -0.258 | 0.00 | 1.00 | -1.52% | low |
| MDT | Healthcare | -0.258 | 0.00 | 1.00 | -0.15% | low |
| GSK | Healthcare | -0.258 | 0.00 | 1.00 | -0.74% | low |

## Sector median pressure

| Sector | n | median pressure | median resid |
|--------|---|-----------------|--------------|
| Healthcare | 1063 | +0.287 | +0.67% |
| Technology | 794 | +0.241 | -0.19% |
| Communication Services | 256 | +0.241 | +0.38% |
| Basic Materials | 288 | +0.193 | +1.71% |
| Consumer Cyclical | 532 | +0.182 | +0.32% |
| Industrials | 712 | +0.182 | +0.02% |
| Real Estate | 250 | +0.174 | -0.30% |
| Consumer Defensive | 242 | +0.155 | -0.03% |
| Financial | 7142 | +0.143 | -0.04% |
| Energy | 252 | +0.054 | +0.04% |
| Utilities | 109 | -0.015 | -0.30% |

## Composite averages by size

| size | n | SPEC | QUAL | pressure |
|------|---|------|------|----------|
| large | 780 | 0.16 | 0.80 | -0.100 |
| mega | 169 | 0.14 | 0.85 | -0.169 |
| micro | 2163 | 0.51 | 0.30 | +0.314 |
| mid | 1189 | 0.36 | 0.51 | +0.117 |
| small | 1613 | 0.49 | 0.41 | +0.245 |
| unknown | 5726 | 0.32 | 0.25 | +0.129 |
