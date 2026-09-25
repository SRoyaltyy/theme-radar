# Composite residual rank — **2026-09-25**

Generated: 2026-09-25T16:51:49.787302-04:00
Prior snapshot (for returns): **2026-09-24**

## Y snapshot (v1 — breadth only)

- **p_risk_on:** 0.6037 (from % names up)
- **pct_up:** 0.5915
- **median_ret:** 0.18%
- **conviction:** 0.2074
- **n:** 11679
- note: price_derived breadth only (v1)

## Method (deliberately simple)

- **residual** = stock return − median stock return (same pair window)
- **composites:** SPEC_DURATION, QUALITY_DEFENSIVE, CROWDING, SIZE_TILT
- **pressure** = conviction × prior effects of composites given p_risk_on
- Ranking is **cross-sectional residual bias**, not an absolute SPY call
- Hand priors only — replace with audit weights later

CSV: `data/composite/2026-09-25_composite_rank.csv`

## Top 20 by residual pressure (favor when risk-on / current Y)

| Ticker | Sector | pressure | SPEC | QUAL | CROWD | SIZE | resid | beta | short |
|--------|--------|----------|------|------|-------|------|-------|------|-------|
| EU | Energy | +0.077 | 0.95 | 0.00 | 0.80 | 1.00 | +1.46% | high | very_high |
| EAF | Industrials | +0.074 | 0.95 | 0.00 | 0.60 | 1.00 | +4.74% | high | elevated |
| ADCT | Healthcare | +0.074 | 0.95 | 0.00 | 0.60 | 1.00 | -1.73% | high | elevated |
| TJGC | Communication Serv | +0.073 | 0.85 | 0.00 | 0.80 | 1.00 | -7.13% | high | very_high |
| LHSW | Technology | +0.073 | 0.85 | 0.00 | 0.80 | 1.00 | -5.44% | high | very_high |
| KAZR | Industrials | +0.073 | 0.85 | 0.00 | 0.80 | 1.00 | -1.65% | high | very_high |
| GRML | Basic Materials | +0.073 | 0.85 | 0.00 | 0.80 | 1.00 | -1.72% | high | very_high |
| FIRY | Communication Serv | +0.073 | 0.85 | 0.00 | 0.80 | 1.00 | -2.69% | high | very_high |
| SATL | Industrials | +0.072 | 0.95 | 0.00 | 0.80 | 0.80 | +3.69% | high | very_high |
| MRAM | Technology | +0.072 | 0.95 | 0.00 | 0.80 | 0.80 | +3.12% | high | very_high |
| TDUP | Consumer Cyclical | +0.070 | 0.85 | 0.00 | 0.60 | 1.00 | +0.72% | high | very_high |
| SRFM | Industrials | +0.070 | 0.85 | 0.00 | 0.60 | 1.00 | +20.47% | high | elevated |
| LXEO | Healthcare | +0.070 | 0.85 | 0.00 | 0.60 | 1.00 | -2.54% | high | very_high |
| PALI | Healthcare | +0.070 | 0.85 | 0.00 | 0.60 | 1.00 | -7.82% | high | very_high |
| TNXP | Healthcare | +0.070 | 0.85 | 0.00 | 0.60 | 1.00 | +1.47% | high | very_high |
| RENX | Real Estate | +0.070 | 0.85 | 0.00 | 0.60 | 1.00 | +7.66% | high | elevated |
| IPDN | Industrials | +0.070 | 0.85 | 0.00 | 0.60 | 1.00 | +7.73% | high | elevated |
| SLMT | Technology | +0.070 | 0.85 | 0.00 | 0.60 | 1.00 | +26.95% | high | elevated |
| NCPL | Financial | +0.070 | 0.85 | 0.00 | 0.60 | 1.00 | +6.91% | high | elevated |
| XHLD | Communication Serv | +0.070 | 0.85 | 0.00 | 0.60 | 1.00 | +1.79% | high | elevated |

## Bottom 15 (lowest pressure)

| Ticker | Sector | pressure | SPEC | QUAL | resid | beta |
|--------|--------|----------|------|------|-------|------|
| TD | Financial | -0.032 | 0.00 | 1.00 | +0.99% | low |
| BP | Energy | -0.032 | 0.00 | 1.00 | -0.76% | low |
| ABBV | Healthcare | -0.032 | 0.00 | 1.00 | -0.47% | low |
| LIN | Basic Materials | -0.032 | 0.00 | 1.00 | +0.19% | low |
| LLY | Healthcare | -0.032 | 0.00 | 1.00 | -0.05% | low |
| LMT | Industrials | -0.032 | 0.00 | 1.00 | -0.97% | low |
| PM | Consumer Defensive | -0.032 | 0.00 | 1.00 | -0.71% | low |
| ABT | Healthcare | -0.032 | 0.00 | 1.00 | +0.04% | low |
| BMY | Healthcare | -0.032 | 0.00 | 1.00 | +2.03% | low |
| MRK | Healthcare | -0.032 | 0.00 | 1.00 | +0.36% | low |
| VLO | Energy | -0.032 | 0.00 | 1.00 | +0.95% | low |
| PFE | Healthcare | -0.032 | 0.00 | 1.00 | +0.74% | low |
| TTE | Energy | -0.032 | 0.00 | 1.00 | -1.21% | low |
| WMT | Consumer Defensive | -0.032 | 0.00 | 1.00 | +0.18% | low |
| MA | Financial | -0.032 | 0.00 | 1.00 | +0.10% | low |

## Sector median pressure

| Sector | n | median pressure | median resid |
|--------|---|-----------------|--------------|
| Healthcare | 1053 | +0.038 | -0.68% |
| Technology | 793 | +0.030 | -0.18% |
| Communication Services | 255 | +0.030 | -0.47% |
| Basic Materials | 292 | +0.025 | +0.04% |
| Consumer Cyclical | 528 | +0.024 | +0.17% |
| Industrials | 718 | +0.024 | +0.08% |
| Real Estate | 247 | +0.022 | -0.14% |
| Consumer Defensive | 242 | +0.019 | -0.18% |
| Financial | 7194 | +0.018 | +0.05% |
| Energy | 251 | +0.007 | -1.21% |
| Utilities | 106 | -0.002 | +0.21% |

## Composite averages by size

| size | n | SPEC | QUAL | pressure |
|------|---|------|------|----------|
| large | 772 | 0.17 | 0.79 | -0.012 |
| mega | 160 | 0.14 | 0.84 | -0.021 |
| micro | 2192 | 0.51 | 0.29 | +0.040 |
| mid | 1142 | 0.36 | 0.51 | +0.015 |
| small | 1632 | 0.48 | 0.40 | +0.031 |
| unknown | 5781 | 0.32 | 0.24 | +0.017 |
