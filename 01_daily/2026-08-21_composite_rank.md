# Composite residual rank — **2026-08-21**

Generated: 2026-08-21T17:43:19.551081-04:00
Prior snapshot (for returns): **2026-08-20**

## Y snapshot (v1 — breadth only)

- **p_risk_on:** 0.7752 (from % names up)
- **pct_up:** 0.6601
- **median_ret:** 0.38%
- **conviction:** 0.5504
- **n:** 11623
- note: price_derived breadth only (v1)

## Method (deliberately simple)

- **residual** = stock return − median stock return (same pair window)
- **composites:** SPEC_DURATION, QUALITY_DEFENSIVE, CROWDING, SIZE_TILT
- **pressure** = conviction × prior effects of composites given p_risk_on
- Ranking is **cross-sectional residual bias**, not an absolute SPY call
- Hand priors only — replace with audit weights later

CSV: `data/composite/2026-08-21_composite_rank.csv`

## Top 20 by residual pressure (favor when risk-on / current Y)

| Ticker | Sector | pressure | SPEC | QUAL | CROWD | SIZE | resid | beta | short |
|--------|--------|----------|------|------|-------|------|-------|------|-------|
| BTCT | Technology | +0.512 | 0.85 | 0.00 | 0.80 | 1.00 | -22.83% | high | very_high |
| PROK | Healthcare | +0.506 | 0.95 | 0.00 | 0.80 | 0.80 | +13.00% | high | very_high |
| SDGR | Healthcare | +0.506 | 0.95 | 0.00 | 0.80 | 0.80 | +0.28% | high | very_high |
| SBET | Financial | +0.506 | 0.95 | 0.00 | 0.80 | 0.80 | +3.84% | high | very_high |
| FDMT | Healthcare | +0.506 | 0.95 | 0.00 | 0.80 | 0.80 | -2.06% | high | very_high |
| ARCT | Healthcare | +0.506 | 0.95 | 0.00 | 0.80 | 0.80 | +22.00% | high | very_high |
| BTCS | Financial | +0.494 | 0.85 | 0.00 | 0.60 | 1.00 | +2.67% | high | elevated |
| XGN | Healthcare | +0.494 | 0.85 | 0.00 | 0.60 | 1.00 | +1.42% | high | elevated |
| ADIL | Healthcare | +0.494 | 0.85 | 0.00 | 0.60 | 1.00 | +5.04% | high | elevated |
| XOS | Industrials | +0.494 | 0.85 | 0.00 | 0.60 | 1.00 | -6.29% | high | elevated |
| BEEM | Technology | +0.494 | 0.85 | 0.00 | 0.60 | 1.00 | +15.06% | high | elevated |
| RCEL | Healthcare | +0.494 | 0.85 | 0.00 | 0.60 | 1.00 | -0.68% | high | elevated |
| VERI | Technology | +0.494 | 0.85 | 0.00 | 0.60 | 1.00 | +2.00% | high | very_high |
| ANY | Financial | +0.494 | 0.85 | 0.00 | 0.60 | 1.00 | +28.83% | high | elevated |
| CAN | Technology | +0.494 | 0.85 | 0.00 | 0.60 | 1.00 | +24.62% | high | elevated |
| JELD | Industrials | +0.494 | 0.85 | 0.00 | 0.60 | 1.00 | +10.20% | high | elevated |
| NAKA | Financial | +0.494 | 0.85 | 0.00 | 0.60 | 1.00 | +11.68% | high | elevated |
| PFSA | Healthcare | +0.494 | 0.85 | 0.00 | 0.60 | 1.00 | -28.25% | high | elevated |
| PEPG | Healthcare | +0.494 | 0.85 | 0.00 | 0.60 | 1.00 | +2.91% | high | elevated |
| AIRS | Healthcare | +0.494 | 0.85 | 0.00 | 0.60 | 1.00 | +2.24% | high | very_high |

## Bottom 15 (lowest pressure)

| Ticker | Sector | pressure | SPEC | QUAL | resid | beta |
|--------|--------|----------|------|------|-------|------|
| ABBV | Healthcare | -0.227 | 0.00 | 1.00 | +0.82% | low |
| NEE | Utilities | -0.227 | 0.00 | 1.00 | -2.00% | low |
| MA | Financial | -0.227 | 0.00 | 1.00 | +0.80% | low |
| MCD | Consumer Cyclical | -0.227 | 0.00 | 1.00 | +0.30% | low |
| TD | Financial | -0.227 | 0.00 | 1.00 | -0.12% | low |
| GSK | Healthcare | -0.227 | 0.00 | 1.00 | +0.49% | low |
| HDB | Financial | -0.227 | 0.00 | 1.00 | +0.73% | low |
| PGR | Financial | -0.227 | 0.00 | 1.00 | -0.86% | low |
| PM | Consumer Defensive | -0.227 | 0.00 | 1.00 | -2.10% | low |
| MFG | Financial | -0.227 | 0.00 | 1.00 | +1.10% | low |
| TTE | Energy | -0.227 | 0.00 | 1.00 | -1.49% | low |
| EQNR | Energy | -0.227 | 0.00 | 1.00 | -0.38% | low |
| V | Financial | -0.227 | 0.00 | 1.00 | +1.07% | low |
| ENB | Energy | -0.227 | 0.00 | 1.00 | -1.42% | low |
| CVS | Healthcare | -0.227 | 0.00 | 1.00 | -1.05% | low |

## Sector median pressure

| Sector | n | median pressure | median resid |
|--------|---|-----------------|--------------|
| Healthcare | 1064 | +0.256 | +0.38% |
| Technology | 791 | +0.212 | +0.32% |
| Communication Services | 258 | +0.212 | +0.01% |
| Basic Materials | 287 | +0.176 | +1.45% |
| Consumer Defensive | 244 | +0.164 | +0.50% |
| Consumer Cyclical | 533 | +0.161 | +0.63% |
| Industrials | 709 | +0.153 | +0.26% |
| Real Estate | 252 | +0.136 | -0.38% |
| Financial | 7122 | +0.126 | -0.05% |
| Energy | 253 | +0.062 | -0.37% |
| Utilities | 110 | -0.014 | -1.49% |

## Composite averages by size

| size | n | SPEC | QUAL | pressure |
|------|---|------|------|----------|
| large | 802 | 0.18 | 0.79 | -0.080 |
| mega | 169 | 0.15 | 0.83 | -0.141 |
| micro | 2139 | 0.51 | 0.30 | +0.278 |
| mid | 1174 | 0.36 | 0.51 | +0.106 |
| small | 1625 | 0.49 | 0.40 | +0.217 |
| unknown | 5714 | 0.32 | 0.24 | +0.118 |
