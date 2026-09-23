# Composite residual rank — **2026-09-23**

Generated: 2026-09-23T19:46:33.333340-04:00
Prior snapshot (for returns): **2026-09-22**

## Y snapshot (v1 — breadth only)

- **p_risk_on:** 0.0 (from % names up)
- **pct_up:** 0.1612
- **median_ret:** -0.97%
- **conviction:** 1.0
- **n:** 11665
- note: price_derived breadth only (v1)

## Method (deliberately simple)

- **residual** = stock return − median stock return (same pair window)
- **composites:** SPEC_DURATION, QUALITY_DEFENSIVE, CROWDING, SIZE_TILT
- **pressure** = conviction × prior effects of composites given p_risk_on
- Ranking is **cross-sectional residual bias**, not an absolute SPY call
- Hand priors only — replace with audit weights later

CSV: `data/composite/2026-09-23_composite_rank.csv`

## Top 20 by residual pressure (favor when risk-on / current Y)

| Ticker | Sector | pressure | SPEC | QUAL | CROWD | SIZE | resid | beta | short |
|--------|--------|----------|------|------|-------|------|-------|------|-------|
| BABA | Consumer Cyclical | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -3.77% | low | low |
| VRTX | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.23% | low | low |
| BRK-A | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +2.21% | low | low |
| BRK-B | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.70% | low | low |
| TTE | Energy | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +2.99% | low | low |
| BTI | Consumer Defensive | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.15% | low | low |
| UNH | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.52% | low | low |
| UL | Consumer Defensive | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.26% | low | low |
| BMY | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.80% | low | low |
| BP | Energy | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +4.19% | low | low |
| ABT | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.77% | low | low |
| VZ | Communication Serv | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.12% | low | low |
| V | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.82% | low | low |
| VLO | Energy | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.62% | low | low |
| TM | Consumer Cyclical | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.08% | low | low |
| BUD | Consumer Defensive | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.49% | low | low |
| CVX | Energy | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +2.50% | low | low |
| DHR | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.18% | low | low |
| SMFG | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.14% | low | low |
| SCHW | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.12% | low | low |

## Bottom 15 (lowest pressure)

| Ticker | Sector | pressure | SPEC | QUAL | resid | beta |
|--------|--------|----------|------|------|-------|------|
| EU | Energy | -1.790 | 0.95 | 0.00 | +1.79% | high |
| ADCT | Healthcare | -1.730 | 0.95 | 0.00 | +7.47% | high |
| EAF | Industrials | -1.730 | 0.95 | 0.00 | +2.30% | high |
| MSS | Consumer Defensive | -1.690 | 0.85 | 0.00 | +35.58% | high |
| DAIC | Technology | -1.690 | 0.85 | 0.00 | -2.79% | high |
| VBIO | Healthcare | -1.690 | 0.85 | 0.00 | +10.61% | high |
| AEMD | Healthcare | -1.690 | 0.85 | 0.00 | +4.62% | high |
| NCPL | Financial | -1.690 | 0.85 | 0.00 | +8.18% | high |
| FIRY | Communication Serv | -1.690 | 0.85 | 0.00 | +4.93% | high |
| KAZR | Industrials | -1.690 | 0.85 | 0.00 | +3.23% | high |
| LGHL | Financial | -1.690 | 0.85 | 0.00 | -6.89% | high |
| GRML | Basic Materials | -1.690 | 0.85 | 0.00 | -19.95% | high |
| BTBT | Financial | -1.670 | 0.95 | 0.00 | -3.87% | high |
| GEMI | Financial | -1.670 | 0.95 | 0.00 | -4.41% | high |
| BKKT | Technology | -1.670 | 0.95 | 0.00 | -8.49% | high |

## Sector median pressure

| Sector | n | median pressure | median resid |
|--------|---|-----------------|--------------|
| Utilities | 106 | +0.045 | -0.77% |
| Energy | 251 | -0.155 | +0.62% |
| Financial | 7181 | -0.415 | +0.10% |
| Consumer Defensive | 242 | -0.478 | -0.06% |
| Real Estate | 247 | -0.505 | -0.60% |
| Industrials | 718 | -0.540 | +0.07% |
| Consumer Cyclical | 528 | -0.550 | -0.32% |
| Basic Materials | 292 | -0.555 | -1.66% |
| Communication Services | 255 | -0.700 | -0.51% |
| Technology | 793 | -0.700 | +0.16% |
| Healthcare | 1052 | -0.875 | -1.64% |

## Composite averages by size

| size | n | SPEC | QUAL | pressure |
|------|---|------|------|----------|
| large | 767 | 0.17 | 0.79 | +0.282 |
| mega | 161 | 0.14 | 0.84 | +0.479 |
| micro | 2189 | 0.51 | 0.30 | -0.923 |
| mid | 1154 | 0.36 | 0.51 | -0.342 |
| small | 1627 | 0.48 | 0.40 | -0.716 |
| unknown | 5767 | 0.32 | 0.24 | -0.387 |
