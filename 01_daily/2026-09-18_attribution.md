# Factor attribution — signal 2026-09-18 → prediction day 2026-09-21

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-09-18** | Features/scores formed from this snapshot (and deltas vs **2026-09-17**). Only data on/before this date. |
| **Prediction day** | **2026-09-21** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-09-18 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-09-21 | Close proxy on prediction day. |
| **Return column** | `fwd_1d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11629** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_1d) = **0.0668**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 0.80% | 23.6% | 2788 |
| 2 | 0.79% | 19.8% | 2022 |
| 3 | 1.45% | 22.6% | 2520 |
| 4 | 0.82% | 30.7% | 2073 |
| 5 | 1.74% | 42.6% | 2226 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Performance (Quarter) | -0.1869 | -0.1740 | -0.1567 | 0.67% | 1.22% | 2997/7988 |
| Short Float | +0.1169 | +0.1910 | -0.0330 | 0.92% | n/a | 5688/0 |
| Relative Strength Index (14) | +0.1035 | +0.2492 | -0.2032 | 1.12% | n/a | 11546/0 |
| d_Performance (Week) | -0.0956 | -0.0494 | -0.0895 | 1.11% | 1.14% | 3328/8096 |
| d_Price | +0.0803 | +0.1955 | -0.1280 | 1.33% | 0.75% | 4261/6857 |
| d_Relative Strength Index (14) | +0.0793 | +0.2683 | -0.1763 | 1.80% | 0.74% | 4351/6918 |
| upside_pct_lvl | +0.0768 | +0.3438 | -0.3031 | 0.68% | 0.01% | 4367/271 |
| d_Volatility (Month) | -0.0697 | -0.0923 | -0.0319 | 1.38% | 1.14% | 4214/5068 |
| Relative Volume | -0.0601 | +0.0809 | -0.0153 | 1.13% | n/a | 11417/0 |
| d_Performance (YTD) | +0.0587 | +0.1350 | -0.0950 | 1.81% | 0.74% | 4348/6927 |
| d_50-Day Simple Moving Average | +0.0586 | +0.1325 | -0.0775 | 1.76% | 0.71% | 4551/6957 |
| d_Market Cap | -0.0546 | +0.0976 | -0.1418 | 1.32% | 0.65% | 2157/3562 |
| d_200-Day Simple Moving Average | +0.0519 | +0.1290 | -0.1005 | 1.76% | 0.75% | 4296/7182 |
| d_Forward P/E | -0.0517 | +0.0117 | -0.0303 | 0.57% | 0.44% | 987/1951 |
| Performance (Week) | +0.0517 | +0.0254 | +0.0294 | 1.42% | 0.99% | 3796/7602 |
| d_20-Day Simple Moving Average | +0.0472 | +0.1262 | -0.0845 | 1.69% | 0.71% | 4924/6588 |
| true_ret | +0.0469 | +0.1067 | -0.0684 | 1.33% | 0.75% | 4261/6857 |
| d_Relative Volume | -0.0389 | +0.0873 | -0.0475 | 1.01% | 1.33% | 7194/4111 |
| d_Sales Growth Quarter Over Quarter | -0.0387 | -0.0283 | -0.0368 | -6.00% | 5.88% | 2/1 |
| d_Performance (Month) | +0.0342 | +0.0660 | -0.0062 | 1.85% | 0.76% | 3889/7473 |
| d_Average Volume | -0.0290 | -0.0526 | -0.0093 | 1.35% | 0.96% | 4563/6491 |
| Performance (Month) | +0.0250 | +0.0013 | +0.0147 | 1.35% | 1.04% | 3350/8086 |
| d_Profit Margin | -0.0168 | -0.0274 | -0.0338 | -2.11% | 1.91% | 1/3 |
| d_Target Price | +0.0164 | -0.0068 | -0.0535 | 0.48% | 0.12% | 102/172 |
| d_Short Float | +0.0160 | +0.0051 | +0.0217 | 2.95% | 0.67% | 25/39 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 328 | 1.64% | 49.4% |
| true_ret>3% & UPTREND | 365 | 3.37% | 62.5% |
| true_ret>3% & MIXED | 253 | 4.20% | 60.1% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 166 | 2.00% | 8.38% |
| WASHED | 1370 | 2.43% | 7.51% |
