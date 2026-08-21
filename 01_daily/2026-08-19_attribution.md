# Factor attribution — signal 2026-08-19 → prediction day 2026-08-21

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-08-19** | Features/scores formed from this snapshot (and deltas vs **2026-08-18**). Only data on/before this date. |
| **Prediction day** | **2026-08-21** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-08-19 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-08-21 | Close proxy on prediction day. |
| **Return column** | `fwd_2d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11586** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_2d) = **0.0519**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 4.96% | 21.7% | 2332 |
| 2 | 0.13% | 12.1% | 2840 |
| 3 | 0.12% | 10.1% | 2294 |
| 4 | 0.38% | 18.0% | 1803 |
| 5 | 3.02% | 34.1% | 2317 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| Relative Strength Index (14) | +0.1284 | -0.0972 | +0.2777 | 1.74% | n/a | 11456/0 |
| d_Performance (YTD) | +0.1173 | +0.2558 | -0.0357 | 1.18% | 2.87% | 7285/3895 |
| d_200-Day Simple Moving Average | +0.1165 | +0.2821 | -0.0560 | 1.20% | 2.71% | 7295/4128 |
| true_ret | +0.1145 | +0.2737 | -0.0495 | 1.17% | 1.67% | 7196/3830 |
| Performance (Week) | +0.1129 | +0.1329 | +0.0845 | 2.37% | 1.19% | 5371/5990 |
| d_50-Day Simple Moving Average | +0.1128 | +0.2943 | -0.0743 | 1.84% | 1.57% | 7258/4171 |
| d_Price | +0.1114 | +0.1708 | +0.0503 | 1.17% | 1.67% | 7196/3830 |
| d_20-Day Simple Moving Average | +0.1053 | +0.2856 | -0.0790 | 1.43% | 2.26% | 7129/4301 |
| Short Float | -0.0909 | +0.1090 | -0.2307 | 2.91% | n/a | 5669/0 |
| d_Performance (Week) | +0.0874 | +0.2479 | -0.0565 | 2.45% | 0.94% | 6114/5186 |
| d_Relative Strength Index (14) | +0.0856 | +0.1862 | +0.1269 | 1.18% | 2.89% | 7272/3867 |
| d_Forward P/E | +0.0853 | +0.1682 | +0.0163 | 0.32% | -0.27% | 1657/1316 |
| d_Performance (Quarter) | +0.0784 | +0.2959 | -0.1247 | 1.61% | 2.29% | 7934/2890 |
| Performance (Month) | +0.0765 | +0.0535 | +0.0579 | 0.87% | 3.27% | 7201/4149 |
| d_Relative Volume | +0.0642 | +0.1566 | -0.0374 | 3.36% | -0.09% | 6005/5126 |
| upside_pct_lvl | -0.0565 | +0.3516 | -0.3680 | 0.31% | 0.14% | 4295/354 |
| Institutional Transactions | -0.0517 | +0.0018 | -0.0793 | 4.78% | 1.50% | 2690/2352 |
| d_Beta | -0.0498 | -0.0805 | +0.0372 | 4.78% | 3.89% | 1829/2382 |
| d_Market Cap | +0.0420 | +0.0992 | -0.0007 | 1.29% | 4.99% | 3321/2395 |
| d_Performance (Month) | +0.0280 | +0.0914 | +0.0127 | 1.34% | 2.12% | 5241/6032 |
| d_Average Volume | -0.0265 | -0.0785 | +0.0492 | 1.81% | 1.76% | 4490/6523 |
| d_Institutional Ownership | -0.0244 | -0.1304 | +0.0469 | -0.15% | 0.33% | 2402/935 |
| d_Target Price | +0.0244 | -0.0340 | +0.0468 | 0.20% | 0.33% | 236/159 |
| d_Short Ratio | +0.0232 | +0.0806 | -0.0630 | 0.57% | 0.02% | 4178/2659 |
| d_Analyst Recom | +0.0180 | -0.0571 | +0.0117 | 0.15% | -0.19% | 103/105 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 523 | 3.97% | 44.6% |
| true_ret>3% & UPTREND | 682 | 1.82% | 39.6% |
| true_ret>3% & MIXED | 514 | 9.15% | 53.5% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 293 | 1.83% | 3.69% |
| WASHED | 544 | 13.74% | -0.85% |
