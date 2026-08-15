# Predictive audit — horizon **3d**

Generated: 2026-08-15T04:32:55.976724-04:00
Signal dates pooled: **4** (`2026-08-06, 2026-08-07, 2026-08-10, 2026-08-11`)

## 1. Prediction accuracy (composite `total_score`, full universe)

Rule: score > +2 → expect UP; score < −2 → expect DOWN; else neutral.

| Metric | Value |
|--------|-------|
| Names graded | 46118 |
| Actionable (|score|>2) | 12970 |
| **Accuracy (actionable)** | **45.6%** |
| Long accuracy | 51.9% |
| Short accuracy | 38.3% |
| Spearman IC(score, fwd) | -0.0098 |

### Per signal date

| Signal | n | Actionable | Accuracy | Long | Short | IC |
|--------|---|------------|----------|------|-------|----|
| 2026-08-06 | 11518 | 314 | 57.6% | 62.1% | 34.0% | +0.0815 |
| 2026-08-07 | 11525 | 4349 | 49.9% | 51.5% | 46.6% | -0.0009 |
| 2026-08-10 | 11533 | 4490 | 37.5% | 47.7% | 31.3% | -0.1054 |
| 2026-08-11 | 11542 | 3817 | 49.4% | 54.5% | 42.8% | +0.0639 |

## 2. Top correlating factors (pooled across dates)

IC = Spearman(factor, forward return). Ranked by |IC|. Spread = mean fwd when factor>0 minus mean fwd when factor<0.

| Rank | Factor | IC | n | Mean fwd if ↑ | Mean fwd if ↓ | Spread |
|------|--------|----|---|---------------|---------------|--------|
| 1 | d_Performance (Week) | -0.1605 | 34417 | +1.22% | +2.85% | -1.63% |
| 2 | d_Relative Strength Index (14) | -0.1104 | 34284 | +0.76% | +4.18% | -3.42% |
| 3 | Performance (YTD) | +0.1051 | 46087 | +0.83% | +5.58% | -4.74% |
| 4 | d_200-Day Simple Moving Average | -0.0978 | 34575 | +0.85% | +3.90% | -3.05% |
| 5 | d_50-Day Simple Moving Average | -0.0887 | 34575 | +0.89% | +3.85% | -2.97% |
| 6 | d_Performance (Quarter) | -0.0883 | 32689 | +0.76% | +3.93% | -3.17% |
| 7 | d_Price | -0.0855 | 34575 | +0.73% | +3.67% | -2.94% |
| 8 | true_ret | -0.0851 | 34575 | +0.73% | +3.67% | -2.94% |
| 9 | d_Forward P/E | -0.0842 | 9154 | +0.44% | +1.11% | -0.66% |
| 10 | d_Performance (YTD) | -0.0839 | 34554 | +0.59% | +3.43% | -2.84% |
| 11 | Beta | +0.0801 | 29266 | +2.18% | +4.44% | -2.26% |
| 12 | 200-Day Simple Moving Average | +0.0785 | 46118 | +0.73% | +5.55% | -4.82% |
| 13 | d_20-Day Simple Moving Average | -0.0757 | 34575 | +0.96% | +3.63% | -2.67% |
| 14 | Sales Year Over Year TTM | +0.0705 | 18168 | +4.51% | +4.41% | +0.09% |
| 15 | Sales Growth Quarter Over Quarter | +0.0676 | 18983 | +2.04% | +3.49% | -1.45% |
| 16 | d_Market Cap | -0.0645 | 17683 | +1.42% | +6.04% | -4.62% |
| 17 | Volatility (Month) | +0.0573 | 34042 | n/a | n/a | n/a |
| 18 | Price | +0.0567 | 46118 | n/a | n/a | n/a |
| 19 | d_Institutional Ownership | +0.0472 | 17536 | +1.40% | +2.82% | -1.42% |
| 20 | Short Float | +0.0467 | 23017 | n/a | n/a | n/a |
| 21 | Analyst Recom | -0.0453 | 18359 | n/a | n/a | n/a |
| 22 | d_Performance (Month) | -0.0448 | 34064 | +1.22% | +3.32% | -2.10% |
| 23 | Market Cap | +0.0419 | 23585 | n/a | n/a | n/a |
| 24 | 50-Day Simple Moving Average | -0.0412 | 46118 | +0.50% | +5.86% | -5.37% |
| 25 | catalyst_score | +0.0401 | 46118 | +2.79% | +2.75% | +0.04% |

## 3. Factor combinations (sign quadrants)

Among stronger single factors: A↑B↑ / A↑B↓ / A↓B↑ / A↓B↓. **Score** = |mean_fwd| × √n (ranking aid only).

| Rank | Combination | n | Mean fwd | % up | % down | Score |
|------|-------------|---|----------|------|--------|-------|
| 1 | d_Relative Strength Index (14)↓ & d_Performance (Quarter)↓ | 10552 | +5.02% | 70.1% | 28.0% | 5.161 |
| 2 | d_50-Day Simple Moving Average↓ & d_Performance (Quarter)↓ | 10648 | +4.82% | 70.9% | 27.2% | 4.974 |
| 3 | d_200-Day Simple Moving Average↓ & d_Performance (Quarter)↓ | 10838 | +4.77% | 71.2% | 27.0% | 4.970 |
| 4 | d_Relative Strength Index (14)↓ & d_200-Day Simple Moving Average↓ | 14068 | +4.18% | 69.0% | 29.1% | 4.958 |
| 5 | d_Relative Strength Index (14)↓ & d_50-Day Simple Moving Average↓ | 13790 | +4.20% | 68.9% | 29.1% | 4.936 |
| 6 | d_200-Day Simple Moving Average↓ & d_50-Day Simple Moving Average↓ | 14571 | +4.01% | 69.6% | 28.2% | 4.838 |
| 7 | d_Performance (Week)↓ & d_Relative Strength Index (14)↓ | 12567 | +4.09% | 69.9% | 28.1% | 4.583 |
| 8 | d_Performance (Week)↓ & d_50-Day Simple Moving Average↓ | 13009 | +3.98% | 70.7% | 27.3% | 4.539 |
| 9 | d_Performance (Week)↓ & d_200-Day Simple Moving Average↓ | 13083 | +3.95% | 71.2% | 26.9% | 4.518 |
| 10 | d_Performance (Quarter)↓ & d_Price↓ | 10341 | +4.38% | 70.2% | 28.0% | 4.454 |
| 11 | d_Performance (Quarter)↓ & true_ret↓ | 10341 | +4.38% | 70.2% | 28.0% | 4.454 |
| 12 | d_Relative Strength Index (14)↓ & d_Price↓ | 14173 | +3.69% | 68.4% | 29.7% | 4.397 |
| 13 | d_Relative Strength Index (14)↓ & true_ret↓ | 14173 | +3.69% | 68.4% | 29.7% | 4.397 |
| 14 | d_Price↓ & true_ret↓ | 14291 | +3.67% | 68.4% | 29.7% | 4.387 |
| 15 | d_Performance (Week)↓ & d_Performance (Quarter)↓ | 11724 | +4.04% | 71.7% | 26.5% | 4.375 |
| 16 | d_50-Day Simple Moving Average↓ & d_Price↓ | 13662 | +3.70% | 68.9% | 29.2% | 4.325 |
| 17 | d_50-Day Simple Moving Average↓ & true_ret↓ | 13662 | +3.70% | 68.9% | 29.2% | 4.325 |
| 18 | d_200-Day Simple Moving Average↓ & d_Price↓ | 13923 | +3.63% | 68.9% | 29.2% | 4.278 |
| 19 | d_200-Day Simple Moving Average↓ & true_ret↓ | 13923 | +3.63% | 68.9% | 29.2% | 4.278 |
| 20 | d_Performance (Week)↓ & d_Price↓ | 12330 | +3.56% | 70.0% | 28.2% | 3.956 |

## Notes

- With few signal dates, treat rankings as **exploratory**.
- `d_*` = day-over-day delta on the signal pair; bare names = levels.
- JSON: `03_scoreboard/predictive_audit_3d.json`
