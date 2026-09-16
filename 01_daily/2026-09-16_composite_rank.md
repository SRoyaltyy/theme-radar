# Composite residual rank — **2026-09-16**

Generated: 2026-09-16T19:40:42.391295-04:00
Prior snapshot (for returns): **2026-09-15**

## Y snapshot (v1 — breadth only)

- **p_risk_on:** 0.0 (from % names up)
- **pct_up:** 0.3099
- **median_ret:** -0.24%
- **conviction:** 1.0
- **n:** 11640
- note: price_derived breadth only (v1)

## Method (deliberately simple)

- **residual** = stock return − median stock return (same pair window)
- **composites:** SPEC_DURATION, QUALITY_DEFENSIVE, CROWDING, SIZE_TILT
- **pressure** = conviction × prior effects of composites given p_risk_on
- Ranking is **cross-sectional residual bias**, not an absolute SPY call
- Hand priors only — replace with audit weights later

CSV: `data/composite/2026-09-16_composite_rank.csv`

## Top 20 by residual pressure (favor when risk-on / current Y)

| Ticker | Sector | pressure | SPEC | QUAL | CROWD | SIZE | resid | beta | short |
|--------|--------|----------|------|------|-------|------|-------|------|-------|
| NVS | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.30% | low | low |
| TD | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.48% | low | low |
| VZ | Communication Serv | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -3.04% | low | low |
| RTX | Industrials | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.92% | low | low |
| JNJ | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.27% | low | low |
| TM | Consumer Cyclical | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -1.43% | low | low |
| SYK | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.40% | low | low |
| LIN | Basic Materials | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.05% | low | low |
| KO | Consumer Defensive | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.71% | low | low |
| SAN | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -1.47% | low | low |
| XOM | Energy | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -3.30% | low | low |
| UNH | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.06% | low | low |
| UL | Consumer Defensive | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.24% | low | low |
| MA | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.72% | low | low |
| LLY | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.39% | low | low |
| LMT | Industrials | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.95% | low | low |
| HSBC | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -1.11% | low | low |
| RY | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.71% | low | low |
| IBM | Technology | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -4.14% | low | low |
| IBN | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.64% | low | low |

## Bottom 15 (lowest pressure)

| Ticker | Sector | pressure | SPEC | QUAL | resid | beta |
|--------|--------|----------|------|------|-------|------|
| VERI | Technology | -1.790 | 0.95 | 0.00 | -1.56% | high |
| EAF | Industrials | -1.730 | 0.95 | 0.00 | +13.99% | high |
| YFOR | Industrials | -1.690 | 0.85 | 0.00 | +23.10% | high |
| CRMT | Consumer Cyclical | -1.690 | 0.85 | 0.00 | +7.98% | high |
| CRDF | Healthcare | -1.690 | 0.85 | 0.00 | +0.99% | high |
| SDGR | Healthcare | -1.670 | 0.95 | 0.00 | +3.17% | high |
| BBNX | Healthcare | -1.670 | 0.95 | 0.00 | +15.58% | high |
| GSUN | Consumer Defensive | -1.630 | 0.85 | 0.00 | +30.68% | high |
| PLAY | Communication Serv | -1.630 | 0.85 | 0.00 | +0.24% | high |
| AIRS | Healthcare | -1.630 | 0.85 | 0.00 | -0.70% | high |
| FLWS | Consumer Cyclical | -1.630 | 0.85 | 0.00 | -11.49% | high |
| BNGO | Healthcare | -1.630 | 0.85 | 0.00 | -2.96% | high |
| TJGC | Communication Serv | -1.630 | 0.85 | 0.00 | +0.51% | high |
| HCWC | Consumer Defensive | -1.630 | 0.85 | 0.00 | +40.76% | high |
| EYPT | Healthcare | -1.630 | 0.85 | 0.00 | -5.50% | high |

## Sector median pressure

| Sector | n | median pressure | median resid |
|--------|---|-----------------|--------------|
| Utilities | 107 | +0.045 | +0.61% |
| Energy | 251 | -0.205 | -1.89% |
| Financial | 7151 | -0.415 | +0.04% |
| Consumer Defensive | 242 | -0.440 | +0.24% |
| Real Estate | 248 | -0.505 | -0.57% |
| Industrials | 717 | -0.530 | -0.02% |
| Basic Materials | 291 | -0.565 | -0.64% |
| Consumer Cyclical | 528 | -0.565 | -0.39% |
| Communication Services | 256 | -0.700 | -0.44% |
| Technology | 794 | -0.700 | -0.22% |
| Healthcare | 1055 | -0.875 | +0.13% |

## Composite averages by size

| size | n | SPEC | QUAL | pressure |
|------|---|------|------|----------|
| large | 772 | 0.17 | 0.80 | +0.285 |
| mega | 163 | 0.14 | 0.84 | +0.491 |
| micro | 2187 | 0.51 | 0.29 | -0.920 |
| mid | 1154 | 0.35 | 0.51 | -0.336 |
| small | 1625 | 0.48 | 0.40 | -0.714 |
| unknown | 5739 | 0.32 | 0.24 | -0.381 |
