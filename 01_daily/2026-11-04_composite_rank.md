# Composite residual rank — **2026-11-04**

Generated: 2026-11-04T16:58:33.786060-05:00
Prior snapshot (for returns): **2026-11-03**

## Y snapshot (v1 — breadth only)

- **p_risk_on:** 0.9006 (from % names up)
- **pct_up:** 0.7103
- **median_ret:** 1.00%
- **conviction:** 0.8013
- **n:** 11755
- note: price_derived breadth only (v1)

## Method (deliberately simple)

- **residual** = stock return − median stock return (same pair window)
- **composites:** SPEC_DURATION, QUALITY_DEFENSIVE, CROWDING, SIZE_TILT
- **pressure** = conviction × prior effects of composites given p_risk_on
- Ranking is **cross-sectional residual bias**, not an absolute SPY call
- Hand priors only — replace with audit weights later

CSV: `data/composite/2026-11-04_composite_rank.csv`

## Top 20 by residual pressure (favor when risk-on / current Y)

| Ticker | Sector | pressure | SPEC | QUAL | CROWD | SIZE | resid | beta | short |
|--------|--------|----------|------|------|-------|------|-------|------|-------|
| KRRO | Healthcare | +1.149 | 0.95 | 0.00 | 0.80 | 1.00 | +3.79% | high | very_high |
| UPB | Healthcare | +1.111 | 0.95 | 0.00 | 0.60 | 1.00 | +8.15% | high | elevated |
| NMRA | Healthcare | +1.111 | 0.95 | 0.00 | 0.60 | 1.00 | -1.00% | high | elevated |
| DMRC | Technology | +1.111 | 0.95 | 0.00 | 0.60 | 1.00 | +0.87% | high | elevated |
| INO | Healthcare | +1.085 | 0.85 | 0.00 | 0.80 | 1.00 | -3.41% | high | very_high |
| WKHS | Consumer Cyclical | +1.085 | 0.85 | 0.00 | 0.80 | 1.00 | +4.08% | high | very_high |
| NCPL | Financial | +1.085 | 0.85 | 0.00 | 0.80 | 1.00 | -10.61% | high | very_high |
| EVGO | Consumer Cyclical | +1.072 | 0.95 | 0.00 | 0.80 | 0.80 | -2.09% | high | very_high |
| CHPT | Consumer Cyclical | +1.072 | 0.95 | 0.00 | 0.80 | 0.80 | +4.75% | high | very_high |
| ARRY | Technology | +1.072 | 0.95 | 0.00 | 0.80 | 0.80 | +13.87% | high | very_high |
| TDOC | Healthcare | +1.072 | 0.95 | 0.00 | 0.80 | 0.80 | +8.11% | high | very_high |
| BMBL | Communication Serv | +1.072 | 0.95 | 0.00 | 0.80 | 0.80 | -0.66% | high | very_high |
| JBLU | Industrials | +1.072 | 0.95 | 0.00 | 0.80 | 0.80 | +10.95% | high | very_high |
| REAL | Consumer Cyclical | +1.072 | 0.95 | 0.00 | 0.80 | 0.80 | +5.85% | high | very_high |
| NUAI | Technology | +1.046 | 0.85 | 0.00 | 0.60 | 1.00 | -22.22% | high | very_high |
| CATX | Healthcare | +1.046 | 0.85 | 0.00 | 0.60 | 1.00 | -2.14% | high | very_high |
| LBGJ | Industrials | +1.046 | 0.85 | 0.00 | 0.60 | 1.00 | +19.26% | high | elevated |
| WATT | Technology | +1.046 | 0.85 | 0.00 | 0.60 | 1.00 | -5.91% | high | very_high |
| BURU | Industrials | +1.046 | 0.85 | 0.00 | 0.60 | 1.00 | -5.00% | high | elevated |
| UPLD | Technology | +1.046 | 0.85 | 0.00 | 0.60 | 1.00 | +9.07% | high | elevated |

## Bottom 15 (lowest pressure)

| Ticker | Sector | pressure | SPEC | QUAL | resid | beta |
|--------|--------|----------|------|------|-------|------|
| GSK | Healthcare | -0.481 | 0.00 | 1.00 | +4.03% | low |
| UL | Consumer Defensive | -0.481 | 0.00 | 1.00 | +2.26% | low |
| ADP | Technology | -0.481 | 0.00 | 1.00 | +1.54% | low |
| TJX | Consumer Cyclical | -0.481 | 0.00 | 1.00 | +4.18% | low |
| EQNR | Energy | -0.481 | 0.00 | 1.00 | -7.20% | low |
| RTX | Industrials | -0.481 | 0.00 | 1.00 | -3.64% | low |
| MUFG | Financial | -0.481 | 0.00 | 1.00 | +2.29% | low |
| BABA | Consumer Cyclical | -0.481 | 0.00 | 1.00 | +3.91% | low |
| MO | Consumer Defensive | -0.481 | 0.00 | 1.00 | +0.39% | low |
| VRTX | Healthcare | -0.481 | 0.00 | 1.00 | +2.45% | low |
| BUD | Consumer Defensive | -0.481 | 0.00 | 1.00 | +2.11% | low |
| BTI | Consumer Defensive | -0.481 | 0.00 | 1.00 | +2.40% | low |
| SCHW | Financial | -0.481 | 0.00 | 1.00 | +3.58% | low |
| HSBC | Financial | -0.481 | 0.00 | 1.00 | +4.78% | low |
| DHR | Healthcare | -0.481 | 0.00 | 1.00 | +1.10% | low |

## Sector median pressure

| Sector | n | median pressure | median resid |
|--------|---|-----------------|--------------|
| Healthcare | 1054 | +0.600 | +1.07% |
| Technology | 802 | +0.456 | -1.00% |
| Communication Services | 252 | +0.449 | +2.24% |
| Basic Materials | 298 | +0.406 | +2.62% |
| Consumer Cyclical | 522 | +0.382 | +2.92% |
| Industrials | 712 | +0.377 | -1.04% |
| Real Estate | 248 | +0.332 | +1.78% |
| Consumer Defensive | 240 | +0.319 | +2.04% |
| Financial | 7268 | +0.266 | -0.10% |
| Energy | 252 | +0.132 | -5.19% |
| Utilities | 107 | +0.019 | +0.73% |

## Composite averages by size

| size | n | SPEC | QUAL | pressure |
|------|---|------|------|----------|
| large | 761 | 0.18 | 0.79 | -0.154 |
| mega | 168 | 0.15 | 0.83 | -0.289 |
| micro | 2256 | 0.52 | 0.28 | +0.604 |
| mid | 1120 | 0.37 | 0.51 | +0.235 |
| small | 1595 | 0.50 | 0.40 | +0.474 |
| unknown | 5855 | 0.33 | 0.24 | +0.252 |
