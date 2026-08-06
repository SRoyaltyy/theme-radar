# Finviz snapshots (current + previous)

Theme Radar always wants **two** Finviz exports ~one month apart.

```
data/snapshots/current.csv    ← newest export
data/snapshots/previous.csv   ← prior export (~30 days older)
data/snapshots/archive/       ← optional dated history
```

## Workflow when a new Finviz file arrives

```bash
# from repo root, with the new raw export saved somewhere:
python -m src.promote_snapshot /path/to/finviz_new.csv --as-of 2026-08-06
```

This will:
1. Move existing `current.csv` → `previous.csv`
2. Write the new file as normalized `current.csv`
3. Optionally archive a dated copy

## What the delta unlocks

| Signal | How used |
|--------|----------|
| Industry median Month / d_Month | Stage 1 cluster discovery |
| Ticker d_Performance (Month) | Acceleration filter |
| d_Institutional Transactions | Smart-money confirmation |
| d_Short Float | Crowding change |
| d_Insider Transactions | Insider cluster shifts |
| New tickers (`is_new`) | IPO / listing awareness |
| Target upside change | Valuation kill switch |

Without `previous.csv`, the system still runs but delta features are blank.
