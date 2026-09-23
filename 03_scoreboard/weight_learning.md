# Weight learning — decision log

_Generated 2026-09-23 17:01 EDT_

- label dates per horizon: 1d: 32, 2d: 31, 3d: 30
- primary horizon for promotion test: **1d** (32 dates)
- existing overrides: {'Price|ret': 0.25, 'Performance (Month)|delta': 0.8433971514371941, 'Average Volume|delta': 0.5483890822743658, 'Relative Strength Index (14)|delta': 0.25, 'Short Float|delta': 1.7252195675728095, 'Institutional Transactions|level': 1.2899479968778684, 'Institutional Ownership|delta': 1.9457500834474015, 'Insider Transactions|level': 0.8726084854014611, 'Target Price|delta': 1.2578261733879856, 'Analyst Recom|delta': 1.9558473189435233, 'Sales Growth Quarter Over Quarter|level': 2.0, 'Sales Year Over Year TTM|level': 2.0, 'Profit Margin|delta': 1.1171601499394408, 'EPS Surprise|level': 1.089559846444787, 'n_catalysts|level': 1.5332502554705358}

## Per-rule aligned IC (direction corrected for polarity)

| Rule | Horizon | Mean aligned IC | Dates | Proposed × | Testable |
|---|---|---|---|---|---|
| Price|ret | 1d | -0.0409 | 30 | 0.250 | yes |
| Price|ret | 2d | -0.0351 | 29 | 0.250 | yes |
| Price|ret | 3d | -0.0253 | 28 | 0.250 | yes |
| Performance (Month)|delta | 1d | -0.0056 | 30 | 0.834 | yes |
| Performance (Month)|delta | 2d | -0.0250 | 29 | 0.801 | yes |
| Performance (Month)|delta | 3d | -0.0323 | 28 | 0.789 | yes |
| Average Volume|delta | 1d | -0.0131 | 30 | 0.534 | NO — logs only |
| Average Volume|delta | 2d | -0.0149 | 29 | 0.532 | NO — logs only |
| Average Volume|delta | 3d | -0.0149 | 28 | 0.532 | NO — logs only |
| Relative Strength Index (14)|delta | 1d | -0.0367 | 30 | 0.250 | yes |
| Relative Strength Index (14)|delta | 2d | -0.0357 | 29 | 0.250 | yes |
| Relative Strength Index (14)|delta | 3d | -0.0270 | 28 | 0.250 | yes |
| Short Float|delta | 1d | -0.0034 | 29 | 1.714 | NO — logs only |
| Short Float|delta | 2d | -0.0064 | 28 | 1.703 | NO — logs only |
| Short Float|delta | 3d | -0.0080 | 27 | 1.697 | NO — logs only |
| Institutional Transactions|level | 1d | -0.0056 | 32 | 1.275 | NO — logs only |
| Institutional Transactions|level | 2d | -0.0053 | 31 | 1.276 | NO — logs only |
| Institutional Transactions|level | 3d | -0.0057 | 30 | 1.275 | NO — logs only |
| Institutional Ownership|delta | 1d | +0.0014 | 30 | 1.951 | NO — logs only |
| Institutional Ownership|delta | 2d | +0.0058 | 29 | 1.968 | NO — logs only |
| Institutional Ownership|delta | 3d | +0.0010 | 28 | 1.950 | NO — logs only |
| Insider Transactions|level | 1d | -0.0071 | 32 | 0.860 | NO — logs only |
| Insider Transactions|level | 2d | -0.0053 | 31 | 0.863 | NO — logs only |
| Insider Transactions|level | 3d | -0.0036 | 30 | 0.866 | NO — logs only |
| Target Price|delta | 1d | +0.0089 | 30 | 1.280 | NO — logs only |
| Target Price|delta | 2d | +0.0047 | 29 | 1.270 | NO — logs only |
| Target Price|delta | 3d | +0.0031 | 28 | 1.266 | NO — logs only |
| Analyst Recom|delta | 1d | +0.0078 | 30 | 1.987 | NO — logs only |
| Analyst Recom|delta | 2d | -0.0002 | 29 | 1.955 | NO — logs only |
| Analyst Recom|delta | 3d | -0.0012 | 28 | 1.951 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 1d | +0.0190 | 32 | 2.000 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 2d | +0.0228 | 31 | 2.000 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 3d | +0.0277 | 30 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 1d | +0.0163 | 32 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 2d | +0.0225 | 31 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 3d | +0.0269 | 30 | 2.000 | NO — logs only |
| Profit Margin|delta | 1d | +0.0050 | 30 | 1.128 | NO — logs only |
| Profit Margin|delta | 2d | +0.0029 | 29 | 1.124 | NO — logs only |
| Profit Margin|delta | 3d | +0.0064 | 28 | 1.131 | NO — logs only |
| EPS Surprise|level | 1d | +0.0139 | 32 | 1.120 | NO — logs only |
| EPS Surprise|level | 2d | +0.0159 | 31 | 1.124 | NO — logs only |
| EPS Surprise|level | 3d | +0.0169 | 30 | 1.126 | NO — logs only |
| n_catalysts|level | 1d | -0.0049 | 32 | 1.518 | yes |
| n_catalysts|level | 2d | -0.0094 | 31 | 1.504 | yes |
| n_catalysts|level | 3d | -0.0129 | 30 | 1.494 | yes |
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
| 2026-08-10 | 1d | -0.0491 | -0.0304 | +0.0187 |
| 2026-08-10 | 2d | -0.0596 | -0.0371 | +0.0226 |
| 2026-08-10 | 3d | -0.1054 | -0.0912 | +0.0142 |
| 2026-08-11 | 1d | +0.1007 | +0.1051 | +0.0043 |
| 2026-08-11 | 2d | +0.0174 | +0.0120 | -0.0054 |
| 2026-08-11 | 3d | +0.0639 | +0.0590 | -0.0048 |
| 2026-08-12 | 1d | -0.0472 | -0.0468 | +0.0004 |
| 2026-08-12 | 2d | +0.0520 | +0.0524 | +0.0004 |
| 2026-08-12 | 3d | +0.0878 | +0.0809 | -0.0069 |
| 2026-08-13 | 1d | -0.0908 | -0.0864 | +0.0044 |
| 2026-08-13 | 2d | -0.1428 | -0.1386 | +0.0042 |
| 2026-08-13 | 3d | -0.1672 | -0.1642 | +0.0030 |
| 2026-08-14 | 1d | +0.1577 | +0.1439 | -0.0138 |
| 2026-08-14 | 2d | -0.1560 | -0.1572 | -0.0013 |
| 2026-08-14 | 3d | -0.1404 | -0.1411 | -0.0008 |
| 2026-08-17 | 1d | -0.2097 | -0.2061 | +0.0036 |
| 2026-08-17 | 2d | -0.1365 | -0.1353 | +0.0013 |
| 2026-08-17 | 3d | -0.1034 | -0.1043 | -0.0009 |
| 2026-08-18 | 1d | +0.0486 | +0.0459 | -0.0027 |
| 2026-08-18 | 2d | +0.0270 | +0.0229 | -0.0041 |
| 2026-08-18 | 3d | +0.0058 | +0.0073 | +0.0015 |
| 2026-08-19 | 1d | +0.0108 | +0.0025 | -0.0083 |
| 2026-08-19 | 2d | +0.0519 | +0.0543 | +0.0024 |
| 2026-08-19 | 3d | +0.1772 | +0.1677 | -0.0095 |
| 2026-08-20 | 1d | -0.0007 | +0.0058 | +0.0064 |
| 2026-08-20 | 2d | +0.0530 | +0.0570 | +0.0040 |
| 2026-08-20 | 3d | +0.0387 | +0.0464 | +0.0076 |
| 2026-08-21 | 1d | -0.0802 | -0.0801 | +0.0001 |
| 2026-08-21 | 2d | +0.0158 | +0.0144 | -0.0014 |
| 2026-08-21 | 3d | -0.0723 | -0.0724 | -0.0000 |
| 2026-08-24 | 1d | +0.0056 | -0.0145 | -0.0202 |
| 2026-08-24 | 2d | -0.0285 | -0.0506 | -0.0221 |
| 2026-08-24 | 3d | -0.0880 | -0.0875 | +0.0005 |
| 2026-08-25 | 1d | -0.0503 | -0.0699 | -0.0195 |
| 2026-08-25 | 2d | -0.1093 | -0.1168 | -0.0074 |
| 2026-08-25 | 3d | -0.0661 | -0.0778 | -0.0117 |
| 2026-08-26 | 1d | -0.0710 | -0.0571 | +0.0139 |
| 2026-08-26 | 2d | -0.0146 | -0.0121 | +0.0025 |
| 2026-08-26 | 3d | -0.0019 | +0.0064 | +0.0084 |
| 2026-08-28 | 1d | -0.0442 | -0.0343 | +0.0099 |
| 2026-08-28 | 2d | +0.0258 | +0.0230 | -0.0028 |
| 2026-08-28 | 3d | +0.0108 | +0.0212 | +0.0104 |
| 2026-08-31 | 1d | -0.0065 | -0.0072 | -0.0007 |
| 2026-08-31 | 2d | +0.0398 | +0.0425 | +0.0027 |
| 2026-08-31 | 3d | +0.1004 | +0.1054 | +0.0050 |
| 2026-09-01 | 1d | -0.0847 | -0.0519 | +0.0329 |
| 2026-09-01 | 2d | -0.2394 | -0.1921 | +0.0474 |
| 2026-09-01 | 3d | -0.2756 | -0.2342 | +0.0414 |
| 2026-09-02 | 1d | -0.0842 | -0.0561 | +0.0282 |
| 2026-09-02 | 2d | -0.1304 | -0.0973 | +0.0331 |
| 2026-09-02 | 3d | -0.1700 | -0.1489 | +0.0211 |
| 2026-09-03 | 1d | -0.0656 | -0.0862 | -0.0205 |
| 2026-09-03 | 2d | -0.0607 | -0.0887 | -0.0280 |
| 2026-09-03 | 3d | -0.1049 | -0.1255 | -0.0206 |
| 2026-09-04 | 1d | -0.0292 | -0.0351 | -0.0060 |
| 2026-09-04 | 2d | -0.0659 | -0.0716 | -0.0057 |
| 2026-09-04 | 3d | -0.1272 | -0.1313 | -0.0041 |
| 2026-09-08 | 1d | -0.0849 | -0.0849 | +0.0000 |
| 2026-09-08 | 2d | -0.1276 | -0.1276 | +0.0000 |
| 2026-09-08 | 3d | -0.0619 | -0.0619 | +0.0000 |
| 2026-09-09 | 1d | -0.0163 | -0.0219 | -0.0056 |
| 2026-09-09 | 2d | +0.0188 | +0.0136 | -0.0053 |
| 2026-09-09 | 3d | -0.0591 | -0.0602 | -0.0010 |
| 2026-09-10 | 1d | -0.0932 | -0.0889 | +0.0043 |
| 2026-09-10 | 2d | +0.1308 | +0.1188 | -0.0119 |
| 2026-09-10 | 3d | +0.1827 | +0.1699 | -0.0127 |
| 2026-09-11 | 1d | -0.0419 | -0.0498 | -0.0079 |
| 2026-09-11 | 2d | -0.0676 | -0.0754 | -0.0078 |
| 2026-09-11 | 3d | -0.1072 | -0.1128 | -0.0056 |
| 2026-09-14 | 1d | -0.0250 | -0.0260 | -0.0011 |
| 2026-09-14 | 2d | -0.1114 | -0.1122 | -0.0008 |
| 2026-09-14 | 3d | -0.2010 | -0.1979 | +0.0031 |
| 2026-09-15 | 1d | -0.0616 | -0.0616 | -0.0000 |
| 2026-09-15 | 2d | -0.1290 | -0.1281 | +0.0009 |
| 2026-09-15 | 3d | -0.1450 | -0.1440 | +0.0010 |
| 2026-09-16 | 1d | -0.0722 | -0.0728 | -0.0005 |
| 2026-09-16 | 2d | -0.0629 | -0.0628 | +0.0001 |
| 2026-09-16 | 3d | -0.0266 | -0.0267 | -0.0001 |
| 2026-09-17 | 1d | +0.0987 | +0.0985 | -0.0001 |
| 2026-09-17 | 2d | +0.2454 | +0.2451 | -0.0003 |
| 2026-09-17 | 3d | +0.3070 | +0.3066 | -0.0004 |
| 2026-09-18 | 1d | +0.0668 | +0.0669 | +0.0001 |
| 2026-09-18 | 2d | +0.0651 | +0.0652 | +0.0001 |
| 2026-09-18 | 3d | +0.1188 | +0.1187 | -0.0001 |
| 2026-09-21 | 1d | +0.1709 | +0.1709 | +0.0000 |
| 2026-09-21 | 2d | -0.0452 | -0.0445 | +0.0008 |
| 2026-09-22 | 1d | -0.1323 | -0.1333 | -0.0010 |

_Champion reconstruction check: mean |rebuilt price category − stored price_score| = 0.2119 (should be ~0; large values mean the learner's model of the engine has drifted from score_engine — distrust this run)._

## Decision

NO PROMOTION — challenger mean IC gain +0.0009 on 1d does not clear +0.001.

_Note: curved-polarity rules (rvol/rsi/sma/short/upside/debt curves) are never auto-adjusted; change those in score_rubric.py by hand with git history as the audit trail._
