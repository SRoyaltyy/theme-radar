# Composite residual rank — **2026-11-09**

Generated: 2026-11-09T17:10:55.709775-05:00
Prior snapshot (for returns): **2026-11-06**

## Y snapshot (v1 — breadth only)

- **p_risk_on:** 1.0 (from % names up)
- **pct_up:** 0.7942
- **median_ret:** 1.82%
- **conviction:** 1.0
- **n:** 11742
- note: price_derived breadth only (v1)

## Method (deliberately simple)

- **residual** = stock return − median stock return (same pair window)
- **composites:** SPEC_DURATION, QUALITY_DEFENSIVE, CROWDING, SIZE_TILT
- **pressure** = conviction × prior effects of composites given p_risk_on
- Ranking is **cross-sectional residual bias**, not an absolute SPY call
- Hand priors only — replace with audit weights later

CSV: `data/composite/2026-11-09_composite_rank.csv`

## Top 20 by residual pressure (favor when risk-on / current Y)

| Ticker | Sector | pressure | SPEC | QUAL | CROWD | SIZE | resid | beta | short |
|--------|--------|----------|------|------|-------|------|-------|------|-------|
| SERV | Industrials | +1.790 | 0.95 | 0.00 | 0.80 | 1.00 | +3.46% | high | very_high |
| HRTX | Healthcare | +1.790 | 0.95 | 0.00 | 0.80 | 1.00 | +25.77% | high | very_high |
| ORGO | Healthcare | +1.790 | 0.95 | 0.00 | 0.80 | 1.00 | +10.53% | high | very_high |
| AMTX | Basic Materials | +1.730 | 0.95 | 0.00 | 0.60 | 1.00 | +4.97% | high | elevated |
| LODE | Basic Materials | +1.730 | 0.95 | 0.00 | 0.60 | 1.00 | -3.36% | high | elevated |
| ARMP | Healthcare | +1.730 | 0.95 | 0.00 | 0.60 | 1.00 | +6.44% | high | elevated |
| STXS | Healthcare | +1.730 | 0.95 | 0.00 | 0.60 | 1.00 | +2.77% | high | elevated |
| DNA | Healthcare | +1.670 | 0.95 | 0.00 | 0.80 | 0.80 | +7.75% | high | very_high |
| EVGO | Consumer Cyclical | +1.670 | 0.95 | 0.00 | 0.80 | 0.80 | -1.27% | high | very_high |
| BKSY | Industrials | +1.670 | 0.95 | 0.00 | 0.80 | 0.80 | +10.23% | high | very_high |
| ARRY | Technology | +1.670 | 0.95 | 0.00 | 0.80 | 0.80 | -13.25% | high | very_high |
| HYMC | Basic Materials | +1.670 | 0.95 | 0.00 | 0.80 | 0.80 | +11.50% | high | very_high |
| SATL | Industrials | +1.670 | 0.95 | 0.00 | 0.80 | 0.80 | +11.97% | high | very_high |
| NRGV | Industrials | +1.670 | 0.95 | 0.00 | 0.80 | 0.80 | +9.91% | high | very_high |
| WOLF | Technology | +1.670 | 0.95 | 0.00 | 0.80 | 0.80 | +7.98% | high | very_high |
| INBX | Healthcare | +1.670 | 0.95 | 0.00 | 0.80 | 0.80 | +6.72% | high | very_high |
| ULCC | Industrials | +1.670 | 0.95 | 0.00 | 0.80 | 0.80 | +10.56% | high | very_high |
| INDI | Technology | +1.670 | 0.95 | 0.00 | 0.80 | 0.80 | +19.73% | high | very_high |
| FIP | Industrials | +1.670 | 0.95 | 0.00 | 0.80 | 0.80 | +5.10% | high | very_high |
| OCGN | Healthcare | +1.670 | 0.95 | 0.00 | 0.80 | 0.80 | +2.48% | high | very_high |

## Bottom 15 (lowest pressure)

| Ticker | Sector | pressure | SPEC | QUAL | resid | beta |
|--------|--------|----------|------|------|-------|------|
| VZ | Communication Serv | -0.750 | 0.00 | 1.00 | -1.01% | low |
| PG | Consumer Defensive | -0.750 | 0.00 | 1.00 | -0.05% | low |
| PGR | Financial | -0.750 | 0.00 | 1.00 | -1.93% | low |
| JNJ | Healthcare | -0.750 | 0.00 | 1.00 | +0.31% | low |
| VRTX | Healthcare | -0.750 | 0.00 | 1.00 | -1.13% | low |
| MUFG | Financial | -0.750 | 0.00 | 1.00 | +1.66% | low |
| TMUS | Communication Serv | -0.750 | 0.00 | 1.00 | +2.32% | low |
| ENB | Energy | -0.750 | 0.00 | 1.00 | -0.73% | low |
| CB | Financial | -0.750 | 0.00 | 1.00 | -2.25% | low |
| RIO | Basic Materials | -0.750 | 0.00 | 1.00 | +1.36% | low |
| GSK | Healthcare | -0.750 | 0.00 | 1.00 | +0.59% | low |
| LMT | Industrials | -0.750 | 0.00 | 1.00 | +1.90% | low |
| LLY | Healthcare | -0.750 | 0.00 | 1.00 | +2.46% | low |
| WMT | Consumer Defensive | -0.750 | 0.00 | 1.00 | -1.71% | low |
| V | Financial | -0.750 | 0.00 | 1.00 | -1.93% | low |

## Sector median pressure

| Sector | n | median pressure | median resid |
|--------|---|-----------------|--------------|
| Healthcare | 1053 | +0.935 | +0.89% |
| Technology | 800 | +0.700 | +1.23% |
| Communication Services | 252 | +0.700 | -0.12% |
| Industrials | 716 | +0.580 | +2.07% |
| Consumer Cyclical | 521 | +0.570 | +0.50% |
| Basic Materials | 298 | +0.545 | +2.40% |
| Consumer Defensive | 240 | +0.505 | -0.19% |
| Real Estate | 247 | +0.505 | -0.63% |
| Financial | 7259 | +0.415 | -0.18% |
| Energy | 252 | +0.205 | -1.05% |
| Utilities | 104 | -0.087 | -0.80% |

## Composite averages by size

| size | n | SPEC | QUAL | pressure |
|------|---|------|------|----------|
| large | 769 | 0.17 | 0.80 | -0.279 |
| mega | 163 | 0.14 | 0.84 | -0.475 |
| micro | 2240 | 0.52 | 0.28 | +0.945 |
| mid | 1112 | 0.36 | 0.52 | +0.345 |
| small | 1610 | 0.50 | 0.40 | +0.737 |
| unknown | 5848 | 0.32 | 0.25 | +0.379 |
