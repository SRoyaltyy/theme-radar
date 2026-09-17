# Weight learning — decision log

_Generated 2026-09-17 16:40 EDT_

- label dates per horizon: 1d: 28, 2d: 27, 3d: 26
- primary horizon for promotion test: **1d** (28 dates)
- existing overrides: {'Price|ret': 0.25, 'Performance (Month)|delta': 0.8543745509856159, 'Average Volume|delta': 0.5610453165124469, 'Relative Strength Index (14)|delta': 0.25, 'Short Float|delta': 1.7360810947250618, 'Institutional Transactions|level': 1.2988047200755224, 'Institutional Ownership|delta': 1.9355228692156583, 'Insider Transactions|level': 0.8833298212974705, 'Target Price|delta': 1.2395145161914445, 'Analyst Recom|delta': 1.9243962218243638, 'Sales Growth Quarter Over Quarter|level': 2.0, 'Sales Year Over Year TTM|level': 2.0, 'Profit Margin|delta': 1.1063482321861713, 'EPS Surprise|level': 1.0670641269567658, 'n_catalysts|level': 1.543458790003396}

## Per-rule aligned IC (direction corrected for polarity)

| Rule | Horizon | Mean aligned IC | Dates | Proposed × | Testable |
|---|---|---|---|---|---|
| Price|ret | 1d | -0.0500 | 26 | 0.250 | yes |
| Price|ret | 2d | -0.0530 | 25 | 0.250 | yes |
| Price|ret | 3d | -0.0452 | 24 | 0.250 | yes |
| Performance (Month)|delta | 1d | -0.0190 | 26 | 0.822 | yes |
| Performance (Month)|delta | 2d | -0.0316 | 25 | 0.800 | yes |
| Performance (Month)|delta | 3d | -0.0494 | 24 | 0.770 | yes |
| Average Volume|delta | 1d | -0.0086 | 26 | 0.551 | NO — logs only |
| Average Volume|delta | 2d | -0.0064 | 25 | 0.554 | NO — logs only |
| Average Volume|delta | 3d | -0.0069 | 24 | 0.553 | NO — logs only |
| Relative Strength Index (14)|delta | 1d | -0.0442 | 26 | 0.250 | yes |
| Relative Strength Index (14)|delta | 2d | -0.0552 | 25 | 0.250 | yes |
| Relative Strength Index (14)|delta | 3d | -0.0448 | 24 | 0.250 | yes |
| Short Float|delta | 1d | -0.0010 | 25 | 1.733 | NO — logs only |
| Short Float|delta | 2d | -0.0058 | 24 | 1.716 | NO — logs only |
| Short Float|delta | 3d | -0.0097 | 23 | 1.702 | NO — logs only |
| Institutional Transactions|level | 1d | -0.0056 | 28 | 1.284 | NO — logs only |
| Institutional Transactions|level | 2d | -0.0074 | 27 | 1.280 | NO — logs only |
| Institutional Transactions|level | 3d | -0.0100 | 26 | 1.273 | NO — logs only |
| Institutional Ownership|delta | 1d | +0.0020 | 26 | 1.943 | NO — logs only |
| Institutional Ownership|delta | 2d | +0.0058 | 25 | 1.958 | NO — logs only |
| Institutional Ownership|delta | 3d | +0.0018 | 24 | 1.942 | NO — logs only |
| Insider Transactions|level | 1d | -0.0043 | 28 | 0.876 | NO — logs only |
| Insider Transactions|level | 2d | -0.0018 | 27 | 0.880 | NO — logs only |
| Insider Transactions|level | 3d | -0.0003 | 26 | 0.883 | NO — logs only |
| Target Price|delta | 1d | +0.0057 | 26 | 1.254 | NO — logs only |
| Target Price|delta | 2d | +0.0040 | 25 | 1.249 | NO — logs only |
| Target Price|delta | 3d | +0.0045 | 24 | 1.251 | NO — logs only |
| Analyst Recom|delta | 1d | +0.0082 | 26 | 1.956 | NO — logs only |
| Analyst Recom|delta | 2d | -0.0013 | 25 | 1.919 | NO — logs only |
| Analyst Recom|delta | 3d | -0.0027 | 24 | 1.914 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 1d | +0.0188 | 28 | 2.000 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 2d | +0.0206 | 27 | 2.000 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 3d | +0.0233 | 26 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 1d | +0.0151 | 28 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 2d | +0.0184 | 27 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 3d | +0.0195 | 26 | 2.000 | NO — logs only |
| Profit Margin|delta | 1d | +0.0074 | 26 | 1.123 | NO — logs only |
| Profit Margin|delta | 2d | +0.0032 | 25 | 1.113 | NO — logs only |
| Profit Margin|delta | 3d | +0.0075 | 24 | 1.123 | NO — logs only |
| EPS Surprise|level | 1d | +0.0111 | 28 | 1.091 | NO — logs only |
| EPS Surprise|level | 2d | +0.0151 | 27 | 1.099 | NO — logs only |
| EPS Surprise|level | 3d | +0.0166 | 26 | 1.103 | NO — logs only |
| n_catalysts|level | 1d | -0.0077 | 28 | 1.520 | yes |
| n_catalysts|level | 2d | -0.0173 | 27 | 1.490 | yes |
| n_catalysts|level | 3d | -0.0234 | 26 | 1.471 | yes |
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
| 2026-08-07 | 3d | -0.0009 | +0.0025 | +0.0035 |
| 2026-08-10 | 1d | -0.0491 | -0.0296 | +0.0195 |
| 2026-08-10 | 2d | -0.0596 | -0.0347 | +0.0249 |
| 2026-08-10 | 3d | -0.1054 | -0.0898 | +0.0156 |
| 2026-08-11 | 1d | +0.1007 | +0.1004 | -0.0004 |
| 2026-08-11 | 2d | +0.0174 | +0.0080 | -0.0094 |
| 2026-08-11 | 3d | +0.0639 | +0.0569 | -0.0069 |
| 2026-08-12 | 1d | -0.0472 | -0.0467 | +0.0005 |
| 2026-08-12 | 2d | +0.0520 | +0.0526 | +0.0007 |
| 2026-08-12 | 3d | +0.0878 | +0.0822 | -0.0056 |
| 2026-08-13 | 1d | -0.0908 | -0.0849 | +0.0059 |
| 2026-08-13 | 2d | -0.1428 | -0.1360 | +0.0068 |
| 2026-08-13 | 3d | -0.1672 | -0.1623 | +0.0048 |
| 2026-08-14 | 1d | +0.1577 | +0.1403 | -0.0174 |
| 2026-08-14 | 2d | -0.1560 | -0.1567 | -0.0008 |
| 2026-08-14 | 3d | -0.1404 | -0.1413 | -0.0009 |
| 2026-08-17 | 1d | -0.2097 | -0.2058 | +0.0039 |
| 2026-08-17 | 2d | -0.1365 | -0.1351 | +0.0014 |
| 2026-08-17 | 3d | -0.1034 | -0.1042 | -0.0008 |
| 2026-08-18 | 1d | +0.0486 | +0.0456 | -0.0030 |
| 2026-08-18 | 2d | +0.0270 | +0.0228 | -0.0043 |
| 2026-08-18 | 3d | +0.0058 | +0.0073 | +0.0015 |
| 2026-08-19 | 1d | +0.0108 | +0.0025 | -0.0083 |
| 2026-08-19 | 2d | +0.0519 | +0.0546 | +0.0027 |
| 2026-08-19 | 3d | +0.1772 | +0.1666 | -0.0106 |
| 2026-08-20 | 1d | -0.0007 | +0.0062 | +0.0069 |
| 2026-08-20 | 2d | +0.0530 | +0.0572 | +0.0043 |
| 2026-08-20 | 3d | +0.0387 | +0.0471 | +0.0084 |
| 2026-08-21 | 1d | -0.0802 | -0.0810 | -0.0008 |
| 2026-08-21 | 2d | +0.0158 | +0.0129 | -0.0030 |
| 2026-08-21 | 3d | -0.0723 | -0.0728 | -0.0005 |
| 2026-08-24 | 1d | +0.0056 | -0.0162 | -0.0218 |
| 2026-08-24 | 2d | -0.0285 | -0.0516 | -0.0232 |
| 2026-08-24 | 3d | -0.0880 | -0.0843 | +0.0038 |
| 2026-08-25 | 1d | -0.0503 | -0.0707 | -0.0203 |
| 2026-08-25 | 2d | -0.1093 | -0.1166 | -0.0073 |
| 2026-08-25 | 3d | -0.0661 | -0.0784 | -0.0123 |
| 2026-08-26 | 1d | -0.0710 | -0.0537 | +0.0173 |
| 2026-08-26 | 2d | -0.0146 | -0.0105 | +0.0041 |
| 2026-08-26 | 3d | -0.0019 | +0.0098 | +0.0118 |
| 2026-08-28 | 1d | -0.0442 | -0.0335 | +0.0108 |
| 2026-08-28 | 2d | +0.0258 | +0.0241 | -0.0018 |
| 2026-08-28 | 3d | +0.0108 | +0.0228 | +0.0120 |
| 2026-08-31 | 1d | -0.0065 | -0.0059 | +0.0006 |
| 2026-08-31 | 2d | +0.0398 | +0.0434 | +0.0037 |
| 2026-08-31 | 3d | +0.1004 | +0.1055 | +0.0051 |
| 2026-09-01 | 1d | -0.0847 | -0.0504 | +0.0344 |
| 2026-09-01 | 2d | -0.2394 | -0.1916 | +0.0479 |
| 2026-09-01 | 3d | -0.2756 | -0.2336 | +0.0420 |
| 2026-09-02 | 1d | -0.0842 | -0.0537 | +0.0306 |
| 2026-09-02 | 2d | -0.1304 | -0.0949 | +0.0355 |
| 2026-09-02 | 3d | -0.1700 | -0.1476 | +0.0224 |
| 2026-09-03 | 1d | -0.0656 | -0.0874 | -0.0217 |
| 2026-09-03 | 2d | -0.0607 | -0.0899 | -0.0292 |
| 2026-09-03 | 3d | -0.1049 | -0.1260 | -0.0211 |
| 2026-09-04 | 1d | -0.0292 | -0.0353 | -0.0061 |
| 2026-09-04 | 2d | -0.0659 | -0.0709 | -0.0049 |
| 2026-09-04 | 3d | -0.1272 | -0.1303 | -0.0031 |
| 2026-09-08 | 1d | -0.0849 | -0.0849 | +0.0000 |
| 2026-09-08 | 2d | -0.1276 | -0.1276 | +0.0000 |
| 2026-09-08 | 3d | -0.0619 | -0.0619 | +0.0000 |
| 2026-09-09 | 1d | -0.0163 | -0.0216 | -0.0054 |
| 2026-09-09 | 2d | +0.0188 | +0.0139 | -0.0049 |
| 2026-09-09 | 3d | -0.0591 | -0.0598 | -0.0006 |
| 2026-09-10 | 1d | -0.0932 | -0.0885 | +0.0047 |
| 2026-09-10 | 2d | +0.1308 | +0.1180 | -0.0127 |
| 2026-09-10 | 3d | +0.1827 | +0.1699 | -0.0127 |
| 2026-09-11 | 1d | -0.0419 | -0.0504 | -0.0085 |
| 2026-09-11 | 2d | -0.0676 | -0.0757 | -0.0082 |
| 2026-09-11 | 3d | -0.1072 | -0.1129 | -0.0057 |
| 2026-09-14 | 1d | -0.0250 | -0.0257 | -0.0007 |
| 2026-09-14 | 2d | -0.1114 | -0.1121 | -0.0007 |
| 2026-09-14 | 3d | -0.2010 | -0.1974 | +0.0037 |
| 2026-09-15 | 1d | -0.0616 | -0.0615 | +0.0001 |
| 2026-09-15 | 2d | -0.1290 | -0.1280 | +0.0010 |
| 2026-09-16 | 1d | -0.0722 | -0.0720 | +0.0002 |

_Champion reconstruction check: mean |rebuilt price category − stored price_score| = 0.2349 (should be ~0; large values mean the learner's model of the engine has drifted from score_engine — distrust this run)._

## Decision

NO PROMOTION — challenger mean IC gain +0.0010 on 1d does not clear +0.001.

_Note: curved-polarity rules (rvol/rsi/sma/short/upside/debt curves) are never auto-adjusted; change those in score_rubric.py by hand with git history as the audit trail._
