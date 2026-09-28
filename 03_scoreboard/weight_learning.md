# Weight learning — decision log

_Generated 2026-09-28 16:45 EDT_

- label dates per horizon: 1d: 35, 2d: 34, 3d: 33
- primary horizon for promotion test: **1d** (35 dates)
- existing overrides: {'Price|ret': 0.25, 'Performance (Month)|delta': 0.8433971514371941, 'Average Volume|delta': 0.5483890822743658, 'Relative Strength Index (14)|delta': 0.25, 'Short Float|delta': 1.7252195675728095, 'Institutional Transactions|level': 1.2899479968778684, 'Institutional Ownership|delta': 1.9457500834474015, 'Insider Transactions|level': 0.8726084854014611, 'Target Price|delta': 1.2578261733879856, 'Analyst Recom|delta': 1.9558473189435233, 'Sales Growth Quarter Over Quarter|level': 2.0, 'Sales Year Over Year TTM|level': 2.0, 'Profit Margin|delta': 1.1171601499394408, 'EPS Surprise|level': 1.089559846444787, 'n_catalysts|level': 1.5332502554705358}

## Per-rule aligned IC (direction corrected for polarity)

| Rule | Horizon | Mean aligned IC | Dates | Proposed × | Testable |
|---|---|---|---|---|---|
| Price|ret | 1d | -0.0395 | 33 | 0.250 | yes |
| Price|ret | 2d | -0.0368 | 32 | 0.250 | yes |
| Price|ret | 3d | -0.0235 | 31 | 0.250 | yes |
| Performance (Month)|delta | 1d | -0.0088 | 33 | 0.828 | yes |
| Performance (Month)|delta | 2d | -0.0198 | 32 | 0.810 | yes |
| Performance (Month)|delta | 3d | -0.0293 | 31 | 0.794 | yes |
| Average Volume|delta | 1d | -0.0122 | 33 | 0.535 | NO — logs only |
| Average Volume|delta | 2d | -0.0160 | 32 | 0.531 | NO — logs only |
| Average Volume|delta | 3d | -0.0164 | 31 | 0.530 | NO — logs only |
| Relative Strength Index (14)|delta | 1d | -0.0352 | 33 | 0.250 | yes |
| Relative Strength Index (14)|delta | 2d | -0.0403 | 32 | 0.250 | yes |
| Relative Strength Index (14)|delta | 3d | -0.0287 | 31 | 0.250 | yes |
| Short Float|delta | 1d | -0.0031 | 31 | 1.714 | NO — logs only |
| Short Float|delta | 2d | -0.0066 | 31 | 1.702 | NO — logs only |
| Short Float|delta | 3d | -0.0082 | 30 | 1.697 | NO — logs only |
| Institutional Transactions|level | 1d | -0.0068 | 35 | 1.272 | NO — logs only |
| Institutional Transactions|level | 2d | -0.0089 | 34 | 1.267 | NO — logs only |
| Institutional Transactions|level | 3d | -0.0095 | 33 | 1.265 | NO — logs only |
| Institutional Ownership|delta | 1d | -0.0001 | 33 | 1.945 | NO — logs only |
| Institutional Ownership|delta | 2d | +0.0043 | 32 | 1.962 | NO — logs only |
| Institutional Ownership|delta | 3d | +0.0017 | 31 | 1.952 | NO — logs only |
| Insider Transactions|level | 1d | -0.0111 | 35 | 0.853 | NO — logs only |
| Insider Transactions|level | 2d | -0.0115 | 34 | 0.853 | NO — logs only |
| Insider Transactions|level | 3d | -0.0107 | 33 | 0.854 | NO — logs only |
| Target Price|delta | 1d | +0.0091 | 33 | 1.281 | NO — logs only |
| Target Price|delta | 2d | +0.0055 | 32 | 1.272 | NO — logs only |
| Target Price|delta | 3d | +0.0057 | 31 | 1.272 | NO — logs only |
| Analyst Recom|delta | 1d | +0.0075 | 33 | 1.985 | NO — logs only |
| Analyst Recom|delta | 2d | +0.0001 | 32 | 1.956 | NO — logs only |
| Analyst Recom|delta | 3d | -0.0011 | 31 | 1.951 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 1d | +0.0186 | 35 | 2.000 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 2d | +0.0226 | 34 | 2.000 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 3d | +0.0266 | 33 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 1d | +0.0152 | 35 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 2d | +0.0206 | 34 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 3d | +0.0243 | 33 | 2.000 | NO — logs only |
| Profit Margin|delta | 1d | +0.0065 | 33 | 1.132 | NO — logs only |
| Profit Margin|delta | 2d | +0.0035 | 32 | 1.125 | NO — logs only |
| Profit Margin|delta | 3d | +0.0053 | 31 | 1.129 | NO — logs only |
| EPS Surprise|level | 1d | +0.0184 | 35 | 1.130 | NO — logs only |
| EPS Surprise|level | 2d | +0.0232 | 34 | 1.140 | NO — logs only |
| EPS Surprise|level | 3d | +0.0253 | 33 | 1.145 | NO — logs only |
| n_catalysts|level | 1d | -0.0079 | 35 | 1.509 | yes |
| n_catalysts|level | 2d | -0.0125 | 34 | 1.495 | yes |
| n_catalysts|level | 3d | -0.0157 | 33 | 1.485 | yes |
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
| 2026-08-11 | 3d | +0.0639 | +0.0571 | -0.0067 |
| 2026-08-12 | 1d | -0.0472 | -0.0466 | +0.0006 |
| 2026-08-12 | 2d | +0.0520 | +0.0528 | +0.0008 |
| 2026-08-12 | 3d | +0.0878 | +0.0818 | -0.0060 |
| 2026-08-13 | 1d | -0.0908 | -0.0864 | +0.0044 |
| 2026-08-13 | 2d | -0.1428 | -0.1378 | +0.0050 |
| 2026-08-13 | 3d | -0.1672 | -0.1634 | +0.0037 |
| 2026-08-14 | 1d | +0.1577 | +0.1420 | -0.0157 |
| 2026-08-14 | 2d | -0.1560 | -0.1569 | -0.0009 |
| 2026-08-14 | 3d | -0.1404 | -0.1412 | -0.0008 |
| 2026-08-17 | 1d | -0.2097 | -0.2058 | +0.0040 |
| 2026-08-17 | 2d | -0.1365 | -0.1351 | +0.0014 |
| 2026-08-17 | 3d | -0.1034 | -0.1042 | -0.0008 |
| 2026-08-18 | 1d | +0.0486 | +0.0457 | -0.0029 |
| 2026-08-18 | 2d | +0.0270 | +0.0231 | -0.0039 |
| 2026-08-18 | 3d | +0.0058 | +0.0074 | +0.0016 |
| 2026-08-19 | 1d | +0.0108 | +0.0025 | -0.0082 |
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
| 2026-08-31 | 1d | -0.0065 | -0.0055 | +0.0011 |
| 2026-08-31 | 2d | +0.0398 | +0.0438 | +0.0040 |
| 2026-08-31 | 3d | +0.1004 | +0.1058 | +0.0054 |
| 2026-09-01 | 1d | -0.0847 | -0.0504 | +0.0343 |
| 2026-09-01 | 2d | -0.2394 | -0.1917 | +0.0478 |
| 2026-09-01 | 3d | -0.2756 | -0.2337 | +0.0419 |
| 2026-09-02 | 1d | -0.0842 | -0.0537 | +0.0305 |
| 2026-09-02 | 2d | -0.1304 | -0.0950 | +0.0354 |
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
| 2026-09-10 | 3d | +0.1827 | +0.1702 | -0.0124 |
| 2026-09-11 | 1d | -0.0419 | -0.0504 | -0.0085 |
| 2026-09-11 | 2d | -0.0676 | -0.0757 | -0.0082 |
| 2026-09-11 | 3d | -0.1072 | -0.1129 | -0.0057 |
| 2026-09-14 | 1d | -0.0250 | -0.0257 | -0.0007 |
| 2026-09-14 | 2d | -0.1114 | -0.1121 | -0.0007 |
| 2026-09-14 | 3d | -0.2010 | -0.1974 | +0.0037 |
| 2026-09-15 | 1d | -0.0616 | -0.0615 | +0.0001 |
| 2026-09-15 | 2d | -0.1290 | -0.1281 | +0.0009 |
| 2026-09-15 | 3d | -0.1450 | -0.1436 | +0.0014 |
| 2026-09-16 | 1d | -0.0722 | -0.0720 | +0.0002 |
| 2026-09-16 | 2d | -0.0629 | -0.0612 | +0.0016 |
| 2026-09-16 | 3d | -0.0266 | -0.0257 | +0.0008 |
| 2026-09-17 | 1d | +0.0987 | +0.1003 | +0.0016 |
| 2026-09-17 | 2d | +0.2454 | +0.2452 | -0.0003 |
| 2026-09-17 | 3d | +0.3070 | +0.3065 | -0.0005 |
| 2026-09-18 | 1d | +0.0668 | +0.0677 | +0.0009 |
| 2026-09-18 | 2d | +0.0651 | +0.0669 | +0.0018 |
| 2026-09-18 | 3d | +0.1188 | +0.1189 | +0.0000 |
| 2026-09-21 | 1d | +0.1709 | +0.1712 | +0.0004 |
| 2026-09-21 | 2d | -0.0452 | -0.0442 | +0.0010 |
| 2026-09-21 | 3d | -0.0110 | -0.0091 | +0.0020 |
| 2026-09-22 | 1d | -0.1323 | -0.1333 | -0.0010 |
| 2026-09-22 | 2d | -0.1167 | -0.1169 | -0.0002 |
| 2026-09-22 | 3d | -0.0566 | -0.0574 | -0.0008 |
| 2026-09-23 | 1d | +0.0928 | +0.0942 | +0.0014 |
| 2026-09-23 | 2d | +0.0398 | +0.0419 | +0.0021 |
| 2026-09-23 | 3d | +0.0444 | +0.0467 | +0.0022 |
| 2026-09-24 | 1d | -0.0345 | -0.0331 | +0.0014 |
| 2026-09-24 | 2d | +0.0435 | +0.0433 | -0.0001 |
| 2026-09-25 | 1d | -0.1114 | -0.1097 | +0.0017 |

_Champion reconstruction check: mean |rebuilt price category − stored price_score| = 0.1941 (should be ~0; large values mean the learner's model of the engine has drifted from score_engine — distrust this run)._

## Decision

NO PROMOTION — challenger mean IC gain +0.0009 on 1d does not clear +0.001.

_Note: curved-polarity rules (rvol/rsi/sma/short/upside/debt curves) are never auto-adjusted; change those in score_rubric.py by hand with git history as the audit trail._
