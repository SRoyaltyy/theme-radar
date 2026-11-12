# Composite residual rank — **2026-11-12**

Generated: 2026-11-12T17:29:41.756382-05:00
Prior snapshot (for returns): **2026-11-11**

## Y snapshot (v1 — breadth only)

- **p_risk_on:** 0.0 (from % names up)
- **pct_up:** 0.175
- **median_ret:** -0.71%
- **conviction:** 1.0
- **n:** 11756
- note: price_derived breadth only (v1)

## Method (deliberately simple)

- **residual** = stock return − median stock return (same pair window)
- **composites:** SPEC_DURATION, QUALITY_DEFENSIVE, CROWDING, SIZE_TILT
- **pressure** = conviction × prior effects of composites given p_risk_on
- Ranking is **cross-sectional residual bias**, not an absolute SPY call
- Hand priors only — replace with audit weights later

CSV: `data/composite/2026-11-12_composite_rank.csv`

## Top 20 by residual pressure (favor when risk-on / current Y)

| Ticker | Sector | pressure | SPEC | QUAL | CROWD | SIZE | resid | beta | short |
|--------|--------|----------|------|------|-------|------|-------|------|-------|
| ABT | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -1.16% | low | low |
| ABBV | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.53% | low | low |
| TM | Consumer Cyclical | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.85% | low | low |
| BUD | Consumer Defensive | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.44% | low | low |
| LLY | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.01% | low | low |
| PM | Consumer Defensive | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.87% | low | low |
| KO | Consumer Defensive | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.58% | low | low |
| TTE | Energy | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +2.52% | low | low |
| TJX | Consumer Cyclical | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.37% | low | low |
| LIN | Basic Materials | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.06% | low | low |
| LMT | Industrials | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.27% | low | low |
| RIO | Basic Materials | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -1.28% | low | low |
| GSK | Healthcare | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.79% | low | low |
| TD | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.32% | low | low |
| MA | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -0.52% | low | low |
| BP | Energy | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.95% | low | low |
| ADP | Technology | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +1.22% | low | low |
| MFG | Financial | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.32% | low | low |
| PG | Consumer Defensive | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | +0.93% | low | low |
| PDD | Consumer Cyclical | +0.750 | 0.00 | 1.00 | 0.00 | 0.00 | -1.16% | low | low |

## Bottom 15 (lowest pressure)

| Ticker | Sector | pressure | SPEC | QUAL | resid | beta |
|--------|--------|----------|------|------|-------|------|
| SERV | Industrials | -1.790 | 0.95 | 0.00 | -7.52% | high |
| EVMN | Healthcare | -1.790 | 0.95 | 0.00 | -6.25% | high |
| WATT | Technology | -1.790 | 0.95 | 0.00 | -2.07% | high |
| ARMP | Healthcare | -1.730 | 0.95 | 0.00 | -3.66% | high |
| KULR | Technology | -1.690 | 0.85 | 0.00 | -10.02% | high |
| NCPL | Financial | -1.690 | 0.85 | 0.00 | -5.20% | high |
| PLCE | Consumer Cyclical | -1.690 | 0.85 | 0.00 | +120.71% | high |
| ARQQ | Technology | -1.690 | 0.85 | 0.00 | -3.97% | high |
| INLF | Industrials | -1.690 | 0.85 | 0.00 | -40.72% | high |
| MRLN | Industrials | -1.690 | 0.85 | 0.00 | -4.24% | high |
| OPTT | Industrials | -1.690 | 0.85 | 0.00 | +20.01% | high |
| WRAP | Technology | -1.690 | 0.85 | 0.00 | -1.65% | high |
| GCTS | Technology | -1.690 | 0.85 | 0.00 | -2.43% | high |
| ANRO | Healthcare | -1.670 | 0.95 | 0.00 | -0.99% | high |
| VOYG | Industrials | -1.670 | 0.95 | 0.00 | -5.34% | high |

## Sector median pressure

| Sector | n | median pressure | median resid |
|--------|---|-----------------|--------------|
| Utilities | 104 | +0.053 | +0.25% |
| Energy | 252 | -0.198 | +1.25% |
| Financial | 7272 | -0.415 | +0.16% |
| Consumer Defensive | 240 | -0.458 | -0.43% |
| Real Estate | 247 | -0.530 | -0.43% |
| Consumer Cyclical | 521 | -0.565 | -1.22% |
| Basic Materials | 298 | -0.605 | -1.65% |
| Industrials | 716 | -0.627 | -0.52% |
| Communication Services | 252 | -0.702 | -1.08% |
| Technology | 800 | -0.735 | -0.80% |
| Healthcare | 1054 | -0.935 | -2.22% |

## Composite averages by size

| size | n | SPEC | QUAL | pressure |
|------|---|------|------|----------|
| large | 751 | 0.17 | 0.81 | +0.284 |
| mega | 168 | 0.14 | 0.84 | +0.474 |
| micro | 2269 | 0.53 | 0.28 | -0.954 |
| mid | 1114 | 0.36 | 0.52 | -0.340 |
| small | 1595 | 0.49 | 0.40 | -0.732 |
| unknown | 5859 | 0.32 | 0.25 | -0.383 |
