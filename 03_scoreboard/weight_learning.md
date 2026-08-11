# Weight learning — decision log

_Generated 2026-08-11 03:42 EDT_

- label dates per horizon: 1d: 2, 2d: 1, 3d: 0
- primary horizon for promotion test: **1d** (2 dates)
- existing overrides: none (champion = base rubric)

## Per-rule aligned IC (direction corrected for polarity)

| Rule | Horizon | Mean aligned IC | Dates | Proposed × | Testable |
|---|---|---|---|---|---|
| Price|ret | 1d | -0.0831 | 1 | 0.834 | yes |
| Performance (Month)|delta | 1d | +0.0216 | 1 | 1.043 | yes |
| Average Volume|delta | 1d | -0.0267 | 1 | 0.947 | NO — logs only |
| Relative Strength Index (14)|delta | 1d | -0.0388 | 1 | 0.922 | yes |
| Institutional Transactions|level | 1d | +0.0080 | 2 | 1.016 | NO — logs only |
| Institutional Transactions|level | 2d | +0.0251 | 1 | 1.050 | NO — logs only |
| Institutional Ownership|delta | 1d | +0.0116 | 1 | 1.023 | NO — logs only |
| Insider Transactions|level | 1d | +0.0054 | 2 | 1.011 | NO — logs only |
| Insider Transactions|level | 2d | +0.0096 | 1 | 1.019 | NO — logs only |
| Target Price|delta | 1d | +0.0256 | 1 | 1.051 | NO — logs only |
| Analyst Recom|delta | 1d | +0.0223 | 1 | 1.045 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 1d | +0.0527 | 2 | 1.105 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 2d | +0.0584 | 1 | 1.117 | NO — logs only |
| Sales Year Over Year TTM|level | 1d | +0.0492 | 2 | 1.098 | NO — logs only |
| Sales Year Over Year TTM|level | 2d | +0.0621 | 1 | 1.124 | NO — logs only |
| Profit Margin|delta | 1d | +0.0095 | 1 | 1.019 | NO — logs only |
| EPS Surprise|level | 1d | -0.0018 | 2 | 0.996 | NO — logs only |
| EPS Surprise|level | 2d | -0.0120 | 1 | 0.976 | NO — logs only |
| n_catalysts|level | 1d | +0.0274 | 2 | 1.055 | yes |
| n_catalysts|level | 2d | +0.0281 | 1 | 1.056 | yes |
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
| 2026-08-07 | 1d | -0.0339 | -0.0305 | +0.0035 |

_Champion reconstruction check: mean |rebuilt price category − stored price_score| = 0.0016 (should be ~0; large values mean the learner's model of the engine has drifted from score_engine — distrust this run)._

## Decision

NO PROMOTION — only 2 distinct label date(s) on 1d; need >= 3. Learning starts once more daily snapshots accumulate.

_Note: curved-polarity rules (rvol/rsi/sma/short/upside/debt curves) are never auto-adjusted; change those in score_rubric.py by hand with git history as the audit trail._
