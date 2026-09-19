# SUMMARY_all — 2d/3d/5d cumulative top-G/L roll-up

Forward Price[T+H]/Price[T]−1 on clean midcap. See README.md for clocks + filters.

| Horizon | # session starts T | Last T | Last T+H | Notes |
|---:|---:|---|---|---|
| 2d | 23 | 2026-09-16 | 2026-09-18 | top25 G + top15 L per T |
| 3d | 22 | 2026-09-15 | 2026-09-18 | top25 G + top15 L per T |
| 5d | 20 | 2026-09-11 | 2026-09-18 | top25 G + top15 L per T |

## Sample top5 (latest valid T per horizon)

### H=2 date_T=2026-09-16 → 2026-09-18

- **SECZ** +39.77% | T-1 RelVol=0.72; T-1 Gap=-1.34%; T-1 Chg=-2.92%; afterT RelVol=1.59; afterT Chg=-2.51%; news=SEC Sends Strong Signal to Robinhood, Coinbase Investors; LAG
- **FWDI** +28.12% | T-1 RelVol=1.65; T-1 Gap=-2.59%; T-1 Chg=-12.52%; afterT RelVol=1.20; afterT Chg=-1.15%; news=Forward Industries Sweetens SkyAI Takeover Offer to 50% Premium; LAG
- **ABTC** +24.08% | T-1 RelVol=0.81; T-1 Gap=-2.68%; T-1 Chg=-7.63%; afterT RelVol=0.71; afterT Chg=+1.88%; news=American Bitcoin Shares Rise 1% Premarket After BTIG Initiates Coverage With Buy; LAG
- **PURR** +23.16% | T-1 RelVol=1.32; T-1 Gap=-4.39%; T-1 Chg=-5.49%; afterT RelVol=0.93; afterT Chg=+2.14%; news=PURR Stock: Compass Point Calls For 63% Upside, HYPE Treasury Bet Nears $2.5B; LAG
- **MSTR** +21.98% | T-1 RelVol=0.99; T-1 Gap=-3.84%; T-1 Chg=-5.36%; afterT RelVol=0.95; afterT Chg=-2.64%; news=Weekly Wrap: Bitcoin Climbs Back Above $80,000; LAG

### H=3 date_T=2026-09-15 → 2026-09-18

- **SECZ** +36.26% | T-1 RelVol=0.85; T-1 Gap=-3.02%; T-1 Chg=-0.73%; afterT RelVol=0.72; afterT Chg=-2.92%; news=SEC Sends Strong Signal to Robinhood, Coinbase Investors; LAG
- **BRUN** +27.27% | T-1 RelVol=1.45; T-1 Gap=-5.35%; T-1 Chg=-12.39%; afterT RelVol=1.53; afterT Chg=-6.86%; news=Boost Run Announces Completion of Warrant Redemption; LAG
- **FWDI** +26.64% | T-1 RelVol=1.09; T-1 Gap=-1.07%; T-1 Chg=+6.11%; afterT RelVol=1.65; afterT Chg=-12.52%; news=Forward Industries Sweetens SkyAI Takeover Offer to 50% Premium; LAG
- **ABTC** +26.41% | T-1 RelVol=1.00; T-1 Gap=-2.04%; T-1 Chg=+3.97%; afterT RelVol=0.81; afterT Chg=-7.63%; news=American Bitcoin Shares Rise 1% Premarket After BTIG Initiates Coverage With Buy; LAG
- **PURR** +25.80% | T-1 RelVol=0.99; T-1 Gap=-1.64%; T-1 Chg=+2.07%; afterT RelVol=1.32; afterT Chg=-5.49%; news=PURR Stock: Compass Point Calls For 63% Upside, HYPE Treasury Bet Nears $2.5B; LAG

### H=5 date_T=2026-09-11 → 2026-09-18

- **SDGR** +52.58% | T-1 RelVol=0.44; T-1 Gap=-2.03%; T-1 Chg=-2.08%; afterT RelVol=0.40; afterT Chg=+1.17%; news=Schrodinger Reports Inducement Grants under Nasdaq Listing Rule 5635(c)(4); LAG
- **BBNX** +32.11% | T-1 RelVol=0.83; T-1 Gap=+1.03%; T-1 Chg=-4.76%; afterT RelVol=0.63; afterT Chg=-0.12%; news=Beta Bionics Announces Pricing of Public Offering of Common Stock and Pre-Funded; LAG
- **TEM** +31.91% | T-1 RelVol=0.85; T-1 Gap=-2.30%; T-1 Chg=-4.14%; afterT RelVol=0.58; afterT Chg=+0.46%; news=Will 2026 Doom and Gloom Lead to Opportunity?; LAG
- **SECZ** +31.32% | T-1 RelVol=0.82; T-1 Gap=-0.83%; T-1 Chg=-4.63%; afterT RelVol=0.53; afterT Chg=+2.86%; news=SEC Sends Strong Signal to Robinhood, Coinbase Investors; LAG
- **TWST** +31.26% | T-1 RelVol=0.72; T-1 Gap=-3.08%; T-1 Chg=+1.06%; afterT RelVol=0.62; afterT Chg=+0.29%; news=TWST Stock Hits Multi-Year High, But Pharma Bro Martin Shkreli Calls Twist A Sho

## Clock reminder

- **Clock B (open of T):** use `knowable_*_Tm1` only.
- **Clock A (open of T+1 after T close):** `after_T_*` are knowable.

## Requested sample dates (trailing as-of — appendix)

Forward tables cannot start at 2026-09-17 (H=2) or 2026-09-18 (H=5) because T+H is past the calendar end 2026-09-18.
Below: **trailing** Price[T]/Price[T−H]−1 as-of those end dates (not in main CSVs; main CSVs are forward).

### As-of 2026-09-17 trailing H=2 (start 2026-09-15 → 2026-09-17)

- **SDGR** +30.06% (23.25→30.24) | T-1 RelVol=2.32; afterT RelVol=7.30; afterT Chg=+26.37%; news=Schrodinger Reports Inducement Grants under Nasdaq Listing Rule 5635(c
- **USDE** +25.98% (6.12→7.71) | T-1 RelVol=0.28; afterT RelVol=2.90; afterT Chg=+24.35%; news=StablecoinX Inc. to Participate in the 28th Annual H.C. Wainwright Glo
- **BRUN** +22.92% (13.57→16.68) | T-1 RelVol=2.14; afterT RelVol=1.37; afterT Chg=+10.03%; news=Boost Run Announces Preliminary Inclusion in the Russell 2000 and Russ
- **FPS** +21.36% (31.36→38.06) | T-1 RelVol=2.55; afterT RelVol=2.39; afterT Chg=+9.24%; news=Most Active Options Report: FPS, TEVA, AFL
- **GNRC** +18.40% (175.03→207.23) | T-1 RelVol=1.53; afterT RelVol=7.64; afterT Chg=+18.34%; news=Why Does Generac Stock Cost More Than Its Faster-Growing Peers?

### As-of 2026-09-18 trailing H=5 (start 2026-09-11 → 2026-09-18)

- **SDGR** +52.58% (19.02→29.02) | T-1 RelVol=7.30; afterT RelVol=3.86; afterT Chg=-4.03%; news=Schrodinger Reports Inducement Grants under Nasdaq Listing Rule 5635(c
- **ELMT** +41.94% (16.19→22.98) | T-1 RelVol=2.06; afterT RelVol=1.78; afterT Chg=+4.60%; news=A Trillion-Dollar Pool of Money Is About to Be Forced to Notice This C
- **USDE** +40.36% (7.26→10.19) | T-1 RelVol=2.90; afterT RelVol=2.87; afterT Chg=+32.17%; news=StablecoinX Inc. to Participate in the 28th Annual H.C. Wainwright Glo
- **BBNX** +32.11% (16.57→21.89) | T-1 RelVol=2.46; afterT RelVol=1.52; afterT Chg=+2.15%; news=Beta Bionics Investors Who Lost Money: Contact Block & Leviton LLP Abo
- **TEM** +31.91% (59.01→77.84) | T-1 RelVol=2.68; afterT RelVol=1.44; afterT Chg=-3.14%; news=The ARK Trade Watch: Cathie Wood Cuts Crypto Exposure, Then Reverses C

## Forward samples (main CSVs) — nearest valid starts

### Forward H=2 date_T=2026-09-16 → 2026-09-18

- **SECZ** +39.77% (7.77→10.86) | T-1 RelVol=0.72; afterT RelVol=1.59; afterT Chg=-2.51%; lag=True
- **FWDI** +28.12% (6.01→7.70) | T-1 RelVol=1.65; afterT RelVol=1.2; afterT Chg=-1.15%; lag=True
- **ABTC** +24.08% (8.14→10.10) | T-1 RelVol=0.81; afterT RelVol=0.71; afterT Chg=+1.88%; lag=True
- **PURR** +23.16% (11.44→14.09) | T-1 RelVol=1.32; afterT RelVol=0.93; afterT Chg=+2.14%; lag=True
- **MSTR** +21.98% (126.18→153.92) | T-1 RelVol=0.99; afterT RelVol=0.95; afterT Chg=-2.64%; lag=True

### Forward H=5 date_T=2026-09-11 → 2026-09-18

- **SDGR** +52.58% (19.02→29.02) | T-1 RelVol=0.44; afterT RelVol=0.4; lag=True
- **BBNX** +32.11% (16.57→21.89) | T-1 RelVol=0.83; afterT RelVol=0.63; lag=True
- **TEM** +31.91% (59.01→77.84) | T-1 RelVol=0.85; afterT RelVol=0.58; lag=True
- **SECZ** +31.32% (8.27→10.86) | T-1 RelVol=0.82; afterT RelVol=0.53; lag=True
- **TWST** +31.26% (127.22→166.99) | T-1 RelVol=0.72; afterT RelVol=0.62; lag=False

