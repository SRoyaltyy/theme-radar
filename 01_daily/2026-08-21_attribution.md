# Factor attribution — signal 2026-08-21 → prediction day 2026-08-26

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-08-21** | Features/scores formed from this snapshot (and deltas vs **2026-08-20**). Only data on/before this date. |
| **Prediction day** | **2026-08-26** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-08-21 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-08-26 | Close proxy on prediction day. |
| **Return column** | `fwd_3d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11602** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_3d) = **-0.0723**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 2.78% | 20.7% | 2352 |
| 2 | 0.03% | 9.9% | 2308 |
| 3 | 0.17% | 13.3% | 2351 |
| 4 | 1.74% | 13.3% | 2775 |
| 5 | 1.99% | 25.2% | 1816 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_50-Day Simple Moving Average | -0.0877 | +0.1000 | -0.1472 | 1.01% | 1.97% | 7788/3672 |
| true_ret | -0.0817 | +0.0769 | -0.1130 | 0.80% | 2.05% | 7670/3362 |
| d_Performance (YTD) | -0.0758 | +0.0599 | -0.0641 | 0.80% | 2.59% | 7737/3445 |
| d_200-Day Simple Moving Average | -0.0748 | +0.0932 | -0.1041 | 1.15% | 1.68% | 7869/3586 |
| d_Performance (Quarter) | -0.0706 | -0.0184 | -0.0618 | 1.28% | 1.57% | 6062/4735 |
| Performance (Month) | -0.0667 | -0.0179 | -0.0361 | 0.69% | 2.89% | 7841/3514 |
| d_Price | -0.0650 | -0.0389 | +0.1004 | 0.80% | 2.05% | 7670/3362 |
| d_Performance (Month) | -0.0626 | +0.1311 | -0.1117 | 1.05% | 2.54% | 8786/2495 |
| d_20-Day Simple Moving Average | -0.0605 | +0.0951 | -0.1106 | 1.21% | 1.53% | 7560/3886 |
| d_Relative Strength Index (14) | -0.0597 | -0.0796 | +0.1220 | 0.81% | 2.28% | 7675/3435 |
| Short Float | -0.0458 | +0.2167 | -0.1453 | 1.82% | n/a | 5690/0 |
| Institutional Transactions | -0.0390 | +0.0398 | -0.0416 | 2.77% | 1.26% | 2690/2352 |
| Relative Strength Index (14) | -0.0365 | -0.1974 | +0.1260 | 1.36% | n/a | 11460/0 |
| d_Target Price | -0.0353 | -0.0198 | +0.0041 | -0.29% | 0.52% | 235/135 |
| d_Forward P/E | -0.0345 | +0.0615 | -0.0613 | 0.15% | 0.78% | 1952/973 |
| Performance (Week) | +0.0334 | -0.0370 | +0.0293 | 1.38% | 1.36% | 4210/7175 |
| Relative Volume | +0.0322 | +0.1506 | -0.0332 | 1.34% | n/a | 11334/0 |
| d_Market Cap | -0.0311 | -0.0110 | +0.0154 | 0.66% | 2.48% | 3583/2122 |
| d_Average Volume | +0.0302 | +0.0150 | -0.0147 | 3.10% | 0.09% | 4754/6280 |
| d_Short Ratio | -0.0296 | -0.0147 | -0.0045 | -0.23% | 2.91% | 3937/2836 |
| d_Volatility (Month) | +0.0275 | +0.0398 | -0.0154 | 1.99% | 1.27% | 5047/4179 |
| d_Performance (Week) | -0.0257 | +0.0637 | -0.0443 | 1.03% | 2.08% | 7656/3690 |
| d_EPS Surprise | -0.0217 | +0.0165 | +0.0008 | 0.77% | 2.08% | 11/13 |
| d_Insider Transactions | +0.0206 | +0.0385 | -0.0104 | 1.03% | 5.33% | 283/321 |
| d_Beta | +0.0190 | -0.0673 | +0.0705 | 2.95% | 3.34% | 1909/2309 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 404 | 5.75% | 32.4% |
| true_ret>3% & UPTREND | 517 | -0.58% | 35.8% |
| true_ret>3% & MIXED | 434 | 6.24% | 35.0% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 471 | 5.96% | 21.58% |
| WASHED | 521 | 14.04% | 18.73% |
