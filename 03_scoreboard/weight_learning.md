# Weight learning — decision log

_Generated 2026-09-09 18:52 EDT_

- label dates per horizon: 1d: 22, 2d: 21, 3d: 20
- primary horizon for promotion test: **1d** (22 dates)
- existing overrides: {'Price|ret': 0.25, 'Performance (Month)|delta': 1.080899801705557, 'Average Volume|delta': 0.6165331475413923, 'Relative Strength Index (14)|delta': 0.25, 'Short Float|delta': 1.7220258238299384, 'Institutional Transactions|level': 1.4126043352232092, 'Institutional Ownership|delta': 1.8693672077742631, 'Insider Transactions|level': 0.9031835883793327, 'Target Price|delta': 1.1931932018381275, 'Analyst Recom|delta': 1.7107068130286374, 'Sales Growth Quarter Over Quarter|level': 2.0, 'Sales Year Over Year TTM|level': 2.0, 'Profit Margin|delta': 1.0308736386719446, 'EPS Surprise|level': 0.9715478979655532, 'n_catalysts|level': 1.718188280967347}

## Per-rule aligned IC (direction corrected for polarity)

| Rule | Horizon | Mean aligned IC | Dates | Proposed × | Testable |
|---|---|---|---|---|---|
| Price|ret | 1d | -0.0542 | 20 | 0.250 | yes |
| Price|ret | 2d | -0.0530 | 20 | 0.250 | yes |
| Price|ret | 3d | -0.0477 | 19 | 0.250 | yes |
| Performance (Month)|delta | 1d | -0.0205 | 20 | 1.037 | yes |
| Performance (Month)|delta | 2d | -0.0450 | 20 | 0.984 | yes |
| Performance (Month)|delta | 3d | -0.0588 | 19 | 0.954 | yes |
| Average Volume|delta | 1d | -0.0103 | 20 | 0.604 | NO — logs only |
| Average Volume|delta | 2d | -0.0128 | 20 | 0.601 | NO — logs only |
| Average Volume|delta | 3d | -0.0129 | 19 | 0.601 | NO — logs only |
| Relative Strength Index (14)|delta | 1d | -0.0444 | 20 | 0.250 | yes |
| Relative Strength Index (14)|delta | 2d | -0.0549 | 20 | 0.250 | yes |
| Relative Strength Index (14)|delta | 3d | -0.0391 | 19 | 0.250 | yes |
| Short Float|delta | 1d | +0.0039 | 19 | 1.735 | NO — logs only |
| Short Float|delta | 2d | -0.0028 | 19 | 1.712 | NO — logs only |
| Short Float|delta | 3d | -0.0084 | 18 | 1.693 | NO — logs only |
| Institutional Transactions|level | 1d | -0.0043 | 22 | 1.401 | NO — logs only |
| Institutional Transactions|level | 2d | -0.0005 | 21 | 1.411 | NO — logs only |
| Institutional Transactions|level | 3d | -0.0031 | 20 | 1.404 | NO — logs only |
| Institutional Ownership|delta | 1d | +0.0032 | 20 | 1.881 | NO — logs only |
| Institutional Ownership|delta | 2d | +0.0094 | 20 | 1.905 | NO — logs only |
| Institutional Ownership|delta | 3d | +0.0051 | 19 | 1.889 | NO — logs only |
| Insider Transactions|level | 1d | +0.0015 | 22 | 0.906 | NO — logs only |
| Insider Transactions|level | 2d | +0.0061 | 21 | 0.914 | NO — logs only |
| Insider Transactions|level | 3d | +0.0099 | 20 | 0.921 | NO — logs only |
| Target Price|delta | 1d | +0.0021 | 20 | 1.198 | NO — logs only |
| Target Price|delta | 2d | +0.0031 | 20 | 1.201 | NO — logs only |
| Target Price|delta | 3d | +0.0021 | 19 | 1.198 | NO — logs only |
| Analyst Recom|delta | 1d | +0.0113 | 20 | 1.749 | NO — logs only |
| Analyst Recom|delta | 2d | -0.0003 | 20 | 1.710 | NO — logs only |
| Analyst Recom|delta | 3d | -0.0030 | 19 | 1.700 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 1d | +0.0193 | 22 | 2.000 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 2d | +0.0228 | 21 | 2.000 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 3d | +0.0257 | 20 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 1d | +0.0177 | 22 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 2d | +0.0239 | 21 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 3d | +0.0267 | 20 | 2.000 | NO — logs only |
| Profit Margin|delta | 1d | +0.0059 | 20 | 1.043 | NO — logs only |
| Profit Margin|delta | 2d | +0.0030 | 20 | 1.037 | NO — logs only |
| Profit Margin|delta | 3d | +0.0075 | 19 | 1.046 | NO — logs only |
| EPS Surprise|level | 1d | +0.0034 | 22 | 0.978 | NO — logs only |
| EPS Surprise|level | 2d | +0.0031 | 21 | 0.978 | NO — logs only |
| EPS Surprise|level | 3d | +0.0027 | 20 | 0.977 | NO — logs only |
| n_catalysts|level | 1d | -0.0035 | 22 | 1.706 | yes |
| n_catalysts|level | 2d | -0.0071 | 21 | 1.694 | yes |
| n_catalysts|level | 3d | -0.0119 | 20 | 1.677 | yes |
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
| 2026-08-07 | 1d | -0.0339 | -0.0196 | +0.0143 |
| 2026-08-07 | 2d | -0.0242 | -0.0159 | +0.0083 |
| 2026-08-07 | 3d | -0.0009 | -0.0006 | +0.0003 |
| 2026-08-10 | 1d | -0.0491 | -0.0312 | +0.0179 |
| 2026-08-10 | 2d | -0.0596 | -0.0392 | +0.0204 |
| 2026-08-10 | 3d | -0.1054 | -0.0931 | +0.0123 |
| 2026-08-11 | 1d | +0.1007 | +0.1089 | +0.0081 |
| 2026-08-11 | 2d | +0.0174 | +0.0145 | -0.0029 |
| 2026-08-11 | 3d | +0.0639 | +0.0582 | -0.0057 |
| 2026-08-12 | 1d | -0.0472 | -0.0444 | +0.0028 |
| 2026-08-12 | 2d | +0.0520 | +0.0503 | -0.0016 |
| 2026-08-12 | 3d | +0.0878 | +0.0744 | -0.0133 |
| 2026-08-13 | 1d | -0.0908 | -0.0858 | +0.0050 |
| 2026-08-13 | 2d | -0.1428 | -0.1359 | +0.0069 |
| 2026-08-13 | 3d | -0.1672 | -0.1637 | +0.0035 |
| 2026-08-14 | 1d | +0.1577 | +0.1576 | -0.0001 |
| 2026-08-14 | 2d | -0.1560 | -0.1594 | -0.0034 |
| 2026-08-14 | 3d | -0.1404 | -0.1413 | -0.0010 |
| 2026-08-17 | 1d | -0.2097 | -0.2086 | +0.0012 |
| 2026-08-17 | 2d | -0.1365 | -0.1355 | +0.0010 |
| 2026-08-17 | 3d | -0.1034 | -0.1030 | +0.0004 |
| 2026-08-18 | 1d | +0.0486 | +0.0487 | +0.0001 |
| 2026-08-18 | 2d | +0.0270 | +0.0262 | -0.0008 |
| 2026-08-18 | 3d | +0.0058 | +0.0074 | +0.0016 |
| 2026-08-19 | 1d | +0.0108 | +0.0075 | -0.0033 |
| 2026-08-19 | 2d | +0.0519 | +0.0533 | +0.0014 |
| 2026-08-19 | 3d | +0.1772 | +0.1747 | -0.0025 |
| 2026-08-20 | 1d | -0.0007 | +0.0028 | +0.0035 |
| 2026-08-20 | 2d | +0.0530 | +0.0552 | +0.0022 |
| 2026-08-20 | 3d | +0.0387 | +0.0423 | +0.0036 |
| 2026-08-21 | 1d | -0.0802 | -0.0816 | -0.0014 |
| 2026-08-21 | 2d | +0.0158 | +0.0138 | -0.0020 |
| 2026-08-21 | 3d | -0.0723 | -0.0738 | -0.0015 |
| 2026-08-24 | 1d | +0.0056 | -0.0048 | -0.0104 |
| 2026-08-24 | 2d | -0.0285 | -0.0395 | -0.0110 |
| 2026-08-24 | 3d | -0.0880 | -0.0904 | -0.0024 |
| 2026-08-25 | 1d | -0.0503 | -0.0611 | -0.0108 |
| 2026-08-25 | 2d | -0.1093 | -0.1165 | -0.0072 |
| 2026-08-25 | 3d | -0.0661 | -0.0746 | -0.0085 |
| 2026-08-26 | 1d | -0.0710 | -0.0689 | +0.0021 |
| 2026-08-26 | 2d | -0.0146 | -0.0174 | -0.0028 |
| 2026-08-26 | 3d | -0.0019 | -0.0022 | -0.0003 |
| 2026-08-28 | 1d | -0.0442 | -0.0403 | +0.0039 |
| 2026-08-28 | 2d | +0.0258 | +0.0235 | -0.0023 |
| 2026-08-28 | 3d | +0.0108 | +0.0161 | +0.0053 |
| 2026-08-31 | 1d | -0.0065 | -0.0088 | -0.0023 |
| 2026-08-31 | 2d | +0.0398 | +0.0409 | +0.0011 |
| 2026-08-31 | 3d | +0.1004 | +0.1024 | +0.0021 |
| 2026-09-01 | 1d | -0.0847 | -0.0675 | +0.0173 |
| 2026-09-01 | 2d | -0.2394 | -0.2201 | +0.0193 |
| 2026-09-01 | 3d | -0.2756 | -0.2575 | +0.0181 |
| 2026-09-02 | 1d | -0.0842 | -0.0715 | +0.0128 |
| 2026-09-02 | 2d | -0.1304 | -0.1132 | +0.0172 |
| 2026-09-02 | 3d | -0.1700 | -0.1607 | +0.0092 |
| 2026-09-03 | 1d | -0.0656 | -0.0752 | -0.0095 |
| 2026-09-03 | 2d | -0.0607 | -0.0749 | -0.0142 |
| 2026-09-03 | 3d | -0.1049 | -0.1172 | -0.0123 |
| 2026-09-04 | 1d | -0.0292 | -0.0325 | -0.0034 |
| 2026-09-04 | 2d | -0.0659 | -0.0712 | -0.0053 |
| 2026-09-08 | 1d | -0.0849 | -0.0849 | +0.0000 |

_Champion reconstruction check: mean |rebuilt price category − stored price_score| = 0.1640 (should be ~0; large values mean the learner's model of the engine has drifted from score_engine — distrust this run)._

## Decision

PROMOTED — challenger mean IC gain +0.0021 on 1d, improved on 59% of 22 dates. New multipliers: Performance (Month)|delta ×1.037, Average Volume|delta ×0.604, Short Float|delta ×1.735, Institutional Transactions|level ×1.401, Institutional Ownership|delta ×1.881, Insider Transactions|level ×0.906, Target Price|delta ×1.198, Analyst Recom|delta ×1.749, Profit Margin|delta ×1.043, EPS Surprise|level ×0.978, n_catalysts|level ×1.706

_Note: curved-polarity rules (rvol/rsi/sma/short/upside/debt curves) are never auto-adjusted; change those in score_rubric.py by hand with git history as the audit trail._
