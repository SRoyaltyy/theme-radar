# Factor attribution — signal 2026-09-15 → prediction day 2026-09-16

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-09-15** | Features/scores formed from this snapshot (and deltas vs **2026-09-14**). Only data on/before this date. |
| **Prediction day** | **2026-09-16** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-09-15 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-09-16 | Close proxy on prediction day. |
| **Return column** | `fwd_1d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11621** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_1d) = **-0.0616**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 0.27% | 13.8% | 2931 |
| 2 | -0.04% | 6.8% | 2399 |
| 3 | -0.33% | 5.5% | 1730 |
| 4 | -0.45% | 6.4% | 2266 |
| 5 | -0.63% | 13.1% | 2295 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Performance (Week) | -0.1625 | -0.1695 | -0.0858 | -0.61% | 0.16% | 5356/6027 |
| Relative Strength Index (14) | -0.1086 | +0.1135 | -0.1499 | -0.20% | n/a | 11530/0 |
| Performance (Week) | -0.0784 | -0.3061 | +0.1136 | -0.77% | -0.05% | 2379/9092 |
| d_Beta | +0.0783 | +0.0688 | +0.0449 | 0.02% | -0.70% | 1886/1552 |
| d_Forward P/E | -0.0747 | -0.0191 | -0.0376 | -0.79% | -0.39% | 1008/1922 |
| d_Performance (Quarter) | -0.0652 | -0.1452 | -0.0179 | -0.09% | -0.29% | 3074/7883 |
| Short Float | -0.0633 | +0.1423 | -0.1596 | -0.17% | n/a | 5700/0 |
| Performance (Month) | -0.0542 | -0.2802 | +0.1277 | -0.70% | -0.05% | 2722/8709 |
| d_Market Cap | -0.0420 | +0.1091 | -0.0967 | -0.44% | -0.04% | 1833/3870 |
| d_Short Float | -0.0305 | -0.0473 | -0.0271 | -1.87% | -0.43% | 81/126 |
| d_EPS Surprise | -0.0304 | -0.0525 | -0.0273 | -0.73% | 3.51% | 5/6 |
| d_50-Day Simple Moving Average | +0.0244 | -0.0894 | +0.0985 | -0.28% | -0.17% | 3155/8325 |
| d_20-Day Simple Moving Average | +0.0240 | -0.0636 | +0.0862 | -0.24% | -0.18% | 3636/7839 |
| d_Gross Margin | -0.0240 | -0.0020 | -0.0092 | -0.21% | 0.51% | 12/12 |
| upside_pct_lvl | +0.0221 | +0.3387 | -0.2433 | -0.22% | -1.05% | 4362/278 |
| d_Performance (Month) | +0.0173 | -0.1580 | +0.1177 | -0.45% | -0.09% | 3440/7856 |
| d_Sales Year Over Year TTM | -0.0171 | +0.0135 | -0.0122 | -0.84% | 1.14% | 11/9 |
| d_Relative Strength Index (14) | -0.0119 | +0.0872 | -0.1249 | -0.31% | -0.17% | 2755/8474 |
| d_Volatility (Month) | -0.0116 | -0.0218 | +0.0046 | -0.07% | -0.35% | 5452/4028 |
| Relative Volume | -0.0115 | -0.0280 | -0.0577 | -0.20% | n/a | 11386/0 |
| d_Short Ratio | -0.0107 | -0.0131 | -0.0219 | -0.07% | -0.35% | 3362/3766 |
| d_Average Volume | +0.0103 | +0.0171 | +0.0208 | -0.30% | -0.08% | 5701/5326 |
| Institutional Transactions | +0.0076 | +0.0624 | -0.0696 | 0.12% | -0.62% | 3211/1829 |
| d_Relative Volume | -0.0052 | -0.0737 | -0.0136 | -0.35% | -0.04% | 5449/5788 |
| d_Profit Margin | -0.0052 | +0.0331 | -0.0071 | -0.55% | 0.95% | 12/8 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 169 | 0.09% | 28.4% |
| true_ret>3% & UPTREND | 196 | -1.61% | 21.9% |
| true_ret>3% & MIXED | 70 | -0.43% | 22.9% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 157 | 1.09% | 8.67% |
| WASHED | 1979 | 0.12% | 0.09% |
