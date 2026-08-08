# Score audit — BBAI — horizon 1d

- **Pair:** 2026-08-06
- **Company:** BigBear.ai Holdings Inc
- **Sector / Industry:** Technology / Information Technology Services
- **Total score:** +5.80  (score_100=23.0, conf=0.8)
- **True return ret_H:** 8.64%
- **Status:** NEUTRAL / DOWNTREND / HIGH_SHORT / OK
- **Flags:** UNCONFIRMED_RALLY

## Status inputs (levels on current snapshot)

| Metric | Value | Role |
|---|---|---|
| Performance (Week) | 17.2 | bucket input |
| Performance (Month) | -1.51 | bucket input |
| RSI (14) | 54.93 | bucket input |
| 50-DMA % | -8.32 | bucket input |
| 200-DMA % | -29.26 | bucket input |
| Short Float | 30.78 | bucket input |
| upside_pct | 22.32 | bucket input |

## Per-rule audit

| Field | Kind | Now | Then | Raw | Direction | Signal | W | Points | Skip / override |
|---|---|---|---|---|---|---|---|---|---|
| Price | ret | 3.27 | 3.01 | +8.64% | up | +1.00 | 3.0 | +3.00 | — |
| Performance (Month) | delta | -1.51 | -9.06 | 7.55 | up | +1.00 | 1.5 | +1.50 | — |
| Relative Volume | level | 0.94 | 0.68 | 0.94 | up | +0.00 | 1.5 | +0.00 | — |
| Average Volume | delta | n/a | n/a | — | — | +0.00 | 0.8 | +0.00 | horizon 1d not in ['1w', '1m'] |
| Relative Strength Index (14) | level | 54.93 | 46.53 | 54.93 | up | +1.00 | 1.0 | +1.00 | — |
| Relative Strength Index (14) | delta | 54.93 | 46.53 | 8.4 | up | +1.00 | 0.5 | +0.50 | — |
| 50-Day Simple Moving Average | level | n/a | n/a | — | — | +0.00 | 1.0 | +0.00 | horizon 1d not in ['1w', '1m'] |
| 200-Day Simple Moving Average | level | n/a | n/a | — | — | +0.00 | 1.0 | +0.00 | horizon 1d not in ['1m'] |
| Volatility (Month) | level | n/a | n/a | — | — | +0.00 | 0.5 | +0.00 | horizon 1d not in ['1w', '1m'] |
| Short Float | level | n/a | n/a | — | — | +0.00 | 1.5 | +0.00 | horizon 1d not in ['1w', '1m'] |
| Short Float | delta | n/a | n/a | — | — | +0.00 | 1.2 | +0.00 | horizon 1d not in ['1m'] |
| Institutional Transactions | level | n/a | n/a | — | — | +0.00 | 1.5 | +0.00 | horizon 1d not in ['1w', '1m'] |
| Institutional Ownership | delta | n/a | n/a | — | — | +0.00 | 1.0 | +0.00 | horizon 1d not in ['1m'] |
| Insider Transactions | level | n/a | n/a | — | — | +0.00 | 1.0 | +0.00 | horizon 1d not in ['1w', '1m'] |
| upside_pct | level | 22.32 | n/a | 22.32 | up | +0.30 | 1.0 | +0.30 | — |
| Target Price | delta | n/a | n/a | — | — | +0.00 | 1.5 | +0.00 | horizon 1d not in ['1w', '1m'] |
| Analyst Recom | delta | n/a | n/a | — | — | +0.00 | 1.0 | +0.00 | horizon 1d not in ['1w', '1m'] |
| Sales Growth Quarter Over Quarter | level | n/a | n/a | — | — | +0.00 | 1.2 | +0.00 | horizon 1d not in ['1m'] |
| Sales Year Over Year TTM | level | n/a | n/a | — | — | +0.00 | 1.0 | +0.00 | horizon 1d not in ['1m'] |
| Profit Margin | delta | n/a | n/a | — | — | +0.00 | 1.0 | +0.00 | horizon 1d not in ['1m'] |
| EPS Surprise | level | n/a | n/a | — | — | +0.00 | 1.0 | +0.00 | horizon 1d not in ['1w', '1m'] |
| Total Debt/Equity | level | n/a | n/a | — | — | +0.00 | 0.5 | +0.00 | horizon 1d not in ['1m'] |
| n_catalysts | level | 0 | n/a | 0 | down | -1.00 | 0.5 | -0.50 | — |

## Category sums (before → after gates)

| Category | Pre-gate | Post-gate |
|---|---|---|
| price | +4.50 | +4.50 |
| flow | +0.00 | +0.00 |
| technical | +1.50 | +1.50 |
| positioning | +0.00 | +0.00 |
| valuation | +0.30 | +0.30 |
| fundamental | +0.00 | +0.00 |
| catalyst | -0.50 | -0.50 |

## Gates fired

- UNCONFIRMED_RALLY: inst_tx=-3.17<0 while ret>0 → conf×0.8

## Arithmetic

- Price now / then: 3.27 / 3.01
- n_pos=5 w_pos=6.3 | n_neg=1 w_neg=0.5
- **total_score = Σ post-gate categories = +5.80**
