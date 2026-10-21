"""Nightly write-once save of new root sources.

Rules:
- Write-once: a source-day that is already saved is never overwritten.
- All-or-nothing per source-day: every pull of a source is held in memory and the
  files are written only if ALL pulls succeeded. If any pull fails, the source-day is
  logged NOT_READY and no partial file is saved (the next run may retry it).
- Wikimedia: descriptive User-Agent, >=0.5 s between requests, retry on 429/5xx
  with exponential backoff that honours Retry-After (5 tries).
- Nasdaq QQQ/IWM: price data kept; shares outstanding is marked NO_SOURCE.
Env (local testing only): NEWROOTS_DIR (output root), NEWROOTS_WIKI_LIMIT (first N tickers),
NEWROOTS_SOURCES (comma list of sources to run).
"""
import requests,os,csv,json,html,time,datetime as D,urllib.parse as u
NOW=D.datetime.now(D.UTC);DAY=NOW.strftime('%Y-%m-%d')
ROOT=os.environ.get('NEWROOTS_DIR','data/newroots');B=f'{ROOT}/{DAY}';os.makedirs(B,exist_ok=True)
UA={'User-Agent':'theme-radar-newroots/1.1 (https://github.com/SRoyaltyy/theme-radar; nightly research job)'}
BR={'User-Agent':'Mozilla/5.0'};NQ={**BR,'Accept':'application/json'}
ONLY=set(filter(None,os.environ.get('NEWROOTS_SOURCES','').split(',')))
LOG=[]  # [source, file, status, http, bytes_or_note]

class PullFail(Exception): pass

def get(url,hdr,ok=lambda r:True,**kw):
  try: r=requests.get(url,headers=hdr,timeout=60,**kw)
  except Exception as e: raise PullFail(f'ERR {repr(e)[:80]}')
  if r.status_code!=200 or not ok(r): raise PullFail(f'HTTP {r.status_code}')
  return r

def source(name,files,pull):
  """files: names this source-day writes; pull() -> {filename: bytes}. All-or-nothing."""
  if ONLY and name not in ONLY: return
  have=[f for f in files if os.path.exists(f'{B}/{f}')]
  if have and len(have)==len(files): LOG.append([name,'*','SKIP_EXISTS','','']);return
  if have: LOG.append([name,'*','NOT_READY','',f'partial files already present: {have}']);return
  try: out=pull()
  except PullFail as e: LOG.append([name,'*','NOT_READY','',str(e)]);return
  assert set(out)==set(files),(name,set(out)^set(files))
  for f,b in out.items():
    tmp=f'{B}/.{f}.tmp';open(tmp,'wb').write(b);os.replace(tmp,f'{B}/{f}')
    LOG.append([name,f,'OK',200,len(b)])

# --- SSGA: SPY + 11 sector funds (one source-day = 12 files)
SS='SPY XLK XLF XLE XLV XLI XLY XLP XLU XLB XLRE XLC'.split()
source('ssga',[f'ssga_{t}.xlsx' for t in SS],lambda:{f'ssga_{t}.xlsx':get(
  f'https://www.ssga.com/us/en/intermediary/etfs/library-content/products/fund-data/etfs/us/navhist-us-en-{t.lower()}.xlsx',
  BR,lambda r:r.content[:2]==b'PK').content for t in SS})

# --- Cboe VIX term structure
VX=['VIX','VIX9D','VIX3M','VIX6M']
source('cboe_vix',[f'cboe_{s}_History.csv' for s in VX],lambda:{f'cboe_{s}_History.csv':get(
  f'https://cdn.cboe.com/api/global/us_indices/daily_prices/{s}_History.csv',UA,lambda r:r.text[:4]=='DATE').content for s in VX})

# --- Cboe put/call (prior UTC day)
d=(NOW-D.timedelta(days=1)).strftime('%Y-%m-%d')
source('cboe_putcall',[f'cboe_putcall_{d}.json'],lambda:{f'cboe_putcall_{d}.json':get(
  f'https://cdn.cboe.com/data/us/options/market_statistics/daily/{d}_daily_options',UA,lambda r:'ratios' in r.text).content})

# --- Nasdaq QQQ / IWM: price data only; shares outstanding has no source here
NT=['QQQ','IWM']
def pull_nasdaq():
  out={};meta={}
  for t in NT:
    r=get(f'https://api.nasdaq.com/api/quote/{t}/summary?assetclass=etf',NQ,lambda r:'"data":{' in r.text)
    out[f'nasdaq_{t}.json']=r.content
    meta[t]={'price_data':'nasdaq_summary','shares_outstanding':'NO_SOURCE',
             'note':'Nasdaq ETF summary has no shares-outstanding field; do not derive market cap from this file'}
  out['nasdaq_meta.json']=json.dumps(meta,indent=1).encode()
  return out
source('nasdaq',[f'nasdaq_{t}.json' for t in NT]+['nasdaq_meta.json'],pull_nasdaq)

# --- Wikimedia page views: last 7 days per article, summing redirect (old) titles
WIKI_GAP=0.5;_last=[0.0]
def wget(url,params=None,tries=5):
  for i in range(tries):
    w=WIKI_GAP-(time.monotonic()-_last[0])
    if w>0: time.sleep(w)
    _last[0]=time.monotonic()
    try: r=requests.get(url,params=params,headers=UA,timeout=30)
    except Exception as e: r=None;err=repr(e)[:80]
    if r is not None and r.status_code not in(429,500,502,503,504): return r
    ra=r.headers.get('Retry-After') if r is not None else None
    try: back=float(ra)
    except (TypeError,ValueError): back=0
    back=min(max(back,2**(i+1)),120)  # 2,4,8,16,32 s or Retry-After if longer
    if i<tries-1: time.sleep(back)
  raise PullFail(f'wiki gave {r.status_code if r is not None else err} after {tries} tries: {url[:90]}')

def pull_wiki():
  m=list(csv.DictReader(open('data/newroots/ticker_wiki_map.csv')))
  n=int(os.environ.get('NEWROOTS_WIKI_LIMIT','0') or 0)
  if n: m=m[:n]
  e=(NOW-D.timedelta(days=1)).strftime('%Y%m%d');s=(NOW-D.timedelta(days=8)).strftime('%Y%m%d');rows=[]
  for x in m:
    t=html.unescape(x['resolved_title']);tot={}
    q=wget('https://en.wikipedia.org/w/api.php',{'action':'query','list':'backlinks','bltitle':t,'blfilterredir':'redirects','bllimit':50,'blnamespace':0,'format':'json'})
    if q.status_code!=200: raise PullFail(f'backlinks HTTP {q.status_code} for {t}')
    rd=q.json().get('query',{}).get('backlinks',[])
    for ti in [t]+[b['title'] for b in rd]:
      r=wget('https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/user/'+u.quote(ti.replace(' ','_'),safe='')+f'/daily/{s}/{e}')
      if r.status_code==404 and ti!=t: continue          # redirect with no recorded views = 0
      if r.status_code!=200: raise PullFail(f'pageviews HTTP {r.status_code} for {ti}')
      for it in r.json()['items']: k=it['timestamp'][:8];tot[k]=tot.get(k,0)+it['views']
    rows+=[[x['ticker'],t,k,v,len(rd)] for k,v in sorted(tot.items())]
  import io;f=io.StringIO();w=csv.writer(f);w.writerow(['ticker','title','date_utc','views_incl_redirects','n_redirects']);w.writerows(rows)
  return {'wiki_pageviews.csv':f.getvalue().encode()}
source('wiki',['wiki_pageviews.csv'],pull_wiki)

# run log (always written; NOT_READY source-days are recorded here, never as data files)
with open(f'{B}/run_log_{NOW.strftime("%H%M%S")}.csv','w',newline='') as fh:
  w=csv.writer(fh);w.writerow(['source','file','status','http','bytes_or_note']);w.writerows(LOG)
for l in LOG: print(*l)
