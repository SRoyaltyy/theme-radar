# Composite residual rank — **2026-11-02**

Generated: 2026-11-02T17:31:27.387443-05:00
Prior snapshot (for returns): **2026-10-30**

## Y snapshot (v1 — breadth only)

- **p_risk_on:** 0.2271 (from % names up)
- **pct_up:** 0.4408
- **median_ret:** -0.05%
- **conviction:** 0.5458
- **n:** 11748
- note: price_derived breadth only (v1)

## Method (deliberately simple)

- **residual** = stock return − median stock return (same pair window)
- **composites:** SPEC_DURATION, QUALITY_DEFENSIVE, CROWDING, SIZE_TILT
- **pressure** = conviction × prior effects of composites given p_risk_on
- Ranking is **cross-sectional residual bias**, not an absolute SPY call
- Hand priors only — replace with audit weights later

CSV: `data/composite/2026-11-02_composite_rank.csv`

## Top 20 by residual pressure (favor when risk-on / current Y)

| Ticker | Sector | pressure | SPEC | QUAL | CROWD | SIZE | resid | beta | short |
|--------|--------|----------|------|------|-------|------|-------|------|-------|
| NVO | Healthcare | +0.223 | 0.00 | 1.00 | 0.00 | 0.00 | +1.18% | low | low |
| ABT | Healthcare | +0.223 | 0.00 | 1.00 | 0.00 | 0.00 | +3.78% | low | low |
| NVS | Healthcare | +0.223 | 0.00 | 1.00 | 0.00 | 0.00 | +0.50% | low | low |
| SMFG | Financial | +0.223 | 0.00 | 1.00 | 0.00 | 0.00 | -0.73% | low | low |
| RY | Financial | +0.223 | 0.00 | 1.00 | 0.00 | 0.00 | +0.83% | low | low |
| HDB | Financial | +0.223 | 0.00 | 1.00 | 0.00 | 0.00 | +2.40% | low | low |
| TD | Financial | +0.223 | 0.00 | 1.00 | 0.00 | 0.00 | +0.48% | low | low |
| SYK | Healthcare | +0.223 | 0.00 | 1.00 | 0.00 | 0.00 | +5.17% | low | low |
| T | Communication Serv | +0.223 | 0.00 | 1.00 | 0.00 | 0.00 | +0.19% | low | low |
| JNJ | Healthcare | +0.223 | 0.00 | 1.00 | 0.00 | 0.00 | -0.92% | low | low |
| RTX | Industrials | +0.223 | 0.00 | 1.00 | 0.00 | 0.00 | +1.55% | low | low |
| MRK | Healthcare | +0.223 | 0.00 | 1.00 | 0.00 | 0.00 | -0.72% | low | low |
| UNH | Healthcare | +0.223 | 0.00 | 1.00 | 0.00 | 0.00 | -1.55% | low | low |
| ADP | Technology | +0.223 | 0.00 | 1.00 | 0.00 | 0.00 | +1.73% | low | low |
| UL | Consumer Defensive | +0.223 | 0.00 | 1.00 | 0.00 | 0.00 | +1.86% | low | low |
| MUFG | Financial | +0.223 | 0.00 | 1.00 | 0.00 | 0.00 | -0.46% | low | low |
| SCHW | Financial | +0.223 | 0.00 | 1.00 | 0.00 | 0.00 | +0.80% | low | low |
| PEP | Consumer Defensive | +0.223 | 0.00 | 1.00 | 0.00 | 0.00 | +2.29% | low | low |
| DHR | Healthcare | +0.223 | 0.00 | 1.00 | 0.00 | 0.00 | -1.78% | low | low |
| PG | Consumer Defensive | +0.223 | 0.00 | 1.00 | 0.00 | 0.00 | +1.28% | low | low |

## Bottom 15 (lowest pressure)

| Ticker | Sector | pressure | SPEC | QUAL | resid | beta |
|--------|--------|----------|------|------|-------|------|
| KRRO | Healthcare | -0.533 | 0.95 | 0.00 | +10.81% | high |
| PLAY | Communication Serv | -0.533 | 0.95 | 0.00 | +8.74% | high |
| AIRS | Healthcare | -0.533 | 0.95 | 0.00 | -3.42% | high |
| UPB | Healthcare | -0.515 | 0.95 | 0.00 | -1.71% | high |
| DMRC | Technology | -0.515 | 0.95 | 0.00 | -0.86% | high |
| NMRA | Healthcare | -0.515 | 0.95 | 0.00 | +35.19% | high |
| USGO | Basic Materials | -0.515 | 0.95 | 0.00 | +9.44% | high |
| VCIG | Industrials | -0.503 | 0.85 | 0.00 | +4700.05% | high |
| INO | Healthcare | -0.503 | 0.85 | 0.00 | +215.05% | high |
| EVGO | Consumer Cyclical | -0.497 | 0.95 | 0.00 | +46.88% | high |
| JBLU | Industrials | -0.497 | 0.95 | 0.00 | +11.28% | high |
| ULCC | Industrials | -0.497 | 0.95 | 0.00 | +15.24% | high |
| TE | Industrials | -0.497 | 0.95 | 0.00 | -5.13% | high |
| TDOC | Healthcare | -0.497 | 0.95 | 0.00 | +1.46% | high |
| BETR | Financial | -0.497 | 0.95 | 0.00 | +0.87% | high |

## Sector median pressure

| Sector | n | median pressure | median resid |
|--------|---|-----------------|--------------|
| Utilities | 107 | -0.009 | +0.83% |
| Energy | 252 | -0.061 | -4.58% |
| Financial | 7262 | -0.124 | -0.01% |
| Consumer Defensive | 240 | -0.142 | +1.04% |
| Real Estate | 248 | -0.150 | +1.19% |
| Industrials | 712 | -0.173 | +0.64% |
| Consumer Cyclical | 522 | -0.176 | +2.07% |
| Basic Materials | 297 | -0.188 | +0.43% |
| Communication Services | 252 | -0.208 | +0.48% |
| Technology | 802 | -0.208 | -1.13% |
| Healthcare | 1054 | -0.279 | -1.43% |

## Composite averages by size

| size | n | SPEC | QUAL | pressure |
|------|---|------|------|----------|
| large | 757 | 0.17 | 0.79 | +0.077 |
| mega | 163 | 0.15 | 0.83 | +0.138 |
| micro | 2270 | 0.52 | 0.28 | -0.283 |
| mid | 1121 | 0.36 | 0.51 | -0.104 |
| small | 1588 | 0.49 | 0.40 | -0.218 |
| unknown | 5849 | 0.32 | 0.24 | -0.114 |
