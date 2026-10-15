# Factor attribution — signal 2026-10-12 → prediction day 2026-10-15

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-10-12** | Features/scores formed from this snapshot (and deltas vs **2026-10-09**). Only data on/before this date. |
| **Prediction day** | **2026-10-15** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-10-12 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-10-15 | Close proxy on prediction day. |
| **Return column** | `fwd_3d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11712** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_3d) = **0.1834**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | -0.61% | 17.4% | 2351 |
| 2 | -1.00% | 15.0% | 2831 |
| 3 | -0.94% | 13.3% | 2588 |
| 4 | -0.33% | 21.4% | 1867 |
| 5 | -0.66% | 29.6% | 2075 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Performance (Quarter) | +0.3751 | +0.1156 | +0.3620 | -0.10% | -0.95% | 3893/7251 |
| d_50-Day Simple Moving Average | +0.3706 | +0.0558 | +0.4417 | 0.05% | -1.37% | 5038/6499 |
| d_20-Day Simple Moving Average | +0.3606 | +0.0800 | +0.4122 | -0.07% | -1.34% | 5335/6203 |
| Performance (Week) | +0.3563 | +0.0684 | +0.4310 | -0.02% | -1.39% | 5500/6037 |
| d_200-Day Simple Moving Average | +0.3499 | +0.0389 | +0.4181 | -0.02% | -1.27% | 4877/6623 |
| true_ret | +0.3484 | +0.0194 | +0.4540 | 0.01% | -1.30% | 4674/6334 |
| d_Performance (YTD) | +0.3459 | +0.0075 | +0.4204 | 0.01% | -1.28% | 4758/6429 |
| upside_pct_lvl | -0.3430 | +0.1914 | -0.4218 | -0.83% | -0.37% | 4353/279 |
| d_Price | +0.3395 | +0.0142 | +0.3371 | 0.01% | -1.30% | 4674/6334 |
| d_Relative Strength Index (14) | +0.3384 | -0.0262 | +0.3253 | -0.00% | -1.29% | 4777/6433 |
| d_Performance (Week) | +0.2833 | -0.0161 | +0.3275 | -0.00% | -1.16% | 4107/7376 |
| d_Performance (Month) | +0.2720 | -0.0733 | +0.3512 | -0.64% | -0.78% | 3845/7591 |
| d_Forward P/E | +0.2175 | -0.0582 | +0.3569 | 0.76% | -1.20% | 1583/1345 |
| d_Market Cap | +0.1958 | -0.0685 | +0.2183 | -0.42% | -0.11% | 2480/3241 |
| d_Institutional Ownership | +0.1634 | +0.0457 | +0.1124 | -0.40% | -1.65% | 2401/640 |
| Institutional Transactions | -0.1570 | -0.0626 | -0.1582 | -0.41% | 0.69% | 3263/1778 |
| d_Beta | +0.1562 | -0.0090 | +0.2054 | -1.35% | 0.90% | 1012/1911 |
| Performance (Month) | +0.0620 | -0.1395 | +0.2507 | -1.38% | -0.39% | 3891/7639 |
| d_Relative Volume | -0.0457 | +0.0435 | -0.0630 | -0.08% | -1.29% | 5174/6071 |
| Relative Strength Index (14) | +0.0447 | +0.0209 | +0.3255 | -0.73% | n/a | 11628/0 |
| d_Target Price | -0.0435 | +0.0358 | -0.0589 | -0.27% | 0.06% | 274/464 |
| d_Institutional Transactions | +0.0402 | -0.0284 | +0.0592 | -0.87% | 1.38% | 3102/1308 |
| d_EPS Surprise | -0.0269 | -0.0109 | -0.0221 | -6.09% | 0.95% | 3/2 |
| d_Insider Transactions | -0.0230 | -0.0066 | +0.0293 | -2.56% | -3.86% | 176/112 |
| d_Average Volume | +0.0201 | -0.0710 | +0.0297 | -0.41% | -1.06% | 5328/5627 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 155 | -0.14% | 39.4% |
| true_ret>3% & UPTREND | 126 | -2.83% | 34.1% |
| true_ret>3% & MIXED | 97 | -3.13% | 39.2% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 173 | -2.04% | -1.51% |
| WASHED | 1192 | 2.49% | -2.83% |
