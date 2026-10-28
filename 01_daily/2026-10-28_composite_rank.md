# Composite residual rank — **2026-10-28**

Generated: 2026-10-28T17:30:26.778191-04:00
Prior snapshot (for returns): **2026-10-27**

## Y snapshot (v1 — breadth only)

- **p_risk_on:** 0.5561 (from % names up)
- **pct_up:** 0.5724
- **median_ret:** 0.12%
- **conviction:** 0.1122
- **n:** 11774
- note: price_derived breadth only (v1)

## Method (deliberately simple)

- **residual** = stock return − median stock return (same pair window)
- **composites:** SPEC_DURATION, QUALITY_DEFENSIVE, CROWDING, SIZE_TILT
- **pressure** = conviction × prior effects of composites given p_risk_on
- Ranking is **cross-sectional residual bias**, not an absolute SPY call
- Hand priors only — replace with audit weights later

CSV: `data/composite/2026-10-28_composite_rank.csv`

## Top 20 by residual pressure (favor when risk-on / current Y)

| Ticker | Sector | pressure | SPEC | QUAL | CROWD | SIZE | resid | beta | short |
|--------|--------|----------|------|------|-------|------|-------|------|-------|
| KRRO | Healthcare | +0.030 | 0.95 | 0.00 | 0.80 | 1.00 | +4.09% | high | very_high |
| TBCH | Technology | +0.030 | 0.95 | 0.00 | 0.80 | 1.00 | -0.48% | high | very_high |
| SLNH | Financial | +0.030 | 0.95 | 0.00 | 0.80 | 1.00 | +10.65% | high | very_high |
| WATT | Technology | +0.030 | 0.95 | 0.00 | 0.80 | 1.00 | +21.53% | high | very_high |
| DMRC | Technology | +0.029 | 0.95 | 0.00 | 0.60 | 1.00 | +9.26% | high | elevated |
| UIS | Technology | +0.029 | 0.95 | 0.00 | 0.60 | 1.00 | +2.93% | high | elevated |
| INGN | Healthcare | +0.029 | 0.95 | 0.00 | 0.60 | 1.00 | +1.56% | high | elevated |
| CRMT | Consumer Cyclical | +0.028 | 0.85 | 0.00 | 0.80 | 1.00 | +8.63% | high | very_high |
| DNA | Healthcare | +0.028 | 0.95 | 0.00 | 0.80 | 0.80 | +18.07% | high | very_high |
| PRME | Healthcare | +0.028 | 0.95 | 0.00 | 0.80 | 0.80 | +23.10% | high | very_high |
| ULCC | Industrials | +0.028 | 0.95 | 0.00 | 0.80 | 0.80 | +11.45% | high | very_high |
| PACB | Healthcare | +0.028 | 0.95 | 0.00 | 0.80 | 0.80 | +15.39% | high | very_high |
| CDZI | Industrials | +0.028 | 0.95 | 0.00 | 0.80 | 0.80 | +1.39% | high | very_high |
| ENVX | Industrials | +0.028 | 0.95 | 0.00 | 0.80 | 0.80 | +4.96% | high | very_high |
| ACDC | Energy | +0.028 | 0.95 | 0.00 | 0.80 | 0.80 | +8.60% | high | very_high |
| BETR | Financial | +0.028 | 0.95 | 0.00 | 0.80 | 0.80 | +3.44% | high | very_high |
| CERT | Healthcare | +0.028 | 0.95 | 0.00 | 0.80 | 0.80 | +4.72% | high | very_high |
| BMBL | Communication Serv | +0.028 | 0.95 | 0.00 | 0.80 | 0.80 | -0.45% | high | very_high |
| TNDM | Healthcare | +0.028 | 0.95 | 0.00 | 0.80 | 0.80 | +2.27% | high | very_high |
| TNXP | Healthcare | +0.027 | 0.85 | 0.00 | 0.60 | 1.00 | -0.49% | high | very_high |

## Bottom 15 (lowest pressure)

| Ticker | Sector | pressure | SPEC | QUAL | resid | beta |
|--------|--------|----------|------|------|-------|------|
| ABT | Healthcare | -0.013 | 0.00 | 1.00 | -0.57% | low |
| DHR | Healthcare | -0.013 | 0.00 | 1.00 | +0.77% | low |
| TD | Financial | -0.013 | 0.00 | 1.00 | +0.42% | low |
| MUFG | Financial | -0.013 | 0.00 | 1.00 | -0.21% | low |
| T | Communication Serv | -0.013 | 0.00 | 1.00 | -1.27% | low |
| TM | Consumer Cyclical | -0.013 | 0.00 | 1.00 | -0.99% | low |
| BMY | Healthcare | -0.013 | 0.00 | 1.00 | -1.71% | low |
| PDD | Consumer Cyclical | -0.013 | 0.00 | 1.00 | -1.32% | low |
| KO | Consumer Defensive | -0.013 | 0.00 | 1.00 | +0.48% | low |
| PFE | Healthcare | -0.013 | 0.00 | 1.00 | -1.29% | low |
| BRK-A | Financial | -0.013 | 0.00 | 1.00 | +0.11% | low |
| BP | Energy | -0.013 | 0.00 | 1.00 | +1.64% | low |
| PSX | Energy | -0.013 | 0.00 | 1.00 | +1.83% | low |
| VRTX | Healthcare | -0.013 | 0.00 | 1.00 | +1.54% | low |
| VLO | Energy | -0.013 | 0.00 | 1.00 | +0.17% | low |

## Sector median pressure

| Sector | n | median pressure | median resid |
|--------|---|-----------------|--------------|
| Healthcare | 1053 | +0.015 | +1.54% |
| Technology | 801 | +0.012 | +0.40% |
| Communication Services | 254 | +0.012 | -0.12% |
| Basic Materials | 297 | +0.010 | -0.12% |
| Consumer Cyclical | 524 | +0.009 | -0.12% |
| Industrials | 714 | +0.009 | +0.09% |
| Real Estate | 248 | +0.009 | -0.81% |
| Consumer Defensive | 240 | +0.007 | -0.60% |
| Financial | 7284 | +0.007 | -0.02% |
| Energy | 252 | +0.003 | +0.61% |
| Utilities | 107 | -0.001 | -0.88% |

## Composite averages by size

| size | n | SPEC | QUAL | pressure |
|------|---|------|------|----------|
| large | 767 | 0.17 | 0.80 | -0.005 |
| mega | 162 | 0.14 | 0.84 | -0.008 |
| micro | 2246 | 0.52 | 0.28 | +0.016 |
| mid | 1129 | 0.36 | 0.52 | +0.006 |
| small | 1594 | 0.49 | 0.41 | +0.012 |
| unknown | 5876 | 0.32 | 0.25 | +0.006 |
