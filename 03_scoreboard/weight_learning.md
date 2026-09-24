# Weight learning — decision log

_Generated 2026-09-24 16:51 EDT_

- label dates per horizon: 1d: 33, 2d: 32, 3d: 31
- primary horizon for promotion test: **1d** (33 dates)
- existing overrides: {'Price|ret': 0.25, 'Performance (Month)|delta': 0.8433971514371941, 'Average Volume|delta': 0.5483890822743658, 'Relative Strength Index (14)|delta': 0.25, 'Short Float|delta': 1.7252195675728095, 'Institutional Transactions|level': 1.2899479968778684, 'Institutional Ownership|delta': 1.9457500834474015, 'Insider Transactions|level': 0.8726084854014611, 'Target Price|delta': 1.2578261733879856, 'Analyst Recom|delta': 1.9558473189435233, 'Sales Growth Quarter Over Quarter|level': 2.0, 'Sales Year Over Year TTM|level': 2.0, 'Profit Margin|delta': 1.1171601499394408, 'EPS Surprise|level': 1.089559846444787, 'n_catalysts|level': 1.5332502554705358}

## Per-rule aligned IC (direction corrected for polarity)

| Rule | Horizon | Mean aligned IC | Dates | Proposed × | Testable |
|---|---|---|---|---|---|
| Price|ret | 1d | -0.0371 | 31 | 0.250 | yes |
| Price|ret | 2d | -0.0397 | 30 | 0.250 | yes |
| Price|ret | 3d | -0.0252 | 29 | 0.250 | yes |
| Performance (Month)|delta | 1d | -0.0028 | 31 | 0.839 | yes |
| Performance (Month)|delta | 2d | -0.0253 | 30 | 0.801 | yes |
| Performance (Month)|delta | 3d | -0.0322 | 29 | 0.789 | yes |
| Average Volume|delta | 1d | -0.0124 | 31 | 0.535 | NO — logs only |
| Average Volume|delta | 2d | -0.0163 | 30 | 0.530 | NO — logs only |
| Average Volume|delta | 3d | -0.0159 | 29 | 0.531 | NO — logs only |
| Relative Strength Index (14)|delta | 1d | -0.0351 | 31 | 0.250 | yes |
| Relative Strength Index (14)|delta | 2d | -0.0398 | 30 | 0.250 | yes |
| Relative Strength Index (14)|delta | 3d | -0.0254 | 29 | 0.250 | yes |
| Short Float|delta | 1d | -0.0040 | 30 | 1.712 | NO — logs only |
| Short Float|delta | 2d | -0.0062 | 29 | 1.704 | NO — logs only |
| Short Float|delta | 3d | -0.0077 | 28 | 1.699 | NO — logs only |
| Institutional Transactions|level | 1d | -0.0058 | 33 | 1.275 | NO — logs only |
| Institutional Transactions|level | 2d | -0.0067 | 32 | 1.273 | NO — logs only |
| Institutional Transactions|level | 3d | -0.0067 | 31 | 1.273 | NO — logs only |
| Institutional Ownership|delta | 1d | +0.0011 | 31 | 1.950 | NO — logs only |
| Institutional Ownership|delta | 2d | +0.0054 | 30 | 1.967 | NO — logs only |
| Institutional Ownership|delta | 3d | +0.0016 | 29 | 1.952 | NO — logs only |
| Insider Transactions|level | 1d | -0.0089 | 33 | 0.857 | NO — logs only |
| Insider Transactions|level | 2d | -0.0072 | 32 | 0.860 | NO — logs only |
| Insider Transactions|level | 3d | -0.0053 | 31 | 0.863 | NO — logs only |
| Target Price|delta | 1d | +0.0103 | 31 | 1.284 | NO — logs only |
| Target Price|delta | 2d | +0.0065 | 30 | 1.274 | NO — logs only |
| Target Price|delta | 3d | +0.0039 | 29 | 1.268 | NO — logs only |
| Analyst Recom|delta | 1d | +0.0082 | 31 | 1.988 | NO — logs only |
| Analyst Recom|delta | 2d | -0.0003 | 30 | 1.955 | NO — logs only |
| Analyst Recom|delta | 3d | -0.0014 | 29 | 1.950 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 1d | +0.0200 | 33 | 2.000 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 2d | +0.0231 | 32 | 2.000 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 3d | +0.0270 | 31 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 1d | +0.0168 | 33 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 2d | +0.0218 | 32 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 3d | +0.0261 | 31 | 2.000 | NO — logs only |
| Profit Margin|delta | 1d | +0.0055 | 31 | 1.129 | NO — logs only |
| Profit Margin|delta | 2d | +0.0028 | 30 | 1.123 | NO — logs only |
| Profit Margin|delta | 3d | +0.0054 | 29 | 1.129 | NO — logs only |
| EPS Surprise|level | 1d | +0.0155 | 33 | 1.123 | NO — logs only |
| EPS Surprise|level | 2d | +0.0194 | 32 | 1.132 | NO — logs only |
| EPS Surprise|level | 3d | +0.0195 | 31 | 1.132 | NO — logs only |
| n_catalysts|level | 1d | -0.0060 | 33 | 1.515 | yes |
| n_catalysts|level | 2d | -0.0107 | 32 | 1.500 | yes |
| n_catalysts|level | 3d | -0.0132 | 31 | 1.493 | yes |
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
| 2026-08-07 | 1d | -0.0339 | -0.0241 | +0.0099 |
| 2026-08-07 | 2d | -0.0242 | -0.0176 | +0.0066 |
| 2026-08-07 | 3d | -0.0009 | +0.0020 | +0.0029 |
| 2026-08-10 | 1d | -0.0491 | -0.0304 | +0.0187 |
| 2026-08-10 | 2d | -0.0596 | -0.0371 | +0.0225 |
| 2026-08-10 | 3d | -0.1054 | -0.0913 | +0.0141 |
| 2026-08-11 | 1d | +0.1007 | +0.1049 | +0.0042 |
| 2026-08-11 | 2d | +0.0174 | +0.0118 | -0.0055 |
| 2026-08-11 | 3d | +0.0639 | +0.0590 | -0.0049 |
| 2026-08-12 | 1d | -0.0472 | -0.0468 | +0.0004 |
| 2026-08-12 | 2d | +0.0520 | +0.0523 | +0.0004 |
| 2026-08-12 | 3d | +0.0878 | +0.0809 | -0.0069 |
| 2026-08-13 | 1d | -0.0908 | -0.0864 | +0.0044 |
| 2026-08-13 | 2d | -0.1428 | -0.1386 | +0.0042 |
| 2026-08-13 | 3d | -0.1672 | -0.1641 | +0.0031 |
| 2026-08-14 | 1d | +0.1577 | +0.1441 | -0.0136 |
| 2026-08-14 | 2d | -0.1560 | -0.1573 | -0.0014 |
| 2026-08-14 | 3d | -0.1404 | -0.1413 | -0.0009 |
| 2026-08-17 | 1d | -0.2097 | -0.2062 | +0.0035 |
| 2026-08-17 | 2d | -0.1365 | -0.1352 | +0.0013 |
| 2026-08-17 | 3d | -0.1034 | -0.1042 | -0.0008 |
| 2026-08-18 | 1d | +0.0486 | +0.0460 | -0.0026 |
| 2026-08-18 | 2d | +0.0270 | +0.0230 | -0.0040 |
| 2026-08-18 | 3d | +0.0058 | +0.0074 | +0.0016 |
| 2026-08-19 | 1d | +0.0108 | +0.0025 | -0.0083 |
| 2026-08-19 | 2d | +0.0519 | +0.0543 | +0.0024 |
| 2026-08-19 | 3d | +0.1772 | +0.1678 | -0.0094 |
| 2026-08-20 | 1d | -0.0007 | +0.0056 | +0.0063 |
| 2026-08-20 | 2d | +0.0530 | +0.0569 | +0.0039 |
| 2026-08-20 | 3d | +0.0387 | +0.0462 | +0.0075 |
| 2026-08-21 | 1d | -0.0802 | -0.0807 | -0.0005 |
| 2026-08-21 | 2d | +0.0158 | +0.0139 | -0.0019 |
| 2026-08-21 | 3d | -0.0723 | -0.0728 | -0.0005 |
| 2026-08-24 | 1d | +0.0056 | -0.0146 | -0.0203 |
| 2026-08-24 | 2d | -0.0285 | -0.0507 | -0.0222 |
| 2026-08-24 | 3d | -0.0880 | -0.0876 | +0.0005 |
| 2026-08-25 | 1d | -0.0503 | -0.0700 | -0.0196 |
| 2026-08-25 | 2d | -0.1093 | -0.1168 | -0.0075 |
| 2026-08-25 | 3d | -0.0661 | -0.0779 | -0.0118 |
| 2026-08-26 | 1d | -0.0710 | -0.0572 | +0.0138 |
| 2026-08-26 | 2d | -0.0146 | -0.0122 | +0.0024 |
| 2026-08-26 | 3d | -0.0019 | +0.0063 | +0.0083 |
| 2026-08-28 | 1d | -0.0442 | -0.0339 | +0.0103 |
| 2026-08-28 | 2d | +0.0258 | +0.0234 | -0.0024 |
| 2026-08-28 | 3d | +0.0108 | +0.0211 | +0.0103 |
| 2026-08-31 | 1d | -0.0065 | -0.0073 | -0.0008 |
| 2026-08-31 | 2d | +0.0398 | +0.0423 | +0.0026 |
| 2026-08-31 | 3d | +0.1004 | +0.1054 | +0.0050 |
| 2026-09-01 | 1d | -0.0847 | -0.0514 | +0.0333 |
| 2026-09-01 | 2d | -0.2394 | -0.1933 | +0.0461 |
| 2026-09-01 | 3d | -0.2756 | -0.2349 | +0.0407 |
| 2026-09-02 | 1d | -0.0842 | -0.0560 | +0.0282 |
| 2026-09-02 | 2d | -0.1304 | -0.0974 | +0.0331 |
| 2026-09-02 | 3d | -0.1700 | -0.1489 | +0.0211 |
| 2026-09-03 | 1d | -0.0656 | -0.0863 | -0.0207 |
| 2026-09-03 | 2d | -0.0607 | -0.0888 | -0.0280 |
| 2026-09-03 | 3d | -0.1049 | -0.1256 | -0.0207 |
| 2026-09-04 | 1d | -0.0292 | -0.0350 | -0.0058 |
| 2026-09-04 | 2d | -0.0659 | -0.0715 | -0.0055 |
| 2026-09-04 | 3d | -0.1272 | -0.1313 | -0.0041 |
| 2026-09-08 | 1d | -0.0849 | -0.0849 | +0.0000 |
| 2026-09-08 | 2d | -0.1276 | -0.1276 | +0.0000 |
| 2026-09-08 | 3d | -0.0619 | -0.0619 | +0.0000 |
| 2026-09-09 | 1d | -0.0163 | -0.0218 | -0.0055 |
| 2026-09-09 | 2d | +0.0188 | +0.0137 | -0.0052 |
| 2026-09-09 | 3d | -0.0591 | -0.0601 | -0.0010 |
| 2026-09-10 | 1d | -0.0932 | -0.0889 | +0.0042 |
| 2026-09-10 | 2d | +0.1308 | +0.1189 | -0.0119 |
| 2026-09-10 | 3d | +0.1827 | +0.1701 | -0.0126 |
| 2026-09-11 | 1d | -0.0419 | -0.0497 | -0.0078 |
| 2026-09-11 | 2d | -0.0676 | -0.0753 | -0.0077 |
| 2026-09-11 | 3d | -0.1072 | -0.1128 | -0.0056 |
| 2026-09-14 | 1d | -0.0250 | -0.0261 | -0.0011 |
| 2026-09-14 | 2d | -0.1114 | -0.1123 | -0.0009 |
| 2026-09-14 | 3d | -0.2010 | -0.1981 | +0.0029 |
| 2026-09-15 | 1d | -0.0616 | -0.0616 | -0.0000 |
| 2026-09-15 | 2d | -0.1290 | -0.1282 | +0.0008 |
| 2026-09-15 | 3d | -0.1450 | -0.1441 | +0.0009 |
| 2026-09-16 | 1d | -0.0722 | -0.0728 | -0.0005 |
| 2026-09-16 | 2d | -0.0629 | -0.0628 | +0.0001 |
| 2026-09-16 | 3d | -0.0266 | -0.0266 | +0.0000 |
| 2026-09-17 | 1d | +0.0987 | +0.0992 | +0.0006 |
| 2026-09-17 | 2d | +0.2454 | +0.2458 | +0.0003 |
| 2026-09-17 | 3d | +0.3070 | +0.3076 | +0.0006 |
| 2026-09-18 | 1d | +0.0668 | +0.0669 | +0.0001 |
| 2026-09-18 | 2d | +0.0651 | +0.0651 | +0.0000 |
| 2026-09-18 | 3d | +0.1188 | +0.1185 | -0.0003 |
| 2026-09-21 | 1d | +0.1709 | +0.1715 | +0.0006 |
| 2026-09-21 | 2d | -0.0452 | -0.0449 | +0.0004 |
| 2026-09-21 | 3d | -0.0110 | -0.0104 | +0.0006 |
| 2026-09-22 | 1d | -0.1323 | -0.1330 | -0.0007 |
| 2026-09-22 | 2d | -0.1167 | -0.1172 | -0.0004 |
| 2026-09-23 | 1d | +0.0928 | +0.0943 | +0.0015 |

_Champion reconstruction check: mean |rebuilt price category − stored price_score| = 0.2056 (should be ~0; large values mean the learner's model of the engine has drifted from score_engine — distrust this run)._

## Decision

NO PROMOTION — challenger mean IC gain +0.0010 on 1d does not clear +0.001.

_Note: curved-polarity rules (rvol/rsi/sma/short/upside/debt curves) are never auto-adjusted; change those in score_rubric.py by hand with git history as the audit trail._
