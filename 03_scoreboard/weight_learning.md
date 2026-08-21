# Weight learning — decision log

_Generated 2026-08-21 17:15 EDT_

- label dates per horizon: 1d: 11, 2d: 10, 3d: 9
- primary horizon for promotion test: **1d** (11 dates)
- existing overrides: {'Price|ret': 0.25, 'Performance (Month)|delta': 1.2021138619148117, 'Average Volume|delta': 0.7433748717738127, 'Relative Strength Index (14)|delta': 0.25, 'Short Float|delta': 1.6262798617505525, 'Institutional Transactions|level': 1.5711829752577813, 'Institutional Ownership|delta': 1.7631919986061904, 'Insider Transactions|level': 0.8121796810351195, 'Target Price|delta': 1.0738791335383366, 'Analyst Recom|delta': 1.408478541539685, 'Sales Growth Quarter Over Quarter|level': 2.0, 'Sales Year Over Year TTM|level': 2.0, 'Profit Margin|delta': 0.924521665455172, 'EPS Surprise|level': 0.9540338726781075, 'n_catalysts|level': 1.9236761333736816}

## Per-rule aligned IC (direction corrected for polarity)

| Rule | Horizon | Mean aligned IC | Dates | Proposed × | Testable |
|---|---|---|---|---|---|
| Price|ret | 1d | -0.0550 | 10 | 0.250 | yes |
| Price|ret | 2d | -0.0427 | 9 | 0.250 | yes |
| Price|ret | 3d | -0.0371 | 8 | 0.250 | yes |
| Performance (Month)|delta | 1d | +0.0056 | 10 | 1.216 | yes |
| Performance (Month)|delta | 2d | -0.0443 | 9 | 1.096 | yes |
| Performance (Month)|delta | 3d | -0.0738 | 8 | 1.025 | yes |
| Average Volume|delta | 1d | -0.0065 | 10 | 0.734 | NO — logs only |
| Average Volume|delta | 2d | -0.0153 | 9 | 0.721 | NO — logs only |
| Average Volume|delta | 3d | -0.0145 | 8 | 0.722 | NO — logs only |
| Relative Strength Index (14)|delta | 1d | -0.0418 | 10 | 0.250 | yes |
| Relative Strength Index (14)|delta | 2d | -0.0455 | 9 | 0.250 | yes |
| Relative Strength Index (14)|delta | 3d | -0.0316 | 8 | 0.250 | yes |
| Short Float|delta | 1d | +0.0009 | 9 | 1.629 | NO — logs only |
| Short Float|delta | 2d | -0.0061 | 8 | 1.606 | NO — logs only |
| Short Float|delta | 3d | -0.0129 | 7 | 1.584 | NO — logs only |
| Institutional Transactions|level | 1d | +0.0009 | 11 | 1.574 | NO — logs only |
| Institutional Transactions|level | 2d | +0.0062 | 10 | 1.591 | NO — logs only |
| Institutional Transactions|level | 3d | +0.0118 | 9 | 1.608 | NO — logs only |
| Institutional Ownership|delta | 1d | +0.0078 | 10 | 1.791 | NO — logs only |
| Institutional Ownership|delta | 2d | +0.0079 | 9 | 1.791 | NO — logs only |
| Institutional Ownership|delta | 3d | +0.0082 | 8 | 1.792 | NO — logs only |
| Insider Transactions|level | 1d | +0.0042 | 11 | 0.819 | NO — logs only |
| Insider Transactions|level | 2d | +0.0100 | 10 | 0.828 | NO — logs only |
| Insider Transactions|level | 3d | +0.0089 | 9 | 0.827 | NO — logs only |
| Target Price|delta | 1d | +0.0057 | 10 | 1.086 | NO — logs only |
| Target Price|delta | 2d | +0.0061 | 9 | 1.087 | NO — logs only |
| Target Price|delta | 3d | +0.0048 | 8 | 1.084 | NO — logs only |
| Analyst Recom|delta | 1d | +0.0052 | 10 | 1.423 | NO — logs only |
| Analyst Recom|delta | 2d | -0.0041 | 9 | 1.397 | NO — logs only |
| Analyst Recom|delta | 3d | -0.0037 | 8 | 1.398 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 1d | +0.0223 | 11 | 2.000 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 2d | +0.0262 | 10 | 2.000 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 3d | +0.0323 | 9 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 1d | +0.0200 | 11 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 2d | +0.0273 | 10 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 3d | +0.0333 | 9 | 2.000 | NO — logs only |
| Profit Margin|delta | 1d | +0.0071 | 10 | 0.938 | NO — logs only |
| Profit Margin|delta | 2d | +0.0010 | 9 | 0.926 | NO — logs only |
| Profit Margin|delta | 3d | +0.0086 | 8 | 0.940 | NO — logs only |
| EPS Surprise|level | 1d | -0.0025 | 11 | 0.949 | NO — logs only |
| EPS Surprise|level | 2d | -0.0014 | 10 | 0.951 | NO — logs only |
| EPS Surprise|level | 3d | -0.0003 | 9 | 0.953 | NO — logs only |
| n_catalysts|level | 1d | +0.0007 | 11 | 1.926 | yes |
| n_catalysts|level | 2d | -0.0072 | 10 | 1.896 | yes |
| n_catalysts|level | 3d | -0.0091 | 9 | 1.888 | yes |
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
| 2026-08-07 | 1d | -0.0339 | -0.0166 | +0.0173 |
| 2026-08-07 | 2d | -0.0242 | -0.0140 | +0.0102 |
| 2026-08-07 | 3d | -0.0009 | -0.0013 | -0.0003 |
| 2026-08-10 | 1d | -0.0491 | -0.0312 | +0.0179 |
| 2026-08-10 | 2d | -0.0596 | -0.0399 | +0.0198 |
| 2026-08-10 | 3d | -0.1054 | -0.0934 | +0.0119 |
| 2026-08-11 | 1d | +0.1007 | +0.1123 | +0.0115 |
| 2026-08-11 | 2d | +0.0174 | +0.0170 | -0.0003 |
| 2026-08-11 | 3d | +0.0639 | +0.0585 | -0.0054 |
| 2026-08-12 | 1d | -0.0472 | -0.0422 | +0.0050 |
| 2026-08-12 | 2d | +0.0520 | +0.0491 | -0.0029 |
| 2026-08-12 | 3d | +0.0878 | +0.0707 | -0.0171 |
| 2026-08-13 | 1d | -0.0908 | -0.0855 | +0.0053 |
| 2026-08-13 | 2d | -0.1428 | -0.1335 | +0.0093 |
| 2026-08-13 | 3d | -0.1672 | -0.1637 | +0.0035 |
| 2026-08-14 | 1d | +0.1577 | +0.1658 | +0.0081 |
| 2026-08-14 | 2d | -0.1560 | -0.1597 | -0.0038 |
| 2026-08-14 | 3d | -0.1404 | -0.1398 | +0.0006 |
| 2026-08-17 | 1d | -0.2097 | -0.2095 | +0.0002 |
| 2026-08-17 | 2d | -0.1365 | -0.1364 | +0.0002 |
| 2026-08-17 | 3d | -0.1034 | -0.1017 | +0.0017 |
| 2026-08-18 | 1d | +0.0486 | +0.0487 | +0.0001 |
| 2026-08-18 | 2d | +0.0270 | +0.0275 | +0.0005 |
| 2026-08-18 | 3d | +0.0058 | +0.0059 | +0.0000 |
| 2026-08-19 | 1d | +0.0108 | +0.0113 | +0.0005 |
| 2026-08-19 | 2d | +0.0519 | +0.0510 | -0.0009 |
| 2026-08-20 | 1d | -0.0007 | -0.0006 | +0.0000 |

_Champion reconstruction check: mean |rebuilt price category − stored price_score| = 0.2322 (should be ~0; large values mean the learner's model of the engine has drifted from score_engine — distrust this run)._

## Decision

PROMOTED — challenger mean IC gain +0.0060 on 1d, improved on 100% of 11 dates. New multipliers: Performance (Month)|delta ×1.216, Average Volume|delta ×0.734, Short Float|delta ×1.629, Institutional Transactions|level ×1.574, Institutional Ownership|delta ×1.791, Insider Transactions|level ×0.819, Target Price|delta ×1.086, Analyst Recom|delta ×1.423, Profit Margin|delta ×0.938, EPS Surprise|level ×0.949, n_catalysts|level ×1.926

_Note: curved-polarity rules (rvol/rsi/sma/short/upside/debt curves) are never auto-adjusted; change those in score_rubric.py by hand with git history as the audit trail._
