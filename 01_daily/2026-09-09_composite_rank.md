# Composite residual rank — **2026-09-09**

Generated: 2026-09-09T19:19:34.084126-04:00
Prior snapshot (for returns): **2026-09-08**

## Y snapshot (v1 — breadth only)

- **p_risk_on:** 0.0 (from % names up)
- **pct_up:** 0.1942
- **median_ret:** -0.57%
- **conviction:** 1.0
- **n:** 11613
- note: price_derived breadth only (v1)

## Method (deliberately simple)

- **residual** = stock return − median stock return (same pair window)
- **composites:** SPEC_DURATION, QUALITY_DEFENSIVE, CROWDING, SIZE_TILT
- **pressure** = conviction × prior effects of composites given p_risk_on
- Ranking is **cross-sectional residual bias**, not an absolute SPY call
- Hand priors only — replace with audit weights later

CSV: `data/composite/2026-09-09_composite_rank.csv`

## Top 20 by residual pressure (favor when risk-on / current Y)

| Ticker | Sector | pressure | SPEC | QUAL | CROWD | SIZE | resid | beta | short |
|--------|--------|----------|------|------|-------|------|-------|------|-------|
| RIO | Basic Materials | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.49% | low | low |
| ABBV | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.43% | low | low |
| SCHW | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.27% | low | low |
| BRK-A | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.75% | low | low |
| BMY | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.14% | low | low |
| EQNR | Energy | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +4.81% | low | low |
| SAN | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.64% | low | low |
| RY | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.47% | low | low |
| BP | Energy | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +2.36% | low | low |
| V | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.23% | low | low |
| CB | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.86% | low | low |
| SHEL | Energy | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.87% | low | low |
| ENB | Energy | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.08% | low | low |
| IBN | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -1.15% | low | low |
| IBM | Technology | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +3.96% | low | low |
| AMGN | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.09% | low | low |
| JNJ | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.18% | low | low |
| LLY | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.60% | low | low |
| LIN | Basic Materials | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.20% | low | low |
| UL | Consumer Defensive | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -1.08% | low | low |

## Bottom 15 (lowest pressure)

| Ticker | Sector | pressure | SPEC | QUAL | resid | beta |
|--------|--------|----------|------|------|-------|------|
| CHPT | Consumer Cyclical | -1.790 | 0.95 | 0.00 | -3.91% | high |
| EOSE | Industrials | -1.670 | 0.95 | 0.00 | -2.91% | high |
| BTBT | Financial | -1.670 | 0.95 | 0.00 | -1.78% | high |
| SST | Industrials | -1.630 | 0.85 | 0.00 | -11.23% | high |
| MSS | Consumer Defensive | -1.630 | 0.85 | 0.00 | +9.38% | high |
| SKYE | Healthcare | -1.630 | 0.85 | 0.00 | +19.19% | high |
| XHLD | Communication Serv | -1.630 | 0.85 | 0.00 | +12.62% | high |
| TJGC | Communication Serv | -1.630 | 0.85 | 0.00 | +1.24% | high |
| DH | Healthcare | -1.630 | 0.85 | 0.00 | +1.55% | high |
| CRBP | Healthcare | -1.570 | 0.85 | 0.00 | -15.84% | high |
| ACH | Healthcare | -1.570 | 0.85 | 0.00 | -2.15% | high |
| GOAI | Technology | -1.555 | 0.85 | 0.00 | +2.29% | high |
| PBM | Healthcare | -1.555 | 0.85 | 0.00 | +2.68% | high |
| PDSB | Healthcare | -1.555 | 0.85 | 0.00 | -2.76% | high |
| MIMI | Industrials | -1.555 | 0.85 | 0.00 | +3.87% | high |

## Sector median pressure

| Sector | n | median pressure | median resid |
|--------|---|-----------------|--------------|
| Utilities | 107 | +0.055 | -0.52% |
| Energy | 253 | -0.155 | +0.98% |
| Financial | 7122 | -0.415 | +0.15% |
| Consumer Defensive | 242 | -0.440 | -0.64% |
| Real Estate | 248 | -0.505 | -0.33% |
| Industrials | 715 | -0.530 | -0.82% |
| Consumer Cyclical | 528 | -0.542 | -1.06% |
| Basic Materials | 291 | -0.580 | +0.07% |
| Communication Services | 257 | -0.700 | -0.95% |
| Technology | 792 | -0.700 | -0.80% |
| Healthcare | 1058 | -0.835 | -1.00% |

## Composite averages by size

| size | n | SPEC | QUAL | pressure |
|------|---|------|------|----------|
| large | 772 | 0.16 | 0.80 | +0.287 |
| mega | 169 | 0.14 | 0.84 | +0.483 |
| micro | 2169 | 0.51 | 0.30 | -0.915 |
| mid | 1178 | 0.36 | 0.51 | -0.335 |
| small | 1614 | 0.48 | 0.41 | -0.707 |
| unknown | 5711 | 0.32 | 0.25 | -0.377 |
