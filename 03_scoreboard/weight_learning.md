# Weight learning — decision log

_Generated 2026-08-20 17:20 EDT_

- label dates per horizon: 1d: 10, 2d: 9, 3d: 8
- primary horizon for promotion test: **1d** (10 dates)
- existing overrides: {'Price|ret': 0.25, 'Performance (Month)|delta': 1.1730692087704369, 'Average Volume|delta': 0.7556364829130159, 'Relative Strength Index (14)|delta': 0.25, 'Short Float|delta': 1.621154365347823, 'Institutional Transactions|level': 1.560880518981233, 'Institutional Ownership|delta': 1.7346824962840992, 'Insider Transactions|level': 0.8045609400185698, 'Target Price|delta': 1.0585700596168497, 'Analyst Recom|delta': 1.391605758962418, 'Sales Growth Quarter Over Quarter|level': 2.0, 'Sales Year Over Year TTM|level': 2.0, 'Profit Margin|delta': 0.91695333854222, 'EPS Surprise|level': 0.9580763760850557, 'n_catalysts|level': 1.9293910807536472}

## Per-rule aligned IC (direction corrected for polarity)

| Rule | Horizon | Mean aligned IC | Dates | Proposed × | Testable |
|---|---|---|---|---|---|
| Price|ret | 1d | -0.0481 | 9 | 0.250 | yes |
| Price|ret | 2d | -0.0624 | 8 | 0.250 | yes |
| Price|ret | 3d | -0.0506 | 7 | 0.250 | yes |
| Performance (Month)|delta | 1d | +0.0124 | 9 | 1.202 | yes |
| Performance (Month)|delta | 2d | -0.0534 | 8 | 1.048 | yes |
| Performance (Month)|delta | 3d | -0.0852 | 7 | 0.973 | yes |
| Average Volume|delta | 1d | -0.0081 | 9 | 0.743 | NO — logs only |
| Average Volume|delta | 2d | -0.0117 | 8 | 0.738 | NO — logs only |
| Average Volume|delta | 3d | -0.0071 | 7 | 0.745 | NO — logs only |
| Relative Strength Index (14)|delta | 1d | -0.0413 | 9 | 0.250 | yes |
| Relative Strength Index (14)|delta | 2d | -0.0618 | 8 | 0.250 | yes |
| Relative Strength Index (14)|delta | 3d | -0.0445 | 7 | 0.250 | yes |
| Short Float|delta | 1d | +0.0016 | 8 | 1.626 | NO — logs only |
| Short Float|delta | 2d | -0.0058 | 7 | 1.602 | NO — logs only |
| Short Float|delta | 3d | -0.0131 | 6 | 1.579 | NO — logs only |
| Institutional Transactions|level | 1d | +0.0033 | 10 | 1.571 | NO — logs only |
| Institutional Transactions|level | 2d | +0.0127 | 9 | 1.600 | NO — logs only |
| Institutional Transactions|level | 3d | +0.0221 | 8 | 1.630 | NO — logs only |
| Institutional Ownership|delta | 1d | +0.0082 | 9 | 1.763 | NO — logs only |
| Institutional Ownership|delta | 2d | +0.0120 | 8 | 1.776 | NO — logs only |
| Institutional Ownership|delta | 3d | +0.0094 | 7 | 1.767 | NO — logs only |
| Insider Transactions|level | 1d | +0.0047 | 10 | 0.812 | NO — logs only |
| Insider Transactions|level | 2d | +0.0043 | 9 | 0.812 | NO — logs only |
| Insider Transactions|level | 3d | -0.0010 | 8 | 0.803 | NO — logs only |
| Target Price|delta | 1d | +0.0072 | 9 | 1.074 | NO — logs only |
| Target Price|delta | 2d | +0.0039 | 8 | 1.067 | NO — logs only |
| Target Price|delta | 3d | +0.0058 | 7 | 1.071 | NO — logs only |
| Analyst Recom|delta | 1d | +0.0061 | 9 | 1.408 | NO — logs only |
| Analyst Recom|delta | 2d | -0.0023 | 8 | 1.385 | NO — logs only |
| Analyst Recom|delta | 3d | -0.0044 | 7 | 1.379 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 1d | +0.0219 | 10 | 2.000 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 2d | +0.0277 | 9 | 2.000 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 3d | +0.0415 | 8 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 1d | +0.0208 | 10 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 2d | +0.0312 | 9 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 3d | +0.0413 | 8 | 2.000 | NO — logs only |
| Profit Margin|delta | 1d | +0.0041 | 9 | 0.925 | NO — logs only |
| Profit Margin|delta | 2d | -0.0005 | 8 | 0.916 | NO — logs only |
| Profit Margin|delta | 3d | +0.0089 | 7 | 0.933 | NO — logs only |
| EPS Surprise|level | 1d | -0.0021 | 10 | 0.954 | NO — logs only |
| EPS Surprise|level | 2d | -0.0011 | 9 | 0.956 | NO — logs only |
| EPS Surprise|level | 3d | +0.0061 | 8 | 0.970 | NO — logs only |
| n_catalysts|level | 1d | -0.0015 | 10 | 1.924 | yes |
| n_catalysts|level | 2d | -0.0077 | 9 | 1.900 | yes |
| n_catalysts|level | 3d | -0.0079 | 8 | 1.899 | yes |
| Relative Volume|level | — | n/a (curved polarity) | — | 1.000 | not adjustable |
| Relative Strength Index (14)|level | — | n/a (curved polarity) | — | 1.000 | not adjustable |
| 50-Day Simple Moving Average|level | — | n/a (curved polarity) | — | 1.000 | not adjustable |
| 200-Day Simple Moving Average|level | — | n/a (curved polarity) | — | 1.000 | not adjustable |
| Volatility (Month)|level | — | n/a (curved polarity) | — | 1.000 | not adjustable |
| Short Float|level | — | n/a (curved polarity) | — | 1.000 | not adjustable |
| upside_pct|level | — | n/a (curved polarity) | — | 1.000 | not adjustable |
| Total Debt/Equity|level | — | n/a (curved polarity) | — | 1.000 | not adjustable |

## Champion vs challenger (1d score)

| Scan date | Horizon | Champion IC | Challenger IC | Δ |
|---|---|---|---|---|
| 2026-08-06 | 1d | +0.0958 | +0.0952 | -0.0005 |
| 2026-08-06 | 2d | +0.0636 | +0.0636 | -0.0000 |
| 2026-08-06 | 3d | +0.0815 | +0.0812 | -0.0003 |
| 2026-08-07 | 1d | -0.0339 | -0.0168 | +0.0172 |
| 2026-08-07 | 2d | -0.0242 | -0.0145 | +0.0097 |
| 2026-08-07 | 3d | -0.0009 | -0.0018 | -0.0009 |
| 2026-08-10 | 1d | -0.0491 | -0.0316 | +0.0174 |
| 2026-08-10 | 2d | -0.0596 | -0.0404 | +0.0192 |
| 2026-08-10 | 3d | -0.1054 | -0.0938 | +0.0116 |
| 2026-08-11 | 1d | +0.1007 | +0.1119 | +0.0112 |
| 2026-08-11 | 2d | +0.0174 | +0.0169 | -0.0005 |
| 2026-08-11 | 3d | +0.0639 | +0.0582 | -0.0057 |
| 2026-08-12 | 1d | -0.0472 | -0.0424 | +0.0048 |
| 2026-08-12 | 2d | +0.0520 | +0.0491 | -0.0029 |
| 2026-08-12 | 3d | +0.0878 | +0.0708 | -0.0170 |
| 2026-08-13 | 1d | -0.0908 | -0.0857 | +0.0051 |
| 2026-08-13 | 2d | -0.1428 | -0.1341 | +0.0087 |
| 2026-08-13 | 3d | -0.1672 | -0.1641 | +0.0031 |
| 2026-08-14 | 1d | +0.1577 | +0.1654 | +0.0077 |
| 2026-08-14 | 2d | -0.1560 | -0.1597 | -0.0037 |
| 2026-08-14 | 3d | -0.1404 | -0.1397 | +0.0007 |
| 2026-08-17 | 1d | -0.2097 | -0.2095 | +0.0002 |
| 2026-08-17 | 2d | -0.1365 | -0.1364 | +0.0002 |
| 2026-08-17 | 3d | -0.1034 | -0.1018 | +0.0016 |
| 2026-08-18 | 1d | +0.0486 | +0.0486 | +0.0000 |
| 2026-08-18 | 2d | +0.0270 | +0.0275 | +0.0005 |
| 2026-08-19 | 1d | +0.0108 | +0.0111 | +0.0004 |

_Champion reconstruction check: mean |rebuilt price category − stored price_score| = 0.2430 (should be ~0; large values mean the learner's model of the engine has drifted from score_engine — distrust this run)._

## Decision

PROMOTED — challenger mean IC gain +0.0064 on 1d, improved on 90% of 10 dates. New multipliers: Performance (Month)|delta ×1.202, Average Volume|delta ×0.743, Short Float|delta ×1.626, Institutional Transactions|level ×1.571, Institutional Ownership|delta ×1.763, Insider Transactions|level ×0.812, Target Price|delta ×1.074, Analyst Recom|delta ×1.408, Profit Margin|delta ×0.925, EPS Surprise|level ×0.954, n_catalysts|level ×1.924

_Note: curved-polarity rules (rvol/rsi/sma/short/upside/debt curves) are never auto-adjusted; change those in score_rubric.py by hand with git history as the audit trail._
