# Weight learning — decision log

_Generated 2026-08-12 04:39 EDT_

- label dates per horizon: 1d: 3, 2d: 2, 3d: 1
- primary horizon for promotion test: **1d** (3 dates)
- existing overrides: {'Price|ret': 0.5451152474423314, 'Performance (Month)|delta': 0.9570559590573052, 'Average Volume|delta': 0.9065825741751846, 'Relative Strength Index (14)|delta': 0.703351829547986, 'Short Float|delta': 1.147576200352282, 'Institutional Transactions|level': 1.119536097221462, 'Institutional Ownership|delta': 1.2175940909118894, 'Insider Transactions|level': 0.9912438612637885, 'Target Price|delta': 0.99299851939214, 'Analyst Recom|delta': 1.0926235756934901, 'Sales Growth Quarter Over Quarter|level': 1.286580904136132, 'Sales Year Over Year TTM|level': 1.274358137363079, 'Profit Margin|delta': 0.9392635337100178, 'EPS Surprise|level': 0.9477192720128296, 'n_catalysts|level': 1.249555910540207}

## Per-rule aligned IC (direction corrected for polarity)

| Rule | Horizon | Mean aligned IC | Dates | Proposed × | Testable |
|---|---|---|---|---|---|
| Price|ret | 1d | -0.0916 | 2 | 0.445 | yes |
| Price|ret | 2d | -0.0711 | 1 | 0.468 | yes |
| Performance (Month)|delta | 1d | -0.0073 | 2 | 0.943 | yes |
| Performance (Month)|delta | 2d | +0.0107 | 1 | 0.977 | yes |
| Average Volume|delta | 1d | -0.0161 | 2 | 0.877 | NO — logs only |
| Average Volume|delta | 2d | -0.0146 | 1 | 0.880 | NO — logs only |
| Relative Strength Index (14)|delta | 1d | -0.0553 | 2 | 0.626 | yes |
| Relative Strength Index (14)|delta | 2d | -0.0437 | 1 | 0.642 | yes |
| Short Float|delta | 1d | +0.0235 | 1 | 1.201 | NO — logs only |
| Institutional Transactions|level | 1d | +0.0192 | 3 | 1.162 | NO — logs only |
| Institutional Transactions|level | 2d | +0.0268 | 2 | 1.180 | NO — logs only |
| Institutional Transactions|level | 3d | +0.0453 | 1 | 1.221 | NO — logs only |
| Institutional Ownership|delta | 1d | +0.0339 | 2 | 1.300 | NO — logs only |
| Institutional Ownership|delta | 2d | -0.0107 | 1 | 1.192 | NO — logs only |
| Insider Transactions|level | 1d | -0.0015 | 3 | 0.988 | NO — logs only |
| Insider Transactions|level | 2d | +0.0173 | 2 | 1.026 | NO — logs only |
| Insider Transactions|level | 3d | -0.0005 | 1 | 0.990 | NO — logs only |
| Target Price|delta | 1d | -0.0012 | 2 | 0.991 | NO — logs only |
| Target Price|delta | 2d | +0.0047 | 1 | 1.002 | NO — logs only |
| Analyst Recom|delta | 1d | +0.0150 | 2 | 1.125 | NO — logs only |
| Analyst Recom|delta | 2d | +0.0096 | 1 | 1.114 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 1d | +0.0438 | 3 | 1.399 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 2d | +0.0571 | 2 | 1.433 | NO — logs only |
| Sales Growth Quarter Over Quarter|level | 3d | +0.0643 | 1 | 1.452 | NO — logs only |
| Sales Year Over Year TTM|level | 1d | +0.0421 | 3 | 1.382 | NO — logs only |
| Sales Year Over Year TTM|level | 2d | +0.0529 | 2 | 1.409 | NO — logs only |
| Sales Year Over Year TTM|level | 3d | +0.0607 | 1 | 1.429 | NO — logs only |
| Profit Margin|delta | 1d | -0.0103 | 2 | 0.920 | NO — logs only |
| Profit Margin|delta | 2d | -0.0046 | 1 | 0.931 | NO — logs only |
| EPS Surprise|level | 1d | -0.0089 | 3 | 0.931 | NO — logs only |
| EPS Surprise|level | 2d | -0.0123 | 2 | 0.924 | NO — logs only |
| EPS Surprise|level | 3d | -0.0133 | 1 | 0.923 | NO — logs only |
| n_catalysts|level | 1d | +0.0385 | 3 | 1.346 | yes |
| n_catalysts|level | 2d | +0.0253 | 2 | 1.313 | yes |
| n_catalysts|level | 3d | +0.0530 | 1 | 1.382 | yes |
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
| 2026-08-07 | 1d | -0.0339 | -0.0264 | +0.0075 |
| 2026-08-07 | 2d | -0.0242 | -0.0186 | +0.0056 |
| 2026-08-10 | 1d | -0.0491 | -0.0356 | +0.0135 |

_Champion reconstruction check: mean |rebuilt price category − stored price_score| = 0.3239 (should be ~0; large values mean the learner's model of the engine has drifted from score_engine — distrust this run)._

## Decision

PROMOTED — challenger mean IC gain +0.0072 on 1d, improved on 100% of 3 dates. New multipliers: Price|ret ×0.445, Performance (Month)|delta ×0.943, Average Volume|delta ×0.877, Relative Strength Index (14)|delta ×0.626, Short Float|delta ×1.201, Institutional Transactions|level ×1.162, Institutional Ownership|delta ×1.300, Insider Transactions|level ×0.988, Target Price|delta ×0.991, Analyst Recom|delta ×1.125, Sales Growth Quarter Over Quarter|level ×1.399, Sales Year Over Year TTM|level ×1.382, Profit Margin|delta ×0.920, EPS Surprise|level ×0.931, n_catalysts|level ×1.346

_Note: curved-polarity rules (rvol/rsi/sma/short/upside/debt curves) are never auto-adjusted; change those in score_rubric.py by hand with git history as the audit trail._
