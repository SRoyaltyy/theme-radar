# Weight learning — decision log

_Generated 2026-10-06 16:57 EDT_

- label dates per horizon: 1d: 41, 2d: 40, 3d: 39
- primary horizon for promotion test: **1d** (41 dates)
- existing overrides: {'Price|ret': 0.25, 'Performance (Month)|delta': 0.8433971514371941, 'Average Volume|delta': 0.5483890822743658, 'Relative Strength Index (14)|delta': 0.25, 'Short Float|delta': 1.7252195675728095, 'Institutional Transactions|level': 1.2899479968778684, 'Institutional Ownership|delta': 1.9457500834474015, 'Insider Transactions|level': 0.8726084854014611, 'Target Price|delta': 1.2578261733879856, 'Analyst Recom|delta': 1.9558473189435233, 'Sales Growth Quarter Over Quarter|level': 2.0, 'Sales Year Over Year TTM|level': 2.0, 'Profit Margin|delta': 1.1171601499394408, 'EPS Surprise|level': 1.089559846444787, 'n_catalysts|level': 1.5332502554705358}

## Per-rule aligned IC (direction corrected for polarity)

| Rule | Horizon | Mean aligned IC | Dates | Proposed × | Testable |
|---|---|---|---|---|---|
| Price|ret | 1d | -0.0365 | 39 | 0.250 | yes |
| Price|ret | 2d | -0.0281 | 38 | 0.250 | yes |
| Price|ret | 3d | -0.0202 | 37 | 0.250 | yes |
| Performance (Month)|delta | 1d | -0.0142 | 39 | 0.819 | yes |
| Performance (Month)|delta | 2d | -0.0184 | 38 | 0.812 | yes |
| Performance (Month)|delta | 3d | -0.0295 | 37 | 0.794 | yes |
| Average Volume|delta | 1d | -0.0137 | 39 | 0.533 | NO — logs only |
| Average Volume|delta | 2d | -0.0180 | 38 | 0.529 | NO — logs only |
| Average Volume|delta | 3d | -0.0192 | 37 | 0.527 | NO — logs only |
| Relative Strength Index (14)|delta | 1d | -0.0340 | 39 | 0.250 | yes |
| Relative Strength Index (14)|delta | 2d | -0.0338 | 38 | 0.250 | yes |
| Relative Strength Index (14)|delta | 3d | -0.0286 | 37 | 0.250 | yes |
| Short Float|delta | 1d | -0.0033 | 37 | 1.714 | NO — logs only |
| Short Float|delta | 2d | -0.0064 | 36 | 1.703 | NO — logs only |
| Short Float|delta | 3d | -0.0078 | 35 | 1.698 | NO — logs only |
| Institutional Transactions|level | 1d | -0.0103 | 41 | 1.263 | NO — logs only |
| Institutional Transactions|level | 2d | -0.0137 | 40 | 1.255 | NO — logs only |
| Institutional Transactions|level | 3d | -0.0154 | 39 | 1.250 | NO — logs only |
| Institutional Ownership|delta | 1d | +0.0013 | 39 | 1.951 | NO — logs only |
| Institutional Ownership|delta | 2d | +0.0069 | 38 | 1.973 | NO — logs only |
| Institutional Ownership|delta | 3d | +0.0041 | 37 | 1.962 | NO — logs only |
| Insider Transactions|level | 1d | -0.0179 | 41 | 0.841 | NO — logs only |
| Insider Transactions|level | 2d | -0.0230 | 40 | 0.833 | NO — logs only |
| Insider Transactions|level | 3d | -0.0253 | 39 | 0.828 | NO — logs only |
| Target Price|delta | 1d | +0.0056 | 39 | 1.272 | NO — logs only |
| Target Price|delta | 2d | +0.0054 | 38 | 1.271 | NO — logs only |
| Target Price|delta | 3d | +0.0054 | 37 | 1.271 | NO — logs only |
| Analyst Recom|delta | 1d | +0.0060 | 39 | 1.979 | NO — logs only |
| Analyst Recom|delta | 2d | -0.0010 | 38 | 1.952 | NO — logs only |
| Analyst Recom|delta | 3d | -0.0020 | 37 | 1.948 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 1d | +0.0237 | 41 | 2.000 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 2d | +0.0282 | 40 | 2.000 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 3d | +0.0320 | 39 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 1d | +0.0201 | 41 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 2d | +0.0252 | 40 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 3d | +0.0278 | 39 | 2.000 | NO — logs only |
| Profit Margin|delta | 1d | +0.0069 | 39 | 1.133 | NO — logs only |
| Profit Margin|delta | 2d | +0.0042 | 38 | 1.126 | NO — logs only |
| Profit Margin|delta | 3d | +0.0045 | 37 | 1.127 | NO — logs only |
| EPS Surprise|level | 1d | +0.0234 | 41 | 1.141 | NO — logs only |
| EPS Surprise|level | 2d | +0.0329 | 40 | 1.161 | NO — logs only |
| EPS Surprise|level | 3d | +0.0383 | 39 | 1.173 | NO — logs only |
| n_catalysts|level | 1d | -0.0049 | 41 | 1.518 | yes |
| n_catalysts|level | 2d | -0.0106 | 40 | 1.501 | yes |
| n_catalysts|level | 3d | -0.0143 | 39 | 1.489 | yes |
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
| 2026-08-07 | 1d | -0.0339 | -0.0277 | +0.0062 |
| 2026-08-07 | 2d | -0.0242 | -0.0202 | +0.0039 |
| 2026-08-07 | 3d | -0.0009 | +0.0026 | +0.0035 |
| 2026-08-10 | 1d | -0.0491 | -0.0296 | +0.0195 |
| 2026-08-10 | 2d | -0.0596 | -0.0347 | +0.0249 |
| 2026-08-10 | 3d | -0.1054 | -0.0898 | +0.0156 |
| 2026-08-11 | 1d | +0.1007 | +0.1004 | -0.0004 |
| 2026-08-11 | 2d | +0.0174 | +0.0080 | -0.0094 |
| 2026-08-11 | 3d | +0.0639 | +0.0569 | -0.0069 |
| 2026-08-12 | 1d | -0.0472 | -0.0466 | +0.0006 |
| 2026-08-12 | 2d | +0.0520 | +0.0528 | +0.0008 |
| 2026-08-12 | 3d | +0.0878 | +0.0823 | -0.0054 |
| 2026-08-13 | 1d | -0.0908 | -0.0844 | +0.0064 |
| 2026-08-13 | 2d | -0.1428 | -0.1355 | +0.0072 |
| 2026-08-13 | 3d | -0.1672 | -0.1622 | +0.0050 |
| 2026-08-14 | 1d | +0.1577 | +0.1401 | -0.0176 |
| 2026-08-14 | 2d | -0.1560 | -0.1563 | -0.0003 |
| 2026-08-14 | 3d | -0.1404 | -0.1412 | -0.0008 |
| 2026-08-17 | 1d | -0.2097 | -0.2058 | +0.0039 |
| 2026-08-17 | 2d | -0.1365 | -0.1351 | +0.0014 |
| 2026-08-17 | 3d | -0.1034 | -0.1042 | -0.0009 |
| 2026-08-18 | 1d | +0.0486 | +0.0456 | -0.0030 |
| 2026-08-18 | 2d | +0.0270 | +0.0227 | -0.0043 |
| 2026-08-18 | 3d | +0.0058 | +0.0073 | +0.0015 |
| 2026-08-19 | 1d | +0.0108 | +0.0025 | -0.0083 |
| 2026-08-19 | 2d | +0.0519 | +0.0546 | +0.0027 |
| 2026-08-19 | 3d | +0.1772 | +0.1665 | -0.0107 |
| 2026-08-20 | 1d | -0.0007 | +0.0062 | +0.0068 |
| 2026-08-20 | 2d | +0.0530 | +0.0572 | +0.0043 |
| 2026-08-20 | 3d | +0.0387 | +0.0471 | +0.0084 |
| 2026-08-21 | 1d | -0.0802 | -0.0811 | -0.0009 |
| 2026-08-21 | 2d | +0.0158 | +0.0128 | -0.0030 |
| 2026-08-21 | 3d | -0.0723 | -0.0728 | -0.0005 |
| 2026-08-24 | 1d | +0.0056 | -0.0162 | -0.0219 |
| 2026-08-24 | 2d | -0.0285 | -0.0517 | -0.0232 |
| 2026-08-24 | 3d | -0.0880 | -0.0843 | +0.0037 |
| 2026-08-25 | 1d | -0.0503 | -0.0707 | -0.0203 |
| 2026-08-25 | 2d | -0.1093 | -0.1166 | -0.0073 |
| 2026-08-25 | 3d | -0.0661 | -0.0784 | -0.0123 |
| 2026-08-26 | 1d | -0.0710 | -0.0537 | +0.0173 |
| 2026-08-26 | 2d | -0.0146 | -0.0105 | +0.0041 |
| 2026-08-26 | 3d | -0.0019 | +0.0098 | +0.0117 |
| 2026-08-28 | 1d | -0.0442 | -0.0334 | +0.0108 |
| 2026-08-28 | 2d | +0.0258 | +0.0240 | -0.0018 |
| 2026-08-28 | 3d | +0.0108 | +0.0227 | +0.0119 |
| 2026-08-31 | 1d | -0.0065 | -0.0059 | +0.0006 |
| 2026-08-31 | 2d | +0.0398 | +0.0434 | +0.0037 |
| 2026-08-31 | 3d | +0.1004 | +0.1055 | +0.0051 |
| 2026-09-01 | 1d | -0.0847 | -0.0501 | +0.0347 |
| 2026-09-01 | 2d | -0.2394 | -0.1911 | +0.0483 |
| 2026-09-01 | 3d | -0.2756 | -0.2330 | +0.0425 |
| 2026-09-02 | 1d | -0.0842 | -0.0536 | +0.0306 |
| 2026-09-02 | 2d | -0.1304 | -0.0949 | +0.0356 |
| 2026-09-02 | 3d | -0.1700 | -0.1475 | +0.0225 |
| 2026-09-03 | 1d | -0.0656 | -0.0874 | -0.0217 |
| 2026-09-03 | 2d | -0.0607 | -0.0899 | -0.0292 |
| 2026-09-03 | 3d | -0.1049 | -0.1260 | -0.0211 |
| 2026-09-04 | 1d | -0.0292 | -0.0351 | -0.0059 |
| 2026-09-04 | 2d | -0.0659 | -0.0709 | -0.0050 |
| 2026-09-04 | 3d | -0.1272 | -0.1304 | -0.0032 |
| 2026-09-08 | 1d | -0.0849 | -0.0849 | +0.0000 |
| 2026-09-08 | 2d | -0.1276 | -0.1276 | +0.0000 |
| 2026-09-08 | 3d | -0.0619 | -0.0619 | +0.0000 |
| 2026-09-09 | 1d | -0.0163 | -0.0216 | -0.0054 |
| 2026-09-09 | 2d | +0.0188 | +0.0139 | -0.0050 |
| 2026-09-09 | 3d | -0.0591 | -0.0598 | -0.0006 |
| 2026-09-10 | 1d | -0.0932 | -0.0882 | +0.0049 |
| 2026-09-10 | 2d | +0.1308 | +0.1180 | -0.0128 |
| 2026-09-10 | 3d | +0.1827 | +0.1698 | -0.0128 |
| 2026-09-11 | 1d | -0.0419 | -0.0508 | -0.0089 |
| 2026-09-11 | 2d | -0.0676 | -0.0759 | -0.0083 |
| 2026-09-11 | 3d | -0.1072 | -0.1130 | -0.0058 |
| 2026-09-14 | 1d | -0.0250 | -0.0257 | -0.0007 |
| 2026-09-14 | 2d | -0.1114 | -0.1120 | -0.0007 |
| 2026-09-14 | 3d | -0.2010 | -0.1973 | +0.0038 |
| 2026-09-15 | 1d | -0.0616 | -0.0615 | +0.0001 |
| 2026-09-15 | 2d | -0.1290 | -0.1280 | +0.0010 |
| 2026-09-15 | 3d | -0.1450 | -0.1435 | +0.0015 |
| 2026-09-16 | 1d | -0.0722 | -0.0719 | +0.0003 |
| 2026-09-16 | 2d | -0.0629 | -0.0611 | +0.0018 |
| 2026-09-16 | 3d | -0.0266 | -0.0255 | +0.0011 |
| 2026-09-17 | 1d | +0.0987 | +0.1003 | +0.0016 |
| 2026-09-17 | 2d | +0.2454 | +0.2451 | -0.0003 |
| 2026-09-17 | 3d | +0.3070 | +0.3064 | -0.0006 |
| 2026-09-18 | 1d | +0.0668 | +0.0677 | +0.0009 |
| 2026-09-18 | 2d | +0.0651 | +0.0670 | +0.0018 |
| 2026-09-18 | 3d | +0.1188 | +0.1188 | -0.0000 |
| 2026-09-21 | 1d | +0.1709 | +0.1712 | +0.0004 |
| 2026-09-21 | 2d | -0.0452 | -0.0441 | +0.0011 |
| 2026-09-21 | 3d | -0.0110 | -0.0091 | +0.0020 |
| 2026-09-22 | 1d | -0.1323 | -0.1333 | -0.0010 |
| 2026-09-22 | 2d | -0.1167 | -0.1169 | -0.0002 |
| 2026-09-22 | 3d | -0.0566 | -0.0574 | -0.0008 |
| 2026-09-23 | 1d | +0.0928 | +0.0940 | +0.0013 |
| 2026-09-23 | 2d | +0.0398 | +0.0420 | +0.0022 |
| 2026-09-23 | 3d | +0.0444 | +0.0467 | +0.0023 |
| 2026-09-24 | 1d | -0.0345 | -0.0330 | +0.0015 |
| 2026-09-24 | 2d | +0.0435 | +0.0432 | -0.0003 |
| 2026-09-24 | 3d | +0.0182 | +0.0190 | +0.0008 |
| 2026-09-25 | 1d | -0.1114 | -0.1097 | +0.0016 |
| 2026-09-25 | 2d | -0.0598 | -0.0579 | +0.0019 |
| 2026-09-25 | 3d | -0.0952 | -0.0929 | +0.0023 |
| 2026-09-28 | 1d | -0.0477 | -0.0459 | +0.0017 |
| 2026-09-28 | 2d | -0.0469 | -0.0443 | +0.0026 |
| 2026-09-28 | 3d | -0.0752 | -0.0721 | +0.0031 |
| 2026-09-29 | 1d | -0.0367 | -0.0355 | +0.0012 |
| 2026-09-29 | 2d | +0.0392 | +0.0404 | +0.0012 |
| 2026-09-29 | 3d | +0.0858 | +0.0876 | +0.0018 |
| 2026-09-30 | 1d | +0.0026 | +0.0040 | +0.0014 |
| 2026-09-30 | 2d | +0.0403 | +0.0420 | +0.0017 |
| 2026-09-30 | 3d | +0.0472 | +0.0501 | +0.0029 |
| 2026-10-01 | 1d | +0.0950 | +0.0953 | +0.0003 |
| 2026-10-01 | 2d | +0.1090 | +0.1098 | +0.0008 |
| 2026-10-01 | 3d | +0.1116 | +0.1127 | +0.0011 |
| 2026-10-02 | 1d | +0.0316 | +0.0327 | +0.0012 |
| 2026-10-02 | 2d | +0.0757 | +0.0763 | +0.0005 |
| 2026-10-05 | 1d | -0.1002 | -0.0996 | +0.0006 |

_Champion reconstruction check: mean |rebuilt price category − stored price_score| = 0.1663 (should be ~0; large values mean the learner's model of the engine has drifted from score_engine — distrust this run)._

## Decision

NO PROMOTION — challenger mean IC gain +0.0010 on 1d does not clear +0.001.

_Note: curved-polarity rules (rvol/rsi/sma/short/upside/debt curves) are never auto-adjusted; change those in score_rubric.py by hand with git history as the audit trail._
