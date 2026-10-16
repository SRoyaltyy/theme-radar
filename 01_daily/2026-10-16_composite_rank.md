# Composite residual rank — **2026-10-16**

Generated: 2026-10-16T16:52:55.565295-04:00
Prior snapshot (for returns): **2026-10-15**

## Y snapshot (v1 — breadth only)

- **p_risk_on:** 0.0 (from % names up)
- **pct_up:** 0.2802
- **median_ret:** -0.63%
- **conviction:** 1.0
- **n:** 11764
- note: price_derived breadth only (v1)

## Method (deliberately simple)

- **residual** = stock return − median stock return (same pair window)
- **composites:** SPEC_DURATION, QUALITY_DEFENSIVE, CROWDING, SIZE_TILT
- **pressure** = conviction × prior effects of composites given p_risk_on
- Ranking is **cross-sectional residual bias**, not an absolute SPY call
- Hand priors only — replace with audit weights later

CSV: `data/composite/2026-10-16_composite_rank.csv`

## Top 20 by residual pressure (favor when risk-on / current Y)

| Ticker | Sector | pressure | SPEC | QUAL | CROWD | SIZE | resid | beta | short |
|--------|--------|----------|------|------|-------|------|-------|------|-------|
| VLO | Energy | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.77% | low | low |
| LIN | Basic Materials | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.68% | low | low |
| SMFG | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.59% | low | low |
| LLY | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.06% | low | low |
| RTX | Industrials | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +4.36% | low | low |
| AMGN | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.27% | low | low |
| VRTX | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -1.14% | low | low |
| BABA | Consumer Cyclical | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -1.19% | low | low |
| T | Communication Serv | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.37% | low | low |
| MCD | Consumer Cyclical | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.82% | low | low |
| AZN | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.13% | low | low |
| HDB | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.95% | low | low |
| RIO | Basic Materials | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.75% | low | low |
| BMY | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.73% | low | low |
| LMT | Industrials | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +4.28% | low | low |
| DHR | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.44% | low | low |
| RY | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.20% | low | low |
| SAN | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.56% | low | low |
| VZ | Communication Serv | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.51% | low | low |
| BUD | Consumer Defensive | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +2.24% | low | low |

## Bottom 15 (lowest pressure)

| Ticker | Sector | pressure | SPEC | QUAL | resid | beta |
|--------|--------|----------|------|------|-------|------|
| LHSW | Technology | -1.690 | 0.85 | 0.00 | +46.46% | high |
| NCPL | Financial | -1.690 | 0.85 | 0.00 | +10.22% | high |
| ABAT | Industrials | -1.630 | 0.85 | 0.00 | -5.10% | high |
| OCGN | Healthcare | -1.630 | 0.85 | 0.00 | -3.08% | high |
| TNXP | Healthcare | -1.630 | 0.85 | 0.00 | -5.29% | high |
| CABA | Healthcare | -1.630 | 0.85 | 0.00 | -8.40% | high |
| ARCT | Healthcare | -1.630 | 0.85 | 0.00 | -7.62% | high |
| ORGO | Healthcare | -1.630 | 0.85 | 0.00 | -9.28% | high |
| BYRN | Industrials | -1.630 | 0.85 | 0.00 | +1.88% | high |
| CPOP | Communication Serv | -1.630 | 0.85 | 0.00 | +3.58% | high |
| CRBP | Healthcare | -1.630 | 0.85 | 0.00 | +5.02% | high |
| SERV | Industrials | -1.630 | 0.85 | 0.00 | -6.82% | high |
| VUZI | Technology | -1.630 | 0.85 | 0.00 | -0.76% | high |
| ATOM | Technology | -1.630 | 0.85 | 0.00 | -6.88% | high |
| LXEO | Healthcare | -1.630 | 0.85 | 0.00 | -3.72% | high |

## Sector median pressure

| Sector | n | median pressure | median resid |
|--------|---|-----------------|--------------|
| Utilities | 107 | +0.045 | +1.63% |
| Energy | 252 | -0.205 | +2.32% |
| Financial | 7271 | -0.415 | +0.25% |
| Consumer Defensive | 241 | -0.485 | +0.63% |
| Real Estate | 248 | -0.505 | +0.44% |
| Consumer Cyclical | 526 | -0.567 | -0.53% |
| Industrials | 717 | -0.570 | -0.52% |
| Basic Materials | 294 | -0.580 | +0.41% |
| Communication Services | 254 | -0.700 | -1.06% |
| Technology | 799 | -0.700 | -2.83% |
| Healthcare | 1055 | -0.935 | -2.48% |

## Composite averages by size

| size | n | SPEC | QUAL | pressure |
|------|---|------|------|----------|
| large | 761 | 0.17 | 0.80 | +0.270 |
| mega | 161 | 0.16 | 0.82 | +0.443 |
| micro | 2259 | 0.52 | 0.28 | -0.941 |
| mid | 1110 | 0.35 | 0.52 | -0.334 |
| small | 1615 | 0.49 | 0.40 | -0.725 |
| unknown | 5858 | 0.32 | 0.24 | -0.380 |
