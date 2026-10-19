# Composite residual rank — **2026-10-19**

Generated: 2026-10-19T16:52:54.606742-04:00
Prior snapshot (for returns): **2026-10-16**

## Y snapshot (v1 — breadth only)

- **p_risk_on:** 0.2028 (from % names up)
- **pct_up:** 0.4311
- **median_ret:** -0.05%
- **conviction:** 0.5943
- **n:** 11755
- note: price_derived breadth only (v1)

## Method (deliberately simple)

- **residual** = stock return − median stock return (same pair window)
- **composites:** SPEC_DURATION, QUALITY_DEFENSIVE, CROWDING, SIZE_TILT
- **pressure** = conviction × prior effects of composites given p_risk_on
- Ranking is **cross-sectional residual bias**, not an absolute SPY call
- Hand priors only — replace with audit weights later

CSV: `data/composite/2026-10-19_composite_rank.csv`

## Top 20 by residual pressure (favor when risk-on / current Y)

| Ticker | Sector | pressure | SPEC | QUAL | CROWD | SIZE | resid | beta | short |
|--------|--------|----------|------|------|-------|------|-------|------|-------|
| ABT | Healthcare | +0.265 | 0.00 | 1.00 | 0.00 | 0.00 | -0.74% | low | low |
| RY | Financial | +0.265 | 0.00 | 1.00 | 0.00 | 0.00 | -0.71% | low | low |
| ABBV | Healthcare | +0.265 | 0.00 | 1.00 | 0.00 | 0.00 | -0.91% | low | low |
| CVS | Healthcare | +0.265 | 0.00 | 1.00 | 0.00 | 0.00 | +0.39% | low | low |
| RIO | Basic Materials | +0.265 | 0.00 | 1.00 | 0.00 | 0.00 | -0.86% | low | low |
| SO | Utilities | +0.265 | 0.00 | 1.00 | 0.00 | 0.00 | -2.05% | low | low |
| JNJ | Healthcare | +0.265 | 0.00 | 1.00 | 0.00 | 0.00 | -0.65% | low | low |
| PFE | Healthcare | +0.265 | 0.00 | 1.00 | 0.00 | 0.00 | -0.43% | low | low |
| T | Communication Serv | +0.265 | 0.00 | 1.00 | 0.00 | 0.00 | -0.98% | low | low |
| BP | Energy | +0.265 | 0.00 | 1.00 | 0.00 | 0.00 | -1.49% | low | low |
| TM | Consumer Cyclical | +0.265 | 0.00 | 1.00 | 0.00 | 0.00 | -0.24% | low | low |
| MDT | Healthcare | +0.265 | 0.00 | 1.00 | 0.00 | 0.00 | -2.04% | low | low |
| NVS | Healthcare | +0.265 | 0.00 | 1.00 | 0.00 | 0.00 | -0.23% | low | low |
| NVO | Healthcare | +0.265 | 0.00 | 1.00 | 0.00 | 0.00 | -1.01% | low | low |
| IBN | Financial | +0.265 | 0.00 | 1.00 | 0.00 | 0.00 | -1.65% | low | low |
| BUD | Consumer Defensive | +0.265 | 0.00 | 1.00 | 0.00 | 0.00 | +0.34% | low | low |
| IBM | Technology | +0.265 | 0.00 | 1.00 | 0.00 | 0.00 | +1.88% | low | low |
| VLO | Energy | +0.265 | 0.00 | 1.00 | 0.00 | 0.00 | -2.52% | low | low |
| HSBC | Financial | +0.265 | 0.00 | 1.00 | 0.00 | 0.00 | -1.66% | low | low |
| BTI | Consumer Defensive | +0.265 | 0.00 | 1.00 | 0.00 | 0.00 | -2.44% | low | low |

## Bottom 15 (lowest pressure)

| Ticker | Sector | pressure | SPEC | QUAL | resid | beta |
|--------|--------|----------|------|------|-------|------|
| LHSW | Technology | -0.597 | 0.85 | 0.00 | -1.38% | high |
| BMBL | Communication Serv | -0.590 | 0.95 | 0.00 | +0.38% | high |
| UNCY | Healthcare | -0.576 | 0.85 | 0.00 | +4.51% | high |
| ABAT | Industrials | -0.576 | 0.85 | 0.00 | -1.98% | high |
| AIRS | Healthcare | -0.576 | 0.85 | 0.00 | -1.53% | high |
| WATT | Technology | -0.576 | 0.85 | 0.00 | +3.55% | high |
| AIRO | Industrials | -0.576 | 0.85 | 0.00 | -0.14% | high |
| CABA | Healthcare | -0.576 | 0.85 | 0.00 | +5.01% | high |
| EYPT | Healthcare | -0.576 | 0.85 | 0.00 | -85.24% | high |
| LFMD | Healthcare | -0.576 | 0.85 | 0.00 | -3.80% | high |
| SERV | Industrials | -0.576 | 0.85 | 0.00 | -4.60% | high |
| BKKT | Technology | -0.576 | 0.85 | 0.00 | -1.56% | high |
| DH | Healthcare | -0.576 | 0.85 | 0.00 | +10.05% | high |
| TNXP | Healthcare | -0.576 | 0.85 | 0.00 | -5.09% | high |
| PDYN | Technology | -0.576 | 0.85 | 0.00 | -1.01% | high |

## Sector median pressure

| Sector | n | median pressure | median resid |
|--------|---|-----------------|--------------|
| Utilities | 107 | +0.016 | -1.66% |
| Energy | 252 | -0.076 | -0.46% |
| Financial | 7268 | -0.147 | +0.03% |
| Consumer Defensive | 240 | -0.164 | -0.75% |
| Real Estate | 248 | -0.185 | -1.69% |
| Industrials | 716 | -0.194 | -0.41% |
| Basic Materials | 295 | -0.205 | -0.55% |
| Consumer Cyclical | 524 | -0.205 | -0.45% |
| Communication Services | 253 | -0.247 | -0.29% |
| Technology | 799 | -0.247 | +0.76% |
| Healthcare | 1053 | -0.330 | +0.36% |

## Composite averages by size

| size | n | SPEC | QUAL | pressure |
|------|---|------|------|----------|
| large | 746 | 0.17 | 0.80 | +0.099 |
| mega | 162 | 0.15 | 0.83 | +0.162 |
| micro | 2260 | 0.52 | 0.28 | -0.333 |
| mid | 1111 | 0.36 | 0.52 | -0.118 |
| small | 1611 | 0.49 | 0.40 | -0.256 |
| unknown | 5865 | 0.32 | 0.24 | -0.133 |
