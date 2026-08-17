# Weight learning — decision log

_Generated 2026-08-17 17:18 EDT_

- label dates per horizon: 1d: 7, 2d: 6, 3d: 5
- primary horizon for promotion test: **1d** (7 dates)
- existing overrides: {'Price|ret': 0.25, 'Performance (Month)|delta': 1.0797565412717471, 'Average Volume|delta': 0.7864432909155041, 'Relative Strength Index (14)|delta': 0.33994895881034404, 'Short Float|delta': 1.5048873942231655, 'Institutional Transactions|level': 1.414682722830413, 'Institutional Ownership|delta': 1.5769312185168642, 'Insider Transactions|level': 0.8707341041176773, 'Target Price|delta': 1.0124987493330437, 'Analyst Recom|delta': 1.3009105487944588, 'Sales Growth Quarter Over Quarter|level': 2.0, 'Sales Year Over Year TTM|level': 2.0, 'Profit Margin|delta': 0.8886522749830997, 'EPS Surprise|level': 0.9354864690632871, 'n_catalysts|level': 1.803172675870968}

## Per-rule aligned IC (direction corrected for polarity)

| Rule | Horizon | Mean aligned IC | Dates | Proposed × | Testable |
|---|---|---|---|---|---|
| Price|ret | 1d | -0.0642 | 6 | 0.250 | yes |
| Price|ret | 2d | -0.0983 | 5 | 0.250 | yes |
| Price|ret | 3d | +0.0006 | 4 | 0.250 | yes |
| Performance (Month)|delta | 1d | +0.0401 | 6 | 1.166 | yes |
| Performance (Month)|delta | 2d | -0.0262 | 5 | 1.023 | yes |
| Performance (Month)|delta | 3d | -0.0340 | 4 | 1.006 | yes |
| Average Volume|delta | 1d | -0.0068 | 6 | 0.776 | NO — logs only |
| Average Volume|delta | 2d | -0.0116 | 5 | 0.768 | NO — logs only |
| Average Volume|delta | 3d | -0.0169 | 4 | 0.760 | NO — logs only |
| Relative Strength Index (14)|delta | 1d | -0.0574 | 6 | 0.301 | yes |
| Relative Strength Index (14)|delta | 2d | -0.0906 | 5 | 0.278 | yes |
| Relative Strength Index (14)|delta | 3d | -0.0068 | 4 | 0.335 | yes |
| Short Float|delta | 1d | +0.0177 | 5 | 1.558 | NO — logs only |
| Short Float|delta | 2d | +0.0001 | 4 | 1.505 | NO — logs only |
| Short Float|delta | 3d | -0.0125 | 3 | 1.467 | NO — logs only |
| Institutional Transactions|level | 1d | +0.0241 | 7 | 1.483 | NO — logs only |
| Institutional Transactions|level | 2d | +0.0362 | 6 | 1.517 | NO — logs only |
| Institutional Transactions|level | 3d | +0.0417 | 5 | 1.533 | NO — logs only |
| Institutional Ownership|delta | 1d | +0.0198 | 6 | 1.639 | NO — logs only |
| Institutional Ownership|delta | 2d | +0.0207 | 5 | 1.642 | NO — logs only |
| Institutional Ownership|delta | 3d | +0.0237 | 4 | 1.652 | NO — logs only |
| Insider Transactions|level | 1d | -0.0232 | 7 | 0.830 | NO — logs only |
| Insider Transactions|level | 2d | -0.0273 | 6 | 0.823 | NO — logs only |
| Insider Transactions|level | 3d | -0.0357 | 5 | 0.808 | NO — logs only |
| Target Price|delta | 1d | +0.0085 | 6 | 1.030 | NO — logs only |
| Target Price|delta | 2d | +0.0064 | 5 | 1.025 | NO — logs only |
| Target Price|delta | 3d | +0.0112 | 4 | 1.035 | NO — logs only |
| Analyst Recom|delta | 1d | +0.0153 | 6 | 1.341 | NO — logs only |
| Analyst Recom|delta | 2d | +0.0051 | 5 | 1.314 | NO — logs only |
| Analyst Recom|delta | 3d | +0.0099 | 4 | 1.327 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 1d | +0.0500 | 7 | 2.000 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 2d | +0.0614 | 6 | 2.000 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 3d | +0.0772 | 5 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 1d | +0.0448 | 7 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 2d | +0.0621 | 6 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 3d | +0.0762 | 5 | 2.000 | NO — logs only |
| Profit Margin|delta | 1d | +0.0040 | 6 | 0.896 | NO — logs only |
| Profit Margin|delta | 2d | -0.0003 | 5 | 0.888 | NO — logs only |
| Profit Margin|delta | 3d | +0.0044 | 4 | 0.896 | NO — logs only |
| EPS Surprise|level | 1d | +0.0050 | 7 | 0.945 | NO — logs only |
| EPS Surprise|level | 2d | +0.0101 | 6 | 0.954 | NO — logs only |
| EPS Surprise|level | 3d | +0.0237 | 5 | 0.980 | NO — logs only |
| n_catalysts|level | 1d | +0.0244 | 7 | 1.891 | yes |
| n_catalysts|level | 2d | +0.0284 | 6 | 1.906 | yes |
| n_catalysts|level | 3d | +0.0357 | 5 | 1.932 | yes |
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
| 2026-08-07 | 1d | -0.0339 | -0.0175 | +0.0164 |
| 2026-08-07 | 2d | -0.0242 | -0.0130 | +0.0112 |
| 2026-08-07 | 3d | -0.0009 | +0.0010 | +0.0020 |
| 2026-08-10 | 1d | -0.0491 | -0.0279 | +0.0212 |
| 2026-08-10 | 2d | -0.0596 | -0.0354 | +0.0242 |
| 2026-08-10 | 3d | -0.1054 | -0.0900 | +0.0154 |
| 2026-08-11 | 1d | +0.1007 | +0.1114 | +0.0107 |
| 2026-08-11 | 2d | +0.0174 | +0.0159 | -0.0015 |
| 2026-08-11 | 3d | +0.0639 | +0.0588 | -0.0051 |
| 2026-08-12 | 1d | -0.0472 | -0.0425 | +0.0047 |
| 2026-08-12 | 2d | +0.0520 | +0.0504 | -0.0016 |
| 2026-08-12 | 3d | +0.0878 | +0.0738 | -0.0139 |
| 2026-08-13 | 1d | -0.0908 | -0.0774 | +0.0134 |
| 2026-08-13 | 2d | -0.1428 | -0.1280 | +0.0148 |
| 2026-08-14 | 1d | +0.1577 | +0.1614 | +0.0037 |

_Champion reconstruction check: mean |rebuilt price category − stored price_score| = 0.3333 (should be ~0; large values mean the learner's model of the engine has drifted from score_engine — distrust this run)._

## Decision

PROMOTED — challenger mean IC gain +0.0101 on 1d, improved on 100% of 7 dates. New multipliers: Performance (Month)|delta ×1.166, Average Volume|delta ×0.776, Relative Strength Index (14)|delta ×0.301, Short Float|delta ×1.558, Institutional Transactions|level ×1.483, Institutional Ownership|delta ×1.639, Insider Transactions|level ×0.830, Target Price|delta ×1.030, Analyst Recom|delta ×1.341, Profit Margin|delta ×0.896, EPS Surprise|level ×0.945, n_catalysts|level ×1.891

_Note: curved-polarity rules (rvol/rsi/sma/short/upside/debt curves) are never auto-adjusted; change those in score_rubric.py by hand with git history as the audit trail._
