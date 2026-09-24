# fresh_cat panel — dated catalyst flags vs live `cat_*` (research only)

**Why.** Live `cat_<theme>` flags (`src/finviz_delta._add_catalyst_flags`) are a keyword
hit on Finviz `Daily Digest` + `News Title`, with no date check. Finviz exports only each
ticker's *latest* headline, with its own `News Time` (ET). Over 2026-08-13..09-24 about
87% of `cat_data_center_power` / `cat_optics_transceiver` hits came from a headline older
than 48h or from the undated Daily Digest.

**What `fresh_cat_<theme>` means.** 1 only if the **headline** (not the digest) matches the
same regex **and** its `News Time` is after the previous trading day's snapshot and not
after this snapshot. Friday-evening / weekend news therefore counts on Monday.

| Field | Meaning |
|---|---|
| `snapshot_anchor_et` | snapshot time (ET): `scrape_ts` if the file has it (from 2026-09-25), else newest `News Time` in the file (`anchor_source`) |
| `fresh_lower_bound_et` | previous trading day's snapshot anchor; if that file is missing, anchor − 72h (`lower_bound_source`, e.g. 2026-08-28 because 2026-08-27 has no snapshot) |
| `news_age_h` | hours from `news_time` to the snapshot anchor (NaN = undated) |
| `cat_*` | live flags, unchanged (still feed `n_catalysts` / scores) |
| `fresh_cat_*` | dated flags (never start with `cat_`, so they are not counted in `n_catalysts`) |

**Sparse layout.** `fresh_cat_panel_2026-08-13_2026-09-24.csv` holds only ticker-days where some
`cat_*` = 1 (11,084 rows, 29 dates). A ticker-day that is absent has every `cat_*` and `fresh_cat_*`
= 0: `fresh_cat_*` ⊆ `cat_*` is asserted by the builder. Daily totals are in
`fresh_cat_daily_counts_2026-08-13_2026-09-24.csv`.

**Totals over the window (ticker-days):** data_center_power 3,020 → 270 fresh; optics_transceiver
816 → 78; all 8 themes 12,080 → 1,086.

**Not wired into scoring.** `data/features` and scores are untouched (feature_log still copies
`cat_*` only). Switching the scoring engine to `fresh_cat_*` needs its own decision.

Rebuild: `python -m research.fresh_cat_panel.build_fresh_cat_panel --start 2026-08-13 --end 2026-09-24`
