# Composite residual rank — **2026-09-15**

Generated: 2026-09-15T19:33:29.473448-04:00
Prior snapshot (for returns): **2026-09-14**

## Y snapshot (v1 — breadth only)

- **p_risk_on:** 0.0 (from % names up)
- **pct_up:** 0.2315
- **median_ret:** -0.43%
- **conviction:** 1.0
- **n:** 11633
- note: price_derived breadth only (v1)

## Method (deliberately simple)

- **residual** = stock return − median stock return (same pair window)
- **composites:** SPEC_DURATION, QUALITY_DEFENSIVE, CROWDING, SIZE_TILT
- **pressure** = conviction × prior effects of composites given p_risk_on
- Ranking is **cross-sectional residual bias**, not an absolute SPY call
- Hand priors only — replace with audit weights later

CSV: `data/composite/2026-09-15_composite_rank.csv`

## Top 20 by residual pressure (favor when risk-on / current Y)

| Ticker | Sector | pressure | SPEC | QUAL | CROWD | SIZE | resid | beta | short |
|--------|--------|----------|------|------|-------|------|-------|------|-------|
| BTI | Consumer Defensive | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.91% | low | low |
| ABBV | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.92% | low | low |
| NEE | Utilities | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.25% | low | low |
| V | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.52% | low | low |
| IBN | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -2.51% | low | low |
| NEM | Basic Materials | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.34% | low | low |
| IBM | Technology | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.15% | low | low |
| SAN | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.18% | low | low |
| PG | Consumer Defensive | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.80% | low | low |
| RY | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.02% | low | low |
| BRK-A | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.70% | low | low |
| MFG | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -1.15% | low | low |
| BRK-B | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.79% | low | low |
| CVS | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.68% | low | low |
| PGR | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.57% | low | low |
| AZN | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.74% | low | low |
| TM | Consumer Cyclical | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.62% | low | low |
| NVO | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -1.68% | low | low |
| SMFG | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -1.25% | low | low |
| BABA | Consumer Cyclical | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.53% | low | low |

## Bottom 15 (lowest pressure)

| Ticker | Sector | pressure | SPEC | QUAL | resid | beta |
|--------|--------|----------|------|------|-------|------|
| VERI | Technology | -1.790 | 0.95 | 0.00 | -3.04% | high |
| CRDF | Healthcare | -1.690 | 0.85 | 0.00 | +2.72% | high |
| SDGR | Healthcare | -1.670 | 0.95 | 0.00 | +12.48% | high |
| KLC | Consumer Defensive | -1.630 | 0.85 | 0.00 | -2.09% | high |
| AIRS | Healthcare | -1.630 | 0.85 | 0.00 | -10.07% | high |
| FGI | Consumer Cyclical | -1.630 | 0.85 | 0.00 | +11.61% | high |
| PLAY | Communication Serv | -1.630 | 0.85 | 0.00 | -18.57% | high |
| BNGO | Healthcare | -1.630 | 0.85 | 0.00 | +17.73% | high |
| FLWS | Consumer Cyclical | -1.630 | 0.85 | 0.00 | +0.76% | high |
| TJGC | Communication Serv | -1.630 | 0.85 | 0.00 | -4.25% | high |
| MYGN | Healthcare | -1.610 | 0.95 | 0.00 | +2.81% | high |
| ACVA | Consumer Cyclical | -1.610 | 0.95 | 0.00 | +0.63% | high |
| CRBU | Healthcare | -1.570 | 0.85 | 0.00 | -1.12% | high |
| LODE | Basic Materials | -1.570 | 0.85 | 0.00 | -4.42% | high |
| CRBP | Healthcare | -1.570 | 0.85 | 0.00 | -13.92% | high |

## Sector median pressure

| Sector | n | median pressure | median resid |
|--------|---|-----------------|--------------|
| Utilities | 107 | +0.045 | -0.56% |
| Energy | 251 | -0.205 | +1.77% |
| Financial | 7144 | -0.415 | +0.08% |
| Consumer Defensive | 242 | -0.440 | -0.65% |
| Real Estate | 248 | -0.505 | -0.12% |
| Industrials | 717 | -0.530 | -0.07% |
| Consumer Cyclical | 528 | -0.560 | -1.36% |
| Basic Materials | 291 | -0.580 | +0.08% |
| Communication Services | 256 | -0.700 | -0.67% |
| Technology | 794 | -0.700 | -0.59% |
| Healthcare | 1055 | -0.840 | -1.15% |

## Composite averages by size

| size | n | SPEC | QUAL | pressure |
|------|---|------|------|----------|
| large | 773 | 0.17 | 0.80 | +0.284 |
| mega | 164 | 0.14 | 0.84 | +0.486 |
| micro | 2180 | 0.51 | 0.29 | -0.920 |
| mid | 1158 | 0.36 | 0.51 | -0.337 |
| small | 1622 | 0.48 | 0.40 | -0.714 |
| unknown | 5736 | 0.32 | 0.24 | -0.383 |
