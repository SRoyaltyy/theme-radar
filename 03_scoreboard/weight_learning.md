# Weight learning — decision log

_Generated 2026-09-18 16:37 EDT_

- label dates per horizon: 1d: 29, 2d: 28, 3d: 27
- primary horizon for promotion test: **1d** (29 dates)
- existing overrides: {'Price|ret': 0.25, 'Performance (Month)|delta': 0.8543745509856159, 'Average Volume|delta': 0.5610453165124469, 'Relative Strength Index (14)|delta': 0.25, 'Short Float|delta': 1.7360810947250618, 'Institutional Transactions|level': 1.2988047200755224, 'Institutional Ownership|delta': 1.9355228692156583, 'Insider Transactions|level': 0.8833298212974705, 'Target Price|delta': 1.2395145161914445, 'Analyst Recom|delta': 1.9243962218243638, 'Sales Growth Quarter Over Quarter|level': 2.0, 'Sales Year Over Year TTM|level': 2.0, 'Profit Margin|delta': 1.1063482321861713, 'EPS Surprise|level': 1.0670641269567658, 'n_catalysts|level': 1.543458790003396}

## Per-rule aligned IC (direction corrected for polarity)

| Rule | Horizon | Mean aligned IC | Dates | Proposed × | Testable |
|---|---|---|---|---|---|
| Price|ret | 1d | -0.0462 | 27 | 0.250 | yes |
| Price|ret | 2d | -0.0481 | 26 | 0.250 | yes |
| Price|ret | 3d | -0.0483 | 25 | 0.250 | yes |
| Performance (Month)|delta | 1d | -0.0144 | 27 | 0.830 | yes |
| Performance (Month)|delta | 2d | -0.0359 | 26 | 0.793 | yes |
| Performance (Month)|delta | 3d | -0.0522 | 25 | 0.765 | yes |
| Average Volume|delta | 1d | -0.0093 | 27 | 0.551 | NO — logs only |
| Average Volume|delta | 2d | -0.0089 | 26 | 0.551 | NO — logs only |
| Average Volume|delta | 3d | -0.0078 | 25 | 0.552 | NO — logs only |
| Relative Strength Index (14)|delta | 1d | -0.0412 | 27 | 0.250 | yes |
| Relative Strength Index (14)|delta | 2d | -0.0495 | 26 | 0.250 | yes |
| Relative Strength Index (14)|delta | 3d | -0.0472 | 25 | 0.250 | yes |
| Short Float|delta | 1d | -0.0025 | 26 | 1.727 | NO — logs only |
| Short Float|delta | 2d | -0.0060 | 25 | 1.715 | NO — logs only |
| Short Float|delta | 3d | -0.0088 | 24 | 1.706 | NO — logs only |
| Institutional Transactions|level | 1d | -0.0041 | 29 | 1.288 | NO — logs only |
| Institutional Transactions|level | 2d | -0.0051 | 28 | 1.286 | NO — logs only |
| Institutional Transactions|level | 3d | -0.0078 | 27 | 1.278 | NO — logs only |
| Institutional Ownership|delta | 1d | +0.0019 | 27 | 1.943 | NO — logs only |
| Institutional Ownership|delta | 2d | +0.0051 | 26 | 1.955 | NO — logs only |
| Institutional Ownership|delta | 3d | +0.0022 | 25 | 1.944 | NO — logs only |
| Insider Transactions|level | 1d | -0.0034 | 29 | 0.877 | NO — logs only |
| Insider Transactions|level | 2d | -0.0009 | 28 | 0.882 | NO — logs only |
| Insider Transactions|level | 3d | +0.0003 | 27 | 0.884 | NO — logs only |
| Target Price|delta | 1d | +0.0067 | 27 | 1.256 | NO — logs only |
| Target Price|delta | 2d | +0.0049 | 26 | 1.252 | NO — logs only |
| Target Price|delta | 3d | +0.0037 | 25 | 1.249 | NO — logs only |
| Analyst Recom|delta | 1d | +0.0094 | 27 | 1.961 | NO — logs only |
| Analyst Recom|delta | 2d | -0.0004 | 26 | 1.923 | NO — logs only |
| Analyst Recom|delta | 3d | -0.0025 | 25 | 1.915 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 1d | +0.0209 | 29 | 2.000 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 2d | +0.0235 | 28 | 2.000 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 3d | +0.0262 | 27 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 1d | +0.0170 | 29 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 2d | +0.0208 | 28 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 3d | +0.0228 | 27 | 2.000 | NO — logs only |
| Profit Margin|delta | 1d | +0.0059 | 27 | 1.119 | NO — logs only |
| Profit Margin|delta | 2d | +0.0051 | 26 | 1.118 | NO — logs only |
| Profit Margin|delta | 3d | +0.0068 | 25 | 1.121 | NO — logs only |
| EPS Surprise|level | 1d | +0.0113 | 29 | 1.091 | NO — logs only |
| EPS Surprise|level | 2d | +0.0143 | 28 | 1.097 | NO — logs only |
| EPS Surprise|level | 3d | +0.0168 | 27 | 1.103 | NO — logs only |
| n_catalysts|level | 1d | -0.0065 | 29 | 1.523 | yes |
| n_catalysts|level | 2d | -0.0142 | 28 | 1.500 | yes |
| n_catalysts|level | 3d | -0.0206 | 27 | 1.480 | yes |
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
| 2026-08-07 | 1d | -0.0339 | -0.0272 | +0.0067 |
| 2026-08-07 | 2d | -0.0242 | -0.0200 | +0.0041 |
| 2026-08-07 | 3d | -0.0009 | +0.0025 | +0.0034 |
| 2026-08-10 | 1d | -0.0491 | -0.0303 | +0.0188 |
| 2026-08-10 | 2d | -0.0596 | -0.0357 | +0.0240 |
| 2026-08-10 | 3d | -0.1054 | -0.0903 | +0.0151 |
| 2026-08-11 | 1d | +0.1007 | +0.1005 | -0.0002 |
| 2026-08-11 | 2d | +0.0174 | +0.0083 | -0.0091 |
| 2026-08-11 | 3d | +0.0639 | +0.0571 | -0.0068 |
| 2026-08-12 | 1d | -0.0472 | -0.0466 | +0.0006 |
| 2026-08-12 | 2d | +0.0520 | +0.0528 | +0.0008 |
| 2026-08-12 | 3d | +0.0878 | +0.0817 | -0.0060 |
| 2026-08-13 | 1d | -0.0908 | -0.0864 | +0.0044 |
| 2026-08-13 | 2d | -0.1428 | -0.1378 | +0.0050 |
| 2026-08-13 | 3d | -0.1672 | -0.1635 | +0.0037 |
| 2026-08-14 | 1d | +0.1577 | +0.1420 | -0.0157 |
| 2026-08-14 | 2d | -0.1560 | -0.1569 | -0.0009 |
| 2026-08-14 | 3d | -0.1404 | -0.1411 | -0.0008 |
| 2026-08-17 | 1d | -0.2097 | -0.2058 | +0.0040 |
| 2026-08-17 | 2d | -0.1365 | -0.1351 | +0.0014 |
| 2026-08-17 | 3d | -0.1034 | -0.1042 | -0.0008 |
| 2026-08-18 | 1d | +0.0486 | +0.0457 | -0.0029 |
| 2026-08-18 | 2d | +0.0270 | +0.0231 | -0.0039 |
| 2026-08-18 | 3d | +0.0058 | +0.0074 | +0.0016 |
| 2026-08-19 | 1d | +0.0108 | +0.0026 | -0.0082 |
| 2026-08-19 | 2d | +0.0519 | +0.0547 | +0.0028 |
| 2026-08-19 | 3d | +0.1772 | +0.1667 | -0.0105 |
| 2026-08-20 | 1d | -0.0007 | +0.0064 | +0.0071 |
| 2026-08-20 | 2d | +0.0530 | +0.0577 | +0.0047 |
| 2026-08-20 | 3d | +0.0387 | +0.0474 | +0.0086 |
| 2026-08-21 | 1d | -0.0802 | -0.0810 | -0.0008 |
| 2026-08-21 | 2d | +0.0158 | +0.0131 | -0.0028 |
| 2026-08-21 | 3d | -0.0723 | -0.0728 | -0.0005 |
| 2026-08-24 | 1d | +0.0056 | -0.0156 | -0.0212 |
| 2026-08-24 | 2d | -0.0285 | -0.0507 | -0.0222 |
| 2026-08-24 | 3d | -0.0880 | -0.0853 | +0.0028 |
| 2026-08-25 | 1d | -0.0503 | -0.0706 | -0.0203 |
| 2026-08-25 | 2d | -0.1093 | -0.1166 | -0.0073 |
| 2026-08-25 | 3d | -0.0661 | -0.0784 | -0.0123 |
| 2026-08-26 | 1d | -0.0710 | -0.0545 | +0.0165 |
| 2026-08-26 | 2d | -0.0146 | -0.0109 | +0.0037 |
| 2026-08-26 | 3d | -0.0019 | +0.0090 | +0.0109 |
| 2026-08-28 | 1d | -0.0442 | -0.0335 | +0.0108 |
| 2026-08-28 | 2d | +0.0258 | +0.0240 | -0.0018 |
| 2026-08-28 | 3d | +0.0108 | +0.0227 | +0.0119 |
| 2026-08-31 | 1d | -0.0065 | -0.0054 | +0.0011 |
| 2026-08-31 | 2d | +0.0398 | +0.0438 | +0.0040 |
| 2026-08-31 | 3d | +0.1004 | +0.1058 | +0.0054 |
| 2026-09-01 | 1d | -0.0847 | -0.0504 | +0.0343 |
| 2026-09-01 | 2d | -0.2394 | -0.1917 | +0.0478 |
| 2026-09-01 | 3d | -0.2756 | -0.2337 | +0.0419 |
| 2026-09-02 | 1d | -0.0842 | -0.0537 | +0.0305 |
| 2026-09-02 | 2d | -0.1304 | -0.0950 | +0.0355 |
| 2026-09-02 | 3d | -0.1700 | -0.1476 | +0.0224 |
| 2026-09-03 | 1d | -0.0656 | -0.0873 | -0.0217 |
| 2026-09-03 | 2d | -0.0607 | -0.0899 | -0.0291 |
| 2026-09-03 | 3d | -0.1049 | -0.1260 | -0.0211 |
| 2026-09-04 | 1d | -0.0292 | -0.0355 | -0.0064 |
| 2026-09-04 | 2d | -0.0659 | -0.0711 | -0.0052 |
| 2026-09-04 | 3d | -0.1272 | -0.1304 | -0.0032 |
| 2026-09-08 | 1d | -0.0849 | -0.0849 | +0.0000 |
| 2026-09-08 | 2d | -0.1276 | -0.1276 | +0.0000 |
| 2026-09-08 | 3d | -0.0619 | -0.0619 | +0.0000 |
| 2026-09-09 | 1d | -0.0163 | -0.0219 | -0.0057 |
| 2026-09-09 | 2d | +0.0188 | +0.0138 | -0.0051 |
| 2026-09-09 | 3d | -0.0591 | -0.0600 | -0.0009 |
| 2026-09-10 | 1d | -0.0932 | -0.0890 | +0.0041 |
| 2026-09-10 | 2d | +0.1308 | +0.1186 | -0.0122 |
| 2026-09-10 | 3d | +0.1827 | +0.1703 | -0.0124 |
| 2026-09-11 | 1d | -0.0419 | -0.0505 | -0.0086 |
| 2026-09-11 | 2d | -0.0676 | -0.0758 | -0.0083 |
| 2026-09-11 | 3d | -0.1072 | -0.1129 | -0.0058 |
| 2026-09-14 | 1d | -0.0250 | -0.0255 | -0.0006 |
| 2026-09-14 | 2d | -0.1114 | -0.1120 | -0.0006 |
| 2026-09-14 | 3d | -0.2010 | -0.1971 | +0.0039 |
| 2026-09-15 | 1d | -0.0616 | -0.0615 | +0.0001 |
| 2026-09-15 | 2d | -0.1290 | -0.1281 | +0.0010 |
| 2026-09-15 | 3d | -0.1450 | -0.1436 | +0.0014 |
| 2026-09-16 | 1d | -0.0722 | -0.0720 | +0.0002 |
| 2026-09-16 | 2d | -0.0629 | -0.0612 | +0.0016 |
| 2026-09-17 | 1d | +0.0987 | +0.1003 | +0.0016 |

_Champion reconstruction check: mean |rebuilt price category − stored price_score| = 0.2269 (should be ~0; large values mean the learner's model of the engine has drifted from score_engine — distrust this run)._

## Decision

NO PROMOTION — challenger mean IC gain +0.0010 on 1d does not clear +0.001.

_Note: curved-polarity rules (rvol/rsi/sma/short/upside/debt curves) are never auto-adjusted; change those in score_rubric.py by hand with git history as the audit trail._
