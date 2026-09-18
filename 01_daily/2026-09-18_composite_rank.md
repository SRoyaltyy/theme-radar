# Composite residual rank — **2026-09-18**

Generated: 2026-09-18T16:40:35.432497-04:00
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
| BUD | Consumer Defensive | +0.636 | 0.00 | 1.00 | 0.00 | 0.00 | -1.12% | low | low |
| ABT | Healthcare | +0.636 | 0.00 | 1.00 | 0.00 | 0.00 | +0.57% | low | low |
| MRK | Healthcare | +0.636 | 0.00 | 1.00 | 0.00 | 0.00 | +0.01% | low | low |
| MUFG | Financial | +0.636 | 0.00 | 1.00 | 0.00 | 0.00 | -1.37% | low | low |
| BP | Energy | +0.636 | 0.00 | 1.00 | 0.00 | 0.00 | -1.65% | low | low |
| IBN | Financial | +0.636 | 0.00 | 1.00 | 0.00 | 0.00 | +0.09% | low | low |
| IBM | Technology | +0.636 | 0.00 | 1.00 | 0.00 | 0.00 | -3.25% | low | low |
| BABA | Consumer Cyclical | +0.636 | 0.00 | 1.00 | 0.00 | 0.00 | +4.53% | low | low |
| TTE | Energy | +0.636 | 0.00 | 1.00 | 0.00 | 0.00 | -0.64% | low | low |
| ENB | Energy | +0.636 | 0.00 | 1.00 | 0.00 | 0.00 | +0.16% | low | low |
| TJX | Consumer Cyclical | +0.636 | 0.00 | 1.00 | 0.00 | 0.00 | +0.75% | low | low |
| RIO | Basic Materials | +0.636 | 0.00 | 1.00 | 0.00 | 0.00 | -0.48% | low | low |
| PM | Consumer Defensive | +0.636 | 0.00 | 1.00 | 0.00 | 0.00 | -0.78% | low | low |
| PGR | Financial | +0.636 | 0.00 | 1.00 | 0.00 | 0.00 | -1.10% | low | low |
| DHR | Healthcare | +0.636 | 0.00 | 1.00 | 0.00 | 0.00 | -0.12% | low | low |
| AEM | Basic Materials | +0.636 | 0.00 | 1.00 | 0.00 | 0.00 | -0.73% | low | low |
| PDD | Consumer Cyclical | +0.636 | 0.00 | 1.00 | 0.00 | 0.00 | +1.71% | low | low |
| MO | Consumer Defensive | +0.636 | 0.00 | 1.00 | 0.00 | 0.00 | -0.06% | low | low |
| TD | Financial | +0.636 | 0.00 | 1.00 | 0.00 | 0.00 | +0.63% | low | low |
| COP | Energy | +0.636 | 0.00 | 1.00 | 0.00 | 0.00 | -0.82% | low | low |

## Bottom 15 (lowest pressure)

| Ticker | Sector | pressure | SPEC | QUAL | resid | beta |
|--------|--------|----------|------|------|-------|------|
| GLSI | Healthcare | -1.518 | 0.95 | 0.00 | +3.46% | high |
| CHPT | Consumer Cyclical | -1.518 | 0.95 | 0.00 | +4.23% | high |
| EAF | Industrials | -1.468 | 0.95 | 0.00 | +2.95% | high |
| YFOR | Industrials | -1.433 | 0.85 | 0.00 | -12.84% | high |
| DAIC | Technology | -1.433 | 0.85 | 0.00 | -32.82% | high |
| CRDF | Healthcare | -1.433 | 0.85 | 0.00 | +5.59% | high |
| NCPL | Financial | -1.433 | 0.85 | 0.00 | +32.34% | high |
| LVWR | Consumer Cyclical | -1.417 | 0.95 | 0.00 | +14.99% | high |
| GEMI | Financial | -1.417 | 0.95 | 0.00 | +31.35% | high |
| BBNX | Healthcare | -1.417 | 0.95 | 0.00 | +2.35% | high |
| FLWS | Consumer Cyclical | -1.383 | 0.85 | 0.00 | -4.41% | high |
| CHOW | Technology | -1.383 | 0.85 | 0.00 | +12.70% | high |
| LASE | Industrials | -1.383 | 0.85 | 0.00 | +0.20% | high |
| TJGC | Communication Serv | -1.383 | 0.85 | 0.00 | +53.15% | high |
| SRFM | Industrials | -1.383 | 0.85 | 0.00 | +11.31% | high |

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
| micro | 2194 | 0.51 | 0.29 | -0.779 |
| mid | 1160 | 0.36 | 0.51 | -0.290 |
| small | 1614 | 0.48 | 0.41 | -0.603 |
| unknown | 5750 | 0.32 | 0.24 | -0.318 |
