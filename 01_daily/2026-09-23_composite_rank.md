# Composite residual rank — **2026-09-23**

Generated: 2026-09-23T17:05:14.453561-04:00
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
| PGR | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.87% | low | low |
| TD | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -1.67% | low | low |
| TJX | Consumer Cyclical | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.58% | low | low |
| PG | Consumer Defensive | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.41% | low | low |
| COP | Energy | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +3.22% | low | low |
| RIO | Basic Materials | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -1.33% | low | low |
| MDT | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.65% | low | low |
| MO | Consumer Defensive | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.42% | low | low |
| IBN | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.50% | low | low |
| IBM | Technology | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.56% | low | low |
| SYK | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.35% | low | low |
| WMT | Consumer Defensive | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.34% | low | low |
| TMUS | Communication Serv | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +2.97% | low | low |
| TM | Consumer Cyclical | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.08% | low | low |
| PM | Consumer Defensive | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.29% | low | low |
| MCK | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.24% | low | low |
| MPC | Energy | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.63% | low | low |
| HSBC | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.35% | low | low |
| JNJ | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.96% | low | low |
| BMY | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.80% | low | low |

## Bottom 15 (lowest pressure)

| Ticker | Sector | pressure | SPEC | QUAL | resid | beta |
|--------|--------|----------|------|------|-------|------|
| EU | Energy | -1.790 | 0.95 | 0.00 | +1.79% | high |
| EAF | Industrials | -1.730 | 0.95 | 0.00 | +2.30% | high |
| ADCT | Healthcare | -1.730 | 0.95 | 0.00 | +7.47% | high |
| DAIC | Technology | -1.690 | 0.85 | 0.00 | -2.79% | high |
| LGHL | Financial | -1.690 | 0.85 | 0.00 | -6.89% | high |
| MSS | Consumer Defensive | -1.690 | 0.85 | 0.00 | +35.58% | high |
| NCPL | Financial | -1.690 | 0.85 | 0.00 | +8.18% | high |
| KAZR | Industrials | -1.690 | 0.85 | 0.00 | +3.23% | high |
| GRML | Basic Materials | -1.690 | 0.85 | 0.00 | -19.95% | high |
| AEMD | Healthcare | -1.690 | 0.85 | 0.00 | +4.62% | high |
| FIRY | Communication Serv | -1.690 | 0.85 | 0.00 | +4.93% | high |
| VBIO | Healthcare | -1.690 | 0.85 | 0.00 | +10.61% | high |
| GEMI | Financial | -1.670 | 0.95 | 0.00 | -4.41% | high |
| BKKT | Technology | -1.670 | 0.95 | 0.00 | -8.49% | high |
| BTBT | Financial | -1.670 | 0.95 | 0.00 | -3.87% | high |

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
| micro | 2188 | 0.51 | 0.30 | -0.923 |
| mid | 1154 | 0.36 | 0.51 | -0.342 |
| small | 1627 | 0.48 | 0.40 | -0.716 |
| unknown | 5768 | 0.32 | 0.24 | -0.387 |
