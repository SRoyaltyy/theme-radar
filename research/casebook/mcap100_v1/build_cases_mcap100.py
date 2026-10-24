# Theme Radar casebook MCAP100 V1 (copy of frozen build_cases.py + checklist-engine theme_radar_wire50_2020_24/MCAP100_ADDENDUM_V1.md filter): F4TR pass-bar cells, 2020-24 ONLY. Never reads 2025/2026 chunks.
import pandas as pd, numpy as np, json, glob, ast, hashlib, gzip, io
C='/workspace/checklist_brainstorm/engine/universe/chunks/'
TAGS='/workspace/checklist_brainstorm/mine/state_test/f4tr/theme-radar_f4tr_tags.csv'
sha=hashlib.sha256(open(TAGS,'rb').read()).hexdigest(); assert sha.startswith('201f39f3'),sha
W=['OWN-TR-00001-C','OWN-TR-00003-C','OWN-TR-00005-C','OWN-TR-00037-C','OWN-TR-00039-C','OWN-TR-00041-C','OWN-TR-00043-C','OWN-TR-00045-C','OWN-TR-00051-C','OWN-TR-00053-C']
def unpack(b,k): return np.stack([(b>>s)&3 for s in (0,2,4,6)],-1).reshape(b.shape[0],-1)[:,:k]
P=[]
for y in range(2020,2025):
    for f in sorted(glob.glob(C+f'{y}__F4TR__*.parquet')):
        assert f.split('/')[-1][:4] in ('2020','2021','2022','2023','2024')
        j=json.load(open(f[:-8]+'.json')); fid=j['ids'] if isinstance(j['ids'],list) else ast.literal_eval(j['ids'])
        ix=[fid.index(w) for w in W]; D=pd.read_parquet(f); D['date']=D.date.astype(str).str[:10]; assert D.date.max()<'2025-01-01'
        cc=unpack(np.stack([np.frombuffer(x,np.uint8) for x in D.packed]),len(fid))[:,ix]
        X=pd.DataFrame(cc.astype('int8'),columns=W); X['ticker']=D.ticker.astype(str).values; X['date']=D.date.values; X['sector']=j['sector']
        P.append(X[(cc==2).any(1)])
A=pd.concat(P,ignore_index=True); print('yes stock-days',len(A))
# prices
px=pd.read_parquet('/workspace/pricehist/universe_2020_survivors.parquet',columns=['ticker','date','open','high','low','close','volume'],
   filters=[('date','>=',pd.Timestamp('2019-06-01')),('date','<=',pd.Timestamp('2024-12-31'))])
px['ticker']=px.ticker.astype(str); px=px.sort_values(['ticker','date']).reset_index(drop=True); px['d']=px.date.dt.strftime('%Y-%m-%d')
assert px.date.max()<=pd.Timestamp('2024-12-31')
drop=pd.read_csv('work/drop_list_v2.csv.gz'); drop['k']=drop.ticker.astype(str)+'|'+drop.date.astype(str)
dropset=set(drop.k)
etf_extra=set()  # v2 list already has its 14 ETFs; also drop funds per Finviz industry as in f4tr_score
snap=pd.read_csv('/workspace/snap_2026-09-29.csv',usecols=['Ticker','Industry'])
funds=set(snap.Ticker[snap.Industry.fillna('').str.match(r'^(Exchange Traded Fund|Closed-End Fund|Shell Companies)')])
# per-row outcomes for every stock-day (for controls)
o=px.open.values.astype(float); h=px.high.values; l=px.low.values; c=px.close.values.astype(float); tk=px.ticker.values
n=len(px); same=np.r_[tk[1:]==tk[:-1],False]
# index of next k-th row within same ticker
grp=px.groupby('ticker',sort=False).cumcount().values; size=px.groupby('ticker',sort=False).ticker.transform('size').values
rem=size-grp-1  # rows after
FEE=0.003
e=np.arange(n)+1  # entry = open of D+1
v1=np.full(n,np.nan); h10=np.full(n,np.nan); v1day=np.full(n,np.nan); v1hit=np.zeros(n,bool)
ok15=rem>=15; ok10=rem>=10
ent=np.where(rem>=1,o[np.minimum(e,n-1)],np.nan)
hitday=np.full(n,99)
for k in range(15):
    idx=np.minimum(e+k,n-1); tgt=ent*1.2
    newhit=(hitday==99)&(h[idx]>=tgt)&ok15
    hitday[newhit]=k+1
    px_exit=np.maximum(o[idx],tgt)
    v1=np.where(newhit,px_exit,v1)
idx15=np.minimum(e+14,n-1)
v1=np.where(ok15&np.isnan(v1),c[idx15],v1); v1=np.where(ok15,v1,np.nan)
v1net=(v1*(1-FEE))/(ent*(1+FEE))-1
idx10=np.minimum(e+9,n-1); h10net=np.where(ok10,(c[idx10]*(1-FEE))/(ent*(1+FEE))-1,np.nan)
px['v1']=v1net; px['h10']=h10net; px['v1_day']=np.where(ok15,np.where(hitday<99,hitday,15),np.nan); px['v1_tp']=hitday<99
px['k']=px.ticker+'|'+px.d
px['buy']=~px.k.isin(dropset)&~px.ticker.isin(funds)&(px.date>=pd.Timestamp('2020-01-01'))
import sys,os; VAR=sys.argv[1]; OUT=f'work_mcap100/{VAR}/'; os.makedirs(OUT,exist_ok=True)
Sh=pd.read_parquet('/workspace/mcap/nb_tags_v2/sec_shares_out_filed_le_2024.parquet'); Sh['ticker']=Sh.ticker.astype(str); Sh['filed']=pd.to_datetime(Sh.filed).astype('datetime64[ns]')
med=Sh.groupby('ticker').val.transform('median'); bad=(Sh.val<=0)|(Sh.val>1e11)|(Sh.val>50*med)|(Sh.val<med/50); nbad=int(bad.sum())
Sh=Sh[~bad].sort_values(['ticker','filed','end']).drop_duplicates(['ticker','filed'],keep='last'); Sh['date']=Sh.filed+pd.Timedelta(days=1)
# row = signal day D; entry E = next bar; shares filed < E; mcap = close(D) x shares
nxt=np.r_[px.date.values[1:],np.datetime64('NaT')]; nxt=np.where(same,nxt,np.datetime64('NaT')).astype('datetime64[ns]')
Q=pd.DataFrame({'ticker':px.ticker.values,'date':nxt,'o':np.arange(n)}); qv=Q.date.notna()
Q2=pd.merge_asof(Q[qv].sort_values('date'),Sh[['ticker','date','val']].sort_values('date'),on='date',by='ticker',direction='backward')
val=np.full(n,np.nan); val[Q2.o.values]=Q2.val.values
MC=val*c; MC[MC>5e12]=np.nan; NOC=~np.isfinite(MC); SMALL=np.isfinite(MC)&(MC<1e8)
REM=np.zeros(n,bool) if VAR=='NONE' else (SMALL if VAR=='MAIN' else SMALL|NOC)
px['mcap']=MC; px['mcap_status']=np.where(NOC,'NOCOUNT',np.where(SMALL,'LT100M','GE100M'))
px['buy']=px.buy&~REM
# context (bars before D only, i.e. through D-1 close)
g=px.groupby('ticker',sort=False)
pc=g.close.shift(1); green=(px.close>px.open).astype(float); red=(px.close<px.open).astype(float)
for w in (10,20,60):
    gs=green.groupby(px.ticker,sort=False).transform(lambda s:s.shift(1).rolling(w,min_periods=w).sum())
    rs=red.groupby(px.ticker,sort=False).transform(lambda s:s.shift(1).rolling(w,min_periods=w).sum())
    px[f'gr{w}']=gs/rs.replace(0,np.nan); px[f'g{w}']=gs; px[f'r{w}']=rs
for w in (21,42,63):
    px[f'ret{w}']=g.close.shift(1)/g.close.shift(1+w)-1
px['sma50']=g.close.transform(lambda s:s.shift(1).rolling(50,min_periods=40).mean())
px['above50']=pc>px.sma50
px['dd_from_63hi']=pc/g.high.transform(lambda s:s.shift(1).rolling(63,min_periods=40).max())-1
px['avgvol20']=g.volume.transform(lambda s:s.shift(1).rolling(20,min_periods=20).mean())
ctrl=px[px.buy&(px.date<=pd.Timestamp('2024-12-31'))].groupby('d')[['v1','h10']].mean().rename(columns={'v1':'ctl_v1','h10':'ctl_h10'})
ctrl_win=px[px.buy].groupby('d')[['v1','h10']].agg(lambda s:(s>0).mean()).rename(columns={'v1':'ctlwin_v1','h10':'ctlwin_h10'})
# collapse runs: any-row YES consecutive trading days per ticker -> first day
A=A.merge(px[['ticker','d']].rename(columns={'d':'date'}).reset_index().rename(columns={'index':'pi'}),on=['ticker','date'],how='left')
nomatch=A.pi.isna().sum(); A=A.dropna(subset=['pi']); A['pi']=A.pi.astype(int); n_pre=len(A); A=A[~REM[A.pi.values]]; A=A.sort_values(['ticker','pi'])
A['new']=(A.ticker!=A.ticker.shift())|(A.pi!=A.pi.shift()+1); A['run']=A.new.cumsum()
runlen=A.groupby('run').size()
F=A[A.new].copy(); F['run_days']=F.run.map(runlen)
F=F.merge(px.drop(columns=['ticker','date','k']).reset_index().rename(columns={'index':'pi'}),on='pi',how='left')
F=F.join(ctrl,on='date').join(ctrl_win,on='date')
F['split']=np.where(F.date<'2023-01-01','discovery_2020_22','confirm_2023_24')
pre=len(F); F['buyable']=F.buy
stats=dict(variant=VAR,filing_rows_removed=nbad,yes_stockdays_removed_by_mcap=int(n_pre-len(A)),tags_sha=sha,yes_stockdays=int(len(A)),no_price_match=int(nomatch),runs=int(pre),buyable_runs=int(F.buyable.sum()))
F=F[F.buyable].copy()
F['cells_yes']=F[W].apply(lambda r:';'.join(w for w in W if r[w]==2),axis=1)
F['v1_excess']=F.v1-F.ctl_v1; F['h10_excess']=F.h10-F.ctl_h10
F['v1_result']=np.where(F.v1.isna(),'n/a (exit after 2024-12-31)',np.where(F.v1>0,'WIN','LOSE'))
F['h10_result']=np.where(F.h10.isna(),'n/a (exit after 2024-12-31)',np.where(F.h10>0,'WIN','LOSE'))
F.to_csv(OUT+'cases.csv.gz',index=False); json.dump(stats,open(OUT+'stats.json','w'),indent=1); print(stats)
# summary
rows=[]
for sp,d in [('ALL',F)]+list(F.groupby('split')):
  for ex in ('v1','h10'):
    dd=d.dropna(subset=[ex]); rows.append(dict(split=sp,exit=ex,n=len(dd),win=(dd[ex]>0).mean(),mean=dd[ex].mean(),median=dd[ex].median(),
      ctl_mean=dd[f'ctl_{ex}'].mean(),ctl_win=dd[f'ctlwin_{ex}'].mean(),excess=dd[f'{ex}_excess'].mean(),tickers=dd.ticker.nunique()))
S=pd.DataFrame(rows); S.insert(0,'variant',VAR); S.to_csv(OUT+'summary.csv',index=False); print(S.round(4).to_string())
pd.DataFrame([dict(split=sp,cell=w,n=int((d[w]==2).sum()),win_v1=(d[d[w]==2].v1.dropna()>0).mean(),win_h10=(d[d[w]==2].h10.dropna()>0).mean(),mean_v1=d[d[w]==2].v1.mean(),mean_h10=d[d[w]==2].h10.mean()) for sp,d in F.groupby('split') for w in W]).to_csv(OUT+'by_cell.csv',index=False)
