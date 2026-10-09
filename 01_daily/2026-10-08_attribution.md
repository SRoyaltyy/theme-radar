# Factor attribution — signal 2026-10-08 → prediction day 2026-10-09

## Trade window (read this first)

| Role | Date | Meaning |
|------|------|---------|
| **Signal as-of** | **2026-10-08** | Features/scores formed from this snapshot (and deltas vs **2026-10-07**). Only data on/before this date. |
| **Prediction day** | **2026-10-09** | The trading day the forward return is for (exit snapshot). |
| **Entry price** | Price @ 2026-10-08 | Long: buy here; short: sell here. |
| **Exit price** | Price @ 2026-10-09 | Close proxy on prediction day. |
| **Return column** | `fwd_1d` | Long: exit/entry − 1; short = opposite. |

Graded **n=11704** names with valid entry and exit prices.

Provisional until multiple signal dates agree.

_Column guide: **IC** = Spearman(feature, long forward return); **IC↑** / **IC↓** = IC among names that went up / down._

## Score calibration (long fwd)
- Spearman IC(total_score, fwd_1d) = **-0.0831**

| Quintile | Mean long fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 0.35% | 21.5% | 2545 |
| 2 | 0.70% | 14.4% | 2172 |
| 3 | 0.38% | 15.9% | 2307 |
| 4 | 0.32% | 15.2% | 2341 |
| 5 | 0.21% | 22.6% | 2339 |

## Top |IC| features

| Feature | IC | IC↑ | IC↓ | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|---|---|
| d_Relative Strength Index (14) | -0.2356 | -0.1403 | +0.2785 | 0.15% | 0.62% | 5324/5963 |
| d_Price | -0.2171 | -0.1813 | +0.1947 | 0.15% | 0.63% | 5250/5901 |
| d_Performance (YTD) | -0.2000 | -0.2134 | +0.1222 | 0.15% | 0.63% | 5329/5974 |
| d_20-Day Simple Moving Average | -0.1998 | -0.1967 | +0.0497 | 0.12% | 0.67% | 5907/5699 |
| d_200-Day Simple Moving Average | -0.1988 | -0.2054 | +0.0982 | 0.12% | 0.64% | 5499/6072 |
| d_50-Day Simple Moving Average | -0.1982 | -0.2138 | +0.0811 | 0.11% | 0.66% | 5637/5962 |
| true_ret | -0.1772 | -0.2252 | +0.1126 | 0.15% | 0.63% | 5250/5901 |
| d_Performance (Quarter) | -0.1180 | -0.0903 | +0.0593 | 0.34% | 0.43% | 5186/5938 |
| d_Forward P/E | -0.1076 | -0.1442 | +0.0407 | 0.01% | 0.62% | 1896/1069 |
| Performance (Month) | +0.0986 | -0.1219 | +0.2951 | 0.83% | 0.18% | 3718/7800 |
| d_Performance (Week) | -0.0910 | -0.1002 | +0.0536 | 0.29% | 0.48% | 5431/6090 |
| d_Market Cap | -0.0902 | -0.1593 | +0.1814 | -0.03% | 0.50% | 2990/2717 |
| d_Performance (Month) | -0.0866 | -0.0244 | +0.0080 | 0.29% | 0.57% | 7321/4080 |
| Relative Strength Index (14) | +0.0641 | -0.0431 | +0.0855 | 0.39% | n/a | 11618/0 |
| d_Target Price | +0.0628 | +0.0725 | -0.0465 | 0.87% | -0.08% | 219/310 |
| d_Average Volume | -0.0466 | -0.0671 | -0.0422 | 0.20% | 0.56% | 5494/5541 |
| d_Short Ratio | +0.0396 | +0.0526 | +0.0163 | 0.48% | 0.21% | 3685/3429 |
| d_Beta | -0.0381 | -0.0309 | -0.0317 | 0.69% | 0.48% | 699/1194 |
| d_Analyst Recom | -0.0361 | +0.0138 | -0.0027 | -0.16% | 0.76% | 58/65 |
| d_Total Debt/Equity | +0.0348 | +0.0325 | +0.0225 | 0.64% | -4.39% | 8/7 |
| d_Profit Margin | +0.0331 | +0.0398 | +0.0458 | -0.91% | -5.26% | 6/10 |
| d_Insider Transactions | -0.0259 | -0.0431 | +0.0140 | -0.72% | 0.71% | 123/147 |
| d_Gross Margin | -0.0205 | +0.0248 | -0.0226 | -3.97% | -1.63% | 9/12 |
| Short Float | -0.0202 | +0.1514 | -0.0687 | 0.23% | n/a | 5690/0 |
| upside_pct_lvl | -0.0151 | +0.2740 | -0.3508 | 0.19% | 0.71% | 4379/257 |

## Combinations

| Pattern | n | Mean long fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 341 | -0.67% | 21.7% |
| true_ret>3% & UPTREND | 187 | 0.50% | 25.1% |
| true_ret>3% & MIXED | 137 | 0.08% | 31.4% |

## Risk dominance probes

| State | n | Mean long fwd | Mean fwd if score top quintile |
|---|---|---|---|
| EXTENDED | 124 | 1.44% | 1.88% |
| WASHED | 1364 | -0.19% | -0.26% |
