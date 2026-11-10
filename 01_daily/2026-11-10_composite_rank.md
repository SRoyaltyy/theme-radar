# Composite residual rank — **2026-11-10**

Generated: 2026-11-10T16:59:33.514028-05:00
Prior snapshot (for returns): **2026-11-09**

## Y snapshot (v1 — breadth only)

- **p_risk_on:** 0.0 (from % names up)
- **pct_up:** 0.261
- **median_ret:** -0.42%
- **conviction:** 1.0
- **n:** 11747
- note: price_derived breadth only (v1)

## Method (deliberately simple)

- **residual** = stock return − median stock return (same pair window)
- **composites:** SPEC_DURATION, QUALITY_DEFENSIVE, CROWDING, SIZE_TILT
- **pressure** = conviction × prior effects of composites given p_risk_on
- Ranking is **cross-sectional residual bias**, not an absolute SPY call
- Hand priors only — replace with audit weights later

CSV: `data/composite/2026-11-10_composite_rank.csv`

## Top 20 by residual pressure (favor when risk-on / current Y)

| Ticker | Sector | pressure | SPEC | QUAL | CROWD | SIZE | resid | beta | short |
|--------|--------|----------|------|------|-------|------|-------|------|-------|
| ABBV | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.62% | low | low |
| AMGN | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.42% | low | low |
| GSK | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.18% | low | low |
| SHEL | Energy | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -1.21% | low | low |
| SCHW | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.74% | low | low |
| NVS | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.16% | low | low |
| NVO | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -1.22% | low | low |
| ENB | Energy | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.18% | low | low |
| ABT | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.38% | low | low |
| TJX | Consumer Cyclical | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.45% | low | low |
| IBM | Technology | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.22% | low | low |
| PEP | Consumer Defensive | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.64% | low | low |
| WMT | Consumer Defensive | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.33% | low | low |
| RTX | Industrials | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +2.44% | low | low |
| PFE | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.87% | low | low |
| T | Communication Serv | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.06% | low | low |
| MUFG | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.19% | low | low |
| PDD | Consumer Cyclical | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.95% | low | low |
| SYK | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.02% | low | low |
| SAN | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.22% | low | low |

## Bottom 15 (lowest pressure)

| Ticker | Sector | pressure | SPEC | QUAL | resid | beta |
|--------|--------|----------|------|------|-------|------|
| EVMN | Healthcare | -1.790 | 0.95 | 0.00 | +2.91% | high |
| HRTX | Healthcare | -1.790 | 0.95 | 0.00 | +0.42% | high |
| UIS | Technology | -1.730 | 0.95 | 0.00 | +7.77% | high |
| ARMP | Healthcare | -1.730 | 0.95 | 0.00 | -0.89% | high |
| DTIL | Healthcare | -1.730 | 0.95 | 0.00 | -1.44% | high |
| STXS | Healthcare | -1.730 | 0.95 | 0.00 | -9.23% | high |
| LODE | Basic Materials | -1.730 | 0.95 | 0.00 | -12.60% | high |
| AMTX | Basic Materials | -1.730 | 0.95 | 0.00 | -7.67% | high |
| KULR | Technology | -1.690 | 0.85 | 0.00 | +22.51% | high |
| GOSS | Healthcare | -1.690 | 0.85 | 0.00 | +6.34% | high |
| NCPL | Financial | -1.690 | 0.85 | 0.00 | +8.66% | high |
| FIP | Industrials | -1.670 | 0.95 | 0.00 | +3.93% | high |
| EVGO | Consumer Cyclical | -1.670 | 0.95 | 0.00 | -0.67% | high |
| OCGN | Healthcare | -1.670 | 0.95 | 0.00 | -1.64% | high |
| JBLU | Industrials | -1.670 | 0.95 | 0.00 | +1.94% | high |

## Sector median pressure

| Sector | n | median pressure | median resid |
|--------|---|-----------------|--------------|
| Utilities | 104 | +0.087 | +0.28% |
| Energy | 252 | -0.215 | +0.46% |
| Financial | 7264 | -0.415 | +0.05% |
| Consumer Defensive | 240 | -0.505 | -0.08% |
| Real Estate | 247 | -0.525 | -0.41% |
| Consumer Cyclical | 521 | -0.565 | -0.51% |
| Basic Materials | 298 | -0.573 | -2.42% |
| Industrials | 716 | -0.593 | -0.11% |
| Communication Services | 252 | -0.700 | -0.02% |
| Technology | 800 | -0.708 | -0.59% |
| Healthcare | 1053 | -0.925 | -0.68% |

## Composite averages by size

| size | n | SPEC | QUAL | pressure |
|------|---|------|------|----------|
| large | 766 | 0.16 | 0.81 | +0.284 |
| mega | 163 | 0.15 | 0.84 | +0.473 |
| micro | 2255 | 0.52 | 0.28 | -0.946 |
| mid | 1116 | 0.36 | 0.52 | -0.346 |
| small | 1594 | 0.49 | 0.40 | -0.734 |
| unknown | 5853 | 0.32 | 0.25 | -0.377 |
