# Suggestion check — signal **2026-08-07** (full universe)

## What this measures

- **Signal as-of:** **2026-08-07** — `total_score` from data through this day only.
- **Expected UP** if score > +2; **Expected DOWN** if score < −2; else NEUTRAL (excluded from accuracy).
- **Hit** = expected UP and fwd>0, or expected DOWN and fwd<0.
- **fwd** = exit/entry − 1 on a **later** snapshot (not scan.md same-window Ret%).
- **Full universe CSV:** `data/attribution/2026-08-07_suggestion_check.csv`

## Prediction accuracy (full universe)

| Horizon | Pred day | n universe | n actionable | Accuracy | Long acc | Short acc | IC(score,fwd) | Mean fwd long | Mean fwd short |
|---------|----------|------------|--------------|----------|----------|-----------|---------------|---------------|----------------|
| 1d | 2026-08-10 | 11525 | 4349 | **45.4%** | 41.9% | 52.3% | -0.0339 | -0.55% | +18.77% |
| 2d | 2026-08-11 | 11525 | 4349 | **47.2%** | 46.0% | 49.7% | -0.0242 | -0.16% | +20.83% |

## Readable slice — horizon 1d (pred day **2026-08-10**)
_(every ticker is in the CSV)_

### Top 15 scores

| Ticker | Score | Entry | Exit | fwd | Hit? |
|---|---|---|---|---|---|
| MP | +9.0 | 51.11 | 54.66 | +6.95% | **YES** |
| NRGV | +9.0 | 3.49 | 3.34 | -4.30% | **NO** |
| TMC | +9.0 | 4.57 | 4.43 | -3.06% | **NO** |
| OKLO | +8.2 | 48.42 | 44.49 | -8.12% | **NO** |
| LIDR | +8.2 | 1.32 | 1.3 | -1.52% | **NO** |
| ALOY | +8.2 | 12.27 | 12.98 | +5.79% | **YES** |
| FIP | +8.2 | 4.27 | 4.3 | +0.70% | **YES** |
| ALM | +8.2 | 14.18 | 13.7 | -3.39% | **NO** |
| UUUU | +8.2 | 14.14 | 14.29 | +1.06% | **YES** |
| USAR | +8.2 | 19.33 | 19.04 | -1.50% | **NO** |
| BVC | +8.0 | 12.55 | 12.83 | +2.23% | **YES** |
| CELH | +8.0 | 27.77 | 27.21 | -2.02% | **NO** |
| DKNG | +8.0 | 24.03 | 24.27 | +1.00% | **YES** |
| AAUC | +8.0 | 21.78 | 22.22 | +2.02% | **YES** |
| SSP | +8.0 | 3.32 | 3.33 | +0.30% | **YES** |

### Bottom 10 scores

| Ticker | Score | Entry | Exit | fwd | Hit? |
|---|---|---|---|---|---|
| CRCT | -7.5 | 5.84 | 5.9 | +1.03% | **NO** |
| PLTZ | -7.5 | 10.25 | 9.85 | -3.90% | **YES** |
| CABR | -7.5 | 1.34 | 1.44 | +7.46% | **NO** |
| ODC | -7.5 | 92.79 | 88.02 | -5.14% | **YES** |
| DUST | -7.5 | 41.75 | 41.13 | -1.49% | **YES** |
| FG | -7.8 | 27.67 | 27.08 | -2.13% | **YES** |
| MI | -7.8 | 7.41 | 7.7 | +3.91% | **NO** |
| DWSN | -7.8 | 4.35 | 4.23 | -2.76% | **YES** |
| SAIH | -8.0 | 20.82 | 22.5 | +8.07% | **NO** |
| ZTG | -8.0 | 9.2 | 9.3 | +1.09% | **NO** |
