# Composite residual rank — **2026-10-30**

Generated: 2026-10-30T18:03:25.875316-04:00
Prior snapshot (for returns): **2026-10-29**

## Y snapshot (v1 — breadth only)

- **p_risk_on:** 0.0 (from % names up)
- **pct_up:** 0.2485
- **median_ret:** -1.07%
- **conviction:** 1.0
- **n:** 11785
- note: price_derived breadth only (v1)

## Method (deliberately simple)

- **residual** = stock return − median stock return (same pair window)
- **composites:** SPEC_DURATION, QUALITY_DEFENSIVE, CROWDING, SIZE_TILT
- **pressure** = conviction × prior effects of composites given p_risk_on
- Ranking is **cross-sectional residual bias**, not an absolute SPY call
- Hand priors only — replace with audit weights later

CSV: `data/composite/2026-10-30_composite_rank.csv`

## Top 20 by residual pressure (favor when risk-on / current Y)

| Ticker | Sector | pressure | SPEC | QUAL | CROWD | SIZE | resid | beta | short |
|--------|--------|----------|------|------|-------|------|-------|------|-------|
| MPC | Energy | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +3.90% | low | low |
| VLO | Energy | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +4.99% | low | low |
| BMY | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +2.85% | low | low |
| BP | Energy | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.15% | low | low |
| MO | Consumer Defensive | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +2.74% | low | low |
| DHR | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.93% | low | low |
| BRK-B | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.17% | low | low |
| BRK-A | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.84% | low | low |
| MUFG | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.66% | low | low |
| NEE | Utilities | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +2.98% | low | low |
| SHEL | Energy | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +2.02% | low | low |
| RY | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.41% | low | low |
| BTI | Consumer Defensive | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.81% | low | low |
| BUD | Consumer Defensive | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +2.15% | low | low |
| IBN | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +2.17% | low | low |
| VRTX | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +4.57% | low | low |
| CB | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.58% | low | low |
| MFG | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -2.23% | low | low |
| NVS | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.88% | low | low |
| NVO | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +3.27% | low | low |

## Bottom 15 (lowest pressure)

| Ticker | Sector | pressure | SPEC | QUAL | resid | beta |
|--------|--------|----------|------|------|-------|------|
| AIRS | Healthcare | -1.790 | 0.95 | 0.00 | +4.66% | high |
| KRRO | Healthcare | -1.790 | 0.95 | 0.00 | +1.84% | high |
| SLNH | Financial | -1.790 | 0.95 | 0.00 | -3.22% | high |
| DMRC | Technology | -1.730 | 0.95 | 0.00 | +1.75% | high |
| UPB | Healthcare | -1.730 | 0.95 | 0.00 | +5.35% | high |
| CRIS | Healthcare | -1.690 | 0.85 | 0.00 | +10.16% | high |
| CRMT | Consumer Cyclical | -1.690 | 0.85 | 0.00 | -0.82% | high |
| PACB | Healthcare | -1.670 | 0.95 | 0.00 | -8.93% | high |
| PCT | Industrials | -1.670 | 0.95 | 0.00 | +1.97% | high |
| TDOC | Healthcare | -1.670 | 0.95 | 0.00 | -1.45% | high |
| REAL | Consumer Cyclical | -1.670 | 0.95 | 0.00 | +6.44% | high |
| NRGV | Utilities | -1.670 | 0.95 | 0.00 | -4.43% | high |
| ABSI | Healthcare | -1.670 | 0.95 | 0.00 | -6.95% | high |
| BMBL | Communication Serv | -1.670 | 0.95 | 0.00 | +1.24% | high |
| PRME | Healthcare | -1.670 | 0.95 | 0.00 | -8.85% | high |

## Sector median pressure

| Sector | n | median pressure | median resid |
|--------|---|-----------------|--------------|
| Utilities | 107 | -0.030 | +1.13% |
| Energy | 252 | -0.185 | +0.86% |
| Financial | 7292 | -0.415 | +0.20% |
| Consumer Defensive | 240 | -0.440 | +1.07% |
| Real Estate | 248 | -0.505 | +0.19% |
| Industrials | 714 | -0.560 | -0.84% |
| Consumer Cyclical | 524 | -0.570 | +0.25% |
| Basic Materials | 297 | -0.580 | -2.33% |
| Technology | 801 | -0.700 | -2.73% |
| Communication Services | 254 | -0.702 | +0.05% |
| Healthcare | 1056 | -0.915 | -1.56% |

## Composite averages by size

| size | n | SPEC | QUAL | pressure |
|------|---|------|------|----------|
| large | 757 | 0.17 | 0.80 | +0.265 |
| mega | 161 | 0.14 | 0.83 | +0.470 |
| micro | 2259 | 0.52 | 0.28 | -0.941 |
| mid | 1127 | 0.36 | 0.51 | -0.348 |
| small | 1597 | 0.49 | 0.41 | -0.724 |
| unknown | 5884 | 0.32 | 0.24 | -0.383 |
