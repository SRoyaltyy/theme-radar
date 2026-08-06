# Finviz universe

Source: full Finviz export with company descriptions.

## Layout

Preferred load order in `finviz_mapper._load_universe()`:

1. `data/finviz_universe.csv` (single file, if present)
2. `data/universe_parts/part_*.csv` (split shards — recommended for git)
3. `data/finviz_with_descriptions.csv` (raw dump fallback)

## How to install the data (one-time)

The processed shards are ~0.85 MB each (4 parts, ~5960 tickers).

**Option A — GitHub web UI**  
Create folder `data/universe_parts/` and upload `part_00.csv` … `part_03.csv`.

**Option B — local git**
```bash
git clone https://github.com/SRoyaltyy/theme-radar.git
cd theme-radar
# copy the four part_*.csv files into data/universe_parts/
git add data/universe_parts
git commit -m "Add Finviz universe with descriptions"
git push
```

## Columns kept

Ticker, Company, Industry, Sector, Country, Exchange, Market Cap, Price,
Average Volume, Short Float, Volume, performance windows (Week/Month/Quarter/
Half Year/YTD/Year), Analyst Recom, Target Price, growth/EPS fields, and
**Finviz_Description** (truncated ~550 chars; still enough for keyword matching
on business model — optical, nuclear, copper, HBM, data center, etc.).

## How the mapper uses descriptions

For each theme, `desc_keywords` are matched against `Finviz_Description`.
Hits boost `rank_score` so true pure plays surface even when Industry is
broad (e.g. "Specialty Industrial Machinery" for GE Vernova nuclear/power).
