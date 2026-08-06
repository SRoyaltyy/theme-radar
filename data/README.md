# Finviz Universe

Place a processed version of the Finviz export here as `finviz_universe.csv`.

## Recommended columns for theme mapping

- Ticker
- Company
- Sector
- Industry
- Market Cap
- Performance (Week / Month / Quarter / Half Year / YTD)
- Relative Strength / technicals if available
- Finviz_Description (or a shortened version)
- Country / Exchange

## Handling the large file

The original export is ~9 MB and contains thousands of rows.  
Do **not** inject the entire CSV into the LLM context.

Instead:

1. Pre-build lightweight indexes (by Sector, by Industry, by keyword in description).
2. When a theme is scored, the mapper queries only the relevant slice (e.g. all “Semiconductors” + description contains “HBM” or “PCIe”).
3. Return a short ranked list of pure-play candidates (ticker, market cap, recent performance, one-line description).

This keeps token usage low and makes the mapping step fast and auditable.
