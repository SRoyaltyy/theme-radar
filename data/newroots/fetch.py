"""Nightly write-once save of new root sources. Never overwrites an existing day file."""
import requests,os,sys,json,csv,html,datetime as D,urllib.parse as u,time
DAY=D.datetime.now(D.UTC).strftime('%Y-%m-%d');B=f'data/newroots/{DAY}';os.makedirs(B,exist_ok=True)
UA={'User-Agent':'theme-radar-newroots/1.0 (github.com/SRoyaltyy/theme-radar)'};LOG=[]
def save(name,url,hdr=UA,ok=lambda r:True):
  p=f'{B}/{name}'
  if os.path.exists(p): LOG.append([name,'SKIP_EXISTS','','']);return None
  try: r=requests.get(url,headers=hdr,timeout=60)
  except Exception as e: LOG.append([name,'ERR',repr(e)[:80],'']);return None
  st='OK' if r.status_code==200 and ok(r) else ('NOT_READY' if r.status_code in(401,403,404,406) or 'Access Denied' in r.text[:500] else 'FAIL')
  if st=='OK': open(p,'wb').write(r.content)
  LOG.append([name,st,r.status_code,len(r.content)]);return r if st=='OK' else None
BR={'User-Agent':'Mozilla/5.0'}
for t in 'SPY XLK XLF XLE XLV XLI XLY XLP XLU XLB XLRE XLC'.split():
  save(f'ssga_{t}.xlsx',f'https://www.ssga.com/us/en/intermediary/etfs/library-content/products/fund-data/etfs/us/navhist-us-en-{t.lower()}.xlsx',BR,lambda r:r.content[:2]==b'PK')
for s in ['VIX','VIX9D','VIX3M','VIX6M']:
  save(f'cboe_{s}_History.csv',f'https://cdn.cboe.com/api/global/us_indices/daily_prices/{s}_History.csv',UA,lambda r:r.text[:4]=='DATE')
d=(D.datetime.now(D.UTC)-D.timedelta(days=1)).strftime('%Y-%m-%d')
save(f'cboe_putcall_{d}.json',f'https://cdn.cboe.com/data/us/options/market_statistics/daily/{d}_daily_options',UA,lambda r:'ratios' in r.text)
NQ={**BR,'Accept':'application/json'}
for t in ['QQQ','IWM']:
  r=save(f'nasdaq_{t}.json',f'https://api.nasdaq.com/api/quote/{t}/summary?assetclass=etf',NQ,lambda r:'"data":{' in r.text)
  if r is not None: print('NASDAQ',t,'shares-outstanding field present:','sharesoutstanding' in r.text.lower().replace(' ',''))
# Wikimedia: last 7 days per article, summing redirect (old) titles
p=f'{B}/wiki_pageviews.csv'
if not os.path.exists(p):
  m=list(csv.DictReader(open('data/newroots/ticker_wiki_map.csv')));e=(D.datetime.now(D.UTC)-D.timedelta(days=1)).strftime('%Y%m%d');s=(D.datetime.now(D.UTC)-D.timedelta(days=8)).strftime('%Y%m%d');rows=[];bad=0
  for x in m:
    t=html.unescape(x['resolved_title']);tot={}
    rd=requests.get('https://en.wikipedia.org/w/api.php',params={'action':'query','list':'backlinks','bltitle':t,'blfilterredir':'redirects','bllimit':50,'blnamespace':0,'format':'json'},headers=UA,timeout=30).json().get('query',{}).get('backlinks',[])
    for ti in [t]+[b['title'] for b in rd]:
      r=requests.get('https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/user/'+u.quote(ti.replace(' ','_'),safe='')+f'/daily/{s}/{e}',headers=UA,timeout=30)
      if r.status_code==200:
        for it in r.json()['items']: tot[it['timestamp'][:8]]=tot.get(it['timestamp'][:8],0)+it['views']
      elif ti==t: bad+=1
    rows+=[[x['ticker'],t,k,v,len(rd)] for k,v in sorted(tot.items())]
  w=csv.writer(open(p,'w'));w.writerow(['ticker','title','date_utc','views_incl_redirects','n_redirects']);w.writerows(rows)
  LOG.append(['wiki_pageviews.csv','OK',f'fail_titles={bad}',len(rows)])
w=csv.writer(open(f'{B}/run_log_{D.datetime.now(D.UTC).strftime("%H%M%S")}.csv','w'));w.writerow(['file','status','http','bytes']);w.writerows(LOG)
for l in LOG: print(*l)
