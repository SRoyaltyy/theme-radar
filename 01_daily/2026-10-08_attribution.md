# Factor attribution — signal 2026-10-08 → prediction day 2026-10-12

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-10-08** | Features/scores formed from this snapshot (and deltas vs **2026-10-07**). Only data on/before this date. |
| **Prediction day** | **2026-10-12** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-10-08 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-10-12 | Close proxy on prediction day. |
| **Return column** | `fwd_2d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11691** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_2d) = **0.1042**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 3.39% | 16.8% | 2542 |
| 2 | 0.22% | 11.4% | 2170 |
| 3 | -0.27% | 13.5% | 2307 |
| 4 | -0.12% | 14.9% | 2334 |
| 5 | -0.04% | 25.7% | 2338 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| upside_pct_lvl | -0.2725 | +0.2253 | -0.4792 | 0.78% | 0.31% | 4376/256 |
| Performance (Week) | +0.2376 | +0.0353 | +0.3225 | 0.18% | 1.33% | 6316/5206 |
| Performance (Month) | +0.1616 | -0.1011 | +0.3151 | 0.28% | 0.90% | 3713/7793 |
| true_ret | +0.1453 | -0.0219 | +0.2886 | 0.07% | 1.36% | 5249/5899 |
| Relative Strength Index (14) | +0.1391 | +0.0234 | +0.1610 | 0.69% | n/a | 11606/0 |
| d_Market Cap | +0.1319 | -0.1194 | +0.2459 | -0.31% | 3.30% | 2987/2713 |
| d_Performance (YTD) | +0.1313 | -0.0125 | +0.2285 | 0.07% | 1.33% | 5327/5972 |
| d_Performance (Week) | +0.1277 | +0.0598 | +0.1473 | -0.02% | 1.34% | 5427/6088 |
| d_50-Day Simple Moving Average | +0.1235 | -0.0091 | +0.2389 | -0.02% | 1.38% | 5635/5960 |
| d_200-Day Simple Moving Average | +0.1228 | -0.0074 | +0.2205 | -0.01% | 1.35% | 5497/6070 |
| d_Forward P/E | +0.1171 | -0.0736 | +0.2149 | 0.22% | -0.36% | 1896/1069 |
| d_Price | +0.1111 | +0.0047 | +0.2073 | 0.07% | 1.36% | 5249/5899 |
| d_20-Day Simple Moving Average | +0.1065 | -0.0023 | +0.2113 | -0.06% | 1.48% | 5905/5697 |
| d_Performance (Month) | +0.0978 | +0.0963 | +0.1005 | -0.09% | 2.15% | 7313/4078 |
| Short Float | -0.0873 | +0.1820 | -0.1414 | 1.47% | n/a | 5680/0 |
| d_Relative Strength Index (14) | +0.0835 | +0.0008 | +0.2124 | 0.06% | 1.31% | 5322/5961 |
| d_Target Price | +0.0581 | +0.0636 | -0.0344 | 0.78% | -0.57% | 219/310 |
| d_Performance (Quarter) | +0.0525 | +0.0081 | +0.1037 | -0.10% | 1.50% | 5181/5937 |
| Institutional Transactions | -0.0480 | +0.0560 | -0.0975 | 2.87% | -0.36% | 3242/1800 |
| d_Volatility (Month) | +0.0410 | -0.0920 | +0.1144 | 1.20% | 0.42% | 4627/4885 |
| d_Profit Margin | +0.0297 | +0.0017 | +0.0382 | 0.21% | 15.65% | 6/10 |
| d_Insider Transactions | -0.0240 | -0.0257 | +0.0029 | 0.14% | 15.41% | 123/147 |
| Relative Volume | +0.0237 | +0.0858 | -0.0067 | 0.70% | n/a | 11445/0 |
| d_EPS Surprise | -0.0214 | -0.0438 | -0.0157 | -1.05% | 2.37% | 8/6 |
| d_Short Ratio | -0.0196 | +0.0386 | -0.0248 | 0.21% | 0.59% | 3683/3429 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 340 | -1.20% | 28.2% |
| true_ret>3% & UPTREND | 187 | 0.65% | 43.3% |
| true_ret>3% & MIXED | 137 | 0.17% | 32.8% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 124 | -0.44% | -2.04% |
| WASHED | 1361 | 5.60% | -2.25% |
