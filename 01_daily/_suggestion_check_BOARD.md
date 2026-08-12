# Suggestion check board — full universe accuracy

Score on **signal_asof**; grade on later **prediction day**. Accuracy = share of actionable names (score >+2 or <-2) whose forward return matched the expected direction.

| Signal | Pred day (1d) | n actionable | Accuracy | Long acc | Short acc | IC |
|--------|---------------|--------------|----------|----------|-----------|----|
| 2026-08-06 | 2026-08-07 | 314 | **58.0%** | 63.3% | 30.0% | +0.0958 |
| 2026-08-07 | 2026-08-10 | 4349 | **45.4%** | 41.9% | 52.3% | -0.0339 |
| 2026-08-10 | 2026-08-11 | 4490 | **43.2%** | 49.8% | 39.2% | -0.0491 |

Detail: `01_daily/<signal>_suggestion_check.md`
All tickers: `data/attribution/<signal>_suggestion_check.csv`
Factors + combos: `03_scoreboard/predictive_audit.md`
