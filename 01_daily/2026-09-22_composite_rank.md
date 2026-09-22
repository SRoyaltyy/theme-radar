# Composite residual rank — **2026-09-22**

Generated: 2026-09-22T19:38:00.794098-04:00
Prior snapshot (for returns): **2026-09-21**

## Y snapshot (v1 — breadth only)

- **p_risk_on:** 0.5121 (from % names up)
- **pct_up:** 0.5548
- **median_ret:** 0.06%
- **conviction:** 0.0241
- **n:** 11647
- note: price_derived breadth only (v1)

## Method (deliberately simple)

- **residual** = stock return − median stock return (same pair window)
- **composites:** SPEC_DURATION, QUALITY_DEFENSIVE, CROWDING, SIZE_TILT
- **pressure** = conviction × prior effects of composites given p_risk_on
- Ranking is **cross-sectional residual bias**, not an absolute SPY call
- Hand priors only — replace with audit weights later

CSV: `data/composite/2026-09-22_composite_rank.csv`

## Top 20 by residual pressure (favor when risk-on / current Y)

| Ticker | Sector | pressure | SPEC | QUAL | CROWD | SIZE | resid | beta | short |
|--------|--------|----------|------|------|-------|------|-------|------|-------|
| GDC | Communication Serv | +0.006 | 0.95 | 0.00 | 0.80 | 1.00 | +9.53% | high | very_high |
| GLSI | Healthcare | +0.006 | 0.95 | 0.00 | 0.80 | 1.00 | +4.72% | high | very_high |
| LVWR | Consumer Cyclical | +0.006 | 0.95 | 0.00 | 0.80 | 1.00 | -5.29% | high | very_high |
| EU | Energy | +0.006 | 0.95 | 0.00 | 0.80 | 1.00 | +15.18% | high | very_high |
| EAF | Industrials | +0.006 | 0.95 | 0.00 | 0.60 | 1.00 | +19.70% | high | elevated |
| KAZR | Industrials | +0.006 | 0.85 | 0.00 | 0.80 | 1.00 | +9.44% | high | very_high |
| YFOR | Industrials | +0.006 | 0.85 | 0.00 | 0.80 | 1.00 | +5.96% | high | very_high |
| ABSI | Healthcare | +0.006 | 0.95 | 0.00 | 0.80 | 0.80 | +9.00% | high | very_high |
| GEMI | Financial | +0.006 | 0.95 | 0.00 | 0.80 | 0.80 | -0.73% | high | very_high |
| GRML | Basic Materials | +0.006 | 0.85 | 0.00 | 0.80 | 1.00 | +50.15% | high | very_high |
| RXT | Technology | +0.006 | 0.95 | 0.00 | 0.80 | 0.80 | +2.16% | high | very_high |
| CRML | Basic Materials | +0.006 | 0.95 | 0.00 | 0.80 | 0.80 | -8.53% | high | very_high |
| WYFI | Technology | +0.006 | 0.95 | 0.00 | 0.80 | 0.80 | +1.80% | high | very_high |
| DAIC | Technology | +0.006 | 0.85 | 0.00 | 0.80 | 1.00 | -3.95% | high | very_high |
| AEMD | Healthcare | +0.006 | 0.85 | 0.00 | 0.80 | 1.00 | +3.89% | high | very_high |
| FIRY | Communication Serv | +0.006 | 0.85 | 0.00 | 0.80 | 1.00 | +17.69% | high | very_high |
| BTBT | Financial | +0.006 | 0.95 | 0.00 | 0.80 | 0.80 | +2.13% | high | very_high |
| NCPL | Financial | +0.006 | 0.85 | 0.00 | 0.80 | 1.00 | -4.02% | high | very_high |
| MRAM | Technology | +0.006 | 0.95 | 0.00 | 0.80 | 0.80 | +2.91% | high | very_high |
| BKKT | Technology | +0.006 | 0.95 | 0.00 | 0.80 | 0.80 | +6.39% | high | very_high |

## Bottom 15 (lowest pressure)

| Ticker | Sector | pressure | SPEC | QUAL | resid | beta |
|--------|--------|----------|------|------|-------|------|
| AEM | Basic Materials | -0.003 | 0.00 | 1.00 | +3.01% | low |
| NVS | Healthcare | -0.003 | 0.00 | 1.00 | +0.15% | low |
| WMT | Consumer Defensive | -0.003 | 0.00 | 1.00 | +2.43% | low |
| SCHW | Financial | -0.003 | 0.00 | 1.00 | -6.17% | low |
| DHR | Healthcare | -0.003 | 0.00 | 1.00 | +2.37% | low |
| COP | Energy | -0.003 | 0.00 | 1.00 | -1.84% | low |
| ENB | Energy | -0.003 | 0.00 | 1.00 | -0.69% | low |
| SHEL | Energy | -0.003 | 0.00 | 1.00 | +0.64% | low |
| TM | Consumer Cyclical | -0.003 | 0.00 | 1.00 | -0.29% | low |
| RIO | Basic Materials | -0.003 | 0.00 | 1.00 | +0.40% | low |
| VZ | Communication Serv | -0.003 | 0.00 | 1.00 | -2.64% | low |
| VRTX | Healthcare | -0.003 | 0.00 | 1.00 | +0.77% | low |
| CB | Financial | -0.003 | 0.00 | 1.00 | -0.50% | low |
| PSX | Energy | -0.003 | 0.00 | 1.00 | -1.96% | low |
| SMFG | Financial | -0.003 | 0.00 | 1.00 | -2.05% | low |

## Sector median pressure

| Sector | n | median pressure | median resid |
|--------|---|-----------------|--------------|
| Healthcare | 1052 | +0.003 | +1.05% |
| Technology | 793 | +0.003 | +0.22% |
| Communication Services | 255 | +0.003 | -0.30% |
| Basic Materials | 291 | +0.002 | +2.25% |
| Consumer Cyclical | 528 | +0.002 | +0.79% |
| Industrials | 718 | +0.002 | +0.38% |
| Real Estate | 247 | +0.002 | +0.07% |
| Consumer Defensive | 242 | +0.002 | +0.31% |
| Financial | 7164 | +0.002 | -0.02% |
| Energy | 251 | +0.001 | -1.21% |
| Utilities | 106 | -0.000 | -0.40% |

## Composite averages by size

| size | n | SPEC | QUAL | pressure |
|------|---|------|------|----------|
| large | 774 | 0.17 | 0.79 | -0.001 |
| mega | 163 | 0.14 | 0.84 | -0.002 |
| micro | 2176 | 0.51 | 0.30 | +0.003 |
| mid | 1166 | 0.36 | 0.51 | +0.001 |
| small | 1617 | 0.48 | 0.41 | +0.003 |
| unknown | 5751 | 0.32 | 0.24 | +0.001 |
