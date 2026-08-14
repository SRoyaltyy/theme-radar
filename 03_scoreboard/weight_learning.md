# Weight learning — decision log

_Generated 2026-08-14 17:17 EDT_

- label dates per horizon: 1d: 6, 2d: 5, 3d: 4
- primary horizon for promotion test: **1d** (6 dates)
- existing overrides: {'Price|ret': 0.29272683324445287, 'Performance (Month)|delta': 1.0700234520405647, 'Average Volume|delta': 0.8072609742736847, 'Relative Strength Index (14)|delta': 0.47619737632065695, 'Short Float|delta': 1.3818772516930546, 'Institutional Transactions|level': 1.3036592858150235, 'Institutional Ownership|delta': 1.4974040975008407, 'Insider Transactions|level': 0.933695549851626, 'Target Price|delta': 0.9980625500420547, 'Analyst Recom|delta': 1.235762997242703, 'Sales Growth Quarter Over Quarter|level': 1.7809867581459398, 'Sales Year Over Year TTM|level': 1.7570521441500462, 'Profit Margin|delta': 0.8814432577905637, 'EPS Surprise|level': 0.9238154494799269, 'n_catalysts|level': 1.6252253723584686}

## Per-rule aligned IC (direction corrected for polarity)

| Rule | Horizon | Mean aligned IC | Dates | Proposed × | Testable |
|---|---|---|---|---|---|
| Price|ret | 1d | -0.0864 | 5 | 0.250 | yes |
| Price|ret | 2d | -0.0465 | 4 | 0.266 | yes |
| Price|ret | 3d | -0.0528 | 3 | 0.262 | yes |
| Performance (Month)|delta | 1d | +0.0023 | 5 | 1.075 | yes |
| Performance (Month)|delta | 2d | +0.0014 | 4 | 1.073 | yes |
| Performance (Month)|delta | 3d | -0.0418 | 3 | 0.981 | yes |
| Average Volume|delta | 1d | -0.0065 | 5 | 0.797 | NO — logs only |
| Average Volume|delta | 2d | -0.0131 | 4 | 0.786 | NO — logs only |
| Average Volume|delta | 3d | -0.0170 | 3 | 0.780 | NO — logs only |
| Relative Strength Index (14)|delta | 1d | -0.0775 | 5 | 0.402 | yes |
| Relative Strength Index (14)|delta | 2d | -0.0402 | 4 | 0.438 | yes |
| Relative Strength Index (14)|delta | 3d | -0.0567 | 3 | 0.422 | yes |
| Short Float|delta | 1d | +0.0218 | 4 | 1.442 | NO — logs only |
| Short Float|delta | 2d | +0.0107 | 3 | 1.412 | NO — logs only |
| Short Float|delta | 3d | -0.0139 | 2 | 1.343 | NO — logs only |
| Institutional Transactions|level | 1d | +0.0209 | 6 | 1.358 | NO — logs only |
| Institutional Transactions|level | 2d | +0.0259 | 5 | 1.371 | NO — logs only |
| Institutional Transactions|level | 3d | +0.0397 | 4 | 1.407 | NO — logs only |
| Institutional Ownership|delta | 1d | +0.0131 | 5 | 1.537 | NO — logs only |
| Institutional Ownership|delta | 2d | +0.0263 | 4 | 1.576 | NO — logs only |
| Institutional Ownership|delta | 3d | +0.0187 | 3 | 1.553 | NO — logs only |
| Insider Transactions|level | 1d | -0.0172 | 6 | 0.902 | NO — logs only |
| Insider Transactions|level | 2d | -0.0176 | 5 | 0.901 | NO — logs only |
| Insider Transactions|level | 3d | -0.0285 | 4 | 0.880 | NO — logs only |
| Target Price|delta | 1d | +0.0036 | 5 | 1.005 | NO — logs only |
| Target Price|delta | 2d | +0.0028 | 4 | 1.004 | NO — logs only |
| Target Price|delta | 3d | +0.0009 | 3 | 1.000 | NO — logs only |
| Analyst Recom|delta | 1d | +0.0130 | 5 | 1.268 | NO — logs only |
| Analyst Recom|delta | 2d | +0.0032 | 4 | 1.244 | NO — logs only |
| Analyst Recom|delta | 3d | +0.0099 | 3 | 1.260 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 1d | +0.0428 | 6 | 1.933 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 2d | +0.0507 | 5 | 1.962 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 3d | +0.0677 | 4 | 2.000 | NO — logs only |
| Sales Year Over Year TTM|level | 1d | +0.0434 | 6 | 1.910 | NO — logs only |
| Sales Year Over Year TTM|level | 2d | +0.0559 | 5 | 1.953 | NO — logs only |
| Sales Year Over Year TTM|level | 3d | +0.0713 | 4 | 2.000 | NO — logs only |
| Profit Margin|delta | 1d | +0.0020 | 5 | 0.885 | NO — logs only |
| Profit Margin|delta | 2d | -0.0012 | 4 | 0.879 | NO — logs only |
| Profit Margin|delta | 3d | -0.0016 | 3 | 0.879 | NO — logs only |
| EPS Surprise|level | 1d | +0.0031 | 6 | 0.930 | NO — logs only |
| EPS Surprise|level | 2d | +0.0155 | 5 | 0.953 | NO — logs only |
| EPS Surprise|level | 3d | +0.0186 | 4 | 0.958 | NO — logs only |
| n_catalysts|level | 1d | +0.0267 | 6 | 1.712 | yes |
| n_catalysts|level | 2d | +0.0247 | 5 | 1.705 | yes |
| n_catalysts|level | 3d | +0.0408 | 4 | 1.758 | yes |
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
| 2026-08-07 | 1d | -0.0339 | -0.0189 | +0.0151 |
| 2026-08-07 | 2d | -0.0242 | -0.0140 | +0.0101 |
| 2026-08-07 | 3d | -0.0009 | +0.0016 | +0.0025 |
| 2026-08-10 | 1d | -0.0491 | -0.0279 | +0.0212 |
| 2026-08-10 | 2d | -0.0596 | -0.0352 | +0.0244 |
| 2026-08-10 | 3d | -0.1054 | -0.0900 | +0.0154 |
| 2026-08-11 | 1d | +0.1007 | +0.1105 | +0.0098 |
| 2026-08-11 | 2d | +0.0174 | +0.0155 | -0.0018 |
| 2026-08-11 | 3d | +0.0639 | +0.0590 | -0.0049 |
| 2026-08-12 | 1d | -0.0472 | -0.0446 | +0.0026 |
| 2026-08-12 | 2d | +0.0520 | +0.0515 | -0.0005 |
| 2026-08-13 | 1d | -0.0908 | -0.0782 | +0.0126 |

_Champion reconstruction check: mean |rebuilt price category − stored price_score| = 0.3505 (should be ~0; large values mean the learner's model of the engine has drifted from score_engine — distrust this run)._

## Decision

PROMOTED — challenger mean IC gain +0.0103 on 1d, improved on 100% of 6 dates. New multipliers: Price|ret ×0.250, Performance (Month)|delta ×1.075, Average Volume|delta ×0.797, Relative Strength Index (14)|delta ×0.402, Short Float|delta ×1.442, Institutional Transactions|level ×1.358, Institutional Ownership|delta ×1.537, Insider Transactions|level ×0.902, Target Price|delta ×1.005, Analyst Recom|delta ×1.268, Sales Growth Quarter Over Quarter|level ×1.933, Sales Year Over Year TTM|level ×1.910, Profit Margin|delta ×0.885, EPS Surprise|level ×0.930, n_catalysts|level ×1.712

_Note: curved-polarity rules (rvol/rsi/sma/short/upside/debt curves) are never auto-adjusted; change those in score_rubric.py by hand with git history as the audit trail._
