# Weight learning — decision log

_Generated 2026-09-10 18:53 EDT_

- label dates per horizon: 1d: 23, 2d: 22, 3d: 21
- primary horizon for promotion test: **1d** (23 dates)
- existing overrides: {'Price|ret': 0.25, 'Performance (Month)|delta': 1.036595239249975, 'Average Volume|delta': 0.6038085225368464, 'Relative Strength Index (14)|delta': 0.25, 'Short Float|delta': 1.7354233643715304, 'Institutional Transactions|level': 1.4005535096032442, 'Institutional Ownership|delta': 1.8814569108738286, 'Insider Transactions|level': 0.9058093437072128, 'Target Price|delta': 1.1982164075888264, 'Analyst Recom|delta': 1.7492565260872688, 'Sales Growth Quarter Over Quarter|level': 2.0, 'Sales Year Over Year TTM|level': 2.0, 'Profit Margin|delta': 1.043037094023276, 'EPS Surprise|level': 0.978067635535136, 'n_catalysts|level': 1.7062444817194047}

## Per-rule aligned IC (direction corrected for polarity)

| Rule | Horizon | Mean aligned IC | Dates | Proposed × | Testable |
|---|---|---|---|---|---|
| Price|ret | 1d | -0.0454 | 21 | 0.250 | yes |
| Price|ret | 2d | -0.0530 | 20 | 0.250 | yes |
| Price|ret | 3d | -0.0466 | 20 | 0.250 | yes |
| Performance (Month)|delta | 1d | -0.0188 | 21 | 0.998 | yes |
| Performance (Month)|delta | 2d | -0.0450 | 20 | 0.943 | yes |
| Performance (Month)|delta | 3d | -0.0610 | 20 | 0.910 | yes |
| Average Volume|delta | 1d | -0.0078 | 21 | 0.594 | NO — logs only |
| Average Volume|delta | 2d | -0.0128 | 20 | 0.588 | NO — logs only |
| Average Volume|delta | 3d | -0.0120 | 20 | 0.589 | NO — logs only |
| Relative Strength Index (14)|delta | 1d | -0.0418 | 21 | 0.250 | yes |
| Relative Strength Index (14)|delta | 2d | -0.0549 | 20 | 0.250 | yes |
| Relative Strength Index (14)|delta | 3d | -0.0389 | 20 | 0.250 | yes |
| Short Float|delta | 1d | +0.0031 | 20 | 1.746 | NO — logs only |
| Short Float|delta | 2d | -0.0028 | 19 | 1.726 | NO — logs only |
| Short Float|delta | 3d | -0.0065 | 19 | 1.713 | NO — logs only |
| Institutional Transactions|level | 1d | -0.0062 | 23 | 1.383 | NO — logs only |
| Institutional Transactions|level | 2d | -0.0039 | 22 | 1.390 | NO — logs only |
| Institutional Transactions|level | 3d | -0.0029 | 21 | 1.393 | NO — logs only |
| Institutional Ownership|delta | 1d | +0.0027 | 21 | 1.891 | NO — logs only |
| Institutional Ownership|delta | 2d | +0.0094 | 20 | 1.917 | NO — logs only |
| Institutional Ownership|delta | 3d | +0.0055 | 20 | 1.902 | NO — logs only |
| Insider Transactions|level | 1d | +0.0020 | 23 | 0.909 | NO — logs only |
| Insider Transactions|level | 2d | +0.0062 | 22 | 0.917 | NO — logs only |
| Insider Transactions|level | 3d | +0.0092 | 21 | 0.922 | NO — logs only |
| Target Price|delta | 1d | +0.0021 | 21 | 1.203 | NO — logs only |
| Target Price|delta | 2d | +0.0031 | 20 | 1.206 | NO — logs only |
| Target Price|delta | 3d | +0.0029 | 20 | 1.205 | NO — logs only |
| Analyst Recom|delta | 1d | +0.0105 | 21 | 1.786 | NO — logs only |
| Analyst Recom|delta | 2d | -0.0003 | 20 | 1.748 | NO — logs only |
| Analyst Recom|delta | 3d | -0.0036 | 20 | 1.737 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 1d | +0.0170 | 23 | 2.000 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 2d | +0.0216 | 22 | 2.000 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 3d | +0.0268 | 21 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 1d | +0.0139 | 23 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 2d | +0.0212 | 22 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 3d | +0.0265 | 21 | 2.000 | NO — logs only |
| Profit Margin|delta | 1d | +0.0059 | 21 | 1.055 | NO — logs only |
| Profit Margin|delta | 2d | +0.0030 | 20 | 1.049 | NO — logs only |
| Profit Margin|delta | 3d | +0.0079 | 20 | 1.060 | NO — logs only |
| EPS Surprise|level | 1d | +0.0058 | 23 | 0.989 | NO — logs only |
| EPS Surprise|level | 2d | +0.0058 | 22 | 0.989 | NO — logs only |
| EPS Surprise|level | 3d | +0.0037 | 21 | 0.985 | NO — logs only |
| n_catalysts|level | 1d | -0.0077 | 23 | 1.680 | yes |
| n_catalysts|level | 2d | -0.0115 | 22 | 1.667 | yes |
| n_catalysts|level | 3d | -0.0127 | 21 | 1.663 | yes |
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
| 2026-08-07 | 1d | -0.0339 | -0.0227 | +0.0112 |
| 2026-08-07 | 2d | -0.0242 | -0.0173 | +0.0068 |
| 2026-08-07 | 3d | -0.0009 | +0.0005 | +0.0015 |
| 2026-08-10 | 1d | -0.0491 | -0.0311 | +0.0179 |
| 2026-08-10 | 2d | -0.0596 | -0.0383 | +0.0214 |
| 2026-08-10 | 3d | -0.1054 | -0.0921 | +0.0133 |
| 2026-08-11 | 1d | +0.1007 | +0.1058 | +0.0051 |
| 2026-08-11 | 2d | +0.0174 | +0.0119 | -0.0055 |
| 2026-08-11 | 3d | +0.0639 | +0.0580 | -0.0058 |
| 2026-08-12 | 1d | -0.0472 | -0.0440 | +0.0032 |
| 2026-08-12 | 2d | +0.0520 | +0.0519 | -0.0001 |
| 2026-08-12 | 3d | +0.0878 | +0.0773 | -0.0104 |
| 2026-08-13 | 1d | -0.0908 | -0.0868 | +0.0040 |
| 2026-08-13 | 2d | -0.1428 | -0.1368 | +0.0060 |
| 2026-08-13 | 3d | -0.1672 | -0.1638 | +0.0033 |
| 2026-08-14 | 1d | +0.1577 | +0.1520 | -0.0057 |
| 2026-08-14 | 2d | -0.1560 | -0.1585 | -0.0025 |
| 2026-08-14 | 3d | -0.1404 | -0.1411 | -0.0007 |
| 2026-08-17 | 1d | -0.2097 | -0.2076 | +0.0021 |
| 2026-08-17 | 2d | -0.1365 | -0.1357 | +0.0009 |
| 2026-08-17 | 3d | -0.1034 | -0.1032 | +0.0002 |
| 2026-08-18 | 1d | +0.0486 | +0.0478 | -0.0008 |
| 2026-08-18 | 2d | +0.0270 | +0.0255 | -0.0015 |
| 2026-08-18 | 3d | +0.0058 | +0.0073 | +0.0015 |
| 2026-08-19 | 1d | +0.0108 | +0.0059 | -0.0049 |
| 2026-08-19 | 2d | +0.0519 | +0.0541 | +0.0022 |
| 2026-08-19 | 3d | +0.1772 | +0.1725 | -0.0047 |
| 2026-08-20 | 1d | -0.0007 | +0.0035 | +0.0041 |
| 2026-08-20 | 2d | +0.0530 | +0.0553 | +0.0024 |
| 2026-08-20 | 3d | +0.0387 | +0.0429 | +0.0042 |
| 2026-08-21 | 1d | -0.0802 | -0.0804 | -0.0002 |
| 2026-08-21 | 2d | +0.0158 | +0.0141 | -0.0018 |
| 2026-08-21 | 3d | -0.0723 | -0.0734 | -0.0010 |
| 2026-08-24 | 1d | +0.0056 | -0.0073 | -0.0129 |
| 2026-08-24 | 2d | -0.0285 | -0.0420 | -0.0135 |
| 2026-08-24 | 3d | -0.0880 | -0.0897 | -0.0017 |
| 2026-08-25 | 1d | -0.0503 | -0.0642 | -0.0138 |
| 2026-08-25 | 2d | -0.1093 | -0.1159 | -0.0066 |
| 2026-08-25 | 3d | -0.0661 | -0.0753 | -0.0093 |
| 2026-08-26 | 1d | -0.0710 | -0.0631 | +0.0079 |
| 2026-08-26 | 2d | -0.0146 | -0.0143 | +0.0003 |
| 2026-08-26 | 3d | -0.0019 | +0.0022 | +0.0041 |
| 2026-08-28 | 1d | -0.0442 | -0.0384 | +0.0058 |
| 2026-08-28 | 2d | +0.0258 | +0.0228 | -0.0030 |
| 2026-08-28 | 3d | +0.0108 | +0.0185 | +0.0077 |
| 2026-08-31 | 1d | -0.0065 | -0.0081 | -0.0016 |
| 2026-08-31 | 2d | +0.0398 | +0.0417 | +0.0020 |
| 2026-08-31 | 3d | +0.1004 | +0.1047 | +0.0043 |
| 2026-09-01 | 1d | -0.0847 | -0.0580 | +0.0268 |
| 2026-09-01 | 2d | -0.2394 | -0.2034 | +0.0361 |
| 2026-09-01 | 3d | -0.2756 | -0.2443 | +0.0313 |
| 2026-09-02 | 1d | -0.0842 | -0.0629 | +0.0213 |
| 2026-09-02 | 2d | -0.1304 | -0.1047 | +0.0257 |
| 2026-09-02 | 3d | -0.1700 | -0.1548 | +0.0152 |
| 2026-09-03 | 1d | -0.0656 | -0.0805 | -0.0149 |
| 2026-09-03 | 2d | -0.0607 | -0.0830 | -0.0223 |
| 2026-09-03 | 3d | -0.1049 | -0.1224 | -0.0175 |
| 2026-09-04 | 1d | -0.0292 | -0.0342 | -0.0050 |
| 2026-09-04 | 2d | -0.0659 | -0.0720 | -0.0061 |
| 2026-09-04 | 3d | -0.1272 | -0.1319 | -0.0047 |
| 2026-09-08 | 1d | -0.0849 | -0.0849 | +0.0000 |
| 2026-09-08 | 2d | -0.1276 | -0.1276 | +0.0000 |
| 2026-09-09 | 1d | -0.0163 | -0.0181 | -0.0019 |

_Champion reconstruction check: mean |rebuilt price category − stored price_score| = 0.1768 (should be ~0; large values mean the learner's model of the engine has drifted from score_engine — distrust this run)._

## Decision

PROMOTED — challenger mean IC gain +0.0021 on 1d, improved on 52% of 23 dates. New multipliers: Performance (Month)|delta ×0.998, Average Volume|delta ×0.594, Short Float|delta ×1.746, Institutional Transactions|level ×1.383, Institutional Ownership|delta ×1.891, Insider Transactions|level ×0.909, Target Price|delta ×1.203, Analyst Recom|delta ×1.786, Profit Margin|delta ×1.055, EPS Surprise|level ×0.989, n_catalysts|level ×1.680

_Note: curved-polarity rules (rvol/rsi/sma/short/upside/debt curves) are never auto-adjusted; change those in score_rubric.py by hand with git history as the audit trail._
