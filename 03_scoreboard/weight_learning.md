# Weight learning — decision log

_Generated 2026-08-25 17:20 EDT_

- label dates per horizon: 1d: 13, 2d: 12, 3d: 11
- primary horizon for promotion test: **1d** (13 dates)
- existing overrides: {'Price|ret': 0.25, 'Performance (Month)|delta': 1.2141630106670946, 'Average Volume|delta': 0.7301904503129326, 'Relative Strength Index (14)|delta': 0.25, 'Short Float|delta': 1.6346105680377971, 'Institutional Transactions|level': 1.5542840566786076, 'Institutional Ownership|delta': 1.8112263577380407, 'Insider Transactions|level': 0.8312629446837688, 'Target Price|delta': 1.1003974238447407, 'Analyst Recom|delta': 1.4311393832435562, 'Sales Growth Quarter Over Quarter|level': 2.0, 'Sales Year Over Year TTM|level': 2.0, 'Profit Margin|delta': 0.9505953422438936, 'EPS Surprise|level': 0.9512529662860748, 'n_catalysts|level': 1.9042983372696707}

## Per-rule aligned IC (direction corrected for polarity)

| Rule | Horizon | Mean aligned IC | Dates | Proposed × | Testable |
|---|---|---|---|---|---|
| Price|ret | 1d | -0.0722 | 12 | 0.250 | yes |
| Price|ret | 2d | -0.0351 | 11 | 0.250 | yes |
| Price|ret | 3d | -0.0138 | 10 | 0.250 | yes |
| Performance (Month)|delta | 1d | +0.0080 | 12 | 1.234 | yes |
| Performance (Month)|delta | 2d | -0.0328 | 11 | 1.135 | yes |
| Performance (Month)|delta | 3d | -0.0392 | 10 | 1.119 | yes |
| Average Volume|delta | 1d | -0.0029 | 12 | 0.726 | NO — logs only |
| Average Volume|delta | 2d | -0.0058 | 11 | 0.722 | NO — logs only |
| Average Volume|delta | 3d | -0.0095 | 10 | 0.716 | NO — logs only |
| Relative Strength Index (14)|delta | 1d | -0.0558 | 12 | 0.250 | yes |
| Relative Strength Index (14)|delta | 2d | -0.0431 | 11 | 0.250 | yes |
| Relative Strength Index (14)|delta | 3d | -0.0102 | 10 | 0.250 | yes |
| Short Float|delta | 1d | +0.0002 | 11 | 1.635 | NO — logs only |
| Short Float|delta | 2d | -0.0065 | 10 | 1.613 | NO — logs only |
| Short Float|delta | 3d | -0.0158 | 9 | 1.583 | NO — logs only |
| Institutional Transactions|level | 1d | -0.0011 | 13 | 1.551 | NO — logs only |
| Institutional Transactions|level | 2d | -0.0021 | 12 | 1.548 | NO — logs only |
| Institutional Transactions|level | 3d | +0.0007 | 11 | 1.556 | NO — logs only |
| Institutional Ownership|delta | 1d | -0.0005 | 12 | 1.809 | NO — logs only |
| Institutional Ownership|delta | 2d | +0.0084 | 11 | 1.842 | NO — logs only |
| Institutional Ownership|delta | 3d | +0.0070 | 10 | 1.837 | NO — logs only |
| Insider Transactions|level | 1d | +0.0097 | 13 | 0.847 | NO — logs only |
| Insider Transactions|level | 2d | +0.0172 | 12 | 0.860 | NO — logs only |
| Insider Transactions|level | 3d | +0.0207 | 11 | 0.866 | NO — logs only |
| Target Price|delta | 1d | +0.0060 | 12 | 1.114 | NO — logs only |
| Target Price|delta | 2d | +0.0049 | 11 | 1.111 | NO — logs only |
| Target Price|delta | 3d | +0.0046 | 10 | 1.111 | NO — logs only |
| Analyst Recom|delta | 1d | +0.0059 | 12 | 1.448 | NO — logs only |
| Analyst Recom|delta | 2d | -0.0059 | 11 | 1.414 | NO — logs only |
| Analyst Recom|delta | 3d | -0.0064 | 10 | 1.413 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 1d | +0.0160 | 13 | 2.000 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 2d | +0.0185 | 12 | 2.000 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 3d | +0.0230 | 11 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 1d | +0.0168 | 13 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 2d | +0.0191 | 12 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 3d | +0.0224 | 11 | 2.000 | NO — logs only |
| Profit Margin|delta | 1d | +0.0046 | 12 | 0.959 | NO — logs only |
| Profit Margin|delta | 2d | +0.0024 | 11 | 0.955 | NO — logs only |
| Profit Margin|delta | 3d | +0.0110 | 10 | 0.972 | NO — logs only |
| EPS Surprise|level | 1d | -0.0069 | 13 | 0.938 | NO — logs only |
| EPS Surprise|level | 2d | -0.0023 | 12 | 0.947 | NO — logs only |
| EPS Surprise|level | 3d | -0.0024 | 11 | 0.947 | NO — logs only |
| n_catalysts|level | 1d | -0.0011 | 13 | 1.900 | yes |
| n_catalysts|level | 2d | -0.0102 | 12 | 1.866 | yes |
| n_catalysts|level | 3d | -0.0121 | 11 | 1.858 | yes |
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
| 2026-08-07 | 2d | -0.0242 | -0.0145 | +0.0096 |
| 2026-08-07 | 3d | -0.0009 | -0.0019 | -0.0010 |
| 2026-08-10 | 1d | -0.0491 | -0.0317 | +0.0174 |
| 2026-08-10 | 2d | -0.0596 | -0.0405 | +0.0191 |
| 2026-08-10 | 3d | -0.1054 | -0.0938 | +0.0116 |
| 2026-08-11 | 1d | +0.1007 | +0.1118 | +0.0111 |
| 2026-08-11 | 2d | +0.0174 | +0.0169 | -0.0005 |
| 2026-08-11 | 3d | +0.0639 | +0.0582 | -0.0057 |
| 2026-08-12 | 1d | -0.0472 | -0.0422 | +0.0050 |
| 2026-08-12 | 2d | +0.0520 | +0.0490 | -0.0030 |
| 2026-08-12 | 3d | +0.0878 | +0.0704 | -0.0173 |
| 2026-08-13 | 1d | -0.0908 | -0.0857 | +0.0051 |
| 2026-08-13 | 2d | -0.1428 | -0.1337 | +0.0091 |
| 2026-08-13 | 3d | -0.1672 | -0.1637 | +0.0035 |
| 2026-08-14 | 1d | +0.1577 | +0.1658 | +0.0081 |
| 2026-08-14 | 2d | -0.1560 | -0.1597 | -0.0038 |
| 2026-08-14 | 3d | -0.1404 | -0.1398 | +0.0006 |
| 2026-08-17 | 1d | -0.2097 | -0.2094 | +0.0003 |
| 2026-08-17 | 2d | -0.1365 | -0.1363 | +0.0002 |
| 2026-08-17 | 3d | -0.1034 | -0.1017 | +0.0017 |
| 2026-08-18 | 1d | +0.0486 | +0.0487 | +0.0001 |
| 2026-08-18 | 2d | +0.0270 | +0.0277 | +0.0007 |
| 2026-08-18 | 3d | +0.0058 | +0.0056 | -0.0002 |
| 2026-08-19 | 1d | +0.0108 | +0.0114 | +0.0006 |
| 2026-08-19 | 2d | +0.0519 | +0.0511 | -0.0008 |
| 2026-08-19 | 3d | +0.1772 | +0.1784 | +0.0013 |
| 2026-08-20 | 1d | -0.0007 | -0.0006 | +0.0001 |
| 2026-08-20 | 2d | +0.0530 | +0.0526 | -0.0004 |
| 2026-08-20 | 3d | +0.0387 | +0.0386 | -0.0001 |
| 2026-08-21 | 1d | -0.0802 | -0.0801 | +0.0001 |
| 2026-08-21 | 2d | +0.0158 | +0.0160 | +0.0001 |
| 2026-08-24 | 1d | +0.0056 | +0.0054 | -0.0002 |

_Champion reconstruction check: mean |rebuilt price category − stored price_score| = 0.2016 (should be ~0; large values mean the learner's model of the engine has drifted from score_engine — distrust this run)._

## Decision

PROMOTED — challenger mean IC gain +0.0050 on 1d, improved on 85% of 13 dates. New multipliers: Performance (Month)|delta ×1.234, Average Volume|delta ×0.726, Short Float|delta ×1.635, Institutional Transactions|level ×1.551, Institutional Ownership|delta ×1.809, Insider Transactions|level ×0.847, Target Price|delta ×1.114, Analyst Recom|delta ×1.448, Profit Margin|delta ×0.959, EPS Surprise|level ×0.938, n_catalysts|level ×1.900

_Note: curved-polarity rules (rvol/rsi/sma/short/upside/debt curves) are never auto-adjusted; change those in score_rubric.py by hand with git history as the audit trail._
