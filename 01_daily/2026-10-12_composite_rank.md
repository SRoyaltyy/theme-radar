# Composite residual rank — **2026-10-12**

Generated: 2026-10-12T17:00:06.782414-04:00
Prior snapshot (for returns): **2026-10-09**

## Y snapshot (v1 — breadth only)

- **p_risk_on:** 0.1219 (from % names up)
- **pct_up:** 0.3988
- **median_ret:** -0.07%
- **conviction:** 0.7561
- **n:** 11726
- note: price_derived breadth only (v1)

## Method (deliberately simple)

- **residual** = stock return − median stock return (same pair window)
- **composites:** SPEC_DURATION, QUALITY_DEFENSIVE, CROWDING, SIZE_TILT
- **pressure** = conviction × prior effects of composites given p_risk_on
- Ranking is **cross-sectional residual bias**, not an absolute SPY call
- Hand priors only — replace with audit weights later

CSV: `data/composite/2026-10-12_composite_rank.csv`

## Top 20 by residual pressure (favor when risk-on / current Y)

| Ticker | Sector | pressure | SPEC | QUAL | CROWD | SIZE | resid | beta | short |
|--------|--------|----------|------|------|-------|------|-------|------|-------|
| CB | Financial | +0.429 | 0.00 | 1.00 | 0.00 | 0.00 | +1.20% | low | low |
| TD | Financial | +0.429 | 0.00 | 1.00 | 0.00 | 0.00 | +1.28% | low | low |
| BTI | Consumer Defensive | +0.429 | 0.00 | 1.00 | 0.00 | 0.00 | +0.28% | low | low |
| MFG | Financial | +0.429 | 0.00 | 1.00 | 0.00 | 0.00 | -0.12% | low | low |
| CVS | Healthcare | +0.429 | 0.00 | 1.00 | 0.00 | 0.00 | +1.90% | low | low |
| UL | Consumer Defensive | +0.429 | 0.00 | 1.00 | 0.00 | 0.00 | +1.18% | low | low |
| WMT | Consumer Defensive | +0.429 | 0.00 | 1.00 | 0.00 | 0.00 | +1.62% | low | low |
| TM | Consumer Cyclical | +0.429 | 0.00 | 1.00 | 0.00 | 0.00 | -0.25% | low | low |
| T | Communication Serv | +0.429 | 0.00 | 1.00 | 0.00 | 0.00 | +1.47% | low | low |
| IBN | Financial | +0.429 | 0.00 | 1.00 | 0.00 | 0.00 | +0.64% | low | low |
| PDD | Consumer Cyclical | +0.429 | 0.00 | 1.00 | 0.00 | 0.00 | -0.46% | low | low |
| BP | Energy | +0.429 | 0.00 | 1.00 | 0.00 | 0.00 | +1.11% | low | low |
| TMUS | Communication Serv | +0.429 | 0.00 | 1.00 | 0.00 | 0.00 | +2.28% | low | low |
| BRK-A | Financial | +0.429 | 0.00 | 1.00 | 0.00 | 0.00 | +0.46% | low | low |
| BRK-B | Financial | +0.429 | 0.00 | 1.00 | 0.00 | 0.00 | +0.45% | low | low |
| XOM | Energy | +0.429 | 0.00 | 1.00 | 0.00 | 0.00 | +1.97% | low | low |
| MUFG | Financial | +0.429 | 0.00 | 1.00 | 0.00 | 0.00 | -0.07% | low | low |
| AMGN | Healthcare | +0.429 | 0.00 | 1.00 | 0.00 | 0.00 | +0.72% | low | low |
| PEP | Consumer Defensive | +0.429 | 0.00 | 1.00 | 0.00 | 0.00 | +0.63% | low | low |
| VZ | Communication Serv | +0.429 | 0.00 | 1.00 | 0.00 | 0.00 | +2.78% | low | low |

## Bottom 15 (lowest pressure)

| Ticker | Sector | pressure | SPEC | QUAL | resid | beta |
|--------|--------|----------|------|------|-------|------|
| INGN | Healthcare | -0.989 | 0.95 | 0.00 | +3.95% | high |
| ADCT | Healthcare | -0.989 | 0.95 | 0.00 | +7.58% | high |
| CRMT | Consumer Cyclical | -0.966 | 0.85 | 0.00 | -2.15% | high |
| VELO | Technology | -0.932 | 0.85 | 0.00 | -7.78% | high |
| LFMD | Healthcare | -0.932 | 0.85 | 0.00 | -2.97% | high |
| PAL | Industrials | -0.932 | 0.85 | 0.00 | -0.77% | high |
| CRBP | Healthcare | -0.932 | 0.85 | 0.00 | -1.98% | high |
| USGO | Basic Materials | -0.932 | 0.85 | 0.00 | -2.02% | high |
| ORGO | Healthcare | -0.932 | 0.85 | 0.00 | -4.58% | high |
| AIRO | Industrials | -0.932 | 0.85 | 0.00 | -2.06% | high |
| BYRN | Industrials | -0.932 | 0.85 | 0.00 | +0.73% | high |
| PDSB | Healthcare | -0.932 | 0.85 | 0.00 | +10.21% | high |
| LXEO | Healthcare | -0.932 | 0.85 | 0.00 | -5.81% | high |
| TNXP | Healthcare | -0.932 | 0.85 | 0.00 | -8.97% | high |
| HUCK | Technology | -0.932 | 0.85 | 0.00 | +0.71% | high |

## Sector median pressure

| Sector | n | median pressure | median resid |
|--------|---|-----------------|--------------|
| Utilities | 107 | +0.026 | +0.63% |
| Energy | 252 | -0.117 | +0.73% |
| Financial | 7237 | -0.237 | +0.05% |
| Consumer Defensive | 241 | -0.257 | +0.34% |
| Real Estate | 247 | -0.289 | +0.32% |
| Industrials | 717 | -0.315 | -0.51% |
| Basic Materials | 293 | -0.323 | -0.95% |
| Consumer Cyclical | 526 | -0.326 | -0.18% |
| Communication Services | 254 | -0.400 | -0.03% |
| Technology | 799 | -0.400 | -1.66% |
| Healthcare | 1053 | -0.529 | -1.27% |

## Composite averages by size

| size | n | SPEC | QUAL | pressure |
|------|---|------|------|----------|
| large | 771 | 0.17 | 0.80 | +0.157 |
| mega | 163 | 0.15 | 0.84 | +0.270 |
| micro | 2210 | 0.51 | 0.29 | -0.533 |
| mid | 1123 | 0.36 | 0.52 | -0.194 |
| small | 1633 | 0.49 | 0.40 | -0.414 |
| unknown | 5826 | 0.32 | 0.25 | -0.216 |
