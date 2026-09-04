# Weight learning — decision log

_Generated 2026-09-04 18:40 EDT_

- label dates per horizon: 1d: 20, 2d: 19, 3d: 18
- primary horizon for promotion test: **1d** (20 dates)
- existing overrides: {'Price|ret': 0.25, 'Performance (Month)|delta': 1.179330137965961, 'Average Volume|delta': 0.6427673995366704, 'Relative Strength Index (14)|delta': 0.25, 'Short Float|delta': 1.7011959320795165, 'Institutional Transactions|level': 1.4312732156669221, 'Institutional Ownership|delta': 1.8489762709187614, 'Insider Transactions|level': 0.8965074132750548, 'Target Price|delta': 1.1817236621792233, 'Analyst Recom|delta': 1.6331367854878502, 'Sales Growth Quarter Over Quarter|level': 2.0, 'Sales Year Over Year TTM|level': 2.0, 'Profit Margin|delta': 1.0075621139156976, 'EPS Surprise|level': 0.9617963717131666, 'n_catalysts|level': 1.7445954657351996}

## Per-rule aligned IC (direction corrected for polarity)

| Rule | Horizon | Mean aligned IC | Dates | Proposed × | Testable |
|---|---|---|---|---|---|
| Price|ret | 1d | -0.0615 | 19 | 0.250 | yes |
| Price|ret | 2d | -0.0537 | 18 | 0.250 | yes |
| Price|ret | 3d | -0.0417 | 17 | 0.250 | yes |
| Performance (Month)|delta | 1d | -0.0221 | 19 | 1.127 | yes |
| Performance (Month)|delta | 2d | -0.0476 | 18 | 1.067 | yes |
| Performance (Month)|delta | 3d | -0.0496 | 17 | 1.062 | yes |
| Average Volume|delta | 1d | -0.0103 | 19 | 0.630 | NO — logs only |
| Average Volume|delta | 2d | -0.0137 | 18 | 0.625 | NO — logs only |
| Average Volume|delta | 3d | -0.0111 | 17 | 0.629 | NO — logs only |
| Relative Strength Index (14)|delta | 1d | -0.0511 | 19 | 0.250 | yes |
| Relative Strength Index (14)|delta | 2d | -0.0555 | 18 | 0.250 | yes |
| Relative Strength Index (14)|delta | 3d | -0.0325 | 17 | 0.250 | yes |
| Short Float|delta | 1d | +0.0022 | 18 | 1.709 | NO — logs only |
| Short Float|delta | 2d | -0.0037 | 17 | 1.689 | NO — logs only |
| Short Float|delta | 3d | -0.0100 | 16 | 1.667 | NO — logs only |
| Institutional Transactions|level | 1d | -0.0054 | 20 | 1.416 | NO — logs only |
| Institutional Transactions|level | 2d | -0.0062 | 19 | 1.414 | NO — logs only |
| Institutional Transactions|level | 3d | -0.0082 | 18 | 1.408 | NO — logs only |
| Institutional Ownership|delta | 1d | +0.0023 | 19 | 1.857 | NO — logs only |
| Institutional Ownership|delta | 2d | +0.0096 | 18 | 1.885 | NO — logs only |
| Institutional Ownership|delta | 3d | +0.0019 | 17 | 1.856 | NO — logs only |
| Insider Transactions|level | 1d | +0.0024 | 20 | 0.901 | NO — logs only |
| Insider Transactions|level | 2d | +0.0079 | 19 | 0.911 | NO — logs only |
| Insider Transactions|level | 3d | +0.0132 | 18 | 0.920 | NO — logs only |
| Target Price|delta | 1d | +0.0027 | 19 | 1.188 | NO — logs only |
| Target Price|delta | 2d | +0.0049 | 18 | 1.193 | NO — logs only |
| Target Price|delta | 3d | +0.0028 | 17 | 1.188 | NO — logs only |
| Analyst Recom|delta | 1d | +0.0122 | 19 | 1.673 | NO — logs only |
| Analyst Recom|delta | 2d | -0.0002 | 18 | 1.633 | NO — logs only |
| Analyst Recom|delta | 3d | -0.0044 | 17 | 1.619 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 1d | +0.0148 | 20 | 2.000 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 2d | +0.0171 | 19 | 2.000 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 3d | +0.0187 | 18 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 1d | +0.0138 | 20 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 2d | +0.0196 | 19 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 3d | +0.0206 | 18 | 2.000 | NO — logs only |
| Profit Margin|delta | 1d | +0.0056 | 19 | 1.019 | NO — logs only |
| Profit Margin|delta | 2d | +0.0013 | 18 | 1.010 | NO — logs only |
| Profit Margin|delta | 3d | +0.0061 | 17 | 1.020 | NO — logs only |
| EPS Surprise|level | 1d | +0.0034 | 20 | 0.968 | NO — logs only |
| EPS Surprise|level | 2d | +0.0038 | 19 | 0.969 | NO — logs only |
| EPS Surprise|level | 3d | +0.0030 | 18 | 0.968 | NO — logs only |
| n_catalysts|level | 1d | -0.0059 | 20 | 1.724 | yes |
| n_catalysts|level | 2d | -0.0148 | 19 | 1.693 | yes |
| n_catalysts|level | 3d | -0.0215 | 18 | 1.670 | yes |
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
| 2026-08-07 | 1d | -0.0339 | -0.0194 | +0.0145 |
| 2026-08-07 | 2d | -0.0242 | -0.0158 | +0.0084 |
| 2026-08-07 | 3d | -0.0009 | -0.0008 | +0.0001 |
| 2026-08-10 | 1d | -0.0491 | -0.0313 | +0.0178 |
| 2026-08-10 | 2d | -0.0596 | -0.0393 | +0.0203 |
| 2026-08-10 | 3d | -0.1054 | -0.0931 | +0.0123 |
| 2026-08-11 | 1d | +0.1007 | +0.1091 | +0.0084 |
| 2026-08-11 | 2d | +0.0174 | +0.0148 | -0.0026 |
| 2026-08-11 | 3d | +0.0639 | +0.0582 | -0.0057 |
| 2026-08-12 | 1d | -0.0472 | -0.0435 | +0.0038 |
| 2026-08-12 | 2d | +0.0520 | +0.0505 | -0.0015 |
| 2026-08-12 | 3d | +0.0878 | +0.0739 | -0.0138 |
| 2026-08-13 | 1d | -0.0908 | -0.0859 | +0.0049 |
| 2026-08-13 | 2d | -0.1428 | -0.1356 | +0.0072 |
| 2026-08-13 | 3d | -0.1672 | -0.1634 | +0.0037 |
| 2026-08-14 | 1d | +0.1577 | +0.1596 | +0.0020 |
| 2026-08-14 | 2d | -0.1560 | -0.1588 | -0.0029 |
| 2026-08-14 | 3d | -0.1404 | -0.1407 | -0.0003 |
| 2026-08-17 | 1d | -0.2097 | -0.2098 | -0.0000 |
| 2026-08-17 | 2d | -0.1365 | -0.1359 | +0.0006 |
| 2026-08-17 | 3d | -0.1034 | -0.1026 | +0.0008 |
| 2026-08-18 | 1d | +0.0486 | +0.0489 | +0.0003 |
| 2026-08-18 | 2d | +0.0270 | +0.0269 | -0.0001 |
| 2026-08-18 | 3d | +0.0058 | +0.0066 | +0.0008 |
| 2026-08-19 | 1d | +0.0108 | +0.0093 | -0.0014 |
| 2026-08-19 | 2d | +0.0519 | +0.0518 | -0.0001 |
| 2026-08-19 | 3d | +0.1772 | +0.1765 | -0.0007 |
| 2026-08-20 | 1d | -0.0007 | +0.0012 | +0.0019 |
| 2026-08-20 | 2d | +0.0530 | +0.0536 | +0.0006 |
| 2026-08-20 | 3d | +0.0387 | +0.0406 | +0.0019 |
| 2026-08-21 | 1d | -0.0802 | -0.0824 | -0.0021 |
| 2026-08-21 | 2d | +0.0158 | +0.0137 | -0.0021 |
| 2026-08-21 | 3d | -0.0723 | -0.0737 | -0.0014 |
| 2026-08-24 | 1d | +0.0056 | +0.0010 | -0.0046 |
| 2026-08-24 | 2d | -0.0285 | -0.0333 | -0.0048 |
| 2026-08-24 | 3d | -0.0880 | -0.0900 | -0.0019 |
| 2026-08-25 | 1d | -0.0503 | -0.0550 | -0.0047 |
| 2026-08-25 | 2d | -0.1093 | -0.1139 | -0.0046 |
| 2026-08-25 | 3d | -0.0661 | -0.0714 | -0.0054 |
| 2026-08-26 | 1d | -0.0710 | -0.0712 | -0.0002 |
| 2026-08-26 | 2d | -0.0146 | -0.0172 | -0.0026 |
| 2026-08-26 | 3d | -0.0019 | -0.0033 | -0.0014 |
| 2026-08-28 | 1d | -0.0442 | -0.0423 | +0.0019 |
| 2026-08-28 | 2d | +0.0258 | +0.0237 | -0.0021 |
| 2026-08-28 | 3d | +0.0108 | +0.0136 | +0.0028 |
| 2026-08-31 | 1d | -0.0065 | -0.0082 | -0.0017 |
| 2026-08-31 | 2d | +0.0398 | +0.0407 | +0.0010 |
| 2026-08-31 | 3d | +0.1004 | +0.1016 | +0.0012 |
| 2026-09-01 | 1d | -0.0847 | -0.0731 | +0.0117 |
| 2026-09-01 | 2d | -0.2394 | -0.2253 | +0.0141 |
| 2026-09-01 | 3d | -0.2756 | -0.2622 | +0.0133 |
| 2026-09-02 | 1d | -0.0842 | -0.0791 | +0.0052 |
| 2026-09-02 | 2d | -0.1304 | -0.1226 | +0.0078 |
| 2026-09-03 | 1d | -0.0656 | -0.0687 | -0.0031 |

_Champion reconstruction check: mean |rebuilt price category − stored price_score| = 0.1453 (should be ~0; large values mean the learner's model of the engine has drifted from score_engine — distrust this run)._

## Decision

PROMOTED — challenger mean IC gain +0.0027 on 1d, improved on 55% of 20 dates. New multipliers: Performance (Month)|delta ×1.127, Average Volume|delta ×0.630, Short Float|delta ×1.709, Institutional Transactions|level ×1.416, Institutional Ownership|delta ×1.857, Insider Transactions|level ×0.901, Target Price|delta ×1.188, Analyst Recom|delta ×1.673, Profit Margin|delta ×1.019, EPS Surprise|level ×0.968, n_catalysts|level ×1.724

_Note: curved-polarity rules (rvol/rsi/sma/short/upside/debt curves) are never auto-adjusted; change those in score_rubric.py by hand with git history as the audit trail._
