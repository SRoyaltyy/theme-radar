# Predictive audit — horizon **1d**

Generated: 2026-08-12T05:19:33.039020-04:00
Signal dates pooled: **3** (`2026-08-06, 2026-08-07, 2026-08-10`)

## 1. Prediction accuracy (composite `total_score`, full universe)

Rule: score > +2 → expect UP; score < −2 → expect DOWN; else neutral.

| Metric | Value |
|--------|-------|
| Names graded | 34601 |
| Actionable (|score|>2) | 9153 |
| **Accuracy (actionable)** | **44.8%** |
| Long accuracy | 45.8% |
| Short accuracy | 43.6% |
| Spearman IC(score, fwd) | -0.0135 |

### Per signal date

| Signal | n | Actionable | Accuracy | Long | Short | IC |
|--------|---|------------|----------|------|-------|----|
| 2026-08-06 | 11543 | 314 | 58.0% | 63.3% | 30.0% | +0.0958 |
| 2026-08-07 | 11525 | 4349 | 45.4% | 41.9% | 52.3% | -0.0339 |
| 2026-08-10 | 11533 | 4490 | 43.2% | 49.8% | 39.2% | -0.0491 |

## 2. Top correlating factors (pooled across dates)

IC = Spearman(factor, forward return). Ranked by |IC|. Spread = mean fwd when factor>0 minus mean fwd when factor<0.

| Rank | Factor | IC | n | Mean fwd if ↑ | Mean fwd if ↓ | Spread |
|------|--------|----|---|---------------|---------------|--------|
| 1 | d_Performance (Week) | -0.1287 | 22941 | +0.46% | +2.65% | -2.19% |
| 2 | d_Price | -0.1226 | 23043 | -0.10% | +3.15% | -3.26% |
| 3 | d_20-Day Simple Moving Average | -0.1211 | 23043 | +0.07% | +3.52% | -3.45% |
| 4 | d_Performance (YTD) | -0.1174 | 23029 | -0.10% | +2.87% | -2.97% |
| 5 | true_ret | -0.1159 | 23043 | -0.10% | +3.15% | -3.26% |
| 6 | d_200-Day Simple Moving Average | -0.1144 | 23043 | +0.05% | +3.68% | -3.63% |
| 7 | d_Relative Strength Index (14) | -0.1120 | 22851 | -0.10% | +4.03% | -4.13% |
| 8 | d_50-Day Simple Moving Average | -0.1099 | 23043 | +0.09% | +3.62% | -3.53% |
| 9 | d_Performance (Quarter) | -0.0882 | 21787 | -0.00% | +3.92% | -3.92% |
| 10 | d_Forward P/E | -0.0857 | 6104 | -0.40% | -0.03% | -0.37% |
| 11 | d_Institutional Ownership | +0.0796 | 11689 | +0.64% | +0.14% | +0.50% |
| 12 | d_Market Cap | -0.0747 | 11784 | +0.72% | +6.11% | -5.39% |
| 13 | upside_pct | +0.0746 | 13948 | +1.86% | +0.04% | +1.82% |
| 14 | upside_pct_lvl | +0.0746 | 13948 | +1.86% | +0.05% | +1.81% |
| 15 | n_pos | -0.0664 | 34601 | n/a | n/a | n/a |
| 16 | Total Debt/Equity | -0.0596 | 10088 | n/a | n/a | n/a |
| 17 | Analyst Recom | -0.0554 | 13770 | n/a | n/a | n/a |
| 18 | Beta | -0.0552 | 19511 | +2.02% | +0.45% | +1.57% |
| 19 | Profit Margin | -0.0498 | 14038 | +0.18% | +8.19% | -8.02% |
| 20 | technical_score | -0.0457 | 34601 | +0.34% | +6.30% | -5.96% |
| 21 | Performance (Quarter) | -0.0446 | 32711 | +0.20% | +3.43% | -3.23% |
| 22 | d_Volatility (Month) | +0.0440 | 11334 | +0.54% | +0.34% | +0.20% |
| 23 | Performance (Week) | +0.0423 | 34431 | +0.42% | +4.91% | -4.48% |
| 24 | Sales Growth Quarter Over Quarter | +0.0421 | 14242 | +0.94% | +1.98% | -1.04% |
| 25 | Short Float | +0.0408 | 17264 | n/a | n/a | n/a |

## 3. Factor combinations (sign quadrants)

Among stronger single factors: A↑B↑ / A↑B↓ / A↓B↑ / A↓B↓. **Score** = |mean_fwd| × √n (ranking aid only).

| Rank | Combination | n | Mean fwd | % up | % down | Score |
|------|-------------|---|----------|------|--------|-------|
| 1 | d_20-Day Simple Moving Average↓ & d_Relative Strength Index (14)↓ | 9011 | +4.01% | 52.8% | 42.2% | 3.804 |
| 2 | d_200-Day Simple Moving Average↓ & d_Relative Strength Index (14)↓ | 9216 | +3.96% | 52.5% | 42.4% | 3.803 |
| 3 | d_Relative Strength Index (14)↓ & d_50-Day Simple Moving Average↓ | 9078 | +3.96% | 52.4% | 42.6% | 3.777 |
| 4 | d_20-Day Simple Moving Average↓ & d_200-Day Simple Moving Average↓ | 9453 | +3.83% | 52.0% | 42.3% | 3.721 |
| 5 | d_20-Day Simple Moving Average↓ & d_50-Day Simple Moving Average↓ | 9519 | +3.80% | 51.8% | 42.5% | 3.704 |
| 6 | d_200-Day Simple Moving Average↓ & d_50-Day Simple Moving Average↓ | 9524 | +3.79% | 51.6% | 42.7% | 3.698 |
| 7 | d_Performance (Week)↓ & d_Relative Strength Index (14)↓ | 8070 | +4.03% | 53.4% | 41.8% | 3.616 |
| 8 | d_Performance (Week)↓ & d_200-Day Simple Moving Average↓ | 8348 | +3.89% | 52.7% | 42.3% | 3.558 |
| 9 | d_Performance (Week)↓ & d_50-Day Simple Moving Average↓ | 8353 | +3.88% | 52.5% | 42.3% | 3.544 |
| 10 | d_Performance (Week)↓ & d_20-Day Simple Moving Average↓ | 8671 | +3.75% | 52.1% | 42.9% | 3.496 |
| 11 | d_Price↓ & d_Relative Strength Index (14)↓ | 9287 | +3.18% | 52.8% | 42.5% | 3.061 |
| 12 | true_ret↓ & d_Relative Strength Index (14)↓ | 9287 | +3.18% | 52.8% | 42.5% | 3.061 |
| 13 | d_Price↓ & true_ret↓ | 9358 | +3.15% | 52.7% | 42.5% | 3.049 |
| 14 | d_Price↓ & d_20-Day Simple Moving Average↓ | 8923 | +3.11% | 53.2% | 42.0% | 2.941 |
| 15 | d_20-Day Simple Moving Average↓ & true_ret↓ | 8923 | +3.11% | 53.2% | 42.0% | 2.941 |
| 16 | d_Price↓ & d_50-Day Simple Moving Average↓ | 8999 | +3.07% | 52.8% | 42.4% | 2.917 |
| 17 | true_ret↓ & d_50-Day Simple Moving Average↓ | 8999 | +3.07% | 52.8% | 42.4% | 2.917 |
| 18 | d_Price↓ & d_200-Day Simple Moving Average↓ | 9131 | +3.04% | 52.9% | 42.3% | 2.903 |
| 19 | true_ret↓ & d_200-Day Simple Moving Average↓ | 9131 | +3.04% | 52.9% | 42.3% | 2.903 |
| 20 | d_Performance (Week)↓ & d_Performance (YTD)↓ | 8074 | +3.15% | 53.5% | 41.7% | 2.828 |

## Notes

- With few signal dates, treat rankings as **exploratory**.
- `d_*` = day-over-day delta on the signal pair; bare names = levels.
- JSON: `03_scoreboard/predictive_audit_1d.json`
