# Composite residual rank — **2026-10-15**

Generated: 2026-10-15T16:49:13.966628-04:00
Prior snapshot (for returns): **2026-10-14**

## Y snapshot (v1 — breadth only)

- **p_risk_on:** 0.8769 (from % names up)
- **pct_up:** 0.7007
- **median_ret:** 0.58%
- **conviction:** 0.7537
- **n:** 11746
- note: price_derived breadth only (v1)

## Method (deliberately simple)

- **residual** = stock return − median stock return (same pair window)
- **composites:** SPEC_DURATION, QUALITY_DEFENSIVE, CROWDING, SIZE_TILT
- **pressure** = conviction × prior effects of composites given p_risk_on
- Ranking is **cross-sectional residual bias**, not an absolute SPY call
- Hand priors only — replace with audit weights later

CSV: `data/composite/2026-10-15_composite_rank.csv`

## Top 20 by residual pressure (favor when risk-on / current Y)

| Ticker | Sector | pressure | SPEC | QUAL | CROWD | SIZE | resid | beta | short |
|--------|--------|----------|------|------|-------|------|-------|------|-------|
| TBCH | Technology | +1.017 | 0.95 | 0.00 | 0.80 | 1.00 | +11.71% | high | very_high |
| NCPL | Financial | +0.960 | 0.85 | 0.00 | 0.80 | 1.00 | +23.95% | high | very_high |
| CRBP | Healthcare | +0.926 | 0.85 | 0.00 | 0.60 | 1.00 | -2.40% | high | very_high |
| PDYN | Technology | +0.926 | 0.85 | 0.00 | 0.60 | 1.00 | -2.75% | high | very_high |
| PDSB | Healthcare | +0.926 | 0.85 | 0.00 | 0.60 | 1.00 | -8.38% | high | elevated |
| ATOM | Technology | +0.926 | 0.85 | 0.00 | 0.60 | 1.00 | -5.17% | high | very_high |
| PAL | Industrials | +0.926 | 0.85 | 0.00 | 0.60 | 1.00 | -5.97% | high | very_high |
| UNCY | Healthcare | +0.926 | 0.85 | 0.00 | 0.60 | 1.00 | -3.56% | high | very_high |
| USGO | Basic Materials | +0.926 | 0.85 | 0.00 | 0.60 | 1.00 | +0.48% | high | very_high |
| LXEO | Healthcare | +0.926 | 0.85 | 0.00 | 0.60 | 1.00 | +4.36% | high | very_high |
| OCGN | Healthcare | +0.926 | 0.85 | 0.00 | 0.60 | 1.00 | -4.15% | high | very_high |
| BKKT | Technology | +0.926 | 0.85 | 0.00 | 0.60 | 1.00 | -1.92% | high | very_high |
| BYRN | Industrials | +0.926 | 0.85 | 0.00 | 0.60 | 1.00 | +2.21% | high | elevated |
| TNXP | Healthcare | +0.926 | 0.85 | 0.00 | 0.60 | 1.00 | -0.27% | high | very_high |
| ORGO | Healthcare | +0.926 | 0.85 | 0.00 | 0.60 | 1.00 | -3.21% | high | very_high |
| AIRO | Industrials | +0.926 | 0.85 | 0.00 | 0.60 | 1.00 | +0.52% | high | very_high |
| ABAT | Industrials | +0.926 | 0.85 | 0.00 | 0.60 | 1.00 | -3.07% | high | very_high |
| AIRS | Healthcare | +0.926 | 0.85 | 0.00 | 0.60 | 1.00 | -1.29% | high | very_high |
| CABA | Healthcare | +0.926 | 0.85 | 0.00 | 0.60 | 1.00 | -4.90% | high | very_high |
| WATT | Technology | +0.926 | 0.85 | 0.00 | 0.60 | 1.00 | -0.47% | high | very_high |

## Bottom 15 (lowest pressure)

| Ticker | Sector | pressure | SPEC | QUAL | resid | beta |
|--------|--------|----------|------|------|-------|------|
| T | Communication Serv | -0.426 | 0.00 | 1.00 | +1.37% | low |
| TD | Financial | -0.426 | 0.00 | 1.00 | +1.24% | low |
| MCD | Consumer Cyclical | -0.426 | 0.00 | 1.00 | +1.18% | low |
| MDT | Healthcare | -0.426 | 0.00 | 1.00 | +0.71% | low |
| MFG | Financial | -0.426 | 0.00 | 1.00 | -0.97% | low |
| LIN | Basic Materials | -0.426 | 0.00 | 1.00 | -0.48% | low |
| LMT | Industrials | -0.426 | 0.00 | 1.00 | +1.41% | low |
| LLY | Healthcare | -0.426 | 0.00 | 1.00 | +2.96% | low |
| MRK | Healthcare | -0.426 | 0.00 | 1.00 | -2.06% | low |
| KO | Consumer Defensive | -0.426 | 0.00 | 1.00 | -0.34% | low |
| JNJ | Healthcare | -0.426 | 0.00 | 1.00 | -0.83% | low |
| UNH | Healthcare | -0.426 | 0.00 | 1.00 | +2.21% | low |
| MUFG | Financial | -0.426 | 0.00 | 1.00 | -0.67% | low |
| UL | Consumer Defensive | -0.426 | 0.00 | 1.00 | +0.65% | low |
| NEM | Basic Materials | -0.426 | 0.00 | 1.00 | +3.21% | low |

## Sector median pressure

| Sector | n | median pressure | median resid |
|--------|---|-----------------|--------------|
| Healthcare | 1054 | +0.525 | +1.16% |
| Technology | 799 | +0.398 | +0.44% |
| Communication Services | 254 | +0.398 | +0.96% |
| Basic Materials | 294 | +0.325 | +1.07% |
| Consumer Cyclical | 526 | +0.324 | +1.92% |
| Industrials | 717 | +0.312 | +0.08% |
| Real Estate | 248 | +0.287 | +0.89% |
| Consumer Defensive | 241 | +0.276 | -0.02% |
| Financial | 7254 | +0.236 | -0.11% |
| Energy | 252 | +0.117 | -1.74% |
| Utilities | 107 | -0.026 | -0.58% |

## Composite averages by size

| size | n | SPEC | QUAL | pressure |
|------|---|------|------|----------|
| large | 767 | 0.17 | 0.80 | -0.156 |
| mega | 163 | 0.15 | 0.83 | -0.263 |
| micro | 2238 | 0.52 | 0.28 | +0.533 |
| mid | 1117 | 0.36 | 0.52 | +0.194 |
| small | 1619 | 0.49 | 0.40 | +0.410 |
| unknown | 5842 | 0.32 | 0.25 | +0.214 |
