# Weight learning — decision log

_Generated 2026-08-28 01:03 EDT_

- label dates per horizon: 1d: 15, 2d: 14, 3d: 13
- primary horizon for promotion test: **1d** (15 dates)
- existing overrides: {'Price|ret': 0.25, 'Performance (Month)|delta': 1.2504723000554405, 'Average Volume|delta': 0.7188635806981882, 'Relative Strength Index (14)|delta': 0.25, 'Short Float|delta': 1.6432386732767064, 'Institutional Transactions|level': 1.537625075659352, 'Institutional Ownership|delta': 1.8179292960757962, 'Insider Transactions|level': 0.8520633901978005, 'Target Price|delta': 1.1194146356620076, 'Analyst Recom|delta': 1.4710490378206726, 'Sales Growth Quarter Over Quarter|level': 2.0, 'Sales Year Over Year TTM|level': 2.0, 'Profit Margin|delta': 0.964751167066774, 'EPS Surprise|level': 0.9357479046079779, 'n_catalysts|level': 1.8957340105674199}

## Per-rule aligned IC (direction corrected for polarity)

| Rule | Horizon | Mean aligned IC | Dates | Proposed × | Testable |
|---|---|---|---|---|---|
| Price|ret | 1d | -0.0821 | 14 | 0.250 | yes |
| Price|ret | 2d | -0.0499 | 13 | 0.250 | yes |
| Price|ret | 3d | -0.0441 | 12 | 0.250 | yes |
| Performance (Month)|delta | 1d | +0.0172 | 14 | 1.293 | yes |
| Performance (Month)|delta | 2d | -0.0174 | 13 | 1.207 | yes |
| Performance (Month)|delta | 3d | -0.0324 | 12 | 1.169 | yes |
| Average Volume|delta | 1d | -0.0078 | 14 | 0.708 | NO — logs only |
| Average Volume|delta | 2d | -0.0105 | 13 | 0.704 | NO — logs only |
| Average Volume|delta | 3d | -0.0081 | 12 | 0.707 | NO — logs only |
| Relative Strength Index (14)|delta | 1d | -0.0629 | 14 | 0.250 | yes |
| Relative Strength Index (14)|delta | 2d | -0.0556 | 13 | 0.250 | yes |
| Relative Strength Index (14)|delta | 3d | -0.0386 | 12 | 0.250 | yes |
| Short Float|delta | 1d | +0.0049 | 13 | 1.659 | NO — logs only |
| Short Float|delta | 2d | -0.0057 | 12 | 1.624 | NO — logs only |
| Short Float|delta | 3d | -0.0132 | 11 | 1.600 | NO — logs only |
| Institutional Transactions|level | 1d | +0.0017 | 15 | 1.543 | NO — logs only |
| Institutional Transactions|level | 2d | +0.0023 | 14 | 1.545 | NO — logs only |
| Institutional Transactions|level | 3d | +0.0034 | 13 | 1.548 | NO — logs only |
| Institutional Ownership|delta | 1d | +0.0050 | 14 | 1.836 | NO — logs only |
| Institutional Ownership|delta | 2d | +0.0071 | 13 | 1.844 | NO — logs only |
| Institutional Ownership|delta | 3d | +0.0018 | 12 | 1.824 | NO — logs only |
| Insider Transactions|level | 1d | -0.0001 | 15 | 0.852 | NO — logs only |
| Insider Transactions|level | 2d | +0.0046 | 14 | 0.860 | NO — logs only |
| Insider Transactions|level | 3d | +0.0135 | 13 | 0.875 | NO — logs only |
| Target Price|delta | 1d | +0.0051 | 14 | 1.131 | NO — logs only |
| Target Price|delta | 2d | +0.0045 | 13 | 1.130 | NO — logs only |
| Target Price|delta | 3d | +0.0017 | 12 | 1.123 | NO — logs only |
| Analyst Recom|delta | 1d | +0.0075 | 14 | 1.493 | NO — logs only |
| Analyst Recom|delta | 2d | +0.0009 | 13 | 1.474 | NO — logs only |
| Analyst Recom|delta | 3d | -0.0042 | 12 | 1.459 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 1d | +0.0216 | 15 | 2.000 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 2d | +0.0223 | 14 | 2.000 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 3d | +0.0237 | 13 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 1d | +0.0220 | 15 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 2d | +0.0247 | 14 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 3d | +0.0264 | 13 | 2.000 | NO — logs only |
| Profit Margin|delta | 1d | +0.0026 | 14 | 0.970 | NO — logs only |
| Profit Margin|delta | 2d | -0.0003 | 13 | 0.964 | NO — logs only |
| Profit Margin|delta | 3d | +0.0062 | 12 | 0.977 | NO — logs only |
| EPS Surprise|level | 1d | -0.0015 | 15 | 0.933 | NO — logs only |
| EPS Surprise|level | 2d | -0.0035 | 14 | 0.929 | NO — logs only |
| EPS Surprise|level | 3d | -0.0070 | 13 | 0.923 | NO — logs only |
| n_catalysts|level | 1d | +0.0009 | 15 | 1.899 | yes |
| n_catalysts|level | 2d | -0.0037 | 14 | 1.882 | yes |
| n_catalysts|level | 3d | -0.0072 | 13 | 1.869 | yes |
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
| 2026-08-06 | 1d | +0.0958 | +0.0963 | +0.0005 |
| 2026-08-06 | 2d | +0.0636 | +0.0636 | +0.0000 |
| 2026-08-06 | 3d | +0.0815 | +0.0818 | +0.0003 |
| 2026-08-07 | 1d | -0.0339 | -0.0165 | +0.0175 |
| 2026-08-07 | 2d | -0.0242 | -0.0139 | +0.0102 |
| 2026-08-07 | 3d | -0.0009 | -0.0015 | -0.0006 |
| 2026-08-10 | 1d | -0.0491 | -0.0313 | +0.0178 |
| 2026-08-10 | 2d | -0.0596 | -0.0400 | +0.0197 |
| 2026-08-10 | 3d | -0.1054 | -0.0934 | +0.0119 |
| 2026-08-11 | 1d | +0.1007 | +0.1125 | +0.0118 |
| 2026-08-11 | 2d | +0.0174 | +0.0173 | -0.0001 |
| 2026-08-11 | 3d | +0.0639 | +0.0586 | -0.0053 |
| 2026-08-12 | 1d | -0.0472 | -0.0417 | +0.0056 |
| 2026-08-12 | 2d | +0.0520 | +0.0493 | -0.0027 |
| 2026-08-12 | 3d | +0.0878 | +0.0702 | -0.0175 |
| 2026-08-13 | 1d | -0.0908 | -0.0857 | +0.0051 |
| 2026-08-13 | 2d | -0.1428 | -0.1337 | +0.0091 |
| 2026-08-13 | 3d | -0.1672 | -0.1637 | +0.0035 |
| 2026-08-14 | 1d | +0.1577 | +0.1665 | +0.0088 |
| 2026-08-14 | 2d | -0.1560 | -0.1597 | -0.0037 |
| 2026-08-14 | 3d | -0.1404 | -0.1397 | +0.0007 |
| 2026-08-17 | 1d | -0.2097 | -0.2089 | +0.0008 |
| 2026-08-17 | 2d | -0.1365 | -0.1364 | +0.0002 |
| 2026-08-17 | 3d | -0.1034 | -0.1008 | +0.0026 |
| 2026-08-18 | 1d | +0.0486 | +0.0484 | -0.0002 |
| 2026-08-18 | 2d | +0.0270 | +0.0278 | +0.0008 |
| 2026-08-18 | 3d | +0.0058 | +0.0050 | -0.0008 |
| 2026-08-19 | 1d | +0.0108 | +0.0127 | +0.0020 |
| 2026-08-19 | 2d | +0.0519 | +0.0501 | -0.0018 |
| 2026-08-19 | 3d | +0.1772 | +0.1792 | +0.0021 |
| 2026-08-20 | 1d | -0.0007 | -0.0022 | -0.0015 |
| 2026-08-20 | 2d | +0.0530 | +0.0515 | -0.0014 |
| 2026-08-20 | 3d | +0.0387 | +0.0373 | -0.0015 |
| 2026-08-21 | 1d | -0.0802 | -0.0792 | +0.0010 |
| 2026-08-21 | 2d | +0.0158 | +0.0168 | +0.0009 |
| 2026-08-21 | 3d | -0.0723 | -0.0717 | +0.0006 |
| 2026-08-24 | 1d | +0.0056 | +0.0095 | +0.0038 |
| 2026-08-24 | 2d | -0.0285 | -0.0246 | +0.0038 |
| 2026-08-24 | 3d | -0.0867 | -0.0823 | +0.0044 |
| 2026-08-25 | 1d | -0.0503 | -0.0482 | +0.0021 |
| 2026-08-25 | 2d | +0.0041 | +0.0051 | +0.0010 |
| 2026-08-26 | 1d | +0.0468 | +0.0490 | +0.0022 |

_Champion reconstruction check: mean |rebuilt price category − stored price_score| = 0.1904 (should be ~0; large values mean the learner's model of the engine has drifted from score_engine — distrust this run)._

## Decision

PROMOTED — challenger mean IC gain +0.0052 on 1d, improved on 87% of 15 dates. New multipliers: Performance (Month)|delta ×1.293, Average Volume|delta ×0.708, Short Float|delta ×1.659, Institutional Transactions|level ×1.543, Institutional Ownership|delta ×1.836, Insider Transactions|level ×0.852, Target Price|delta ×1.131, Analyst Recom|delta ×1.493, Profit Margin|delta ×0.970, EPS Surprise|level ×0.933, n_catalysts|level ×1.899

_Note: curved-polarity rules (rvol/rsi/sma/short/upside/debt curves) are never auto-adjusted; change those in score_rubric.py by hand with git history as the audit trail._
