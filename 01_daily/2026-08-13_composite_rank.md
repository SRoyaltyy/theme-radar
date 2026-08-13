# Composite residual rank — **2026-08-13**

Generated: 2026-08-13T18:06:13.540388-04:00
Prior snapshot (for returns): **2026-08-12**

## Y snapshot (v1 — breadth only)

- **p_risk_on:** 0.7463 (from % names up)
- **pct_up:** 0.6485
- **median_ret:** 0.26%
- **conviction:** 0.4925
- **n:** 11579
- note: price_derived breadth only (v1)

## Method (deliberately simple)

- **residual** = stock return − median stock return (same pair window)
- **composites:** SPEC_DURATION, QUALITY_DEFENSIVE, CROWDING, SIZE_TILT
- **pressure** = conviction × prior effects of composites given p_risk_on
- Ranking is **cross-sectional residual bias**, not an absolute SPY call
- Hand priors only — replace with audit weights later

CSV: `data/composite/2026-08-13_composite_rank.csv`

## Top 20 by residual pressure (favor when risk-on / current Y)

| Ticker | Sector | pressure | SPEC | QUAL | CROWD | SIZE | resid | beta | short |
|--------|--------|----------|------|------|-------|------|-------|------|-------|
| ARCT | Healthcare | +0.434 | 0.95 | 0.00 | 0.80 | 1.00 | +3.17% | high | very_high |
| ZENA | Technology | +0.420 | 0.95 | 0.00 | 0.60 | 1.00 | +11.85% | high | elevated |
| JSPR | Healthcare | +0.410 | 0.85 | 0.00 | 0.80 | 1.00 | +4.62% | high | very_high |
| INO | Healthcare | +0.410 | 0.85 | 0.00 | 0.80 | 1.00 | +16.63% | high | very_high |
| ACHV | Healthcare | +0.405 | 0.95 | 0.00 | 0.80 | 0.80 | +8.12% | high | very_high |
| TNDM | Healthcare | +0.405 | 0.95 | 0.00 | 0.80 | 0.80 | -1.58% | high | very_high |
| BBNX | Healthcare | +0.405 | 0.95 | 0.00 | 0.80 | 0.80 | +4.07% | high | very_high |
| INDI | Technology | +0.405 | 0.95 | 0.00 | 0.80 | 0.80 | +2.99% | high | very_high |
| AIRO | Industrials | +0.405 | 0.95 | 0.00 | 0.80 | 0.80 | +25.89% | high | very_high |
| SDGR | Healthcare | +0.405 | 0.95 | 0.00 | 0.80 | 0.80 | -1.17% | high | very_high |
| SMRT | Technology | +0.402 | 0.95 | 0.00 | 0.35 | 1.00 | -0.94% | high | low |
| PEPG | Healthcare | +0.395 | 0.85 | 0.00 | 0.60 | 1.00 | +2.50% | high | elevated |
| RCEL | Healthcare | +0.395 | 0.85 | 0.00 | 0.60 | 1.00 | -1.61% | high | elevated |
| JELD | Industrials | +0.395 | 0.85 | 0.00 | 0.60 | 1.00 | +3.45% | high | elevated |
| ALGS | Healthcare | +0.395 | 0.85 | 0.00 | 0.60 | 1.00 | -3.54% | high | elevated |
| HRTX | Healthcare | +0.395 | 0.85 | 0.00 | 0.60 | 1.00 | -3.20% | high | very_high |
| EBS | Healthcare | +0.395 | 0.85 | 0.00 | 0.60 | 1.00 | -1.57% | high | very_high |
| AIRS | Healthcare | +0.395 | 0.85 | 0.00 | 0.60 | 1.00 | +3.74% | high | very_high |
| AIFA | Technology | +0.395 | 0.85 | 0.00 | 0.60 | 1.00 | +4.80% | high | elevated |
| UPLD | Technology | +0.395 | 0.85 | 0.00 | 0.60 | 1.00 | +20.30% | high | elevated |

## Bottom 15 (lowest pressure)

| Ticker | Sector | pressure | SPEC | QUAL | resid | beta |
|--------|--------|----------|------|------|-------|------|
| PDD | Consumer Cyclical | -0.182 | 0.00 | 1.00 | -5.72% | low |
| TTE | Energy | -0.182 | 0.00 | 1.00 | -1.00% | low |
| WMT | Consumer Defensive | -0.182 | 0.00 | 1.00 | -0.51% | low |
| PEP | Consumer Defensive | -0.182 | 0.00 | 1.00 | +1.13% | low |
| BP | Energy | -0.182 | 0.00 | 1.00 | -0.49% | low |
| NEM | Basic Materials | -0.182 | 0.00 | 1.00 | -3.35% | low |
| ABBV | Healthcare | -0.182 | 0.00 | 1.00 | +0.57% | low |
| CVS | Healthcare | -0.182 | 0.00 | 1.00 | +0.03% | low |
| MRK | Healthcare | -0.182 | 0.00 | 1.00 | +1.72% | low |
| MO | Consumer Defensive | -0.182 | 0.00 | 1.00 | +0.83% | low |
| BTI | Consumer Defensive | -0.182 | 0.00 | 1.00 | +2.45% | low |
| SMFG | Financial | -0.182 | 0.00 | 1.00 | +0.70% | low |
| BUD | Consumer Defensive | -0.182 | 0.00 | 1.00 | +1.06% | low |
| SAN | Financial | -0.182 | 0.00 | 1.00 | -0.53% | low |
| MDT | Healthcare | -0.182 | 0.00 | 1.00 | -0.45% | low |

## Sector median pressure

| Sector | n | median pressure | median resid |
|--------|---|-----------------|--------------|
| Healthcare | 1064 | +0.210 | -0.56% |
| Technology | 790 | +0.170 | +0.82% |
| Communication Services | 259 | +0.170 | +0.73% |
| Basic Materials | 288 | +0.141 | -1.06% |
| Consumer Cyclical | 533 | +0.137 | +0.13% |
| Industrials | 708 | +0.129 | -0.26% |
| Consumer Defensive | 244 | +0.122 | +0.47% |
| Real Estate | 253 | +0.110 | +0.51% |
| Financial | 7078 | +0.101 | +0.01% |
| Energy | 253 | +0.044 | -0.50% |
| Utilities | 109 | -0.011 | +0.20% |

## Composite averages by size

| size | n | SPEC | QUAL | pressure |
|------|---|------|------|----------|
| large | 805 | 0.18 | 0.79 | -0.063 |
| mega | 169 | 0.16 | 0.83 | -0.110 |
| micro | 2146 | 0.51 | 0.30 | +0.224 |
| mid | 1169 | 0.37 | 0.51 | +0.086 |
| small | 1618 | 0.49 | 0.40 | +0.175 |
| unknown | 5672 | 0.33 | 0.24 | +0.096 |
