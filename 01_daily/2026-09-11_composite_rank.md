# Composite residual rank — **2026-09-11**

Generated: 2026-09-11T19:19:30.242383-04:00
Prior snapshot (for returns): **2026-09-10**

## Y snapshot (v1 — breadth only)

- **p_risk_on:** 0.72 (from % names up)
- **pct_up:** 0.638
- **median_ret:** 0.38%
- **conviction:** 0.4399
- **n:** 11632
- note: price_derived breadth only (v1)

## Method (deliberately simple)

- **residual** = stock return − median stock return (same pair window)
- **composites:** SPEC_DURATION, QUALITY_DEFENSIVE, CROWDING, SIZE_TILT
- **pressure** = conviction × prior effects of composites given p_risk_on
- Ranking is **cross-sectional residual bias**, not an absolute SPY call
- Hand priors only — replace with audit weights later

CSV: `data/composite/2026-09-11_composite_rank.csv`

## Top 20 by residual pressure (favor when risk-on / current Y)

| Ticker | Sector | pressure | SPEC | QUAL | CROWD | SIZE | resid | beta | short |
|--------|--------|----------|------|------|-------|------|-------|------|-------|
| VERI | Technology | +0.346 | 0.95 | 0.00 | 0.80 | 1.00 | +17.80% | high | very_high |
| MSS | Consumer Defensive | +0.327 | 0.85 | 0.00 | 0.80 | 1.00 | +6.13% | high | very_high |
| DH | Healthcare | +0.316 | 0.85 | 0.00 | 0.60 | 1.00 | +1.56% | high | elevated |
| GAME | Communication Serv | +0.316 | 0.85 | 0.00 | 0.60 | 1.00 | +5.67% | high | elevated |
| XHLD | Communication Serv | +0.316 | 0.85 | 0.00 | 0.60 | 1.00 | +15.21% | high | elevated |
| FGI | Consumer Cyclical | +0.316 | 0.85 | 0.00 | 0.60 | 1.00 | -2.15% | high | elevated |
| TJGC | Communication Serv | +0.316 | 0.85 | 0.00 | 0.60 | 1.00 | +4.49% | high | elevated |
| FLWS | Consumer Cyclical | +0.316 | 0.85 | 0.00 | 0.60 | 1.00 | -1.04% | high | very_high |
| KLC | Consumer Defensive | +0.316 | 0.85 | 0.00 | 0.60 | 1.00 | -5.96% | high | very_high |
| ACVA | Consumer Cyclical | +0.312 | 0.95 | 0.00 | 0.60 | 0.80 | +43.80% | high | elevated |
| NMRA | Healthcare | +0.304 | 0.85 | 0.00 | 0.40 | 1.00 | -9.15% | high | elevated |
| FHTX | Healthcare | +0.304 | 0.85 | 0.00 | 0.40 | 1.00 | -1.94% | high | elevated |
| CRBU | Healthcare | +0.304 | 0.85 | 0.00 | 0.40 | 1.00 | -7.68% | high | elevated |
| ACH | Healthcare | +0.304 | 0.85 | 0.00 | 0.40 | 1.00 | -0.38% | high | elevated |
| CRBP | Healthcare | +0.304 | 0.85 | 0.00 | 0.40 | 1.00 | -1.83% | high | elevated |
| ELTX | Healthcare | +0.304 | 0.85 | 0.00 | 0.40 | 1.00 | -3.22% | high | elevated |
| STRO | Healthcare | +0.304 | 0.85 | 0.00 | 0.40 | 1.00 | -5.82% | high | elevated |
| LODE | Basic Materials | +0.304 | 0.85 | 0.00 | 0.40 | 1.00 | -4.79% | high | elevated |
| CNTX | Healthcare | +0.304 | 0.85 | 0.00 | 0.40 | 1.00 | -5.78% | high | elevated |
| SLE | Communication Serv | +0.301 | 0.85 | 0.00 | 0.35 | 1.00 | +7.06% | high | unknown |

## Bottom 15 (lowest pressure)

| Ticker | Sector | pressure | SPEC | QUAL | resid | beta |
|--------|--------|----------|------|------|-------|------|
| ABBV | Healthcare | -0.145 | 0.00 | 1.00 | +0.45% | low |
| ABT | Healthcare | -0.145 | 0.00 | 1.00 | -1.74% | low |
| AMGN | Healthcare | -0.145 | 0.00 | 1.00 | -1.72% | low |
| WMT | Consumer Defensive | -0.145 | 0.00 | 1.00 | +0.96% | low |
| UNH | Healthcare | -0.145 | 0.00 | 1.00 | -2.75% | low |
| MDT | Healthcare | -0.145 | 0.00 | 1.00 | -1.10% | low |
| MFG | Financial | -0.145 | 0.00 | 1.00 | +3.15% | low |
| LLY | Healthcare | -0.145 | 0.00 | 1.00 | -1.03% | low |
| NVO | Healthcare | -0.145 | 0.00 | 1.00 | -2.51% | low |
| UL | Consumer Defensive | -0.145 | 0.00 | 1.00 | +0.25% | low |
| LMT | Industrials | -0.145 | 0.00 | 1.00 | -1.50% | low |
| NVS | Healthcare | -0.145 | 0.00 | 1.00 | -0.61% | low |
| LIN | Basic Materials | -0.145 | 0.00 | 1.00 | +0.62% | low |
| MCK | Healthcare | -0.145 | 0.00 | 1.00 | -0.30% | low |
| PDD | Consumer Cyclical | -0.145 | 0.00 | 1.00 | -0.42% | low |

## Sector median pressure

| Sector | n | median pressure | median resid |
|--------|---|-----------------|--------------|
| Healthcare | 1058 | +0.163 | -0.42% |
| Technology | 792 | +0.136 | +0.52% |
| Communication Services | 257 | +0.136 | +0.20% |
| Basic Materials | 291 | +0.112 | -0.38% |
| Consumer Cyclical | 528 | +0.103 | +0.28% |
| Industrials | 715 | +0.103 | +0.29% |
| Real Estate | 248 | +0.098 | -0.48% |
| Consumer Defensive | 242 | +0.085 | -0.38% |
| Financial | 7141 | +0.080 | +0.04% |
| Energy | 253 | +0.035 | -0.55% |
| Utilities | 107 | -0.011 | -0.83% |

## Composite averages by size

| size | n | SPEC | QUAL | pressure |
|------|---|------|------|----------|
| large | 773 | 0.17 | 0.80 | -0.055 |
| mega | 168 | 0.14 | 0.84 | -0.094 |
| micro | 2174 | 0.51 | 0.30 | +0.177 |
| mid | 1169 | 0.36 | 0.51 | +0.064 |
| small | 1620 | 0.48 | 0.41 | +0.137 |
| unknown | 5728 | 0.32 | 0.24 | +0.074 |
