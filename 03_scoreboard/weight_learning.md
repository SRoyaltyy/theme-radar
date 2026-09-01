# Weight learning — decision log

_Generated 2026-09-01 18:56 EDT_

- label dates per horizon: 1d: 17, 2d: 16, 3d: 15
- primary horizon for promotion test: **1d** (17 dates)
- existing overrides: {'Price|ret': 0.25, 'Performance (Month)|delta': 1.2775975879795898, 'Average Volume|delta': 0.6806066500466065, 'Relative Strength Index (14)|delta': 0.25, 'Short Float|delta': 1.6800562333734255, 'Institutional Transactions|level': 1.494001536541956, 'Institutional Ownership|delta': 1.8342212299745162, 'Insider Transactions|level': 0.8699238720929051, 'Target Price|delta': 1.1426480510148118, 'Analyst Recom|delta': 1.5377715655231161, 'Sales Growth Quarter Over Quarter|level': 2.0, 'Sales Year Over Year TTM|level': 2.0, 'Profit Margin|delta': 0.980767454285858, 'EPS Surprise|level': 0.9435352923164397, 'n_catalysts|level': 1.853113773442114}

## Per-rule aligned IC (direction corrected for polarity)

| Rule | Horizon | Mean aligned IC | Dates | Proposed × | Testable |
|---|---|---|---|---|---|
| Price|ret | 1d | -0.0574 | 16 | 0.250 | yes |
| Price|ret | 2d | -0.0452 | 15 | 0.250 | yes |
| Price|ret | 3d | -0.0310 | 14 | 0.250 | yes |
| Performance (Month)|delta | 1d | -0.0041 | 16 | 1.267 | yes |
| Performance (Month)|delta | 2d | -0.0204 | 15 | 1.226 | yes |
| Performance (Month)|delta | 3d | -0.0369 | 14 | 1.183 | yes |
| Average Volume|delta | 1d | -0.0089 | 16 | 0.669 | NO — logs only |
| Average Volume|delta | 2d | -0.0122 | 15 | 0.664 | NO — logs only |
| Average Volume|delta | 3d | -0.0161 | 14 | 0.659 | NO — logs only |
| Relative Strength Index (14)|delta | 1d | -0.0501 | 16 | 0.250 | yes |
| Relative Strength Index (14)|delta | 2d | -0.0526 | 15 | 0.250 | yes |
| Relative Strength Index (14)|delta | 3d | -0.0270 | 14 | 0.250 | yes |
| Short Float|delta | 1d | +0.0021 | 15 | 1.687 | NO — logs only |
| Short Float|delta | 2d | -0.0054 | 14 | 1.662 | NO — logs only |
| Short Float|delta | 3d | -0.0104 | 13 | 1.645 | NO — logs only |
| Institutional Transactions|level | 1d | -0.0083 | 17 | 1.469 | NO — logs only |
| Institutional Transactions|level | 2d | -0.0088 | 16 | 1.468 | NO — logs only |
| Institutional Transactions|level | 3d | -0.0122 | 15 | 1.457 | NO — logs only |
| Institutional Ownership|delta | 1d | -0.0008 | 16 | 1.831 | NO — logs only |
| Institutional Ownership|delta | 2d | +0.0039 | 15 | 1.848 | NO — logs only |
| Institutional Ownership|delta | 3d | +0.0024 | 14 | 1.843 | NO — logs only |
| Insider Transactions|level | 1d | +0.0066 | 17 | 0.881 | NO — logs only |
| Insider Transactions|level | 2d | +0.0133 | 16 | 0.893 | NO — logs only |
| Insider Transactions|level | 3d | +0.0175 | 15 | 0.900 | NO — logs only |
| Target Price|delta | 1d | +0.0050 | 16 | 1.154 | NO — logs only |
| Target Price|delta | 2d | +0.0021 | 15 | 1.148 | NO — logs only |
| Target Price|delta | 3d | +0.0032 | 14 | 1.150 | NO — logs only |
| Analyst Recom|delta | 1d | +0.0091 | 16 | 1.566 | NO — logs only |
| Analyst Recom|delta | 2d | -0.0024 | 15 | 1.530 | NO — logs only |
| Analyst Recom|delta | 3d | -0.0080 | 14 | 1.513 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 1d | +0.0114 | 17 | 2.000 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 2d | +0.0115 | 16 | 2.000 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 3d | +0.0138 | 15 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 1d | +0.0099 | 17 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 2d | +0.0134 | 16 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 3d | +0.0164 | 15 | 2.000 | NO — logs only |
| Profit Margin|delta | 1d | +0.0044 | 16 | 0.989 | NO — logs only |
| Profit Margin|delta | 2d | -0.0014 | 15 | 0.978 | NO — logs only |
| Profit Margin|delta | 3d | +0.0056 | 14 | 0.992 | NO — logs only |
| EPS Surprise|level | 1d | +0.0049 | 17 | 0.953 | NO — logs only |
| EPS Surprise|level | 2d | +0.0049 | 16 | 0.953 | NO — logs only |
| EPS Surprise|level | 3d | +0.0056 | 15 | 0.954 | NO — logs only |
| n_catalysts|level | 1d | -0.0110 | 17 | 1.813 | yes |
| n_catalysts|level | 2d | -0.0176 | 16 | 1.788 | yes |
| n_catalysts|level | 3d | -0.0218 | 15 | 1.772 | yes |
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
| 2026-08-07 | 1d | -0.0339 | -0.0167 | +0.0172 |
| 2026-08-07 | 2d | -0.0242 | -0.0145 | +0.0097 |
| 2026-08-07 | 3d | -0.0009 | -0.0020 | -0.0010 |
| 2026-08-10 | 1d | -0.0491 | -0.0317 | +0.0174 |
| 2026-08-10 | 2d | -0.0596 | -0.0405 | +0.0191 |
| 2026-08-10 | 3d | -0.1054 | -0.0938 | +0.0116 |
| 2026-08-11 | 1d | +0.1007 | +0.1119 | +0.0112 |
| 2026-08-11 | 2d | +0.0174 | +0.0169 | -0.0004 |
| 2026-08-11 | 3d | +0.0639 | +0.0582 | -0.0057 |
| 2026-08-12 | 1d | -0.0472 | -0.0418 | +0.0054 |
| 2026-08-12 | 2d | +0.0520 | +0.0492 | -0.0028 |
| 2026-08-12 | 3d | +0.0878 | +0.0704 | -0.0173 |
| 2026-08-13 | 1d | -0.0908 | -0.0858 | +0.0050 |
| 2026-08-13 | 2d | -0.1428 | -0.1338 | +0.0090 |
| 2026-08-13 | 3d | -0.1672 | -0.1636 | +0.0035 |
| 2026-08-14 | 1d | +0.1577 | +0.1662 | +0.0085 |
| 2026-08-14 | 2d | -0.1560 | -0.1597 | -0.0038 |
| 2026-08-14 | 3d | -0.1404 | -0.1397 | +0.0006 |
| 2026-08-17 | 1d | -0.2097 | -0.2091 | +0.0007 |
| 2026-08-17 | 2d | -0.1365 | -0.1361 | +0.0004 |
| 2026-08-17 | 3d | -0.1034 | -0.1013 | +0.0021 |
| 2026-08-18 | 1d | +0.0486 | +0.0484 | -0.0002 |
| 2026-08-18 | 2d | +0.0270 | +0.0277 | +0.0006 |
| 2026-08-18 | 3d | +0.0058 | +0.0049 | -0.0009 |
| 2026-08-19 | 1d | +0.0108 | +0.0128 | +0.0020 |
| 2026-08-19 | 2d | +0.0519 | +0.0505 | -0.0014 |
| 2026-08-19 | 3d | +0.1772 | +0.1795 | +0.0023 |
| 2026-08-20 | 1d | -0.0007 | -0.0015 | -0.0008 |
| 2026-08-20 | 2d | +0.0530 | +0.0520 | -0.0010 |
| 2026-08-20 | 3d | +0.0387 | +0.0376 | -0.0012 |
| 2026-08-21 | 1d | -0.0802 | -0.0791 | +0.0011 |
| 2026-08-21 | 2d | +0.0158 | +0.0165 | +0.0006 |
| 2026-08-21 | 3d | -0.0723 | -0.0719 | +0.0005 |
| 2026-08-24 | 1d | +0.0056 | +0.0068 | +0.0012 |
| 2026-08-24 | 2d | -0.0285 | -0.0272 | +0.0013 |
| 2026-08-24 | 3d | -0.0880 | -0.0880 | +0.0000 |
| 2026-08-25 | 1d | -0.0503 | -0.0487 | +0.0016 |
| 2026-08-25 | 2d | -0.1093 | -0.1084 | +0.0009 |
| 2026-08-25 | 3d | -0.0661 | -0.0656 | +0.0005 |
| 2026-08-26 | 1d | -0.0710 | -0.0710 | -0.0000 |
| 2026-08-26 | 2d | -0.0146 | -0.0141 | +0.0005 |
| 2026-08-26 | 3d | -0.0019 | -0.0016 | +0.0003 |
| 2026-08-28 | 1d | -0.0442 | -0.0434 | +0.0008 |
| 2026-08-28 | 2d | +0.0258 | +0.0266 | +0.0007 |
| 2026-08-31 | 1d | -0.0065 | -0.0062 | +0.0003 |

_Champion reconstruction check: mean |rebuilt price category − stored price_score| = 0.1802 (should be ~0; large values mean the learner's model of the engine has drifted from score_engine — distrust this run)._

## Decision

PROMOTED — challenger mean IC gain +0.0042 on 1d, improved on 76% of 17 dates. New multipliers: Performance (Month)|delta ×1.267, Average Volume|delta ×0.669, Short Float|delta ×1.687, Institutional Transactions|level ×1.469, Institutional Ownership|delta ×1.831, Insider Transactions|level ×0.881, Target Price|delta ×1.154, Analyst Recom|delta ×1.566, Profit Margin|delta ×0.989, EPS Surprise|level ×0.953, n_catalysts|level ×1.813

_Note: curved-polarity rules (rvol/rsi/sma/short/upside/debt curves) are never auto-adjusted; change those in score_rubric.py by hand with git history as the audit trail._
