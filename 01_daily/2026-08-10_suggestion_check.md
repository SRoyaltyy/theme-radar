# Suggestion check — signal **2026-08-10** (full universe)

## What this measures

- **Signal as-of:** **2026-08-10** — `total_score` from data through this day only.
- **Expected UP** if score > +2; **Expected DOWN** if score < −2; else NEUTRAL (excluded from accuracy).
- **Hit** = expected UP and fwd>0, or expected DOWN and fwd<0.
- **fwd** = exit/entry − 1 on a **later** snapshot (not scan.md same-window Ret%).
- **Full universe CSV:** `data/attribution/2026-08-10_suggestion_check.csv`

## Prediction accuracy (full universe)

| Horizon | Pred day | n universe | n actionable | Accuracy | Long acc | Short acc | IC(score,fwd) | Mean fwd long | Mean fwd short |
|---------|----------|------------|--------------|----------|----------|-----------|---------------|---------------|----------------|
| 1d | 2026-08-11 | 11533 | 4490 | **43.2%** | 49.8% | 39.2% | -0.0491 | +0.90% | +0.42% |

## Readable slice — horizon 1d (pred day **2026-08-11**)
_(every ticker is in the CSV)_

### Top 15 scores

| Ticker | Score | Entry | Exit | fwd | Hit? |
|---|---|---|---|---|---|
| ACHR | +8.5 | 6.26 | 6.79 | +8.47% | **YES** |
| ATCX | +8.2 | 3.14 | 3.2 | +1.91% | **YES** |
| MP | +8.2 | 54.66 | 55.24 | +1.06% | **YES** |
| LAR | +8.2 | 7.1 | 6.65 | -6.34% | **NO** |
| ALOY | +8.2 | 12.98 | 12.75 | -1.77% | **NO** |
| SLI | +8.2 | 2.53 | 2.45 | -3.16% | **NO** |
| SLSR | +8.2 | 8.25 | 8.13 | -1.45% | **NO** |
| PDS | +8.0 | 81.39 | 83.02 | +2.00% | **YES** |
| GLBS | +8.0 | 3.39 | 3.68 | +8.55% | **YES** |
| DDC | +8.0 | 0.55 | 0.49 | -10.91% | **NO** |
| PPBT | +8.0 | 1.5 | 1.55 | +3.33% | **YES** |
| SAFX | +8.0 | 0.45 | 0.45 | +0.00% | **NO** |
| CRC | +8.0 | 53.75 | 54.13 | +0.71% | **YES** |
| NSLR | +8.0 | 10.33 | 10.64 | +3.00% | **YES** |
| HNRG | +8.0 | 15.88 | 15.64 | -1.51% | **NO** |

### Bottom 10 scores

| Ticker | Score | Entry | Exit | fwd | Hit? |
|---|---|---|---|---|---|
| FEDU | -7.8 | 7.5 | 6.91 | -7.87% | **YES** |
| UAN | -7.8 | 117.01 | 120.17 | +2.70% | **NO** |
| AFL | -7.8 | 121.94 | 121.07 | -0.71% | **YES** |
| PSMT | -7.8 | 168.81 | 172.86 | +2.40% | **NO** |
| WPP | -8.2 | 26.69 | 27.04 | +1.31% | **NO** |
| NYC | -8.5 | 8.23 | 8.0 | -2.79% | **YES** |
| TISI | -8.5 | 16.55 | 22.71 | +37.22% | **NO** |
| VSTS | -8.5 | 13.87 | 13.88 | +0.07% | **NO** |
| OPHC | -9.0 | 8.92 | 9.2 | +3.14% | **NO** |
| HNST | -9.0 | 5.23 | 5.21 | -0.38% | **YES** |
