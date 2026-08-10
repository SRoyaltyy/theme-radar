# Factor attribution — 2026-08-07

Full-universe analysis. Label=`fwd_1d`, n=11525.
Provisional until multiple scan dates agree.

## Score calibration
- Spearman IC(total_score, fwd_1d) = **0.0548**

| Quintile | Mean fwd | Hit up>1.5% | n |
|---|---|---|---|
| 1 | 11.30% | 11.1% | 2323 |
| 2 | 2.84% | 2.9% | 2579 |
| 3 | 0.08% | 2.6% | 2042 |
| 4 | 0.22% | 7.7% | 2463 |
| 5 | 0.40% | 15.5% | 2118 |

## Top |IC| features (full universe)

| Feature | IC | Mean fwd when + | Mean fwd when − | n+/n− |
|---|---|---|---|---|
| upside_pct_lvl | +0.1390 | 2.36% | -0.03% | 4266/382 |
| Relative Strength Index (14) | -0.1101 | 3.07% | nan% | 11429/0 |
| Short Float | +0.1067 | 6.02% | nan% | 5697/0 |
| Performance (Month) | -0.1051 | 0.11% | 7.30% | 6563/4716 |
| d_20-Day Simple Moving Average | +0.0719 | 0.36% | 11.12% | 8572/2881 |
| d_50-Day Simple Moving Average | +0.0626 | 0.36% | 11.12% | 8563/2884 |
| d_Average Volume | -0.0572 | 7.77% | 0.20% | 4352/6657 |
| d_Performance (Quarter) | +0.0571 | 0.17% | 13.77% | 8332/2435 |
| Institutional Transactions | +0.0486 | 11.33% | 2.24% | 2536/2487 |
| true_ret | +0.0485 | 0.17% | 9.57% | 8421/2677 |
| Relative Volume | +0.0480 | 3.13% | nan% | 11237/0 |
| d_200-Day Simple Moving Average | +0.0473 | 0.35% | 11.23% | 8578/2860 |
| d_Performance (YTD) | +0.0455 | 0.17% | 8.10% | 8488/2733 |
| d_Target Price | -0.0447 | 0.22% | 0.47% | 435/284 |
| Performance (Week) | +0.0419 | 0.18% | 13.12% | 8834/2556 |
| d_Performance (Week) | +0.0350 | 0.97% | 7.39% | 7544/3771 |
| d_Short Ratio | +0.0302 | 0.22% | 3.93% | 4345/2655 |
| d_Insider Transactions | +0.0282 | 0.70% | 0.05% | 198/207 |
| d_Price | +0.0257 | 0.17% | 9.57% | 8421/2677 |
| d_Relative Volume | +0.0254 | 2.62% | 3.64% | 5190/5900 |
| d_Sales Growth Quarter Over Quarter | -0.0227 | 0.07% | 0.17% | 202/183 |
| d_Sales Year Over Year TTM | -0.0221 | 0.06% | 0.25% | 205/157 |
| d_Analyst Recom | -0.0199 | 0.14% | 0.20% | 80/72 |
| d_Profit Margin | +0.0183 | 0.23% | 0.00% | 211/181 |
| d_Gross Margin | +0.0174 | 0.26% | 0.14% | 220/194 |

## Combinations

| Pattern | n | Mean fwd | Hit up |
|---|---|---|---|
| true_ret>3% & DOWNTREND | 643 | 1.04% | 29.2% |
| true_ret>3% & UPTREND | 649 | 0.14% | 12.0% |
| true_ret>3% & MIXED | 466 | 0.22% | 18.2% |
| MonthΔ+ & Month<0 | 938 | 0.60% | 21.2% |
| MonthΔ+ & Month>0 | 1402 | 0.09% | 11.2% |

## Risk dominance probes

| State | n | Mean fwd | Mean fwd if score top quintile |
|---|---|---|---|
| Week>40% | 173 | 0.24% | 1.05% |
| Week>25% | 434 | 0.34% | 0.66% |
| Week>100% | 18 | -1.58% | n/a |
| RSI>75 | 217 | -0.54% | n/a |
