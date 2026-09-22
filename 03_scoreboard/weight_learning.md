# Weight learning — decision log

_Generated 2026-09-22 16:46 EDT_

- label dates per horizon: 1d: 31, 2d: 30, 3d: 29
- primary horizon for promotion test: **1d** (31 dates)
- existing overrides: {'Price|ret': 0.25, 'Performance (Month)|delta': 0.8543745509856159, 'Average Volume|delta': 0.5610453165124469, 'Relative Strength Index (14)|delta': 0.25, 'Short Float|delta': 1.7360810947250618, 'Institutional Transactions|level': 1.2988047200755224, 'Institutional Ownership|delta': 1.9355228692156583, 'Insider Transactions|level': 0.8833298212974705, 'Target Price|delta': 1.2395145161914445, 'Analyst Recom|delta': 1.9243962218243638, 'Sales Growth Quarter Over Quarter|level': 2.0, 'Sales Year Over Year TTM|level': 2.0, 'Profit Margin|delta': 1.1063482321861713, 'EPS Surprise|level': 1.0670641269567658, 'n_catalysts|level': 1.543458790003396}

## Per-rule aligned IC (direction corrected for polarity)

| Rule | Horizon | Mean aligned IC | Dates | Proposed × | Testable |
|---|---|---|---|---|---|
| Price|ret | 1d | -0.0362 | 29 | 0.250 | yes |
| Price|ret | 2d | -0.0341 | 28 | 0.250 | yes |
| Price|ret | 3d | -0.0305 | 27 | 0.250 | yes |
| Performance (Month)|delta | 1d | -0.0064 | 29 | 0.843 | yes |
| Performance (Month)|delta | 2d | -0.0242 | 28 | 0.813 | yes |
| Performance (Month)|delta | 3d | -0.0374 | 27 | 0.790 | yes |
| Average Volume|delta | 1d | -0.0113 | 29 | 0.548 | NO — logs only |
| Average Volume|delta | 2d | -0.0136 | 28 | 0.546 | NO — logs only |
| Average Volume|delta | 3d | -0.0135 | 27 | 0.546 | NO — logs only |
| Relative Strength Index (14)|delta | 1d | -0.0329 | 29 | 0.250 | yes |
| Relative Strength Index (14)|delta | 2d | -0.0361 | 28 | 0.250 | yes |
| Relative Strength Index (14)|delta | 3d | -0.0330 | 27 | 0.250 | yes |
| Short Float|delta | 1d | -0.0031 | 28 | 1.725 | NO — logs only |
| Short Float|delta | 2d | -0.0066 | 27 | 1.713 | NO — logs only |
| Short Float|delta | 3d | -0.0080 | 26 | 1.708 | NO — logs only |
| Institutional Transactions|level | 1d | -0.0034 | 31 | 1.290 | NO — logs only |
| Institutional Transactions|level | 2d | -0.0036 | 30 | 1.289 | NO — logs only |
| Institutional Transactions|level | 3d | -0.0047 | 29 | 1.287 | NO — logs only |
| Institutional Ownership|delta | 1d | +0.0026 | 29 | 1.946 | NO — logs only |
| Institutional Ownership|delta | 2d | +0.0048 | 28 | 1.954 | NO — logs only |
| Institutional Ownership|delta | 3d | +0.0018 | 27 | 1.942 | NO — logs only |
| Insider Transactions|level | 1d | -0.0061 | 31 | 0.873 | NO — logs only |
| Insider Transactions|level | 2d | -0.0045 | 30 | 0.875 | NO — logs only |
| Insider Transactions|level | 3d | -0.0015 | 29 | 0.881 | NO — logs only |
| Target Price|delta | 1d | +0.0074 | 29 | 1.258 | NO — logs only |
| Target Price|delta | 2d | +0.0043 | 28 | 1.250 | NO — logs only |
| Target Price|delta | 3d | +0.0030 | 27 | 1.247 | NO — logs only |
| Analyst Recom|delta | 1d | +0.0082 | 29 | 1.956 | NO — logs only |
| Analyst Recom|delta | 2d | +0.0002 | 28 | 1.925 | NO — logs only |
| Analyst Recom|delta | 3d | -0.0009 | 27 | 1.921 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 1d | +0.0197 | 31 | 2.000 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 2d | +0.0248 | 30 | 2.000 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 3d | +0.0292 | 29 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 1d | +0.0175 | 31 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 2d | +0.0242 | 30 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 3d | +0.0273 | 29 | 2.000 | NO — logs only |
| Profit Margin|delta | 1d | +0.0049 | 29 | 1.117 | NO — logs only |
| Profit Margin|delta | 2d | +0.0035 | 28 | 1.114 | NO — logs only |
| Profit Margin|delta | 3d | +0.0067 | 27 | 1.121 | NO — logs only |
| EPS Surprise|level | 1d | +0.0105 | 31 | 1.090 | NO — logs only |
| EPS Surprise|level | 2d | +0.0138 | 30 | 1.097 | NO — logs only |
| EPS Surprise|level | 3d | +0.0157 | 29 | 1.100 | NO — logs only |
| n_catalysts|level | 1d | -0.0033 | 31 | 1.533 | yes |
| n_catalysts|level | 2d | -0.0094 | 30 | 1.515 | yes |
| n_catalysts|level | 3d | -0.0142 | 29 | 1.500 | yes |
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
| 2026-08-07 | 1d | -0.0339 | -0.0240 | +0.0099 |
| 2026-08-07 | 2d | -0.0242 | -0.0176 | +0.0065 |
| 2026-08-07 | 3d | -0.0009 | +0.0020 | +0.0029 |
| 2026-08-10 | 1d | -0.0491 | -0.0303 | +0.0188 |
| 2026-08-10 | 2d | -0.0596 | -0.0370 | +0.0226 |
| 2026-08-10 | 3d | -0.1054 | -0.0912 | +0.0142 |
| 2026-08-11 | 1d | +0.1007 | +0.1050 | +0.0042 |
| 2026-08-11 | 2d | +0.0174 | +0.0118 | -0.0055 |
| 2026-08-11 | 3d | +0.0639 | +0.0590 | -0.0049 |
| 2026-08-12 | 1d | -0.0472 | -0.0469 | +0.0004 |
| 2026-08-12 | 2d | +0.0520 | +0.0523 | +0.0003 |
| 2026-08-12 | 3d | +0.0878 | +0.0809 | -0.0068 |
| 2026-08-13 | 1d | -0.0908 | -0.0858 | +0.0050 |
| 2026-08-13 | 2d | -0.1428 | -0.1374 | +0.0053 |
| 2026-08-13 | 3d | -0.1672 | -0.1643 | +0.0029 |
| 2026-08-14 | 1d | +0.1577 | +0.1447 | -0.0130 |
| 2026-08-14 | 2d | -0.1560 | -0.1579 | -0.0020 |
| 2026-08-14 | 3d | -0.1404 | -0.1419 | -0.0016 |
| 2026-08-17 | 1d | -0.2097 | -0.2062 | +0.0036 |
| 2026-08-17 | 2d | -0.1365 | -0.1352 | +0.0013 |
| 2026-08-17 | 3d | -0.1034 | -0.1042 | -0.0008 |
| 2026-08-18 | 1d | +0.0486 | +0.0460 | -0.0026 |
| 2026-08-18 | 2d | +0.0270 | +0.0230 | -0.0040 |
| 2026-08-18 | 3d | +0.0058 | +0.0074 | +0.0016 |
| 2026-08-19 | 1d | +0.0108 | +0.0027 | -0.0081 |
| 2026-08-19 | 2d | +0.0519 | +0.0542 | +0.0024 |
| 2026-08-19 | 3d | +0.1772 | +0.1679 | -0.0093 |
| 2026-08-20 | 1d | -0.0007 | +0.0058 | +0.0065 |
| 2026-08-20 | 2d | +0.0530 | +0.0567 | +0.0037 |
| 2026-08-20 | 3d | +0.0387 | +0.0461 | +0.0073 |
| 2026-08-21 | 1d | -0.0802 | -0.0807 | -0.0004 |
| 2026-08-21 | 2d | +0.0158 | +0.0139 | -0.0019 |
| 2026-08-21 | 3d | -0.0723 | -0.0728 | -0.0005 |
| 2026-08-24 | 1d | +0.0056 | -0.0146 | -0.0203 |
| 2026-08-24 | 2d | -0.0285 | -0.0507 | -0.0222 |
| 2026-08-24 | 3d | -0.0880 | -0.0875 | +0.0005 |
| 2026-08-25 | 1d | -0.0503 | -0.0698 | -0.0195 |
| 2026-08-25 | 2d | -0.1093 | -0.1167 | -0.0074 |
| 2026-08-25 | 3d | -0.0661 | -0.0778 | -0.0117 |
| 2026-08-26 | 1d | -0.0710 | -0.0572 | +0.0138 |
| 2026-08-26 | 2d | -0.0146 | -0.0122 | +0.0024 |
| 2026-08-26 | 3d | -0.0019 | +0.0064 | +0.0084 |
| 2026-08-28 | 1d | -0.0442 | -0.0339 | +0.0103 |
| 2026-08-28 | 2d | +0.0258 | +0.0241 | -0.0017 |
| 2026-08-28 | 3d | +0.0108 | +0.0215 | +0.0107 |
| 2026-08-31 | 1d | -0.0065 | -0.0073 | -0.0008 |
| 2026-08-31 | 2d | +0.0398 | +0.0424 | +0.0026 |
| 2026-08-31 | 3d | +0.1004 | +0.1053 | +0.0050 |
| 2026-09-01 | 1d | -0.0847 | -0.0518 | +0.0329 |
| 2026-09-01 | 2d | -0.2394 | -0.1940 | +0.0454 |
| 2026-09-01 | 3d | -0.2756 | -0.2357 | +0.0399 |
| 2026-09-02 | 1d | -0.0842 | -0.0560 | +0.0282 |
| 2026-09-02 | 2d | -0.1304 | -0.0974 | +0.0331 |
| 2026-09-02 | 3d | -0.1700 | -0.1489 | +0.0210 |
| 2026-09-03 | 1d | -0.0656 | -0.0862 | -0.0206 |
| 2026-09-03 | 2d | -0.0607 | -0.0889 | -0.0281 |
| 2026-09-03 | 3d | -0.1049 | -0.1257 | -0.0208 |
| 2026-09-04 | 1d | -0.0292 | -0.0350 | -0.0058 |
| 2026-09-04 | 2d | -0.0659 | -0.0715 | -0.0055 |
| 2026-09-04 | 3d | -0.1272 | -0.1313 | -0.0041 |
| 2026-09-08 | 1d | -0.0849 | -0.0849 | +0.0000 |
| 2026-09-08 | 2d | -0.1276 | -0.1276 | +0.0000 |
| 2026-09-08 | 3d | -0.0619 | -0.0619 | +0.0000 |
| 2026-09-09 | 1d | -0.0163 | -0.0217 | -0.0055 |
| 2026-09-09 | 2d | +0.0188 | +0.0137 | -0.0051 |
| 2026-09-09 | 3d | -0.0591 | -0.0601 | -0.0009 |
| 2026-09-10 | 1d | -0.0932 | -0.0892 | +0.0040 |
| 2026-09-10 | 2d | +0.1308 | +0.1192 | -0.0116 |
| 2026-09-10 | 3d | +0.1827 | +0.1705 | -0.0122 |
| 2026-09-11 | 1d | -0.0419 | -0.0497 | -0.0078 |
| 2026-09-11 | 2d | -0.0676 | -0.0751 | -0.0075 |
| 2026-09-11 | 3d | -0.1072 | -0.1125 | -0.0053 |
| 2026-09-14 | 1d | -0.0250 | -0.0260 | -0.0010 |
| 2026-09-14 | 2d | -0.1114 | -0.1122 | -0.0008 |
| 2026-09-14 | 3d | -0.2010 | -0.1980 | +0.0030 |
| 2026-09-15 | 1d | -0.0616 | -0.0614 | +0.0002 |
| 2026-09-15 | 2d | -0.1290 | -0.1282 | +0.0008 |
| 2026-09-15 | 3d | -0.1450 | -0.1443 | +0.0007 |
| 2026-09-16 | 1d | -0.0722 | -0.0727 | -0.0005 |
| 2026-09-16 | 2d | -0.0629 | -0.0628 | +0.0001 |
| 2026-09-16 | 3d | -0.0266 | -0.0266 | +0.0000 |
| 2026-09-17 | 1d | +0.0987 | +0.0993 | +0.0006 |
| 2026-09-17 | 2d | +0.2454 | +0.2458 | +0.0004 |
| 2026-09-17 | 3d | +0.3070 | +0.3076 | +0.0006 |
| 2026-09-18 | 1d | +0.0668 | +0.0669 | +0.0001 |
| 2026-09-18 | 2d | +0.0651 | +0.0652 | +0.0001 |
| 2026-09-21 | 1d | +0.1709 | +0.1715 | +0.0006 |

_Champion reconstruction check: mean |rebuilt price category − stored price_score| = 0.2124 (should be ~0; large values mean the learner's model of the engine has drifted from score_engine — distrust this run)._

## Decision

PROMOTED — challenger mean IC gain +0.0011 on 1d, improved on 55% of 31 dates. New multipliers: Performance (Month)|delta ×0.843, Average Volume|delta ×0.548, Short Float|delta ×1.725, Institutional Transactions|level ×1.290, Institutional Ownership|delta ×1.946, Insider Transactions|level ×0.873, Target Price|delta ×1.258, Analyst Recom|delta ×1.956, Profit Margin|delta ×1.117, EPS Surprise|level ×1.090, n_catalysts|level ×1.533

_Note: curved-polarity rules (rvol/rsi/sma/short/upside/debt curves) are never auto-adjusted; change those in score_rubric.py by hand with git history as the audit trail._
