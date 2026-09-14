# Weight learning — decision log

_Generated 2026-09-14 19:37 EDT_

- label dates per horizon: 1d: 25, 2d: 24, 3d: 23
- primary horizon for promotion test: **1d** (25 dates)
- existing overrides: {'Price|ret': 0.25, 'Performance (Month)|delta': 0.9522534748533565, 'Average Volume|delta': 0.5828050628315926, 'Relative Strength Index (14)|delta': 0.25, 'Short Float|delta': 1.7489449022404506, 'Institutional Transactions|level': 1.3644690596660152, 'Institutional Ownership|delta': 1.901146279329447, 'Insider Transactions|level': 0.9046593363206851, 'Target Price|delta': 1.2097479324346823, 'Analyst Recom|delta': 1.8262040969156572, 'Sales Growth Quarter Over Quarter|level': 2.0, 'Sales Year Over Year TTM|level': 2.0, 'Profit Margin|delta': 1.0664480177871105, 'EPS Surprise|level': 1.0054828229591395, 'n_catalysts|level': 1.655747986138051}

## Per-rule aligned IC (direction corrected for polarity)

| Rule | Horizon | Mean aligned IC | Dates | Proposed × | Testable |
|---|---|---|---|---|---|
| Price|ret | 1d | -0.0553 | 23 | 0.250 | yes |
| Price|ret | 2d | -0.0410 | 22 | 0.250 | yes |
| Price|ret | 3d | -0.0445 | 21 | 0.250 | yes |
| Performance (Month)|delta | 1d | -0.0192 | 23 | 0.916 | yes |
| Performance (Month)|delta | 2d | -0.0326 | 22 | 0.890 | yes |
| Performance (Month)|delta | 3d | -0.0608 | 21 | 0.836 | yes |
| Average Volume|delta | 1d | -0.0065 | 23 | 0.575 | NO — logs only |
| Average Volume|delta | 2d | -0.0082 | 22 | 0.573 | NO — logs only |
| Average Volume|delta | 3d | -0.0102 | 21 | 0.571 | NO — logs only |
| Relative Strength Index (14)|delta | 1d | -0.0477 | 23 | 0.250 | yes |
| Relative Strength Index (14)|delta | 2d | -0.0468 | 22 | 0.250 | yes |
| Relative Strength Index (14)|delta | 3d | -0.0401 | 21 | 0.250 | yes |
| Short Float|delta | 1d | -0.0000 | 22 | 1.749 | NO — logs only |
| Short Float|delta | 2d | -0.0036 | 21 | 1.736 | NO — logs only |
| Short Float|delta | 3d | -0.0075 | 20 | 1.723 | NO — logs only |
| Institutional Transactions|level | 1d | -0.0080 | 25 | 1.343 | NO — logs only |
| Institutional Transactions|level | 2d | -0.0077 | 24 | 1.343 | NO — logs only |
| Institutional Transactions|level | 3d | -0.0085 | 23 | 1.341 | NO — logs only |
| Institutional Ownership|delta | 1d | +0.0030 | 23 | 1.913 | NO — logs only |
| Institutional Ownership|delta | 2d | +0.0047 | 22 | 1.919 | NO — logs only |
| Institutional Ownership|delta | 3d | +0.0031 | 21 | 1.913 | NO — logs only |
| Insider Transactions|level | 1d | -0.0030 | 25 | 0.899 | NO — logs only |
| Insider Transactions|level | 2d | +0.0009 | 24 | 0.906 | NO — logs only |
| Insider Transactions|level | 3d | +0.0048 | 23 | 0.913 | NO — logs only |
| Target Price|delta | 1d | +0.0025 | 23 | 1.216 | NO — logs only |
| Target Price|delta | 2d | +0.0035 | 22 | 1.218 | NO — logs only |
| Target Price|delta | 3d | +0.0031 | 21 | 1.217 | NO — logs only |
| Analyst Recom|delta | 1d | +0.0095 | 23 | 1.861 | NO — logs only |
| Analyst Recom|delta | 2d | -0.0005 | 22 | 1.824 | NO — logs only |
| Analyst Recom|delta | 3d | -0.0033 | 21 | 1.814 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 1d | +0.0146 | 25 | 2.000 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 2d | +0.0188 | 24 | 2.000 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 3d | +0.0239 | 23 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 1d | +0.0122 | 25 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 2d | +0.0167 | 24 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 3d | +0.0207 | 23 | 2.000 | NO — logs only |
| Profit Margin|delta | 1d | +0.0055 | 23 | 1.078 | NO — logs only |
| Profit Margin|delta | 2d | +0.0032 | 22 | 1.073 | NO — logs only |
| Profit Margin|delta | 3d | +0.0087 | 21 | 1.085 | NO — logs only |
| EPS Surprise|level | 1d | +0.0086 | 25 | 1.023 | NO — logs only |
| EPS Surprise|level | 2d | +0.0106 | 24 | 1.027 | NO — logs only |
| EPS Surprise|level | 3d | +0.0099 | 23 | 1.025 | NO — logs only |
| n_catalysts|level | 1d | -0.0114 | 25 | 1.618 | yes |
| n_catalysts|level | 2d | -0.0177 | 24 | 1.597 | yes |
| n_catalysts|level | 3d | -0.0204 | 23 | 1.588 | yes |
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
| 2026-08-07 | 3d | -0.0009 | +0.0010 | +0.0020 |
| 2026-08-10 | 1d | -0.0491 | -0.0306 | +0.0185 |
| 2026-08-10 | 2d | -0.0596 | -0.0374 | +0.0222 |
| 2026-08-10 | 3d | -0.1054 | -0.0918 | +0.0136 |
| 2026-08-11 | 1d | +0.1007 | +0.1054 | +0.0047 |
| 2026-08-11 | 2d | +0.0174 | +0.0114 | -0.0060 |
| 2026-08-11 | 3d | +0.0639 | +0.0580 | -0.0059 |
| 2026-08-12 | 1d | -0.0472 | -0.0461 | +0.0011 |
| 2026-08-12 | 2d | +0.0520 | +0.0520 | -0.0000 |
| 2026-08-12 | 3d | +0.0878 | +0.0796 | -0.0081 |
| 2026-08-13 | 1d | -0.0908 | -0.0864 | +0.0044 |
| 2026-08-13 | 2d | -0.1428 | -0.1365 | +0.0063 |
| 2026-08-13 | 3d | -0.1672 | -0.1638 | +0.0034 |
| 2026-08-14 | 1d | +0.1577 | +0.1508 | -0.0069 |
| 2026-08-14 | 2d | -0.1560 | -0.1576 | -0.0016 |
| 2026-08-14 | 3d | -0.1404 | -0.1410 | -0.0007 |
| 2026-08-17 | 1d | -0.2097 | -0.2075 | +0.0022 |
| 2026-08-17 | 2d | -0.1365 | -0.1355 | +0.0010 |
| 2026-08-17 | 3d | -0.1034 | -0.1035 | -0.0001 |
| 2026-08-18 | 1d | +0.0486 | +0.0470 | -0.0016 |
| 2026-08-18 | 2d | +0.0270 | +0.0247 | -0.0023 |
| 2026-08-18 | 3d | +0.0058 | +0.0073 | +0.0015 |
| 2026-08-19 | 1d | +0.0108 | +0.0049 | -0.0059 |
| 2026-08-19 | 2d | +0.0519 | +0.0544 | +0.0025 |
| 2026-08-19 | 3d | +0.1772 | +0.1709 | -0.0062 |
| 2026-08-20 | 1d | -0.0007 | +0.0048 | +0.0055 |
| 2026-08-20 | 2d | +0.0530 | +0.0567 | +0.0038 |
| 2026-08-20 | 3d | +0.0387 | +0.0447 | +0.0060 |
| 2026-08-21 | 1d | -0.0802 | -0.0811 | -0.0009 |
| 2026-08-21 | 2d | +0.0158 | +0.0137 | -0.0021 |
| 2026-08-21 | 3d | -0.0723 | -0.0735 | -0.0012 |
| 2026-08-24 | 1d | +0.0056 | -0.0103 | -0.0159 |
| 2026-08-24 | 2d | -0.0285 | -0.0455 | -0.0170 |
| 2026-08-24 | 3d | -0.0880 | -0.0892 | -0.0012 |
| 2026-08-25 | 1d | -0.0503 | -0.0659 | -0.0155 |
| 2026-08-25 | 2d | -0.1093 | -0.1164 | -0.0071 |
| 2026-08-25 | 3d | -0.0661 | -0.0767 | -0.0107 |
| 2026-08-26 | 1d | -0.0710 | -0.0616 | +0.0094 |
| 2026-08-26 | 2d | -0.0146 | -0.0141 | +0.0005 |
| 2026-08-26 | 3d | -0.0019 | +0.0028 | +0.0047 |
| 2026-08-28 | 1d | -0.0442 | -0.0364 | +0.0078 |
| 2026-08-28 | 2d | +0.0258 | +0.0234 | -0.0024 |
| 2026-08-28 | 3d | +0.0108 | +0.0203 | +0.0095 |
| 2026-08-31 | 1d | -0.0065 | -0.0069 | -0.0004 |
| 2026-08-31 | 2d | +0.0398 | +0.0430 | +0.0032 |
| 2026-08-31 | 3d | +0.1004 | +0.1060 | +0.0056 |
| 2026-09-01 | 1d | -0.0847 | -0.0533 | +0.0315 |
| 2026-09-01 | 2d | -0.2394 | -0.1960 | +0.0434 |
| 2026-09-01 | 3d | -0.2756 | -0.2380 | +0.0376 |
| 2026-09-02 | 1d | -0.0842 | -0.0601 | +0.0242 |
| 2026-09-02 | 2d | -0.1304 | -0.1017 | +0.0287 |
| 2026-09-02 | 3d | -0.1700 | -0.1535 | +0.0165 |
| 2026-09-03 | 1d | -0.0656 | -0.0840 | -0.0184 |
| 2026-09-03 | 2d | -0.0607 | -0.0862 | -0.0255 |
| 2026-09-03 | 3d | -0.1049 | -0.1239 | -0.0190 |
| 2026-09-04 | 1d | -0.0292 | -0.0339 | -0.0047 |
| 2026-09-04 | 2d | -0.0659 | -0.0716 | -0.0056 |
| 2026-09-04 | 3d | -0.1272 | -0.1316 | -0.0044 |
| 2026-09-08 | 1d | -0.0849 | -0.0849 | +0.0000 |
| 2026-09-08 | 2d | -0.1276 | -0.1276 | +0.0000 |
| 2026-09-08 | 3d | -0.0619 | -0.0619 | +0.0000 |
| 2026-09-09 | 1d | -0.0163 | -0.0198 | -0.0036 |
| 2026-09-09 | 2d | +0.0188 | +0.0158 | -0.0030 |
| 2026-09-09 | 3d | -0.0591 | -0.0593 | -0.0001 |
| 2026-09-10 | 1d | -0.0932 | -0.0911 | +0.0021 |
| 2026-09-10 | 2d | +0.1308 | +0.1228 | -0.0079 |
| 2026-09-11 | 1d | -0.0419 | -0.0464 | -0.0045 |

_Champion reconstruction check: mean |rebuilt price category − stored price_score| = 0.2051 (should be ~0; large values mean the learner's model of the engine has drifted from score_engine — distrust this run)._

## Decision

PROMOTED — challenger mean IC gain +0.0017 on 1d, improved on 52% of 25 dates. New multipliers: Performance (Month)|delta ×0.916, Average Volume|delta ×0.575, Short Float|delta ×1.749, Institutional Transactions|level ×1.343, Institutional Ownership|delta ×1.913, Insider Transactions|level ×0.899, Target Price|delta ×1.216, Analyst Recom|delta ×1.861, Profit Margin|delta ×1.078, EPS Surprise|level ×1.023, n_catalysts|level ×1.618

_Note: curved-polarity rules (rvol/rsi/sma/short/upside/debt curves) are never auto-adjusted; change those in score_rubric.py by hand with git history as the audit trail._
