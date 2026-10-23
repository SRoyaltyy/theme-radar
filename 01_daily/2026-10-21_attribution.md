# Factor attribution — signal 2026-10-21 → prediction day 2026-10-23

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-10-21** | Features/scores formed from this snapshot (and deltas vs **2026-10-20**). Only data on/before this date. |
| **Prediction day** | **2026-10-23** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-10-21 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-10-23 | Close proxy on prediction day. |
| **Return column** | `fwd_2d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11755** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_2d) = **-0.0301**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 3.95% | 23.0% | 2363 |
| 2 | -0.56% | 14.9% | 3013 |
| 3 | -1.37% | 13.6% | 1711 |
| 4 | -0.81% | 13.2% | 2444 |
| 5 | -2.55% | 23.5% | 2224 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Performance (Week) | -0.4522 | +0.0270 | -0.5162 | -1.25% | 2.94% | 8593/2898 |
| d_20-Day Simple Moving Average | -0.3944 | -0.1295 | -0.4085 | -2.24% | 3.61% | 7518/4016 |
| Performance (Month) | +0.3708 | -0.0722 | +0.5394 | 0.27% | -0.41% | 3624/7935 |
| d_50-Day Simple Moving Average | -0.3437 | -0.0990 | -0.3378 | -2.03% | 3.57% | 7789/3762 |
| d_200-Day Simple Moving Average | -0.3288 | -0.1254 | -0.2920 | -2.10% | 3.17% | 7321/4175 |
| upside_pct_lvl | -0.3251 | +0.1331 | -0.3509 | -0.68% | 0.37% | 4324/310 |
| d_Performance (YTD) | -0.3184 | -0.1347 | -0.2534 | -2.07% | 3.15% | 7104/4097 |
| true_ret | -0.3182 | -0.1425 | -0.2903 | -2.09% | 3.28% | 7017/3996 |
| d_Relative Strength Index (14) | -0.3166 | -0.1447 | -0.0649 | -2.09% | 3.09% | 7113/4116 |
| d_Price | -0.3149 | -0.1371 | -0.1659 | -2.09% | 3.28% | 7017/3996 |
| d_Performance (Quarter) | -0.3102 | -0.0267 | -0.2860 | -1.67% | 4.30% | 8310/2868 |
| Relative Strength Index (14) | +0.2853 | -0.0830 | +0.4265 | -0.21% | n/a | 11675/0 |
| d_Beta | +0.2495 | -0.0642 | +0.3108 | 7.92% | 0.71% | 679/1708 |
| d_Forward P/E | -0.2195 | -0.0395 | -0.2434 | -1.03% | 1.40% | 1508/1420 |
| Performance (Week) | +0.1728 | +0.1105 | +0.2005 | -0.67% | 0.67% | 7427/4117 |
| d_Market Cap | -0.1636 | -0.0373 | -0.1022 | -1.64% | 4.40% | 2906/2772 |
| d_Performance (Month) | -0.0938 | -0.0479 | -0.0586 | -1.61% | 1.59% | 6386/5002 |
| Relative Volume | +0.0693 | +0.0819 | -0.0464 | -0.19% | n/a | 11389/0 |
| Institutional Transactions | -0.0498 | +0.0461 | -0.1158 | 2.49% | -0.47% | 3260/1788 |
| d_Analyst Recom | +0.0407 | +0.0169 | +0.0035 | -0.05% | -1.96% | 83/54 |
| d_Volatility (Month) | -0.0378 | +0.1618 | -0.1649 | 0.58% | -1.19% | 5872/3828 |
| d_Average Volume | +0.0356 | -0.0188 | -0.0288 | 0.84% | -1.27% | 5947/5049 |
| d_Gross Margin | -0.0308 | -0.0392 | +0.0445 | -1.63% | 4.42% | 24/16 |
| Short Float | +0.0275 | +0.2362 | -0.1963 | 1.08% | n/a | 5638/0 |
| d_Short Ratio | -0.0245 | +0.0132 | +0.0065 | -1.12% | -1.01% | 3161/3690 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 652 | -7.30% | 13.5% |
| true_ret>3% & UPTREND | 255 | -2.48% | 28.6% |
| true_ret>3% & MIXED | 185 | -5.74% | 13.0% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 157 | 0.22% | 1.63% |
| WASHED | 1475 | 4.25% | -6.89% |
