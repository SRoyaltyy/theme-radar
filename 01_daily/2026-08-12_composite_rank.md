# Composite residual rank — **2026-08-12**

Generated: 2026-08-12T18:06:29.762187-04:00
Prior snapshot (for returns): **2026-08-11**

## Y snapshot (v1 — breadth only)

- **p_risk_on:** 0.6607 (from % names up)
- **pct_up:** 0.6143
- **median_ret:** 0.15%
- **conviction:** 0.3214
- **n:** 11568
- note: price_derived breadth only (v1)

## Method (deliberately simple)

- **residual** = stock return − median stock return (same pair window)
- **composites:** SPEC_DURATION, QUALITY_DEFENSIVE, CROWDING, SIZE_TILT
- **pressure** = conviction × prior effects of composites given p_risk_on
- Ranking is **cross-sectional residual bias**, not an absolute SPY call
- Hand priors only — replace with audit weights later

CSV: `data/composite/2026-08-12_composite_rank.csv`

## Top 20 by residual pressure (favor when risk-on / current Y)

| Ticker | Sector | pressure | SPEC | QUAL | CROWD | SIZE | resid | beta | short |
|--------|--------|----------|------|------|-------|------|-------|------|-------|
| VERI | Technology | +0.185 | 0.95 | 0.00 | 0.80 | 1.00 | +1.87% | high | very_high |
| ARCT | Healthcare | +0.185 | 0.95 | 0.00 | 0.80 | 1.00 | +0.92% | high | very_high |
| ZENA | Technology | +0.179 | 0.95 | 0.00 | 0.60 | 1.00 | +4.25% | high | elevated |
| JSPR | Healthcare | +0.175 | 0.85 | 0.00 | 0.80 | 1.00 | -8.01% | high | very_high |
| PROP | Energy | +0.175 | 0.85 | 0.00 | 0.80 | 1.00 | -1.27% | high | very_high |
| BKSY | Industrials | +0.172 | 0.95 | 0.00 | 0.80 | 0.80 | +6.48% | high | very_high |
| WOLF | Technology | +0.172 | 0.95 | 0.00 | 0.80 | 0.80 | +5.06% | high | very_high |
| HTZ | Industrials | +0.172 | 0.95 | 0.00 | 0.80 | 0.80 | +14.14% | high | very_high |
| SDGR | Healthcare | +0.172 | 0.95 | 0.00 | 0.80 | 0.80 | -0.25% | high | very_high |
| FIP | Industrials | +0.172 | 0.95 | 0.00 | 0.80 | 0.80 | +3.06% | high | very_high |
| TNDM | Healthcare | +0.172 | 0.95 | 0.00 | 0.80 | 0.80 | -0.15% | high | very_high |
| SGMT | Healthcare | +0.172 | 0.95 | 0.00 | 0.80 | 0.80 | -1.51% | high | very_high |
| BBNX | Healthcare | +0.172 | 0.95 | 0.00 | 0.80 | 0.80 | -1.79% | high | very_high |
| SATL | Industrials | +0.172 | 0.95 | 0.00 | 0.80 | 0.80 | +3.85% | high | very_high |
| SMRT | Technology | +0.171 | 0.95 | 0.00 | 0.35 | 1.00 | +2.69% | high | low |
| EU | Energy | +0.171 | 0.95 | 0.00 | 0.35 | 1.00 | -0.15% | high | unknown |
| WXM | Industrials | +0.168 | 0.85 | 0.00 | 0.60 | 1.00 | -39.89% | high | elevated |
| AIRS | Healthcare | +0.168 | 0.85 | 0.00 | 0.60 | 1.00 | +1.10% | high | very_high |
| JELD | Industrials | +0.168 | 0.85 | 0.00 | 0.60 | 1.00 | -0.15% | high | elevated |
| AIFA | Technology | +0.168 | 0.85 | 0.00 | 0.60 | 1.00 | -13.04% | high | elevated |

## Bottom 15 (lowest pressure)

| Ticker | Sector | pressure | SPEC | QUAL | resid | beta |
|--------|--------|----------|------|------|-------|------|
| SYK | Healthcare | -0.077 | 0.00 | 1.00 | -0.42% | low |
| BRK-A | Financial | -0.077 | 0.00 | 1.00 | -1.57% | low |
| BRK-B | Financial | -0.077 | 0.00 | 1.00 | -1.38% | low |
| NVO | Healthcare | -0.077 | 0.00 | 1.00 | -1.80% | low |
| NVS | Healthcare | -0.077 | 0.00 | 1.00 | -1.63% | low |
| TTE | Energy | -0.077 | 0.00 | 1.00 | -0.43% | low |
| RIO | Basic Materials | -0.077 | 0.00 | 1.00 | +0.08% | low |
| VRTX | Healthcare | -0.077 | 0.00 | 1.00 | -0.89% | low |
| GD | Industrials | -0.077 | 0.00 | 1.00 | +0.45% | low |
| DHR | Healthcare | -0.077 | 0.00 | 1.00 | -0.94% | low |
| VZ | Communication Serv | -0.077 | 0.00 | 1.00 | -0.76% | low |
| NEE | Utilities | -0.077 | 0.00 | 1.00 | -0.10% | low |
| RY | Financial | -0.077 | 0.00 | 1.00 | +1.39% | low |
| BTI | Consumer Defensive | -0.077 | 0.00 | 1.00 | -1.85% | low |
| SAN | Financial | -0.077 | 0.00 | 1.00 | +0.60% | low |

## Sector median pressure

| Sector | n | median pressure | median resid |
|--------|---|-----------------|--------------|
| Healthcare | 1064 | +0.090 | -0.11% |
| Technology | 790 | +0.072 | -0.03% |
| Communication Services | 259 | +0.072 | -0.22% |
| Basic Materials | 288 | +0.061 | -0.43% |
| Consumer Cyclical | 533 | +0.058 | -0.68% |
| Industrials | 708 | +0.055 | -0.15% |
| Real Estate | 253 | +0.052 | +0.34% |
| Consumer Defensive | 244 | +0.050 | -0.15% |
| Financial | 7067 | +0.043 | +0.02% |
| Energy | 253 | +0.016 | -0.15% |
| Utilities | 109 | -0.005 | +0.12% |

## Composite averages by size

| size | n | SPEC | QUAL | pressure |
|------|---|------|------|----------|
| large | 802 | 0.18 | 0.79 | -0.027 |
| mega | 168 | 0.15 | 0.83 | -0.047 |
| micro | 2144 | 0.51 | 0.30 | +0.095 |
| mid | 1173 | 0.37 | 0.51 | +0.037 |
| small | 1616 | 0.49 | 0.40 | +0.075 |
| unknown | 5665 | 0.32 | 0.25 | +0.040 |
