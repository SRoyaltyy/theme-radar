# Composite residual rank — **2026-10-13**

Generated: 2026-10-13T16:48:17.687327-04:00
Prior snapshot (for returns): **2026-10-12**

## Y snapshot (v1 — breadth only)

- **p_risk_on:** 0.2008 (from % names up)
- **pct_up:** 0.4303
- **median_ret:** -0.02%
- **conviction:** 0.5984
- **n:** 11726
- note: price_derived breadth only (v1)

## Method (deliberately simple)

- **residual** = stock return − median stock return (same pair window)
- **composites:** SPEC_DURATION, QUALITY_DEFENSIVE, CROWDING, SIZE_TILT
- **pressure** = conviction × prior effects of composites given p_risk_on
- Ranking is **cross-sectional residual bias**, not an absolute SPY call
- Hand priors only — replace with audit weights later

CSV: `data/composite/2026-10-13_composite_rank.csv`

## Top 20 by residual pressure (favor when risk-on / current Y)

| Ticker | Sector | pressure | SPEC | QUAL | CROWD | SIZE | resid | beta | short |
|--------|--------|----------|------|------|-------|------|-------|------|-------|
| AZN | Healthcare | +0.269 | 0.00 | 1.00 | 0.00 | 0.00 | -1.57% | low | low |
| DHR | Healthcare | +0.269 | 0.00 | 1.00 | 0.00 | 0.00 | +0.76% | low | low |
| RTX | Industrials | +0.269 | 0.00 | 1.00 | 0.00 | 0.00 | -1.93% | low | low |
| RY | Financial | +0.269 | 0.00 | 1.00 | 0.00 | 0.00 | +1.01% | low | low |
| SAN | Financial | +0.269 | 0.00 | 1.00 | 0.00 | 0.00 | +0.54% | low | low |
| UNH | Healthcare | +0.269 | 0.00 | 1.00 | 0.00 | 0.00 | -0.18% | low | low |
| SCHW | Financial | +0.269 | 0.00 | 1.00 | 0.00 | 0.00 | -1.13% | low | low |
| MUFG | Financial | +0.269 | 0.00 | 1.00 | 0.00 | 0.00 | +0.24% | low | low |
| CVX | Energy | +0.269 | 0.00 | 1.00 | 0.00 | 0.00 | +1.29% | low | low |
| MCK | Healthcare | +0.269 | 0.00 | 1.00 | 0.00 | 0.00 | +0.66% | low | low |
| CVS | Healthcare | +0.269 | 0.00 | 1.00 | 0.00 | 0.00 | -0.20% | low | low |
| HDB | Financial | +0.269 | 0.00 | 1.00 | 0.00 | 0.00 | +0.82% | low | low |
| TTE | Energy | +0.269 | 0.00 | 1.00 | 0.00 | 0.00 | +0.68% | low | low |
| COP | Energy | +0.269 | 0.00 | 1.00 | 0.00 | 0.00 | +2.45% | low | low |
| MRK | Healthcare | +0.269 | 0.00 | 1.00 | 0.00 | 0.00 | -2.37% | low | low |
| SMFG | Financial | +0.269 | 0.00 | 1.00 | 0.00 | 0.00 | +0.74% | low | low |
| SO | Utilities | +0.269 | 0.00 | 1.00 | 0.00 | 0.00 | +1.25% | low | low |
| MCD | Consumer Cyclical | +0.269 | 0.00 | 1.00 | 0.00 | 0.00 | +0.09% | low | low |
| MO | Consumer Defensive | +0.269 | 0.00 | 1.00 | 0.00 | 0.00 | -0.12% | low | low |
| IBN | Financial | +0.269 | 0.00 | 1.00 | 0.00 | 0.00 | +1.77% | low | low |

## Bottom 15 (lowest pressure)

| Ticker | Sector | pressure | SPEC | QUAL | resid | beta |
|--------|--------|----------|------|------|-------|------|
| ADCT | Healthcare | -0.620 | 0.95 | 0.00 | -8.58% | high |
| CRMT | Consumer Cyclical | -0.605 | 0.85 | 0.00 | +11.38% | high |
| NCPL | Financial | -0.605 | 0.85 | 0.00 | -9.72% | high |
| AI | Technology | -0.598 | 0.95 | 0.00 | +3.47% | high |
| WBUY | Consumer Cyclical | -0.584 | 0.85 | 0.00 | +14.83% | high |
| PDSB | Healthcare | -0.584 | 0.85 | 0.00 | +5.28% | high |
| ABAT | Industrials | -0.584 | 0.85 | 0.00 | -4.35% | high |
| ABEO | Healthcare | -0.584 | 0.85 | 0.00 | -7.74% | high |
| AIRO | Industrials | -0.584 | 0.85 | 0.00 | -5.32% | high |
| CRBP | Healthcare | -0.584 | 0.85 | 0.00 | -9.28% | high |
| WATT | Technology | -0.584 | 0.85 | 0.00 | -10.74% | high |
| LXEO | Healthcare | -0.584 | 0.85 | 0.00 | -9.85% | high |
| PDYN | Technology | -0.584 | 0.85 | 0.00 | -3.91% | high |
| PAL | Industrials | -0.584 | 0.85 | 0.00 | -1.11% | high |
| CABA | Healthcare | -0.584 | 0.85 | 0.00 | -5.57% | high |

## Sector median pressure

| Sector | n | median pressure | median resid |
|--------|---|-----------------|--------------|
| Utilities | 107 | +0.016 | +0.24% |
| Energy | 252 | -0.073 | +1.07% |
| Financial | 7237 | -0.149 | +0.02% |
| Consumer Defensive | 241 | -0.167 | -0.07% |
| Real Estate | 247 | -0.181 | -0.21% |
| Industrials | 717 | -0.197 | -0.10% |
| Basic Materials | 293 | -0.202 | -0.54% |
| Consumer Cyclical | 526 | -0.204 | +0.43% |
| Communication Services | 254 | -0.251 | +0.07% |
| Technology | 799 | -0.251 | -0.42% |
| Healthcare | 1053 | -0.335 | -2.67% |

## Composite averages by size

| size | n | SPEC | QUAL | pressure |
|------|---|------|------|----------|
| large | 769 | 0.17 | 0.80 | +0.097 |
| mega | 164 | 0.15 | 0.84 | +0.168 |
| micro | 2221 | 0.51 | 0.28 | -0.335 |
| mid | 1116 | 0.36 | 0.52 | -0.120 |
| small | 1631 | 0.49 | 0.40 | -0.261 |
| unknown | 5825 | 0.32 | 0.25 | -0.136 |
