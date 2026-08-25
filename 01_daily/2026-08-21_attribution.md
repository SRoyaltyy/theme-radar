# Factor attribution — signal 2026-08-21 → prediction day 2026-08-25

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-08-21** | Features/scores formed from this snapshot (and deltas vs **2026-08-20**). Only data on/before this date. |
| **Prediction day** | **2026-08-25** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-08-21 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-08-25 | Close proxy on prediction day. |
| **Return column** | `fwd_2d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11602** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_2d) = **0.0158**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 2.27% | 19.6% | 2352 |
| 2 | 0.10% | 10.7% | 2308 |
| 3 | 0.42% | 13.7% | 2351 |
| 4 | 2.04% | 15.4% | 2775 |
| 5 | 4.10% | 33.5% | 1816 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Performance (Week) | +0.1731 | +0.0633 | +0.1184 | 1.77% | 1.72% | 4210/7175 |
| Relative Volume | +0.0818 | +0.1823 | -0.0416 | 1.70% | n/a | 11334/0 |
| Relative Strength Index (14) | +0.0613 | -0.1054 | +0.1767 | 1.73% | n/a | 11460/0 |
| Performance (Month) | +0.0536 | +0.0828 | +0.0266 | 1.43% | 2.43% | 7841/3514 |
| d_Performance (Week) | +0.0520 | +0.1296 | -0.0062 | 1.66% | 1.90% | 7656/3690 |
| d_Average Volume | +0.0510 | +0.0469 | -0.0274 | 3.70% | 0.29% | 4754/6280 |
| d_Beta | -0.0509 | -0.1170 | +0.0423 | 3.26% | 4.40% | 1909/2309 |
| d_Volatility (Month) | +0.0409 | +0.0580 | -0.0410 | 2.83% | 1.16% | 5047/4179 |
| d_Short Ratio | -0.0395 | -0.0350 | +0.0119 | 0.02% | 4.32% | 3937/2836 |
| d_Performance (Month) | +0.0385 | +0.2025 | -0.0764 | 1.66% | 2.08% | 8786/2495 |
| upside_pct_lvl | +0.0308 | +0.4007 | -0.3016 | 2.48% | -0.06% | 4290/356 |
| d_Performance (Quarter) | -0.0280 | +0.0261 | -0.0501 | 1.90% | 1.62% | 6062/4735 |
| d_Insider Transactions | +0.0255 | +0.0316 | +0.0182 | 1.45% | 5.55% | 283/321 |
| d_Relative Strength Index (14) | -0.0222 | -0.0382 | +0.1364 | 1.42% | 2.11% | 7675/3435 |
| d_50-Day Simple Moving Average | -0.0214 | +0.1512 | -0.1344 | 1.61% | 1.85% | 7788/3672 |
| d_Sales Growth Quarter Over Quarter | +0.0198 | +0.0070 | +0.0088 | 2.19% | 1.70% | 20/21 |
| d_Institutional Ownership | -0.0185 | -0.0021 | -0.0296 | 0.04% | 0.78% | 394/1182 |
| d_Price | -0.0181 | +0.0185 | +0.0849 | 1.41% | 1.87% | 7670/3362 |
| d_Gross Margin | -0.0156 | -0.0223 | +0.0012 | -0.37% | 2.26% | 20/23 |
| Institutional Transactions | -0.0142 | +0.0603 | -0.0486 | 3.53% | 1.48% | 2690/2352 |
| d_Sales Year Over Year TTM | +0.0141 | -0.0296 | +0.0042 | 0.51% | 0.15% | 23/18 |
| d_Relative Volume | +0.0140 | +0.0506 | +0.0056 | 1.44% | 2.01% | 5320/5847 |
| d_20-Day Simple Moving Average | -0.0115 | +0.1377 | -0.1051 | 1.81% | 1.44% | 7560/3886 |
| d_Analyst Recom | +0.0107 | +0.0142 | +0.0446 | 0.45% | -0.09% | 76/103 |
| d_EPS Surprise | -0.0087 | +0.0041 | -0.0233 | 1.41% | 2.55% | 11/13 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 404 | 12.07% | 32.9% |
| true_ret>3% & UPTREND | 517 | 0.36% | 47.4% |
| true_ret>3% & MIXED | 434 | 7.96% | 45.4% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 471 | 7.57% | 24.41% |
| WASHED | 521 | 14.06% | 19.56% |
