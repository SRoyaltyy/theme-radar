# Composite residual rank — **2026-09-18**

Generated: 2026-09-18T19:21:35.691845-04:00
Prior snapshot (for returns): **2026-09-17**

## Y snapshot (v1 — breadth only)

- **p_risk_on:** 0.0395 (from % names up)
- **pct_up:** 0.3658
- **median_ret:** -0.20%
- **conviction:** 0.921
- **n:** 11654
- note: price_derived breadth only (v1)

## Method (deliberately simple)

- **residual** = stock return − median stock return (same pair window)
- **composites:** SPEC_DURATION, QUALITY_DEFENSIVE, CROWDING, SIZE_TILT
- **pressure** = conviction × prior effects of composites given p_risk_on
- Ranking is **cross-sectional residual bias**, not an absolute SPY call
- Hand priors only — replace with audit weights later

CSV: `data/composite/2026-09-18_composite_rank.csv`

## Top 20 by residual pressure (favor when risk-on / current Y)

| Ticker | Sector | pressure | SPEC | QUAL | CROWD | SIZE | resid | beta | short |
|--------|--------|----------|------|------|-------|------|-------|------|-------|
| XOM | Energy | +0.636 | 0.00 | 1.00 | 0.00 | 0.00 | +0.37% | low | low |
| MCD | Consumer Cyclical | +0.636 | 0.00 | 1.00 | 0.00 | 0.00 | +0.10% | low | low |
| TD | Financial | +0.636 | 0.00 | 1.00 | 0.00 | 0.00 | +0.63% | low | low |
| MFG | Financial | +0.636 | 0.00 | 1.00 | 0.00 | 0.00 | -0.97% | low | low |
| CVX | Energy | +0.636 | 0.00 | 1.00 | 0.00 | 0.00 | -0.77% | low | low |
| MDT | Healthcare | +0.636 | 0.00 | 1.00 | 0.00 | 0.00 | -0.49% | low | low |
| MA | Financial | +0.636 | 0.00 | 1.00 | 0.00 | 0.00 | +0.11% | low | low |
| TJX | Consumer Cyclical | +0.636 | 0.00 | 1.00 | 0.00 | 0.00 | +0.75% | low | low |
| RTX | Industrials | +0.636 | 0.00 | 1.00 | 0.00 | 0.00 | +0.44% | low | low |
| BTI | Consumer Defensive | +0.636 | 0.00 | 1.00 | 0.00 | 0.00 | -0.14% | low | low |
| TM | Consumer Cyclical | +0.636 | 0.00 | 1.00 | 0.00 | 0.00 | -1.03% | low | low |
| TMUS | Communication Serv | +0.636 | 0.00 | 1.00 | 0.00 | 0.00 | +1.24% | low | low |
| BUD | Consumer Defensive | +0.636 | 0.00 | 1.00 | 0.00 | 0.00 | -1.12% | low | low |
| BMY | Healthcare | +0.636 | 0.00 | 1.00 | 0.00 | 0.00 | +0.55% | low | low |
| RY | Financial | +0.636 | 0.00 | 1.00 | 0.00 | 0.00 | +0.07% | low | low |
| MO | Consumer Defensive | +0.636 | 0.00 | 1.00 | 0.00 | 0.00 | -0.06% | low | low |
| LIN | Basic Materials | +0.636 | 0.00 | 1.00 | 0.00 | 0.00 | +0.62% | low | low |
| SYK | Healthcare | +0.636 | 0.00 | 1.00 | 0.00 | 0.00 | -1.59% | low | low |
| MRK | Healthcare | +0.636 | 0.00 | 1.00 | 0.00 | 0.00 | +0.01% | low | low |
| LLY | Healthcare | +0.636 | 0.00 | 1.00 | 0.00 | 0.00 | +0.24% | low | low |

## Bottom 15 (lowest pressure)

| Ticker | Sector | pressure | SPEC | QUAL | resid | beta |
|--------|--------|----------|------|------|-------|------|
| CHPT | Consumer Cyclical | -1.518 | 0.95 | 0.00 | +4.23% | high |
| GLSI | Healthcare | -1.518 | 0.95 | 0.00 | +3.46% | high |
| EAF | Industrials | -1.468 | 0.95 | 0.00 | +2.95% | high |
| YFOR | Industrials | -1.433 | 0.85 | 0.00 | -12.84% | high |
| DAIC | Technology | -1.433 | 0.85 | 0.00 | -32.82% | high |
| NCPL | Financial | -1.433 | 0.85 | 0.00 | +32.34% | high |
| CRDF | Healthcare | -1.433 | 0.85 | 0.00 | +5.59% | high |
| GEMI | Financial | -1.417 | 0.95 | 0.00 | +31.35% | high |
| LVWR | Consumer Cyclical | -1.417 | 0.95 | 0.00 | +14.99% | high |
| BBNX | Healthcare | -1.417 | 0.95 | 0.00 | +2.35% | high |
| XGN | Healthcare | -1.383 | 0.85 | 0.00 | +7.06% | high |
| IMCC | Healthcare | -1.383 | 0.85 | 0.00 | +143.30% | high |
| CHOW | Technology | -1.383 | 0.85 | 0.00 | +12.70% | high |
| SKIL | Consumer Defensive | -1.383 | 0.85 | 0.00 | -2.01% | high |
| LASE | Industrials | -1.383 | 0.85 | 0.00 | +0.20% | high |

## Sector median pressure

| Sector | n | median pressure | median resid |
|--------|---|-----------------|--------------|
| Utilities | 107 | +0.038 | -1.03% |
| Energy | 251 | -0.174 | -0.42% |
| Financial | 7164 | -0.352 | +0.06% |
| Consumer Defensive | 242 | -0.380 | -0.44% |
| Real Estate | 248 | -0.428 | -0.65% |
| Industrials | 717 | -0.450 | +0.10% |
| Consumer Cyclical | 528 | -0.479 | -0.63% |
| Basic Materials | 291 | -0.492 | -0.34% |
| Communication Services | 256 | -0.594 | -0.63% |
| Technology | 794 | -0.594 | -0.32% |
| Healthcare | 1056 | -0.734 | -0.17% |

## Composite averages by size

| size | n | SPEC | QUAL | pressure |
|------|---|------|------|----------|
| large | 771 | 0.17 | 0.80 | +0.240 |
| mega | 165 | 0.14 | 0.84 | +0.416 |
| micro | 2195 | 0.51 | 0.29 | -0.779 |
| mid | 1160 | 0.36 | 0.51 | -0.290 |
| small | 1615 | 0.48 | 0.40 | -0.603 |
| unknown | 5748 | 0.32 | 0.24 | -0.318 |
