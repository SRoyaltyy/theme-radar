# Composite residual rank — **2026-10-20**

Generated: 2026-10-20T16:48:59.075268-04:00
Prior snapshot (for returns): **2026-10-19**

## Y snapshot (v1 — breadth only)

- **p_risk_on:** 0.801 (from % names up)
- **pct_up:** 0.6704
- **median_ret:** 0.36%
- **conviction:** 0.602
- **n:** 11757
- note: price_derived breadth only (v1)

## Method (deliberately simple)

- **residual** = stock return − median stock return (same pair window)
- **composites:** SPEC_DURATION, QUALITY_DEFENSIVE, CROWDING, SIZE_TILT
- **pressure** = conviction × prior effects of composites given p_risk_on
- Ranking is **cross-sectional residual bias**, not an absolute SPY call
- Hand priors only — replace with audit weights later

CSV: `data/composite/2026-10-20_composite_rank.csv`

## Top 20 by residual pressure (favor when risk-on / current Y)

| Ticker | Sector | pressure | SPEC | QUAL | CROWD | SIZE | resid | beta | short |
|--------|--------|----------|------|------|-------|------|-------|------|-------|
| BETR | Financial | +0.649 | 0.95 | 0.00 | 0.80 | 1.00 | +13.31% | high | very_high |
| DMRC | Technology | +0.627 | 0.95 | 0.00 | 0.60 | 1.00 | +8.05% | high | elevated |
| NMRA | Healthcare | +0.627 | 0.95 | 0.00 | 0.60 | 1.00 | -0.36% | high | elevated |
| BDTX | Healthcare | +0.627 | 0.95 | 0.00 | 0.60 | 1.00 | +14.00% | high | elevated |
| INGN | Healthcare | +0.627 | 0.95 | 0.00 | 0.60 | 1.00 | +1.78% | high | elevated |
| LHSW | Technology | +0.613 | 0.85 | 0.00 | 0.80 | 1.00 | +5.44% | high | very_high |
| NCPL | Financial | +0.613 | 0.85 | 0.00 | 0.80 | 1.00 | +23.57% | high | very_high |
| MAZE | Healthcare | +0.605 | 0.95 | 0.00 | 0.80 | 0.80 | +8.90% | high | very_high |
| BMBL | Communication Serv | +0.605 | 0.95 | 0.00 | 0.80 | 0.80 | -0.53% | high | very_high |
| SGMT | Healthcare | +0.605 | 0.95 | 0.00 | 0.80 | 0.80 | +9.57% | high | very_high |
| IRLA | Healthcare | +0.591 | 0.85 | 0.00 | 0.60 | 1.00 | +16.53% | high | elevated |
| CRBP | Healthcare | +0.591 | 0.85 | 0.00 | 0.60 | 1.00 | -1.26% | high | very_high |
| SERV | Industrials | +0.591 | 0.85 | 0.00 | 0.60 | 1.00 | -1.33% | high | very_high |
| AIRS | Healthcare | +0.591 | 0.85 | 0.00 | 0.60 | 1.00 | +3.64% | high | very_high |
| VELO | Technology | +0.591 | 0.85 | 0.00 | 0.60 | 1.00 | -2.29% | high | very_high |
| WATT | Technology | +0.591 | 0.85 | 0.00 | 0.60 | 1.00 | -2.28% | high | very_high |
| BKKT | Technology | +0.591 | 0.85 | 0.00 | 0.60 | 1.00 | -0.54% | high | very_high |
| OCGN | Healthcare | +0.591 | 0.85 | 0.00 | 0.60 | 1.00 | +2.17% | high | very_high |
| ATOM | Technology | +0.591 | 0.85 | 0.00 | 0.60 | 1.00 | -2.65% | high | very_high |
| DH | Healthcare | +0.591 | 0.85 | 0.00 | 0.60 | 1.00 | +2.37% | high | elevated |

## Bottom 15 (lowest pressure)

| Ticker | Sector | pressure | SPEC | QUAL | resid | beta |
|--------|--------|----------|------|------|-------|------|
| DHR | Healthcare | -0.272 | 0.00 | 1.00 | -0.45% | low |
| VLO | Energy | -0.272 | 0.00 | 1.00 | -0.34% | low |
| BP | Energy | -0.272 | 0.00 | 1.00 | -0.46% | low |
| LMT | Industrials | -0.272 | 0.00 | 1.00 | -0.27% | low |
| LLY | Healthcare | -0.272 | 0.00 | 1.00 | +3.13% | low |
| LIN | Basic Materials | -0.272 | 0.00 | 1.00 | -0.67% | low |
| RTX | Industrials | -0.272 | 0.00 | 1.00 | +0.28% | low |
| BABA | Consumer Cyclical | -0.272 | 0.00 | 1.00 | -0.32% | low |
| AZN | Healthcare | -0.272 | 0.00 | 1.00 | +2.61% | low |
| SO | Utilities | -0.272 | 0.00 | 1.00 | +1.25% | low |
| WMT | Consumer Defensive | -0.272 | 0.00 | 1.00 | -1.08% | low |
| SAN | Financial | -0.272 | 0.00 | 1.00 | +0.48% | low |
| MCD | Consumer Cyclical | -0.272 | 0.00 | 1.00 | +1.23% | low |
| GSK | Healthcare | -0.272 | 0.00 | 1.00 | +2.01% | low |
| CVS | Healthcare | -0.272 | 0.00 | 1.00 | +1.87% | low |

## Sector median pressure

| Sector | n | median pressure | median resid |
|--------|---|-----------------|--------------|
| Healthcare | 1053 | +0.328 | +2.16% |
| Technology | 799 | +0.254 | +0.65% |
| Communication Services | 253 | +0.254 | +0.72% |
| Basic Materials | 295 | +0.210 | -0.36% |
| Consumer Cyclical | 524 | +0.205 | +0.63% |
| Industrials | 716 | +0.199 | -0.02% |
| Real Estate | 248 | +0.183 | +1.51% |
| Consumer Defensive | 240 | +0.166 | +0.15% |
| Financial | 7270 | +0.150 | -0.12% |
| Energy | 252 | +0.074 | -0.41% |
| Utilities | 107 | -0.016 | +0.95% |

## Composite averages by size

| size | n | SPEC | QUAL | pressure |
|------|---|------|------|----------|
| large | 765 | 0.17 | 0.80 | -0.097 |
| mega | 163 | 0.15 | 0.83 | -0.164 |
| micro | 2258 | 0.52 | 0.28 | +0.340 |
| mid | 1118 | 0.36 | 0.52 | +0.124 |
| small | 1592 | 0.49 | 0.40 | +0.263 |
| unknown | 5861 | 0.32 | 0.24 | +0.137 |
