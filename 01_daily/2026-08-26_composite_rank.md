# Composite residual rank — **2026-08-26**

Generated: 2026-08-26T20:51:09.512703-04:00
Prior snapshot (for returns): **2026-08-25**

## Y snapshot (v1 — breadth only)

- **p_risk_on:** 0.1227 (from % names up)
- **pct_up:** 0.3991
- **median_ret:** -0.05%
- **conviction:** 0.7546
- **n:** 11637
- note: price_derived breadth only (v1)

## Method (deliberately simple)

- **residual** = stock return − median stock return (same pair window)
- **composites:** SPEC_DURATION, QUALITY_DEFENSIVE, CROWDING, SIZE_TILT
- **pressure** = conviction × prior effects of composites given p_risk_on
- Ranking is **cross-sectional residual bias**, not an absolute SPY call
- Hand priors only — replace with audit weights later

CSV: `data/composite/2026-08-26_composite_rank.csv`

## Top 20 by residual pressure (favor when risk-on / current Y)

| Ticker | Sector | pressure | SPEC | QUAL | CROWD | SIZE | resid | beta | short |
|--------|--------|----------|------|------|-------|------|-------|------|-------|
| JNJ | Healthcare | +0.427 | 0.00 | 1.00 | 0.00 | 0.00 | -1.10% | low | low |
| GD | Industrials | +0.427 | 0.00 | 1.00 | 0.00 | 0.00 | +1.50% | low | low |
| MCK | Healthcare | +0.427 | 0.00 | 1.00 | 0.00 | 0.00 | -0.88% | low | low |
| BABA | Consumer Cyclical | +0.427 | 0.00 | 1.00 | 0.00 | 0.00 | +0.38% | low | low |
| BTI | Consumer Defensive | +0.427 | 0.00 | 1.00 | 0.00 | 0.00 | +1.77% | low | low |
| MFG | Financial | +0.427 | 0.00 | 1.00 | 0.00 | 0.00 | +0.44% | low | low |
| MDT | Healthcare | +0.427 | 0.00 | 1.00 | 0.00 | 0.00 | +1.02% | low | low |
| TTE | Energy | +0.427 | 0.00 | 1.00 | 0.00 | 0.00 | -1.83% | low | low |
| NEE | Utilities | +0.427 | 0.00 | 1.00 | 0.00 | 0.00 | +0.05% | low | low |
| VLO | Energy | +0.427 | 0.00 | 1.00 | 0.00 | 0.00 | +2.29% | low | low |
| RIO | Basic Materials | +0.427 | 0.00 | 1.00 | 0.00 | 0.00 | -1.92% | low | low |
| CVX | Energy | +0.427 | 0.00 | 1.00 | 0.00 | 0.00 | +0.21% | low | low |
| CVS | Healthcare | +0.427 | 0.00 | 1.00 | 0.00 | 0.00 | +1.58% | low | low |
| MPC | Energy | +0.427 | 0.00 | 1.00 | 0.00 | 0.00 | +2.14% | low | low |
| SO | Utilities | +0.427 | 0.00 | 1.00 | 0.00 | 0.00 | -0.18% | low | low |
| BRK-B | Financial | +0.427 | 0.00 | 1.00 | 0.00 | 0.00 | +0.17% | low | low |
| BRK-A | Financial | +0.427 | 0.00 | 1.00 | 0.00 | 0.00 | +0.26% | low | low |
| PDD | Consumer Cyclical | +0.427 | 0.00 | 1.00 | 0.00 | 0.00 | -1.10% | low | low |
| TD | Financial | +0.427 | 0.00 | 1.00 | 0.00 | 0.00 | +0.36% | low | low |
| BP | Energy | +0.427 | 0.00 | 1.00 | 0.00 | 0.00 | -0.79% | low | low |

## Bottom 15 (lowest pressure)

| Ticker | Sector | pressure | SPEC | QUAL | resid | beta |
|--------|--------|----------|------|------|-------|------|
| LVWR | Consumer Cyclical | -1.019 | 0.95 | 0.00 | +11.43% | high |
| SPRB | Healthcare | -1.019 | 0.95 | 0.00 | -2.98% | high |
| CRBP | Healthcare | -0.985 | 0.95 | 0.00 | -0.04% | high |
| YYGH | Industrials | -0.962 | 0.85 | 0.00 | +84.40% | high |
| WW | Healthcare | -0.962 | 0.85 | 0.00 | -0.23% | high |
| BTCT | Technology | -0.962 | 0.85 | 0.00 | -9.45% | high |
| CRML | Basic Materials | -0.951 | 0.95 | 0.00 | -1.31% | high |
| WBTN | Communication Serv | -0.951 | 0.95 | 0.00 | +10.85% | high |
| PACB | Healthcare | -0.951 | 0.95 | 0.00 | +2.68% | high |
| SBET | Financial | -0.951 | 0.95 | 0.00 | -0.31% | high |
| ARCT | Healthcare | -0.951 | 0.95 | 0.00 | +2.58% | high |
| INBX | Healthcare | -0.951 | 0.95 | 0.00 | +2.19% | high |
| EBS | Healthcare | -0.951 | 0.95 | 0.00 | +5.90% | high |
| SGMT | Healthcare | -0.951 | 0.95 | 0.00 | +5.59% | high |
| AQST | Healthcare | -0.951 | 0.95 | 0.00 | +6.16% | high |

## Sector median pressure

| Sector | n | median pressure | median resid |
|--------|---|-----------------|--------------|
| Utilities | 109 | +0.026 | +0.31% |
| Energy | 252 | -0.085 | +0.02% |
| Financial | 7138 | -0.236 | +0.01% |
| Consumer Defensive | 243 | -0.256 | -0.22% |
| Real Estate | 251 | -0.288 | -0.82% |
| Industrials | 711 | -0.288 | +0.10% |
| Consumer Cyclical | 533 | -0.305 | -0.41% |
| Basic Materials | 287 | -0.316 | -0.96% |
| Communication Services | 258 | -0.399 | -0.62% |
| Technology | 791 | -0.399 | +0.01% |
| Healthcare | 1064 | -0.475 | -0.29% |

## Composite averages by size

| size | n | SPEC | QUAL | pressure |
|------|---|------|------|----------|
| large | 792 | 0.17 | 0.80 | +0.158 |
| mega | 171 | 0.15 | 0.84 | +0.271 |
| micro | 2153 | 0.51 | 0.30 | -0.522 |
| mid | 1186 | 0.36 | 0.51 | -0.193 |
| small | 1609 | 0.49 | 0.40 | -0.407 |
| unknown | 5726 | 0.32 | 0.25 | -0.217 |
