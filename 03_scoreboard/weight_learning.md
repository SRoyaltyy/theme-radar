# Weight learning — decision log

_Generated 2026-09-15 16:49 EDT_

- label dates per horizon: 1d: 26, 2d: 25, 3d: 24
- primary horizon for promotion test: **1d** (26 dates)
- existing overrides: {'Price|ret': 0.25, 'Performance (Month)|delta': 0.9156732957647578, 'Average Volume|delta': 0.5752305402565514, 'Relative Strength Index (14)|delta': 0.25, 'Short Float|delta': 1.748848322406948, 'Institutional Transactions|level': 1.342773604391473, 'Institutional Ownership|delta': 1.9126100808472706, 'Insider Transactions|level': 0.8993116666796332, 'Target Price|delta': 1.2157172988649867, 'Analyst Recom|delta': 1.8610597180369464, 'Sales Growth Quarter Over Quarter|level': 2.0, 'Sales Year Over Year TTM|level': 2.0, 'Profit Margin|delta': 1.0781244549394309, 'EPS Surprise|level': 1.0228190948511149, 'n_catalysts|level': 1.617888084216515}

## Per-rule aligned IC (direction corrected for polarity)

| Rule | Horizon | Mean aligned IC | Dates | Proposed × | Testable |
|---|---|---|---|---|---|
| Price|ret | 1d | -0.0546 | 24 | 0.250 | yes |
| Price|ret | 2d | -0.0477 | 23 | 0.250 | yes |
| Price|ret | 3d | -0.0292 | 22 | 0.250 | yes |
| Performance (Month)|delta | 1d | -0.0170 | 24 | 0.884 | yes |
| Performance (Month)|delta | 2d | -0.0303 | 23 | 0.860 | yes |
| Performance (Month)|delta | 3d | -0.0464 | 22 | 0.831 | yes |
| Average Volume|delta | 1d | -0.0062 | 24 | 0.568 | NO — logs only |
| Average Volume|delta | 2d | -0.0057 | 23 | 0.569 | NO — logs only |
| Average Volume|delta | 3d | -0.0076 | 22 | 0.567 | NO — logs only |
| Relative Strength Index (14)|delta | 1d | -0.0498 | 24 | 0.250 | yes |
| Relative Strength Index (14)|delta | 2d | -0.0499 | 23 | 0.250 | yes |
| Relative Strength Index (14)|delta | 3d | -0.0314 | 22 | 0.250 | yes |
| Short Float|delta | 1d | -0.0018 | 23 | 1.742 | NO — logs only |
| Short Float|delta | 2d | -0.0047 | 22 | 1.733 | NO — logs only |
| Short Float|delta | 3d | -0.0077 | 21 | 1.722 | NO — logs only |
| Institutional Transactions|level | 1d | -0.0083 | 26 | 1.321 | NO — logs only |
| Institutional Transactions|level | 2d | -0.0090 | 25 | 1.319 | NO — logs only |
| Institutional Transactions|level | 3d | -0.0101 | 24 | 1.316 | NO — logs only |
| Institutional Ownership|delta | 1d | +0.0030 | 24 | 1.924 | NO — logs only |
| Institutional Ownership|delta | 2d | +0.0060 | 23 | 1.935 | NO — logs only |
| Institutional Ownership|delta | 3d | +0.0014 | 22 | 1.918 | NO — logs only |
| Insider Transactions|level | 1d | -0.0045 | 26 | 0.891 | NO — logs only |
| Insider Transactions|level | 2d | -0.0002 | 25 | 0.899 | NO — logs only |
| Insider Transactions|level | 3d | +0.0016 | 24 | 0.902 | NO — logs only |
| Target Price|delta | 1d | +0.0049 | 24 | 1.228 | NO — logs only |
| Target Price|delta | 2d | +0.0047 | 23 | 1.227 | NO — logs only |
| Target Price|delta | 3d | +0.0041 | 22 | 1.226 | NO — logs only |
| Analyst Recom|delta | 1d | +0.0084 | 24 | 1.892 | NO — logs only |
| Analyst Recom|delta | 2d | -0.0017 | 23 | 1.855 | NO — logs only |
| Analyst Recom|delta | 3d | -0.0037 | 22 | 1.847 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 1d | +0.0155 | 26 | 2.000 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 2d | +0.0169 | 25 | 2.000 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 3d | +0.0228 | 24 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 1d | +0.0113 | 26 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 2d | +0.0145 | 25 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 3d | +0.0186 | 24 | 2.000 | NO — logs only |
| Profit Margin|delta | 1d | +0.0065 | 24 | 1.092 | NO — logs only |
| Profit Margin|delta | 2d | +0.0035 | 23 | 1.086 | NO — logs only |
| Profit Margin|delta | 3d | +0.0078 | 22 | 1.095 | NO — logs only |
| EPS Surprise|level | 1d | +0.0107 | 26 | 1.045 | NO — logs only |
| EPS Surprise|level | 2d | +0.0126 | 25 | 1.049 | NO — logs only |
| EPS Surprise|level | 3d | +0.0129 | 24 | 1.049 | NO — logs only |
| n_catalysts|level | 1d | -0.0116 | 26 | 1.580 | yes |
| n_catalysts|level | 2d | -0.0210 | 25 | 1.550 | yes |
| n_catalysts|level | 3d | -0.0235 | 24 | 1.542 | yes |
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
| 2026-08-07 | 1d | -0.0339 | -0.0232 | +0.0107 |
| 2026-08-07 | 2d | -0.0242 | -0.0176 | +0.0066 |
| 2026-08-07 | 3d | -0.0009 | +0.0011 | +0.0021 |
| 2026-08-10 | 1d | -0.0491 | -0.0306 | +0.0185 |
| 2026-08-10 | 2d | -0.0596 | -0.0374 | +0.0223 |
| 2026-08-10 | 3d | -0.1054 | -0.0918 | +0.0136 |
| 2026-08-11 | 1d | +0.1007 | +0.1054 | +0.0047 |
| 2026-08-11 | 2d | +0.0174 | +0.0114 | -0.0060 |
| 2026-08-11 | 3d | +0.0639 | +0.0580 | -0.0058 |
| 2026-08-12 | 1d | -0.0472 | -0.0463 | +0.0009 |
| 2026-08-12 | 2d | +0.0520 | +0.0520 | +0.0000 |
| 2026-08-12 | 3d | +0.0878 | +0.0799 | -0.0079 |
| 2026-08-13 | 1d | -0.0908 | -0.0862 | +0.0046 |
| 2026-08-13 | 2d | -0.1428 | -0.1364 | +0.0064 |
| 2026-08-13 | 3d | -0.1672 | -0.1639 | +0.0033 |
| 2026-08-14 | 1d | +0.1577 | +0.1503 | -0.0073 |
| 2026-08-14 | 2d | -0.1560 | -0.1576 | -0.0016 |
| 2026-08-14 | 3d | -0.1404 | -0.1411 | -0.0008 |
| 2026-08-17 | 1d | -0.2097 | -0.2059 | +0.0038 |
| 2026-08-17 | 2d | -0.1365 | -0.1351 | +0.0015 |
| 2026-08-17 | 3d | -0.1034 | -0.1038 | -0.0004 |
| 2026-08-18 | 1d | +0.0486 | +0.0462 | -0.0024 |
| 2026-08-18 | 2d | +0.0270 | +0.0234 | -0.0036 |
| 2026-08-18 | 3d | +0.0058 | +0.0074 | +0.0016 |
| 2026-08-19 | 1d | +0.0108 | +0.0038 | -0.0070 |
| 2026-08-19 | 2d | +0.0519 | +0.0543 | +0.0024 |
| 2026-08-19 | 3d | +0.1772 | +0.1691 | -0.0081 |
| 2026-08-20 | 1d | -0.0007 | +0.0057 | +0.0064 |
| 2026-08-20 | 2d | +0.0530 | +0.0572 | +0.0042 |
| 2026-08-20 | 3d | +0.0387 | +0.0459 | +0.0072 |
| 2026-08-21 | 1d | -0.0802 | -0.0798 | +0.0004 |
| 2026-08-21 | 2d | +0.0158 | +0.0142 | -0.0016 |
| 2026-08-21 | 3d | -0.0723 | -0.0727 | -0.0003 |
| 2026-08-24 | 1d | +0.0056 | -0.0128 | -0.0184 |
| 2026-08-24 | 2d | -0.0285 | -0.0484 | -0.0199 |
| 2026-08-24 | 3d | -0.0880 | -0.0868 | +0.0013 |
| 2026-08-25 | 1d | -0.0503 | -0.0675 | -0.0171 |
| 2026-08-25 | 2d | -0.1093 | -0.1158 | -0.0065 |
| 2026-08-25 | 3d | -0.0661 | -0.0767 | -0.0106 |
| 2026-08-26 | 1d | -0.0710 | -0.0580 | +0.0131 |
| 2026-08-26 | 2d | -0.0146 | -0.0121 | +0.0025 |
| 2026-08-26 | 3d | -0.0019 | +0.0063 | +0.0083 |
| 2026-08-28 | 1d | -0.0442 | -0.0349 | +0.0093 |
| 2026-08-28 | 2d | +0.0258 | +0.0237 | -0.0021 |
| 2026-08-28 | 3d | +0.0108 | +0.0207 | +0.0099 |
| 2026-08-31 | 1d | -0.0065 | -0.0073 | -0.0008 |
| 2026-08-31 | 2d | +0.0398 | +0.0427 | +0.0029 |
| 2026-08-31 | 3d | +0.1004 | +0.1057 | +0.0054 |
| 2026-09-01 | 1d | -0.0847 | -0.0523 | +0.0324 |
| 2026-09-01 | 2d | -0.2394 | -0.1947 | +0.0447 |
| 2026-09-01 | 3d | -0.2756 | -0.2362 | +0.0394 |
| 2026-09-02 | 1d | -0.0842 | -0.0568 | +0.0275 |
| 2026-09-02 | 2d | -0.1304 | -0.0983 | +0.0321 |
| 2026-09-02 | 3d | -0.1700 | -0.1500 | +0.0200 |
| 2026-09-03 | 1d | -0.0656 | -0.0856 | -0.0199 |
| 2026-09-03 | 2d | -0.0607 | -0.0880 | -0.0273 |
| 2026-09-03 | 3d | -0.1049 | -0.1250 | -0.0201 |
| 2026-09-04 | 1d | -0.0292 | -0.0350 | -0.0058 |
| 2026-09-04 | 2d | -0.0659 | -0.0716 | -0.0057 |
| 2026-09-04 | 3d | -0.1272 | -0.1312 | -0.0040 |
| 2026-09-08 | 1d | -0.0849 | -0.0849 | +0.0000 |
| 2026-09-08 | 2d | -0.1276 | -0.1276 | +0.0000 |
| 2026-09-08 | 3d | -0.0619 | -0.0619 | +0.0000 |
| 2026-09-09 | 1d | -0.0163 | -0.0210 | -0.0047 |
| 2026-09-09 | 2d | +0.0188 | +0.0150 | -0.0039 |
| 2026-09-09 | 3d | -0.0591 | -0.0593 | -0.0002 |
| 2026-09-10 | 1d | -0.0932 | -0.0894 | +0.0038 |
| 2026-09-10 | 2d | +0.1308 | +0.1206 | -0.0101 |
| 2026-09-10 | 3d | +0.1827 | +0.1721 | -0.0106 |
| 2026-09-11 | 1d | -0.0419 | -0.0484 | -0.0065 |
| 2026-09-11 | 2d | -0.0676 | -0.0737 | -0.0061 |
| 2026-09-14 | 1d | -0.0250 | -0.0255 | -0.0005 |

_Champion reconstruction check: mean |rebuilt price category − stored price_score| = 0.2176 (should be ~0; large values mean the learner's model of the engine has drifted from score_engine — distrust this run)._

## Decision

PROMOTED — challenger mean IC gain +0.0017 on 1d, improved on 54% of 26 dates. New multipliers: Performance (Month)|delta ×0.884, Average Volume|delta ×0.568, Short Float|delta ×1.742, Institutional Transactions|level ×1.321, Institutional Ownership|delta ×1.924, Insider Transactions|level ×0.891, Target Price|delta ×1.228, Analyst Recom|delta ×1.892, Profit Margin|delta ×1.092, EPS Surprise|level ×1.045, n_catalysts|level ×1.580

_Note: curved-polarity rules (rvol/rsi/sma/short/upside/debt curves) are never auto-adjusted; change those in score_rubric.py by hand with git history as the audit trail._
