# Factor attribution — signal 2026-10-15 → prediction day 2026-10-16

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-10-15** | Features/scores formed from this snapshot (and deltas vs **2026-10-14**). Only data on/before this date. |
| **Prediction day** | **2026-10-16** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-10-15 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-10-16 | Close proxy on prediction day. |
| **Return column** | `fwd_1d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11733** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_1d) = **0.0598**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | -2.47% | 9.0% | 2686 |
| 2 | -0.77% | 5.0% | 2260 |
| 3 | -0.69% | 4.6% | 2269 |
| 4 | -1.61% | 8.9% | 2179 |
| 5 | -1.87% | 9.1% | 2339 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Performance (Week) | +0.4022 | +0.0299 | +0.4685 | -0.49% | -2.50% | 5541/5999 |
| d_Performance (Week) | -0.3924 | -0.2270 | -0.3766 | -1.83% | -0.68% | 8728/2798 |
| upside_pct_lvl | -0.3634 | +0.2266 | -0.4378 | -1.97% | -1.53% | 4336/303 |
| Relative Strength Index (14) | +0.3165 | -0.0417 | +0.3896 | -1.53% | n/a | 11664/0 |
| Short Float | -0.3118 | +0.0057 | -0.2941 | -1.71% | n/a | 5672/0 |
| d_Beta | -0.3102 | -0.0508 | -0.3461 | -2.85% | -1.00% | 3045/1527 |
| d_Volatility (Month) | -0.1675 | +0.0611 | -0.2308 | -1.78% | -1.56% | 6518/3356 |
| d_Performance (Quarter) | -0.1651 | -0.1340 | -0.1275 | -1.50% | -1.68% | 8761/2462 |
| d_Relative Strength Index (14) | +0.1061 | -0.3713 | +0.2605 | -1.35% | -2.06% | 8310/3073 |
| Institutional Transactions | -0.1051 | +0.0189 | -0.1520 | -2.14% | -1.17% | 3265/1778 |
| Performance (Month) | +0.1021 | -0.1427 | +0.2323 | -1.31% | -1.69% | 4612/6928 |
| d_20-Day Simple Moving Average | -0.0946 | -0.0596 | -0.1173 | -1.44% | -1.82% | 8690/2932 |
| d_Forward P/E | -0.0938 | -0.2124 | -0.0280 | -1.03% | -1.12% | 2216/751 |
| d_50-Day Simple Moving Average | -0.0728 | -0.0670 | -0.0817 | -1.39% | -1.94% | 8566/3047 |
| d_Price | +0.0633 | -0.1977 | +0.1508 | -1.34% | -2.07% | 8231/3028 |
| d_Target Price | -0.0631 | -0.0093 | -0.0371 | -1.08% | -0.66% | 208/365 |
| true_ret | -0.0627 | -0.0843 | -0.0586 | -1.34% | -2.07% | 8231/3028 |
| d_Market Cap | +0.0565 | -0.2170 | +0.1379 | -1.57% | -1.97% | 3912/1815 |
| d_200-Day Simple Moving Average | -0.0507 | -0.0912 | -0.0392 | -1.38% | -1.95% | 8375/3213 |
| d_Short Float | +0.0441 | -0.0138 | +0.0484 | -1.91% | -3.42% | 35/72 |
| d_Performance (YTD) | -0.0294 | -0.1047 | -0.0053 | -1.35% | -2.06% | 8301/3067 |
| d_Short Ratio | +0.0259 | +0.0199 | +0.0519 | -1.47% | -1.69% | 2643/4397 |
| d_Sales Year Over Year TTM | -0.0258 | -0.0423 | -0.0013 | -1.67% | 1.23% | 12/8 |
| d_Average Volume | -0.0248 | -0.0180 | -0.0908 | -1.64% | -1.45% | 6695/4337 |
| d_EPS Surprise | -0.0191 | +0.0200 | -0.0129 | -0.52% | -0.05% | 9/15 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 1093 | -3.79% | 8.0% |
| true_ret>3% & UPTREND | 393 | -2.43% | 7.6% |
| true_ret>3% & MIXED | 300 | -2.97% | 10.7% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 155 | -1.51% | -1.37% |
| WASHED | 1205 | -4.19% | -5.79% |
