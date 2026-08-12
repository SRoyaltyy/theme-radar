# Weight learning — decision log

_Generated 2026-08-12 03:57 EDT_

- label dates per horizon: 1d: 3, 2d: 2, 3d: 1
- primary horizon for promotion test: **1d** (3 dates)
- existing overrides: {'Price|ret': 0.8168884895314386, 'Performance (Month)|delta': 0.9854753763889705, 'Average Volume|delta': 0.9678375230223384, 'Relative Strength Index (14)|delta': 0.8893189375899748, 'Short Float|delta': 1.0469529805016375, 'Institutional Transactions|level': 1.038355418876544, 'Institutional Ownership|delta': 1.0678268675384883, 'Insider Transactions|level': 0.9970727265190981, 'Target Price|delta': 0.9976607050971793, 'Analyst Recom|delta': 1.0299675031986535, 'Sales Growth Quarter Over Quarter|level': 1.0876246295036764, 'Sales Year Over Year TTM|level': 1.084169450075137, 'Profit Margin|delta': 0.9793302148725767, 'EPS Surprise|level': 0.9822602529364043, 'n_catalysts|level': 1.0770897616741502}

## Per-rule aligned IC (direction corrected for polarity)

| Rule | Horizon | Mean aligned IC | Dates | Proposed × | Testable |
|---|---|---|---|---|---|
| Price|ret | 1d | -0.0916 | 2 | 0.667 | yes |
| Price|ret | 2d | -0.0711 | 1 | 0.701 | yes |
| Performance (Month)|delta | 1d | -0.0073 | 2 | 0.971 | yes |
| Performance (Month)|delta | 2d | +0.0107 | 1 | 1.006 | yes |
| Average Volume|delta | 1d | -0.0161 | 2 | 0.937 | NO — logs only |
| Average Volume|delta | 2d | -0.0146 | 1 | 0.940 | NO — logs only |
| Relative Strength Index (14)|delta | 1d | -0.0553 | 2 | 0.791 | yes |
| Relative Strength Index (14)|delta | 2d | -0.0437 | 1 | 0.812 | yes |
| Short Float|delta | 1d | +0.0235 | 1 | 1.096 | NO — logs only |
| Institutional Transactions|level | 1d | +0.0192 | 3 | 1.078 | NO — logs only |
| Institutional Transactions|level | 2d | +0.0268 | 2 | 1.094 | NO — logs only |
| Institutional Transactions|level | 3d | +0.0453 | 1 | 1.133 | NO — logs only |
| Institutional Ownership|delta | 1d | +0.0339 | 2 | 1.140 | NO — logs only |
| Institutional Ownership|delta | 2d | -0.0107 | 1 | 1.045 | NO — logs only |
| Insider Transactions|level | 1d | -0.0015 | 3 | 0.994 | NO — logs only |
| Insider Transactions|level | 2d | +0.0173 | 2 | 1.032 | NO — logs only |
| Insider Transactions|level | 3d | -0.0005 | 1 | 0.996 | NO — logs only |
| Target Price|delta | 1d | -0.0012 | 2 | 0.995 | NO — logs only |
| Target Price|delta | 2d | +0.0047 | 1 | 1.007 | NO — logs only |
| Analyst Recom|delta | 1d | +0.0150 | 2 | 1.061 | NO — logs only |
| Analyst Recom|delta | 2d | +0.0096 | 1 | 1.050 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 1d | +0.0438 | 3 | 1.183 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 2d | +0.0571 | 2 | 1.212 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 3d | +0.0643 | 1 | 1.227 | NO — logs only |
| Sales Year Over Year TTM|level | 1d | +0.0421 | 3 | 1.175 | NO — logs only |
| Sales Year Over Year TTM|level | 2d | +0.0529 | 2 | 1.199 | NO — logs only |
| Sales Year Over Year TTM|level | 3d | +0.0607 | 1 | 1.216 | NO — logs only |
| Profit Margin|delta | 1d | -0.0103 | 2 | 0.959 | NO — logs only |
| Profit Margin|delta | 2d | -0.0046 | 1 | 0.970 | NO — logs only |
| EPS Surprise|level | 1d | -0.0089 | 3 | 0.965 | NO — logs only |
| EPS Surprise|level | 2d | -0.0123 | 2 | 0.958 | NO — logs only |
| EPS Surprise|level | 3d | -0.0133 | 1 | 0.956 | NO — logs only |
| n_catalysts|level | 1d | +0.0385 | 3 | 1.160 | yes |
| n_catalysts|level | 2d | +0.0253 | 2 | 1.132 | yes |
| n_catalysts|level | 3d | +0.0530 | 1 | 1.191 | yes |
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
| 2026-08-07 | 1d | -0.0339 | -0.0305 | +0.0034 |
| 2026-08-07 | 2d | -0.0242 | -0.0210 | +0.0032 |
| 2026-08-10 | 1d | -0.0491 | -0.0416 | +0.0075 |

_Champion reconstruction check: mean |rebuilt price category − stored price_score| = 0.1308 (should be ~0; large values mean the learner's model of the engine has drifted from score_engine — distrust this run)._

## Decision

PROMOTED — challenger mean IC gain +0.0038 on 1d, improved on 100% of 3 dates. New multipliers: Price|ret ×0.667, Performance (Month)|delta ×0.971, Average Volume|delta ×0.937, Relative Strength Index (14)|delta ×0.791, Short Float|delta ×1.096, Institutional Transactions|level ×1.078, Institutional Ownership|delta ×1.140, Insider Transactions|level ×0.994, Target Price|delta ×0.995, Analyst Recom|delta ×1.061, Sales Growth Quarter Over Quarter|level ×1.183, Sales Year Over Year TTM|level ×1.175, Profit Margin|delta ×0.959, EPS Surprise|level ×0.965, n_catalysts|level ×1.160

_Note: curved-polarity rules (rvol/rsi/sma/short/upside/debt curves) are never auto-adjusted; change those in score_rubric.py by hand with git history as the audit trail._
