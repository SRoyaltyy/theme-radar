# Composite residual rank — **2026-08-28**

Generated: 2026-08-28T23:12:06.225152-04:00
Prior snapshot (for returns): **2026-08-26**

## Y snapshot (v1 — breadth only)

- **p_risk_on:** 0.0009 (from % names up)
- **pct_up:** 0.3504
- **median_ret:** -0.30%
- **conviction:** 0.9981
- **n:** 11659
- note: price_derived breadth only (v1)

## Method (deliberately simple)

- **residual** = stock return − median stock return (same pair window)
- **composites:** SPEC_DURATION, QUALITY_DEFENSIVE, CROWDING, SIZE_TILT
- **pressure** = conviction × prior effects of composites given p_risk_on
- Ranking is **cross-sectional residual bias**, not an absolute SPY call
- Hand priors only — replace with audit weights later

CSV: `data/composite/2026-08-28_composite_rank.csv`

## Top 20 by residual pressure (favor when risk-on / current Y)

| Ticker | Sector | pressure | SPEC | QUAL | CROWD | SIZE | resid | beta | short |
|--------|--------|----------|------|------|-------|------|-------|------|-------|
| SNY | Healthcare | +0.747 | 0.00 | 1.00 | 0.00 | 0.00 | -1.02% | low | low |
| BABA | Consumer Cyclical | +0.747 | 0.00 | 1.00 | 0.00 | 0.00 | -0.47% | low | low |
| SHEL | Energy | +0.747 | 0.00 | 1.00 | 0.00 | 0.00 | +0.08% | low | low |
| ABT | Healthcare | +0.747 | 0.00 | 1.00 | 0.00 | 0.00 | -1.13% | low | low |
| HDB | Financial | +0.747 | 0.00 | 1.00 | 0.00 | 0.00 | -0.09% | low | low |
| TTE | Energy | +0.747 | 0.00 | 1.00 | 0.00 | 0.00 | -0.59% | low | low |
| SMFG | Financial | +0.747 | 0.00 | 1.00 | 0.00 | 0.00 | +2.27% | low | low |
| AZN | Healthcare | +0.747 | 0.00 | 1.00 | 0.00 | 0.00 | -1.84% | low | low |
| VLO | Energy | +0.747 | 0.00 | 1.00 | 0.00 | 0.00 | +1.55% | low | low |
| SYK | Healthcare | +0.747 | 0.00 | 1.00 | 0.00 | 0.00 | +0.61% | low | low |
| T | Communication Serv | +0.747 | 0.00 | 1.00 | 0.00 | 0.00 | +0.84% | low | low |
| RTX | Industrials | +0.747 | 0.00 | 1.00 | 0.00 | 0.00 | +0.17% | low | low |
| BMY | Healthcare | +0.747 | 0.00 | 1.00 | 0.00 | 0.00 | -1.16% | low | low |
| RY | Financial | +0.747 | 0.00 | 1.00 | 0.00 | 0.00 | -1.14% | low | low |
| VRTX | Healthcare | +0.747 | 0.00 | 1.00 | 0.00 | 0.00 | -0.72% | low | low |
| SAN | Financial | +0.747 | 0.00 | 1.00 | 0.00 | 0.00 | +0.10% | low | low |
| SCHW | Financial | +0.747 | 0.00 | 1.00 | 0.00 | 0.00 | +1.01% | low | low |
| RIO | Basic Materials | +0.747 | 0.00 | 1.00 | 0.00 | 0.00 | -1.03% | low | low |
| BRK-B | Financial | +0.747 | 0.00 | 1.00 | 0.00 | 0.00 | +0.32% | low | low |
| BRK-A | Financial | +0.747 | 0.00 | 1.00 | 0.00 | 0.00 | +0.44% | low | low |

## Bottom 15 (lowest pressure)

| Ticker | Sector | pressure | SPEC | QUAL | resid | beta |
|--------|--------|----------|------|------|-------|------|
| WCT | Technology | -1.684 | 0.85 | 0.00 | +27.05% | high |
| YYGH | Industrials | -1.684 | 0.85 | 0.00 | -26.58% | high |
| BTCT | Technology | -1.684 | 0.85 | 0.00 | +7.48% | high |
| INBX | Healthcare | -1.664 | 0.95 | 0.00 | -1.24% | high |
| ARCT | Healthcare | -1.664 | 0.95 | 0.00 | -3.74% | high |
| NAKA | Financial | -1.624 | 0.85 | 0.00 | +7.51% | high |
| JELD | Industrials | -1.624 | 0.85 | 0.00 | +4.85% | high |
| DAIC | Technology | -1.624 | 0.85 | 0.00 | -9.60% | high |
| CHAI | Communication Serv | -1.624 | 0.85 | 0.00 | +54.15% | high |
| NCPL | Financial | -1.624 | 0.85 | 0.00 | +38.30% | high |
| TJGC | Communication Serv | -1.624 | 0.85 | 0.00 | +57.70% | high |
| RCEL | Healthcare | -1.624 | 0.85 | 0.00 | -1.96% | high |
| XHLD | Communication Serv | -1.624 | 0.85 | 0.00 | +9.07% | high |
| AMPL | Technology | -1.604 | 0.95 | 0.00 | +10.64% | high |
| MEI | Technology | -1.604 | 0.95 | 0.00 | +7.04% | high |

## Sector median pressure

| Sector | n | median pressure | median resid |
|--------|---|-----------------|--------------|
| Utilities | 109 | +0.045 | -1.16% |
| Energy | 252 | -0.152 | +0.68% |
| Financial | 7157 | -0.413 | +0.12% |
| Consumer Defensive | 243 | -0.448 | -0.48% |
| Real Estate | 251 | -0.503 | -0.57% |
| Industrials | 711 | -0.503 | -1.13% |
| Consumer Cyclical | 533 | -0.533 | -0.64% |
| Basic Materials | 288 | -0.540 | -0.80% |
| Communication Services | 258 | -0.697 | -0.18% |
| Technology | 793 | -0.697 | -0.16% |
| Healthcare | 1064 | -0.832 | -1.88% |

## Composite averages by size

| size | n | SPEC | QUAL | pressure |
|------|---|------|------|----------|
| large | 786 | 0.16 | 0.80 | +0.290 |
| mega | 168 | 0.14 | 0.84 | +0.483 |
| micro | 2159 | 0.51 | 0.30 | -0.910 |
| mid | 1178 | 0.36 | 0.51 | -0.335 |
| small | 1629 | 0.48 | 0.41 | -0.706 |
| unknown | 5739 | 0.32 | 0.25 | -0.377 |
