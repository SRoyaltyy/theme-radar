# Weight learning — decision log

_Generated 2026-09-11 18:56 EDT_

- label dates per horizon: 1d: 24, 2d: 23, 3d: 22
- primary horizon for promotion test: **1d** (24 dates)
- existing overrides: {'Price|ret': 0.25, 'Performance (Month)|delta': 0.997653044130433, 'Average Volume|delta': 0.5943661419738967, 'Relative Strength Index (14)|delta': 0.25, 'Short Float|delta': 1.746112087205599, 'Institutional Transactions|level': 1.383214914470539, 'Institutional Ownership|delta': 1.8914419057220313, 'Insider Transactions|level': 0.9093808453980674, 'Target Price|delta': 1.2033067342193218, 'Analyst Recom|delta': 1.7860946226616015, 'Sales Growth Quarter Over Quarter|level': 2.0, 'Sales Year Over Year TTM|level': 2.0, 'Profit Margin|delta': 1.0553956686115462, 'EPS Surprise|level': 0.9893166800869619, 'n_catalysts|level': 1.6800249497556725}

## Per-rule aligned IC (direction corrected for polarity)

| Rule | Horizon | Mean aligned IC | Dates | Proposed × | Testable |
|---|---|---|---|---|---|
| Price|ret | 1d | -0.0503 | 22 | 0.250 | yes |
| Price|ret | 2d | -0.0503 | 21 | 0.250 | yes |
| Price|ret | 3d | -0.0466 | 20 | 0.250 | yes |
| Performance (Month)|delta | 1d | -0.0228 | 22 | 0.952 | yes |
| Performance (Month)|delta | 2d | -0.0431 | 21 | 0.912 | yes |
| Performance (Month)|delta | 3d | -0.0610 | 20 | 0.876 | yes |
| Average Volume|delta | 1d | -0.0097 | 22 | 0.583 | NO — logs only |
| Average Volume|delta | 2d | -0.0112 | 21 | 0.581 | NO — logs only |
| Average Volume|delta | 3d | -0.0120 | 20 | 0.580 | NO — logs only |
| Relative Strength Index (14)|delta | 1d | -0.0432 | 22 | 0.250 | yes |
| Relative Strength Index (14)|delta | 2d | -0.0561 | 21 | 0.250 | yes |
| Relative Strength Index (14)|delta | 3d | -0.0389 | 20 | 0.250 | yes |
| Short Float|delta | 1d | +0.0008 | 21 | 1.749 | NO — logs only |
| Short Float|delta | 2d | -0.0032 | 20 | 1.735 | NO — logs only |
| Short Float|delta | 3d | -0.0065 | 19 | 1.724 | NO — logs only |
| Institutional Transactions|level | 1d | -0.0068 | 24 | 1.364 | NO — logs only |
| Institutional Transactions|level | 2d | -0.0057 | 23 | 1.367 | NO — logs only |
| Institutional Transactions|level | 3d | -0.0060 | 22 | 1.367 | NO — logs only |
| Institutional Ownership|delta | 1d | +0.0026 | 22 | 1.901 | NO — logs only |
| Institutional Ownership|delta | 2d | +0.0074 | 21 | 1.920 | NO — logs only |
| Institutional Ownership|delta | 3d | +0.0055 | 20 | 1.912 | NO — logs only |
| Insider Transactions|level | 1d | -0.0026 | 24 | 0.905 | NO — logs only |
| Insider Transactions|level | 2d | +0.0033 | 23 | 0.915 | NO — logs only |
| Insider Transactions|level | 3d | +0.0067 | 22 | 0.922 | NO — logs only |
| Target Price|delta | 1d | +0.0027 | 22 | 1.210 | NO — logs only |
| Target Price|delta | 2d | +0.0031 | 21 | 1.211 | NO — logs only |
| Target Price|delta | 3d | +0.0029 | 20 | 1.210 | NO — logs only |
| Analyst Recom|delta | 1d | +0.0112 | 22 | 1.826 | NO — logs only |
| Analyst Recom|delta | 2d | -0.0004 | 21 | 1.785 | NO — logs only |
| Analyst Recom|delta | 3d | -0.0036 | 20 | 1.773 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 1d | +0.0181 | 24 | 2.000 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 2d | +0.0214 | 23 | 2.000 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 3d | +0.0269 | 22 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 1d | +0.0143 | 24 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 2d | +0.0189 | 23 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 3d | +0.0244 | 22 | 2.000 | NO — logs only |
| Profit Margin|delta | 1d | +0.0052 | 22 | 1.066 | NO — logs only |
| Profit Margin|delta | 2d | +0.0038 | 21 | 1.063 | NO — logs only |
| Profit Margin|delta | 3d | +0.0079 | 20 | 1.072 | NO — logs only |
| EPS Surprise|level | 1d | +0.0082 | 24 | 1.005 | NO — logs only |
| EPS Surprise|level | 2d | +0.0089 | 23 | 1.007 | NO — logs only |
| EPS Surprise|level | 3d | +0.0071 | 22 | 1.003 | NO — logs only |
| n_catalysts|level | 1d | -0.0072 | 24 | 1.656 | yes |
| n_catalysts|level | 2d | -0.0139 | 23 | 1.633 | yes |
| n_catalysts|level | 3d | -0.0157 | 22 | 1.627 | yes |
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
| 2026-08-07 | 1d | -0.0339 | -0.0231 | +0.0108 |
| 2026-08-07 | 2d | -0.0242 | -0.0175 | +0.0066 |
| 2026-08-07 | 3d | -0.0009 | +0.0010 | +0.0020 |
| 2026-08-10 | 1d | -0.0491 | -0.0307 | +0.0184 |
| 2026-08-10 | 2d | -0.0596 | -0.0375 | +0.0221 |
| 2026-08-10 | 3d | -0.1054 | -0.0918 | +0.0136 |
| 2026-08-11 | 1d | +0.1007 | +0.1054 | +0.0047 |
| 2026-08-11 | 2d | +0.0174 | +0.0115 | -0.0059 |
| 2026-08-11 | 3d | +0.0639 | +0.0579 | -0.0060 |
| 2026-08-12 | 1d | -0.0472 | -0.0453 | +0.0019 |
| 2026-08-12 | 2d | +0.0520 | +0.0524 | +0.0004 |
| 2026-08-12 | 3d | +0.0878 | +0.0797 | -0.0081 |
| 2026-08-13 | 1d | -0.0908 | -0.0865 | +0.0043 |
| 2026-08-13 | 2d | -0.1428 | -0.1366 | +0.0061 |
| 2026-08-13 | 3d | -0.1672 | -0.1639 | +0.0032 |
| 2026-08-14 | 1d | +0.1577 | +0.1512 | -0.0065 |
| 2026-08-14 | 2d | -0.1560 | -0.1577 | -0.0018 |
| 2026-08-14 | 3d | -0.1404 | -0.1410 | -0.0007 |
| 2026-08-17 | 1d | -0.2097 | -0.2079 | +0.0018 |
| 2026-08-17 | 2d | -0.1365 | -0.1358 | +0.0008 |
| 2026-08-17 | 3d | -0.1034 | -0.1036 | -0.0002 |
| 2026-08-18 | 1d | +0.0486 | +0.0477 | -0.0009 |
| 2026-08-18 | 2d | +0.0270 | +0.0250 | -0.0020 |
| 2026-08-18 | 3d | +0.0058 | +0.0076 | +0.0018 |
| 2026-08-19 | 1d | +0.0108 | +0.0057 | -0.0051 |
| 2026-08-19 | 2d | +0.0519 | +0.0545 | +0.0026 |
| 2026-08-19 | 3d | +0.1772 | +0.1722 | -0.0050 |
| 2026-08-20 | 1d | -0.0007 | +0.0037 | +0.0044 |
| 2026-08-20 | 2d | +0.0530 | +0.0553 | +0.0023 |
| 2026-08-20 | 3d | +0.0387 | +0.0435 | +0.0048 |
| 2026-08-21 | 1d | -0.0802 | -0.0810 | -0.0008 |
| 2026-08-21 | 2d | +0.0158 | +0.0138 | -0.0020 |
| 2026-08-21 | 3d | -0.0723 | -0.0736 | -0.0012 |
| 2026-08-24 | 1d | +0.0056 | -0.0097 | -0.0153 |
| 2026-08-24 | 2d | -0.0285 | -0.0446 | -0.0161 |
| 2026-08-24 | 3d | -0.0880 | -0.0888 | -0.0007 |
| 2026-08-25 | 1d | -0.0503 | -0.0654 | -0.0151 |
| 2026-08-25 | 2d | -0.1093 | -0.1165 | -0.0072 |
| 2026-08-25 | 3d | -0.0661 | -0.0760 | -0.0099 |
| 2026-08-26 | 1d | -0.0710 | -0.0621 | +0.0089 |
| 2026-08-26 | 2d | -0.0146 | -0.0140 | +0.0006 |
| 2026-08-26 | 3d | -0.0019 | +0.0030 | +0.0049 |
| 2026-08-28 | 1d | -0.0442 | -0.0369 | +0.0073 |
| 2026-08-28 | 2d | +0.0258 | +0.0235 | -0.0024 |
| 2026-08-28 | 3d | +0.0108 | +0.0191 | +0.0083 |
| 2026-08-31 | 1d | -0.0065 | -0.0082 | -0.0016 |
| 2026-08-31 | 2d | +0.0398 | +0.0415 | +0.0018 |
| 2026-08-31 | 3d | +0.1004 | +0.1040 | +0.0036 |
| 2026-09-01 | 1d | -0.0847 | -0.0565 | +0.0282 |
| 2026-09-01 | 2d | -0.2394 | -0.2030 | +0.0365 |
| 2026-09-01 | 3d | -0.2756 | -0.2434 | +0.0322 |
| 2026-09-02 | 1d | -0.0842 | -0.0625 | +0.0218 |
| 2026-09-02 | 2d | -0.1304 | -0.1040 | +0.0264 |
| 2026-09-02 | 3d | -0.1700 | -0.1542 | +0.0158 |
| 2026-09-03 | 1d | -0.0656 | -0.0813 | -0.0156 |
| 2026-09-03 | 2d | -0.0607 | -0.0834 | -0.0227 |
| 2026-09-03 | 3d | -0.1049 | -0.1227 | -0.0178 |
| 2026-09-04 | 1d | -0.0292 | -0.0335 | -0.0043 |
| 2026-09-04 | 2d | -0.0659 | -0.0715 | -0.0055 |
| 2026-09-04 | 3d | -0.1272 | -0.1318 | -0.0046 |
| 2026-09-08 | 1d | -0.0849 | -0.0849 | +0.0000 |
| 2026-09-08 | 2d | -0.1276 | -0.1276 | +0.0000 |
| 2026-09-08 | 3d | -0.0619 | -0.0619 | +0.0000 |
| 2026-09-09 | 1d | -0.0163 | -0.0200 | -0.0037 |
| 2026-09-09 | 2d | +0.0188 | +0.0153 | -0.0035 |
| 2026-09-10 | 1d | -0.0932 | -0.0913 | +0.0019 |

_Champion reconstruction check: mean |rebuilt price category − stored price_score| = 0.1879 (should be ~0; large values mean the learner's model of the engine has drifted from score_engine — distrust this run)._

## Decision

PROMOTED — challenger mean IC gain +0.0019 on 1d, improved on 54% of 24 dates. New multipliers: Performance (Month)|delta ×0.952, Average Volume|delta ×0.583, Short Float|delta ×1.749, Institutional Transactions|level ×1.364, Institutional Ownership|delta ×1.901, Insider Transactions|level ×0.905, Target Price|delta ×1.210, Analyst Recom|delta ×1.826, Profit Margin|delta ×1.066, EPS Surprise|level ×1.005, n_catalysts|level ×1.656

_Note: curved-polarity rules (rvol/rsi/sma/short/upside/debt curves) are never auto-adjusted; change those in score_rubric.py by hand with git history as the audit trail._
