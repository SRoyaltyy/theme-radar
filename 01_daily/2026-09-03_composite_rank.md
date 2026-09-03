# Composite residual rank — **2026-09-03**

Generated: 2026-09-03T19:19:52.081722-04:00
Prior snapshot (for returns): **2026-09-02**

## Y snapshot (v1 — breadth only)

- **p_risk_on:** 0.828 (from % names up)
- **pct_up:** 0.6812
- **median_ret:** 0.43%
- **conviction:** 0.6559
- **n:** 11643
- note: price_derived breadth only (v1)

## Method (deliberately simple)

- **residual** = stock return − median stock return (same pair window)
- **composites:** SPEC_DURATION, QUALITY_DEFENSIVE, CROWDING, SIZE_TILT
- **pressure** = conviction × prior effects of composites given p_risk_on
- Ranking is **cross-sectional residual bias**, not an absolute SPY call
- Hand priors only — replace with audit weights later

CSV: `data/composite/2026-09-03_composite_rank.csv`

## Top 20 by residual pressure (favor when risk-on / current Y)

| Ticker | Sector | pressure | SPEC | QUAL | CROWD | SIZE | resid | beta | short |
|--------|--------|----------|------|------|-------|------|-------|------|-------|
| CHPT | Consumer Cyclical | +0.770 | 0.95 | 0.00 | 0.80 | 1.00 | +74.52% | high | very_high |
| GPRO | Technology | +0.770 | 0.95 | 0.00 | 0.80 | 1.00 | -18.18% | high | very_high |
| WCT | Technology | +0.727 | 0.85 | 0.00 | 0.80 | 1.00 | +13.74% | high | very_high |
| AQST | Healthcare | +0.719 | 0.95 | 0.00 | 0.80 | 0.80 | -0.99% | high | very_high |
| ARCT | Healthcare | +0.719 | 0.95 | 0.00 | 0.80 | 0.80 | -7.48% | high | very_high |
| NVAX | Healthcare | +0.719 | 0.95 | 0.00 | 0.80 | 0.80 | -0.23% | high | very_high |
| SST | Industrials | +0.701 | 0.85 | 0.00 | 0.60 | 1.00 | +24.49% | high | elevated |
| CHGG | Consumer Defensive | +0.701 | 0.85 | 0.00 | 0.60 | 1.00 | +17.64% | high | elevated |
| NAKA | Financial | +0.701 | 0.85 | 0.00 | 0.60 | 1.00 | +7.77% | high | elevated |
| COSM | Healthcare | +0.701 | 0.85 | 0.00 | 0.60 | 1.00 | +22.30% | high | elevated |
| RCEL | Healthcare | +0.701 | 0.85 | 0.00 | 0.60 | 1.00 | +1.24% | high | elevated |
| ADIL | Healthcare | +0.701 | 0.85 | 0.00 | 0.60 | 1.00 | +4.95% | high | elevated |
| ATOM | Technology | +0.701 | 0.85 | 0.00 | 0.60 | 1.00 | -1.93% | high | very_high |
| TJGC | Communication Serv | +0.701 | 0.85 | 0.00 | 0.60 | 1.00 | -2.22% | high | elevated |
| SSM | Consumer Cyclical | +0.701 | 0.85 | 0.00 | 0.60 | 1.00 | -27.51% | high | elevated |
| DH | Healthcare | +0.701 | 0.85 | 0.00 | 0.60 | 1.00 | -0.43% | high | elevated |
| DPRO | Technology | +0.701 | 0.85 | 0.00 | 0.60 | 1.00 | +12.58% | high | elevated |
| XHLD | Communication Serv | +0.701 | 0.85 | 0.00 | 0.60 | 1.00 | -0.54% | high | elevated |
| EOLS | Healthcare | +0.693 | 0.95 | 0.00 | 0.60 | 0.80 | -0.54% | high | elevated |
| JANX | Healthcare | +0.693 | 0.95 | 0.00 | 0.60 | 0.80 | +0.08% | high | elevated |

## Bottom 15 (lowest pressure)

| Ticker | Sector | pressure | SPEC | QUAL | resid | beta |
|--------|--------|----------|------|------|-------|------|
| NEM | Basic Materials | -0.323 | 0.00 | 1.00 | +3.78% | low |
| NEE | Utilities | -0.323 | 0.00 | 1.00 | +0.73% | low |
| ABT | Healthcare | -0.323 | 0.00 | 1.00 | -1.95% | low |
| ABBV | Healthcare | -0.323 | 0.00 | 1.00 | -1.01% | low |
| TD | Financial | -0.323 | 0.00 | 1.00 | +1.09% | low |
| MUFG | Financial | -0.323 | 0.00 | 1.00 | +2.60% | low |
| RTX | Industrials | -0.323 | 0.00 | 1.00 | +0.24% | low |
| AZN | Healthcare | -0.323 | 0.00 | 1.00 | +1.51% | low |
| LMT | Industrials | -0.323 | 0.00 | 1.00 | -0.17% | low |
| LIN | Basic Materials | -0.323 | 0.00 | 1.00 | -1.51% | low |
| LLY | Healthcare | -0.323 | 0.00 | 1.00 | -0.47% | low |
| WMT | Consumer Defensive | -0.323 | 0.00 | 1.00 | +1.77% | low |
| BABA | Consumer Cyclical | -0.323 | 0.00 | 1.00 | -0.43% | low |
| SNY | Healthcare | -0.323 | 0.00 | 1.00 | -0.74% | low |
| TM | Consumer Cyclical | -0.323 | 0.00 | 1.00 | +0.36% | low |

## Sector median pressure

| Sector | n | median pressure | median resid |
|--------|---|-----------------|--------------|
| Healthcare | 1063 | +0.359 | -0.80% |
| Technology | 794 | +0.301 | +0.53% |
| Communication Services | 256 | +0.301 | -0.43% |
| Basic Materials | 288 | +0.239 | -0.38% |
| Consumer Cyclical | 532 | +0.228 | -0.30% |
| Industrials | 712 | +0.228 | +0.35% |
| Real Estate | 250 | +0.217 | -0.28% |
| Consumer Defensive | 242 | +0.194 | -0.79% |
| Financial | 7145 | +0.179 | +0.09% |
| Energy | 252 | +0.077 | -0.70% |
| Utilities | 109 | -0.019 | +0.33% |

## Composite averages by size

| size | n | SPEC | QUAL | pressure |
|------|---|------|------|----------|
| large | 781 | 0.17 | 0.80 | -0.124 |
| mega | 173 | 0.14 | 0.84 | -0.209 |
| micro | 2170 | 0.51 | 0.30 | +0.393 |
| mid | 1178 | 0.36 | 0.51 | +0.145 |
| small | 1616 | 0.49 | 0.41 | +0.305 |
| unknown | 5725 | 0.32 | 0.25 | +0.164 |
