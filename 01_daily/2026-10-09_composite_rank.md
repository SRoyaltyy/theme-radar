# Composite residual rank — **2026-10-09**

Generated: 2026-10-09T16:57:51.118164-04:00
Prior snapshot (for returns): **2026-10-08**

## Y snapshot (v1 — breadth only)

- **p_risk_on:** 0.7111 (from % names up)
- **pct_up:** 0.6344
- **median_ret:** 0.33%
- **conviction:** 0.4221
- **n:** 11724
- note: price_derived breadth only (v1)

## Method (deliberately simple)

- **residual** = stock return − median stock return (same pair window)
- **composites:** SPEC_DURATION, QUALITY_DEFENSIVE, CROWDING, SIZE_TILT
- **pressure** = conviction × prior effects of composites given p_risk_on
- Ranking is **cross-sectional residual bias**, not an absolute SPY call
- Hand priors only — replace with audit weights later

CSV: `data/composite/2026-10-09_composite_rank.csv`

## Top 20 by residual pressure (favor when risk-on / current Y)

| Ticker | Sector | pressure | SPEC | QUAL | CROWD | SIZE | resid | beta | short |
|--------|--------|----------|------|------|-------|------|-------|------|-------|
| ANGI | Communication Serv | +0.308 | 0.95 | 0.00 | 0.60 | 1.00 | +4.61% | high | elevated |
| ADCT | Healthcare | +0.308 | 0.95 | 0.00 | 0.60 | 1.00 | +8.48% | high | elevated |
| CRMT | Consumer Cyclical | +0.301 | 0.85 | 0.00 | 0.80 | 1.00 | +7.67% | high | very_high |
| PRME | Healthcare | +0.298 | 0.95 | 0.00 | 0.80 | 0.80 | +11.13% | high | very_high |
| PDSB | Healthcare | +0.290 | 0.85 | 0.00 | 0.60 | 1.00 | +34.97% | high | elevated |
| TNXP | Healthcare | +0.290 | 0.85 | 0.00 | 0.60 | 1.00 | -0.05% | high | very_high |
| HUCK | Technology | +0.290 | 0.85 | 0.00 | 0.60 | 1.00 | +0.97% | high | very_high |
| VERI | Technology | +0.290 | 0.85 | 0.00 | 0.60 | 1.00 | -7.11% | high | very_high |
| LDI | Financial | +0.290 | 0.85 | 0.00 | 0.60 | 1.00 | -10.00% | high | very_high |
| VELO | Technology | +0.290 | 0.85 | 0.00 | 0.60 | 1.00 | -3.78% | high | very_high |
| QTEX | Technology | +0.290 | 0.85 | 0.00 | 0.60 | 1.00 | +10.33% | high | elevated |
| BYRN | Industrials | +0.290 | 0.85 | 0.00 | 0.60 | 1.00 | -4.77% | high | elevated |
| NXH | Consumer Cyclical | +0.290 | 0.85 | 0.00 | 0.60 | 1.00 | -2.07% | high | very_high |
| CRBP | Healthcare | +0.290 | 0.85 | 0.00 | 0.60 | 1.00 | +1.76% | high | very_high |
| CNSY | Healthcare | +0.290 | 0.85 | 0.00 | 0.60 | 1.00 | +7.50% | high | elevated |
| AMPL | Technology | +0.287 | 0.95 | 0.00 | 0.60 | 0.80 | +2.16% | high | elevated |
| ACVA | Consumer Cyclical | +0.287 | 0.95 | 0.00 | 0.60 | 0.80 | -0.33% | high | elevated |
| CD | Financial | +0.287 | 0.95 | 0.00 | 0.60 | 0.80 | -20.95% | high | elevated |
| TARA | Healthcare | +0.280 | 0.85 | 0.00 | 0.40 | 1.00 | +3.83% | high | elevated |
| LODE | Basic Materials | +0.280 | 0.85 | 0.00 | 0.40 | 1.00 | -0.33% | high | elevated |

## Bottom 15 (lowest pressure)

| Ticker | Sector | pressure | SPEC | QUAL | resid | beta |
|--------|--------|----------|------|------|-------|------|
| SAN | Financial | -0.134 | 0.00 | 1.00 | -0.25% | low |
| CVS | Healthcare | -0.134 | 0.00 | 1.00 | -2.19% | low |
| RTX | Industrials | -0.134 | 0.00 | 1.00 | +0.57% | low |
| RY | Financial | -0.134 | 0.00 | 1.00 | +0.38% | low |
| MCK | Healthcare | -0.134 | 0.00 | 1.00 | +0.60% | low |
| NVO | Healthcare | -0.134 | 0.00 | 1.00 | +0.88% | low |
| JNJ | Healthcare | -0.134 | 0.00 | 1.00 | +1.61% | low |
| AMGN | Healthcare | -0.134 | 0.00 | 1.00 | +1.50% | low |
| NVS | Healthcare | -0.134 | 0.00 | 1.00 | +0.12% | low |
| SMFG | Financial | -0.134 | 0.00 | 1.00 | -1.04% | low |
| WMT | Consumer Defensive | -0.134 | 0.00 | 1.00 | +0.39% | low |
| DHR | Healthcare | -0.134 | 0.00 | 1.00 | +0.76% | low |
| TJX | Consumer Cyclical | -0.134 | 0.00 | 1.00 | -0.32% | low |
| UNH | Healthcare | -0.134 | 0.00 | 1.00 | +1.93% | low |
| KO | Consumer Defensive | -0.134 | 0.00 | 1.00 | -0.01% | low |

## Sector median pressure

| Sector | n | median pressure | median resid |
|--------|---|-----------------|--------------|
| Healthcare | 1055 | +0.160 | +0.76% |
| Technology | 798 | +0.125 | +0.09% |
| Communication Services | 256 | +0.125 | -0.91% |
| Consumer Cyclical | 528 | +0.101 | -0.33% |
| Basic Materials | 294 | +0.100 | +0.26% |
| Industrials | 717 | +0.098 | -0.38% |
| Real Estate | 247 | +0.090 | -0.35% |
| Consumer Defensive | 241 | +0.080 | -0.33% |
| Financial | 7230 | +0.074 | +0.03% |
| Energy | 251 | +0.036 | -0.45% |
| Utilities | 107 | -0.008 | +0.02% |

## Composite averages by size

| size | n | SPEC | QUAL | pressure |
|------|---|------|------|----------|
| large | 775 | 0.17 | 0.79 | -0.049 |
| mega | 163 | 0.15 | 0.84 | -0.085 |
| micro | 2207 | 0.51 | 0.29 | +0.165 |
| mid | 1125 | 0.36 | 0.52 | +0.060 |
| small | 1638 | 0.49 | 0.40 | +0.129 |
| unknown | 5816 | 0.32 | 0.25 | +0.067 |
