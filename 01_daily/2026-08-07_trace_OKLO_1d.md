# Score audit — OKLO — horizon 1d

- **Pair:** 2026-08-06
- **Company:** Oklo Inc
- **Sector / Industry:** Utilities / Utilities - Independent Power Producers
- **Total score:** +8.25  (score_100=32.7, conf=1.0)
- **True return ret_H:** 14.77%
- **Status:** NEUTRAL / DOWNTREND / ELEVATED / OK
- **Flags:** —

## Status inputs (levels on current snapshot)

| Metric | Value | Role |
|---|---|---|
| Performance (Week) | 24.7 | bucket input |
| Performance (Month) | -1.73 | bucket input |
| RSI (14) | 55.41 | bucket input |
| 50-DMA % | -5.57 | bucket input |
| 200-DMA % | -33.34 | bucket input |
| Short Float | 19.13 | bucket input |
| upside_pct | 67.16 | bucket input |

## Per-rule audit

| Field | Kind | Now | Then | Raw | Direction | Signal | W | Points | Skip / override |
|---|---|---|---|---|---|---|---|---|---|
| Price | ret | 48.42 | 42.19 | +14.77% | up | +1.00 | 3.0 | +3.00 | — |
| Performance (Month) | delta | -1.73 | -10.77 | 9.04 | up | +1.00 | 1.5 | +1.50 | — |
| Relative Volume | level | 1.83 | 0.93 | 1.83 | up | +0.50 | 1.5 | +0.75 | — |
| Average Volume | delta | n/a | n/a | — | — | +0.00 | 0.8 | +0.00 | horizon 1d not in ['1w', '1m'] |
| Relative Strength Index (14) | level | 55.41 | 44.07 | 55.41 | up | +1.00 | 1.0 | +1.00 | — |
| Relative Strength Index (14) | delta | 55.41 | 44.07 | 11.34 | up | +1.00 | 0.5 | +0.50 | — |
| 50-Day Simple Moving Average | level | n/a | n/a | — | — | +0.00 | 1.0 | +0.00 | horizon 1d not in ['1w', '1m'] |
| 200-Day Simple Moving Average | level | n/a | n/a | — | — | +0.00 | 1.0 | +0.00 | horizon 1d not in ['1m'] |
| Volatility (Month) | level | n/a | n/a | — | — | +0.00 | 0.5 | +0.00 | horizon 1d not in ['1w', '1m'] |
| Short Float | level | n/a | n/a | — | — | +0.00 | 1.5 | +0.00 | horizon 1d not in ['1w', '1m'] |
| Short Float | delta | n/a | n/a | — | — | +0.00 | 1.2 | +0.00 | horizon 1d not in ['1m'] |
| Institutional Transactions | level | n/a | n/a | — | — | +0.00 | 1.5 | +0.00 | horizon 1d not in ['1w', '1m'] |
| Institutional Ownership | delta | n/a | n/a | — | — | +0.00 | 1.0 | +0.00 | horizon 1d not in ['1m'] |
| Insider Transactions | level | n/a | n/a | — | — | +0.00 | 1.0 | +0.00 | horizon 1d not in ['1w', '1m'] |
| upside_pct | level | 67.16 | n/a | 67.16 | up | +1.00 | 1.0 | +1.00 | — |
| Target Price | delta | n/a | n/a | — | — | +0.00 | 1.5 | +0.00 | horizon 1d not in ['1w', '1m'] |
| Analyst Recom | delta | n/a | n/a | — | — | +0.00 | 1.0 | +0.00 | horizon 1d not in ['1w', '1m'] |
| Sales Growth Quarter Over Quarter | level | n/a | n/a | — | — | +0.00 | 1.2 | +0.00 | horizon 1d not in ['1m'] |
| Sales Year Over Year TTM | level | n/a | n/a | — | — | +0.00 | 1.0 | +0.00 | horizon 1d not in ['1m'] |
| Profit Margin | delta | n/a | n/a | — | — | +0.00 | 1.0 | +0.00 | horizon 1d not in ['1m'] |
| EPS Surprise | level | n/a | n/a | — | — | +0.00 | 1.0 | +0.00 | horizon 1d not in ['1w', '1m'] |
| Total Debt/Equity | level | n/a | n/a | — | — | +0.00 | 0.5 | +0.00 | horizon 1d not in ['1m'] |
| n_catalysts | level | 1 | n/a | 1 | up | +1.00 | 0.5 | +0.50 | — |

## Category sums (before → after gates)

| Category | Pre-gate | Post-gate |
|---|---|---|
| price | +4.50 | +4.50 |
| flow | +0.75 | +0.75 |
| technical | +1.50 | +1.50 |
| positioning | +0.00 | +0.00 |
| valuation | +1.00 | +1.00 |
| fundamental | +0.00 | +0.00 |
| catalyst | +0.50 | +0.50 |

## Gates fired

_None._

## Arithmetic

- Price now / then: 48.42 / 42.19
- n_pos=7 w_pos=8.25 | n_neg=0 w_neg=0.0
- **total_score = Σ post-gate categories = +8.25**
