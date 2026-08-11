# Weight learning — decision log

_Generated 2026-08-11 17:37 EDT_

- label dates per horizon: 1d: 3, 2d: 2, 3d: 1
- primary horizon for promotion test: **1d** (3 dates)
- existing overrides: none (champion = base rubric)

## Per-rule aligned IC (direction corrected for polarity)

| Rule | Horizon | Mean aligned IC | Dates | Proposed × | Testable |
|---|---|---|---|---|---|
| Price|ret | 1d | -0.0916 | 2 | 0.817 | yes |
| Price|ret | 2d | -0.0711 | 1 | 0.858 | yes |
| Performance (Month)|delta | 1d | -0.0073 | 2 | 0.985 | yes |
| Performance (Month)|delta | 2d | +0.0107 | 1 | 1.021 | yes |
| Average Volume|delta | 1d | -0.0161 | 2 | 0.968 | NO — logs only |
| Average Volume|delta | 2d | -0.0146 | 1 | 0.971 | NO — logs only |
| Relative Strength Index (14)|delta | 1d | -0.0553 | 2 | 0.889 | yes |
| Relative Strength Index (14)|delta | 2d | -0.0437 | 1 | 0.913 | yes |
| Short Float|delta | 1d | +0.0235 | 1 | 1.047 | NO — logs only |
| Institutional Transactions|level | 1d | +0.0192 | 3 | 1.038 | NO — logs only |
| Institutional Transactions|level | 2d | +0.0268 | 2 | 1.054 | NO — logs only |
| Institutional Transactions|level | 3d | +0.0453 | 1 | 1.091 | NO — logs only |
| Institutional Ownership|delta | 1d | +0.0339 | 2 | 1.068 | NO — logs only |
| Institutional Ownership|delta | 2d | -0.0107 | 1 | 0.979 | NO — logs only |
| Insider Transactions|level | 1d | -0.0015 | 3 | 0.997 | NO — logs only |
| Insider Transactions|level | 2d | +0.0173 | 2 | 1.035 | NO — logs only |
| Insider Transactions|level | 3d | -0.0005 | 1 | 0.999 | NO — logs only |
| Target Price|delta | 1d | -0.0012 | 2 | 0.998 | NO — logs only |
| Target Price|delta | 2d | +0.0047 | 1 | 1.009 | NO — logs only |
| Analyst Recom|delta | 1d | +0.0150 | 2 | 1.030 | NO — logs only |
| Analyst Recom|delta | 2d | +0.0096 | 1 | 1.019 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 1d | +0.0438 | 3 | 1.088 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 2d | +0.0571 | 2 | 1.114 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 3d | +0.0643 | 1 | 1.129 | NO — logs only |
| Sales Year Over Year TTM|level | 1d | +0.0421 | 3 | 1.084 | NO — logs only |
| Sales Year Over Year TTM|level | 2d | +0.0529 | 2 | 1.106 | NO — logs only |
| Sales Year Over Year TTM|level | 3d | +0.0607 | 1 | 1.121 | NO — logs only |
| Profit Margin|delta | 1d | -0.0103 | 2 | 0.979 | NO — logs only |
| Profit Margin|delta | 2d | -0.0046 | 1 | 0.991 | NO — logs only |
| EPS Surprise|level | 1d | -0.0089 | 3 | 0.982 | NO — logs only |
| EPS Surprise|level | 2d | -0.0123 | 2 | 0.975 | NO — logs only |
| EPS Surprise|level | 3d | -0.0133 | 1 | 0.973 | NO — logs only |
| n_catalysts|level | 1d | +0.0385 | 3 | 1.077 | yes |
| n_catalysts|level | 2d | +0.0253 | 2 | 1.051 | yes |
| n_catalysts|level | 3d | +0.0530 | 1 | 1.106 | yes |
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
| 2026-08-07 | 1d | -0.0339 | -0.0312 | +0.0027 |
| 2026-08-07 | 2d | -0.0242 | -0.0212 | +0.0030 |
| 2026-08-10 | 1d | -0.0491 | -0.0441 | +0.0050 |

_Champion reconstruction check: mean |rebuilt price category − stored price_score| = 0.0023 (should be ~0; large values mean the learner's model of the engine has drifted from score_engine — distrust this run)._

## Decision

PROMOTED — challenger mean IC gain +0.0027 on 1d, improved on 100% of 3 dates. New multipliers: Price|ret ×0.817, Performance (Month)|delta ×0.985, Average Volume|delta ×0.968, Relative Strength Index (14)|delta ×0.889, Short Float|delta ×1.047, Institutional Transactions|level ×1.038, Institutional Ownership|delta ×1.068, Insider Transactions|level ×0.997, Target Price|delta ×0.998, Analyst Recom|delta ×1.030, Sales Growth Quarter Over Quarter|level ×1.088, Sales Year Over Year TTM|level ×1.084, Profit Margin|delta ×0.979, EPS Surprise|level ×0.982, n_catalysts|level ×1.077

_Note: curved-polarity rules (rvol/rsi/sma/short/upside/debt curves) are never auto-adjusted; change those in score_rubric.py by hand with git history as the audit trail._
