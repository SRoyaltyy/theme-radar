# Composite residual rank — **2026-11-18**

Generated: 2026-11-18T21:40:21.371223-05:00
Prior snapshot (for returns): **2026-11-17**

## Y snapshot (v1 — breadth only)

- **p_risk_on:** 0.1791 (from % names up)
- **pct_up:** 0.4217
- **median_ret:** -0.06%
- **conviction:** 0.6417
- **n:** 11756
- note: price_derived breadth only (v1)

## Method (deliberately simple)

- **residual** = stock return − median stock return (same pair window)
- **composites:** SPEC_DURATION, QUALITY_DEFENSIVE, CROWDING, SIZE_TILT
- **pressure** = conviction × prior effects of composites given p_risk_on
- Ranking is **cross-sectional residual bias**, not an absolute SPY call
- Hand priors only — replace with audit weights later

CSV: `data/composite/2026-11-18_composite_rank.csv`

## Top 20 by residual pressure (favor when risk-on / current Y)

| Ticker | Sector | pressure | SPEC | QUAL | CROWD | SIZE | resid | beta | short |
|--------|--------|----------|------|------|-------|------|-------|------|-------|
| BUD | Consumer Defensive | +0.309 | 0.00 | 1.00 | 0.00 | 0.00 | -0.52% | low | low |
| ABT | Healthcare | +0.309 | 0.00 | 1.00 | 0.00 | 0.00 | -0.16% | low | low |
| NVS | Healthcare | +0.309 | 0.00 | 1.00 | 0.00 | 0.00 | -2.41% | low | low |
| AMGN | Healthcare | +0.309 | 0.00 | 1.00 | 0.00 | 0.00 | -3.01% | low | low |
| JNJ | Healthcare | +0.309 | 0.00 | 1.00 | 0.00 | 0.00 | -2.10% | low | low |
| BTI | Consumer Defensive | +0.309 | 0.00 | 1.00 | 0.00 | 0.00 | -1.06% | low | low |
| NVO | Healthcare | +0.309 | 0.00 | 1.00 | 0.00 | 0.00 | -3.06% | low | low |
| LMT | Industrials | +0.309 | 0.00 | 1.00 | 0.00 | 0.00 | -2.00% | low | low |
| LIN | Basic Materials | +0.309 | 0.00 | 1.00 | 0.00 | 0.00 | -0.52% | low | low |
| LLY | Healthcare | +0.309 | 0.00 | 1.00 | 0.00 | 0.00 | -2.26% | low | low |
| MCK | Healthcare | +0.309 | 0.00 | 1.00 | 0.00 | 0.00 | -0.61% | low | low |
| SNY | Healthcare | +0.309 | 0.00 | 1.00 | 0.00 | 0.00 | -0.81% | low | low |
| TTE | Energy | +0.309 | 0.00 | 1.00 | 0.00 | 0.00 | -3.55% | low | low |
| CME | Financial | +0.309 | 0.00 | 1.00 | 0.00 | 0.00 | -0.36% | low | low |
| LOW | Consumer Cyclical | +0.309 | 0.00 | 1.00 | 0.00 | 0.00 | +1.11% | low | low |
| SMFG | Financial | +0.309 | 0.00 | 1.00 | 0.00 | 0.00 | -2.17% | low | low |
| SO | Utilities | +0.309 | 0.00 | 1.00 | 0.00 | 0.00 | +0.92% | low | low |
| MCD | Consumer Cyclical | +0.309 | 0.00 | 1.00 | 0.00 | 0.00 | -0.59% | low | low |
| SAN | Financial | +0.309 | 0.00 | 1.00 | 0.00 | 0.00 | -1.88% | low | low |
| RY | Financial | +0.309 | 0.00 | 1.00 | 0.00 | 0.00 | -3.19% | low | low |

## Bottom 15 (lowest pressure)

| Ticker | Sector | pressure | SPEC | QUAL | resid | beta |
|--------|--------|----------|------|------|-------|------|
| TDUP | Consumer Cyclical | -0.713 | 0.95 | 0.00 | +16.84% | high |
| NCPL | Financial | -0.696 | 0.85 | 0.00 | +22.00% | high |
| BMBL | Communication Serv | -0.688 | 0.95 | 0.00 | +0.06% | high |
| GLSI | Healthcare | -0.688 | 0.95 | 0.00 | +10.11% | high |
| WSHP | Communication Serv | -0.671 | 0.85 | 0.00 | -10.39% | high |
| WATT | Technology | -0.671 | 0.85 | 0.00 | -3.10% | high |
| ABR | Real Estate | -0.671 | 0.85 | 0.00 | +1.81% | high |
| ABAT | Industrials | -0.671 | 0.85 | 0.00 | -6.19% | high |
| EU | Energy | -0.671 | 0.85 | 0.00 | -2.03% | high |
| PALI | Healthcare | -0.671 | 0.85 | 0.00 | -6.87% | high |
| VUZI | Technology | -0.671 | 0.85 | 0.00 | +0.88% | high |
| ASPI | Basic Materials | -0.671 | 0.85 | 0.00 | -10.16% | high |
| INSG | Technology | -0.671 | 0.85 | 0.00 | +5.64% | high |
| LVWR | Consumer Cyclical | -0.671 | 0.85 | 0.00 | +0.06% | high |
| GPRO | Technology | -0.671 | 0.85 | 0.00 | -4.86% | high |

## Sector median pressure

| Sector | n | median pressure | median resid |
|--------|---|-----------------|--------------|
| Utilities | 103 | +0.049 | +0.36% |
| Energy | 252 | -0.089 | -1.77% |
| Financial | 7276 | -0.171 | -0.00% |
| Consumer Defensive | 239 | -0.202 | +0.06% |
| Real Estate | 246 | -0.212 | +0.34% |
| Industrials | 716 | -0.222 | +0.06% |
| Consumer Cyclical | 520 | -0.233 | +1.36% |
| Basic Materials | 298 | -0.249 | -3.05% |
| Communication Services | 252 | -0.288 | -0.02% |
| Technology | 800 | -0.299 | +0.06% |
| Healthcare | 1054 | -0.386 | -0.46% |

## Composite averages by size

| size | n | SPEC | QUAL | pressure |
|------|---|------|------|----------|
| large | 742 | 0.15 | 0.81 | +0.127 |
| mega | 154 | 0.13 | 0.85 | +0.205 |
| micro | 2312 | 0.52 | 0.27 | -0.396 |
| mid | 1102 | 0.34 | 0.53 | -0.129 |
| small | 1578 | 0.49 | 0.40 | -0.298 |
| unknown | 5868 | 0.32 | 0.24 | -0.157 |
