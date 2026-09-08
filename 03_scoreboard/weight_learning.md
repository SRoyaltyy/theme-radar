# Weight learning — decision log

_Generated 2026-09-08 19:05 EDT_

- label dates per horizon: 1d: 21, 2d: 20, 3d: 19
- primary horizon for promotion test: **1d** (21 dates)
- existing overrides: {'Price|ret': 0.25, 'Performance (Month)|delta': 1.1270979617584045, 'Average Volume|delta': 0.6295259305388498, 'Relative Strength Index (14)|delta': 0.25, 'Short Float|delta': 1.7087317128584723, 'Institutional Transactions|level': 1.4156954172204765, 'Institutional Ownership|delta': 1.8573551896432936, 'Insider Transactions|level': 0.9008679482548193, 'Target Price|delta': 1.188191054550536, 'Analyst Recom|delta': 1.6730066496814064, 'Sales Growth Quarter Over Quarter|level': 2.0, 'Sales Year Over Year TTM|level': 2.0, 'Profit Margin|delta': 1.0188520283680536, 'EPS Surprise|level': 0.9682615942886365, 'n_catalysts|level': 1.7240870458815738}

## Per-rule aligned IC (direction corrected for polarity)

| Rule | Horizon | Mean aligned IC | Dates | Proposed × | Testable |
|---|---|---|---|---|---|
| Price|ret | 1d | -0.0542 | 20 | 0.250 | yes |
| Price|ret | 2d | -0.0581 | 19 | 0.250 | yes |
| Price|ret | 3d | -0.0421 | 18 | 0.250 | yes |
| Performance (Month)|delta | 1d | -0.0205 | 20 | 1.081 | yes |
| Performance (Month)|delta | 2d | -0.0453 | 19 | 1.025 | yes |
| Performance (Month)|delta | 3d | -0.0587 | 18 | 0.995 | yes |
| Average Volume|delta | 1d | -0.0103 | 20 | 0.617 | NO — logs only |
| Average Volume|delta | 2d | -0.0134 | 19 | 0.613 | NO — logs only |
| Average Volume|delta | 3d | -0.0133 | 18 | 0.613 | NO — logs only |
| Relative Strength Index (14)|delta | 1d | -0.0444 | 20 | 0.250 | yes |
| Relative Strength Index (14)|delta | 2d | -0.0597 | 19 | 0.250 | yes |
| Relative Strength Index (14)|delta | 3d | -0.0353 | 18 | 0.250 | yes |
| Short Float|delta | 1d | +0.0039 | 19 | 1.722 | NO — logs only |
| Short Float|delta | 2d | -0.0042 | 18 | 1.694 | NO — logs only |
| Short Float|delta | 3d | -0.0081 | 17 | 1.681 | NO — logs only |
| Institutional Transactions|level | 1d | -0.0011 | 21 | 1.413 | NO — logs only |
| Institutional Transactions|level | 2d | -0.0019 | 20 | 1.410 | NO — logs only |
| Institutional Transactions|level | 3d | -0.0048 | 19 | 1.402 | NO — logs only |
| Institutional Ownership|delta | 1d | +0.0032 | 20 | 1.869 | NO — logs only |
| Institutional Ownership|delta | 2d | +0.0089 | 19 | 1.890 | NO — logs only |
| Institutional Ownership|delta | 3d | +0.0051 | 18 | 1.876 | NO — logs only |
| Insider Transactions|level | 1d | +0.0013 | 21 | 0.903 | NO — logs only |
| Insider Transactions|level | 2d | +0.0069 | 20 | 0.913 | NO — logs only |
| Insider Transactions|level | 3d | +0.0108 | 19 | 0.920 | NO — logs only |
| Target Price|delta | 1d | +0.0021 | 20 | 1.193 | NO — logs only |
| Target Price|delta | 2d | +0.0029 | 19 | 1.195 | NO — logs only |
| Target Price|delta | 3d | +0.0030 | 18 | 1.195 | NO — logs only |
| Analyst Recom|delta | 1d | +0.0113 | 20 | 1.711 | NO — logs only |
| Analyst Recom|delta | 2d | +0.0009 | 19 | 1.676 | NO — logs only |
| Analyst Recom|delta | 3d | -0.0038 | 18 | 1.660 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 1d | +0.0185 | 21 | 2.000 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 2d | +0.0195 | 20 | 2.000 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 3d | +0.0233 | 19 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 1d | +0.0176 | 21 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 2d | +0.0210 | 20 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 3d | +0.0256 | 19 | 2.000 | NO — logs only |
| Profit Margin|delta | 1d | +0.0059 | 20 | 1.031 | NO — logs only |
| Profit Margin|delta | 2d | +0.0026 | 19 | 1.024 | NO — logs only |
| Profit Margin|delta | 3d | +0.0067 | 18 | 1.032 | NO — logs only |
| EPS Surprise|level | 1d | +0.0017 | 21 | 0.972 | NO — logs only |
| EPS Surprise|level | 2d | +0.0035 | 20 | 0.975 | NO — logs only |
| EPS Surprise|level | 3d | +0.0020 | 19 | 0.972 | NO — logs only |
| n_catalysts|level | 1d | -0.0017 | 21 | 1.718 | yes |
| n_catalysts|level | 2d | -0.0096 | 20 | 1.691 | yes |
| n_catalysts|level | 3d | -0.0158 | 19 | 1.670 | yes |
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
| 2026-08-07 | 1d | -0.0339 | -0.0196 | +0.0144 |
| 2026-08-07 | 2d | -0.0242 | -0.0159 | +0.0083 |
| 2026-08-07 | 3d | -0.0009 | -0.0007 | +0.0002 |
| 2026-08-10 | 1d | -0.0491 | -0.0313 | +0.0178 |
| 2026-08-10 | 2d | -0.0596 | -0.0392 | +0.0204 |
| 2026-08-10 | 3d | -0.1054 | -0.0931 | +0.0123 |
| 2026-08-11 | 1d | +0.1007 | +0.1089 | +0.0082 |
| 2026-08-11 | 2d | +0.0174 | +0.0145 | -0.0028 |
| 2026-08-11 | 3d | +0.0639 | +0.0581 | -0.0058 |
| 2026-08-12 | 1d | -0.0472 | -0.0441 | +0.0031 |
| 2026-08-12 | 2d | +0.0520 | +0.0504 | -0.0016 |
| 2026-08-12 | 3d | +0.0878 | +0.0742 | -0.0136 |
| 2026-08-13 | 1d | -0.0908 | -0.0857 | +0.0051 |
| 2026-08-13 | 2d | -0.1428 | -0.1354 | +0.0074 |
| 2026-08-13 | 3d | -0.1672 | -0.1633 | +0.0039 |
| 2026-08-14 | 1d | +0.1577 | +0.1586 | +0.0009 |
| 2026-08-14 | 2d | -0.1560 | -0.1588 | -0.0029 |
| 2026-08-14 | 3d | -0.1404 | -0.1407 | -0.0003 |
| 2026-08-17 | 1d | -0.2097 | -0.2094 | +0.0003 |
| 2026-08-17 | 2d | -0.1365 | -0.1364 | +0.0001 |
| 2026-08-17 | 3d | -0.1034 | -0.1032 | +0.0002 |
| 2026-08-18 | 1d | +0.0486 | +0.0484 | -0.0002 |
| 2026-08-18 | 2d | +0.0270 | +0.0265 | -0.0005 |
| 2026-08-18 | 3d | +0.0058 | +0.0066 | +0.0008 |
| 2026-08-19 | 1d | +0.0108 | +0.0089 | -0.0018 |
| 2026-08-19 | 2d | +0.0519 | +0.0533 | +0.0014 |
| 2026-08-19 | 3d | +0.1772 | +0.1758 | -0.0014 |
| 2026-08-20 | 1d | -0.0007 | +0.0018 | +0.0024 |
| 2026-08-20 | 2d | +0.0530 | +0.0542 | +0.0013 |
| 2026-08-20 | 3d | +0.0387 | +0.0411 | +0.0024 |
| 2026-08-21 | 1d | -0.0802 | -0.0816 | -0.0014 |
| 2026-08-21 | 2d | +0.0158 | +0.0141 | -0.0018 |
| 2026-08-21 | 3d | -0.0723 | -0.0733 | -0.0009 |
| 2026-08-24 | 1d | +0.0056 | -0.0007 | -0.0063 |
| 2026-08-24 | 2d | -0.0285 | -0.0348 | -0.0063 |
| 2026-08-24 | 3d | -0.0880 | -0.0900 | -0.0020 |
| 2026-08-25 | 1d | -0.0503 | -0.0571 | -0.0068 |
| 2026-08-25 | 2d | -0.1093 | -0.1157 | -0.0064 |
| 2026-08-25 | 3d | -0.0661 | -0.0738 | -0.0077 |
| 2026-08-26 | 1d | -0.0710 | -0.0699 | +0.0011 |
| 2026-08-26 | 2d | -0.0146 | -0.0171 | -0.0026 |
| 2026-08-26 | 3d | -0.0019 | -0.0032 | -0.0013 |
| 2026-08-28 | 1d | -0.0442 | -0.0423 | +0.0019 |
| 2026-08-28 | 2d | +0.0258 | +0.0230 | -0.0029 |
| 2026-08-28 | 3d | +0.0108 | +0.0148 | +0.0040 |
| 2026-08-31 | 1d | -0.0065 | -0.0074 | -0.0009 |
| 2026-08-31 | 2d | +0.0398 | +0.0427 | +0.0029 |
| 2026-08-31 | 3d | +0.1004 | +0.1030 | +0.0026 |
| 2026-09-01 | 1d | -0.0847 | -0.0691 | +0.0156 |
| 2026-09-01 | 2d | -0.2394 | -0.2187 | +0.0208 |
| 2026-09-01 | 3d | -0.2756 | -0.2569 | +0.0187 |
| 2026-09-02 | 1d | -0.0842 | -0.0730 | +0.0112 |
| 2026-09-02 | 2d | -0.1304 | -0.1161 | +0.0143 |
| 2026-09-02 | 3d | -0.1700 | -0.1630 | +0.0070 |
| 2026-09-03 | 1d | -0.0656 | -0.0737 | -0.0080 |
| 2026-09-03 | 2d | -0.0607 | -0.0727 | -0.0120 |
| 2026-09-04 | 1d | -0.0292 | -0.0324 | -0.0032 |

_Champion reconstruction check: mean |rebuilt price category − stored price_score| = 0.1542 (should be ~0; large values mean the learner's model of the engine has drifted from score_engine — distrust this run)._

## Decision

PROMOTED — challenger mean IC gain +0.0025 on 1d, improved on 57% of 21 dates. New multipliers: Performance (Month)|delta ×1.081, Average Volume|delta ×0.617, Short Float|delta ×1.722, Institutional Transactions|level ×1.413, Institutional Ownership|delta ×1.869, Insider Transactions|level ×0.903, Target Price|delta ×1.193, Analyst Recom|delta ×1.711, Profit Margin|delta ×1.031, EPS Surprise|level ×0.972, n_catalysts|level ×1.718

_Note: curved-polarity rules (rvol/rsi/sma/short/upside/debt curves) are never auto-adjusted; change those in score_rubric.py by hand with git history as the audit trail._
