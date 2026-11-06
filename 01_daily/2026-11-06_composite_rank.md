# Composite residual rank — **2026-11-06**

Generated: 2026-11-06T16:56:59.807457-05:00
Prior snapshot (for returns): **2026-11-05**

## Y snapshot (v1 — breadth only)

- **p_risk_on:** 0.5155 (from % names up)
- **pct_up:** 0.5562
- **median_ret:** 0.12%
- **conviction:** 0.0311
- **n:** 11758
- note: price_derived breadth only (v1)

## Method (deliberately simple)

- **residual** = stock return − median stock return (same pair window)
- **composites:** SPEC_DURATION, QUALITY_DEFENSIVE, CROWDING, SIZE_TILT
- **pressure** = conviction × prior effects of composites given p_risk_on
- Ranking is **cross-sectional residual bias**, not an absolute SPY call
- Hand priors only — replace with audit weights later

CSV: `data/composite/2026-11-06_composite_rank.csv`

## Top 20 by residual pressure (favor when risk-on / current Y)

| Ticker | Sector | pressure | SPEC | QUAL | CROWD | SIZE | resid | beta | short |
|--------|--------|----------|------|------|-------|------|-------|------|-------|
| SERV | Industrials | +0.008 | 0.95 | 0.00 | 0.80 | 1.00 | +38.68% | high | very_high |
| LODE | Basic Materials | +0.008 | 0.95 | 0.00 | 0.60 | 1.00 | +13.26% | high | elevated |
| STXS | Healthcare | +0.008 | 0.95 | 0.00 | 0.60 | 1.00 | +3.69% | high | elevated |
| AMTX | Basic Materials | +0.008 | 0.95 | 0.00 | 0.60 | 1.00 | -6.48% | high | elevated |
| FOA | Financial | +0.008 | 0.95 | 0.00 | 0.60 | 1.00 | -0.82% | high | elevated |
| NMRA | Healthcare | +0.008 | 0.95 | 0.00 | 0.60 | 1.00 | +1.92% | high | elevated |
| WETO | Technology | +0.008 | 0.85 | 0.00 | 0.80 | 1.00 | +20.12% | high | very_high |
| CSIQ | Technology | +0.008 | 0.95 | 0.00 | 0.80 | 0.80 | +7.74% | high | very_high |
| ARRY | Technology | +0.008 | 0.95 | 0.00 | 0.80 | 0.80 | +10.45% | high | very_high |
| OCGN | Healthcare | +0.008 | 0.95 | 0.00 | 0.80 | 0.80 | +13.30% | high | very_high |
| CHPT | Consumer Cyclical | +0.008 | 0.95 | 0.00 | 0.80 | 0.80 | +5.63% | high | very_high |
| JBLU | Industrials | +0.008 | 0.95 | 0.00 | 0.80 | 0.80 | +5.04% | high | very_high |
| FIP | Industrials | +0.008 | 0.95 | 0.00 | 0.80 | 0.80 | +17.91% | high | very_high |
| BMBL | Communication Serv | +0.008 | 0.95 | 0.00 | 0.80 | 0.80 | -0.28% | high | very_high |
| EVGO | Consumer Cyclical | +0.008 | 0.95 | 0.00 | 0.80 | 0.80 | +4.45% | high | very_high |
| ARTV | Healthcare | +0.008 | 0.85 | 0.00 | 0.60 | 1.00 | +0.37% | high | very_high |
| BLNK | Industrials | +0.008 | 0.85 | 0.00 | 0.60 | 1.00 | +24.27% | high | elevated |
| SLNH | Financial | +0.008 | 0.85 | 0.00 | 0.60 | 1.00 | +12.93% | high | very_high |
| TNXP | Healthcare | +0.008 | 0.85 | 0.00 | 0.60 | 1.00 | +2.93% | high | very_high |
| AIRS | Healthcare | +0.008 | 0.85 | 0.00 | 0.60 | 1.00 | -63.31% | high | very_high |

## Bottom 15 (lowest pressure)

| Ticker | Sector | pressure | SPEC | QUAL | resid | beta |
|--------|--------|----------|------|------|-------|------|
| ABBV | Healthcare | -0.004 | 0.00 | 1.00 | +0.95% | low |
| NVS | Healthcare | -0.004 | 0.00 | 1.00 | +0.27% | low |
| NVO | Healthcare | -0.004 | 0.00 | 1.00 | -0.09% | low |
| GSK | Healthcare | -0.004 | 0.00 | 1.00 | -0.28% | low |
| SO | Utilities | -0.004 | 0.00 | 1.00 | -1.19% | low |
| MO | Consumer Defensive | -0.004 | 0.00 | 1.00 | -2.00% | low |
| VZ | Communication Serv | -0.004 | 0.00 | 1.00 | -1.05% | low |
| NEM | Basic Materials | -0.004 | 0.00 | 1.00 | +0.89% | low |
| NEE | Utilities | -0.004 | 0.00 | 1.00 | -1.59% | low |
| TJX | Consumer Cyclical | -0.004 | 0.00 | 1.00 | -2.49% | low |
| IBM | Technology | -0.004 | 0.00 | 1.00 | -0.97% | low |
| SYK | Healthcare | -0.004 | 0.00 | 1.00 | -2.87% | low |
| LIN | Basic Materials | -0.004 | 0.00 | 1.00 | -1.26% | low |
| LOW | Consumer Cyclical | -0.004 | 0.00 | 1.00 | -1.30% | low |
| CME | Financial | -0.004 | 0.00 | 1.00 | -0.56% | low |

## Sector median pressure

| Sector | n | median pressure | median resid |
|--------|---|-----------------|--------------|
| Healthcare | 1054 | +0.004 | +1.70% |
| Technology | 802 | +0.003 | +1.46% |
| Communication Services | 252 | +0.003 | +0.48% |
| Basic Materials | 298 | +0.003 | +1.44% |
| Industrials | 712 | +0.003 | +0.51% |
| Consumer Cyclical | 522 | +0.003 | -0.92% |
| Consumer Defensive | 240 | +0.002 | -0.81% |
| Real Estate | 248 | +0.002 | -0.76% |
| Financial | 7271 | +0.002 | -0.03% |
| Energy | 252 | +0.001 | +0.86% |
| Utilities | 107 | -0.000 | -0.12% |

## Composite averages by size

| size | n | SPEC | QUAL | pressure |
|------|---|------|------|----------|
| large | 753 | 0.16 | 0.81 | -0.001 |
| mega | 160 | 0.14 | 0.84 | -0.002 |
| micro | 2272 | 0.52 | 0.28 | +0.004 |
| mid | 1111 | 0.35 | 0.52 | +0.002 |
| small | 1604 | 0.49 | 0.40 | +0.003 |
| unknown | 5858 | 0.32 | 0.24 | +0.002 |
