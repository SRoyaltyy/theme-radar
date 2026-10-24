import textwrap, pandas as pd, numpy as np, json, matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt; from matplotlib.backends.backend_pdf import PdfPages
F=pd.read_parquet('work/cases.parquet'); S=pd.read_csv('work/summary.csv'); B=pd.read_csv('work/by_cell.csv'); st=json.load(open('work/stats.json'))
W=['OWN-TR-00001-C','OWN-TR-00003-C','OWN-TR-00005-C','OWN-TR-00037-C','OWN-TR-00039-C','OWN-TR-00041-C','OWN-TR-00043-C','OWN-TR-00045-C','OWN-TR-00051-C','OWN-TR-00053-C']
Q={'OWN-TR-00001-C':'net insider buy $ >0 (fixed thr, N=1)','OWN-TR-00003-C':'fixed thr N=3','OWN-TR-00005-C':'fixed thr N=5',
'OWN-TR-00037-C':'net buy $ crosses up (N=1)','OWN-TR-00039-C':'cross N=3','OWN-TR-00041-C':'cross N=5','OWN-TR-00043-C':'cross N=10','OWN-TR-00045-C':'cross N=20',
'OWN-TR-00051-C':'net buy streak N=3','OWN-TR-00053-C':'net buy streak N=5'}
F=F.sort_values(['split','date','ticker'],ascending=[False,True,True]).reset_index(drop=True)
F['case_id']=['C%04d'%(i+1) for i in range(len(F))]
ans=lambda v:{0:'NR',1:'NO',2:'YES'}[int(v)]
for w in W: F[w+'_ans']=F[w].map(ans)
cols=['case_id','split','ticker','sector','date','run_days','cells_yes']+[w+'_ans' for w in W]+['v1','v1_result','v1_day','v1_tp','h10','h10_result','ctl_v1','ctl_h10','v1_excess','h10_excess',
 'ret21','ret42','ret63','above50','dd_from_63hi','g10','r10','gr10','g20','r20','gr20','g60','r60','gr60','avgvol20']
F[cols].rename(columns={'date':'setup_date','v1':'exit_rule_v1_net','h10':'hold10_net'}).to_csv('theme_radar_casebook_2020_24.csv',index=False,float_format='%.5f')
px=pd.read_parquet('/workspace/pricehist/universe_2020_survivors.parquet',columns=['ticker','date','open','high','low','close'],
   filters=[('date','>=',pd.Timestamp('2019-06-01')),('date','<=',pd.Timestamp('2024-12-31'))])
px['ticker']=px.ticker.astype(str); px=px[px.ticker.isin(set(F.ticker))].sort_values(['ticker','date'])
G={t:d.reset_index(drop=True) for t,d in px.groupby('ticker')}
def pct(x): return 'n/a' if pd.isna(x) else f'{x*100:+.1f}%'
with PdfPages('theme_radar_casebook_2020_24.pdf') as pdf:
    fig=plt.figure(figsize=(8.5,11)); fig.text(.06,.95,'Theme Radar casebook — F4TR insider net-buy cells, 2020–24 practice data (HINT)',fontsize=12,weight='bold')
    txt=[f"Built 2026-10-23 HKT. 2025–26 sealed and NOT read (only 2020–24 chunks/prices opened; price file filtered <=2024-12-31).",
    f"Tags sha {st['tags_sha'][:16]}…  Cells = 10 pass-bar row ids from 2020_24_f4tr_score.md.",
    f"YES stock-days {st['yes_stockdays']} -> runs (consecutive YES days per ticker = 1 case) {st['runs']} -> buyable {st['buyable_runs']}.",
    "Never-buy filter (applied to cases AND controls): drop_list_v2 (ee93a2a/50e3243): 20d avg vol>=500k, prior-day vol>0,",
    "  SPAC suffix/flat-$10 rule, partial ETF list (14); plus Finviz fund/shell industries. Min-mcap rule NOT applied.",
    "Entry = open D+1 (Form 4 counted from next open). 30bp each way.",
    "EXIT_RULE_V1: +20% take-profit (fill max(open,target)), no stop, else sell close of day 15. 10d hold: close of day 10.",
    "Control = mean of all buyable stock-days same setup date, same exit. Win = net>0.",
    "Context (bars through D-1): prior 21/42/63d return, above 50d SMA, drawdown from 63d high, green:red day counts 10/20/60d.",
    "Survivor-only prices: winners may be flattered. Finviz 43 pilot fires: NOT included (see gaps).","", "Results by split:"]
    for r in S.itertuples(): txt.append(f"  {r.split:18s} {r.exit:4s} n={r.n:5d} win {r.win*100:5.1f}% mean {r.mean*100:+.2f}%  control win {r.ctl_win*100:.1f}% mean {r.ctl_mean*100:+.2f}%  excess {r.excess*100:+.2f}%")
    txt+=['','By cell (win v1 / win h10 / n):']
    for r in B.itertuples(): txt.append(f"  {r.split[:9]} {r.cell} {Q[r.cell]:34s} n={r.n:4d} v1 {r.win_v1*100:4.1f}% h10 {r.win_h10*100:4.1f}%")
    for i,t in enumerate(txt): fig.text(.05,.92-i*.0175,t,fontsize=6.6,family='monospace')
    pdf.savefig(fig); plt.close(fig)
    for p0 in range(0,len(F),6):
        fig,axs=plt.subplots(3,2,figsize=(8.5,11)); 
        for ax,(_,r) in zip(axs.flat,F.iloc[p0:p0+6].iterrows()):
            d=G[r.ticker]; i=int(np.searchsorted(d.date.values,np.datetime64(r.date))); a=max(0,i-63); b=min(len(d),i+16)
            s=d.iloc[a:b]; ax.plot(s.date,s.close,lw=.8,color='k'); ax.axvline(d.date.iloc[i],color='b',lw=.6)
            if i+1<len(d):
                ent=d.open.iloc[i+1]; ax.axhline(ent*1.2,color='g',ls=':',lw=.6); ax.axhline(ent,color='gray',ls=':',lw=.6)
                if not pd.isna(r.v1_day): ax.axvline(d.date.iloc[min(len(d)-1,i+int(r.v1_day))],color='r',lw=.6)
            ax.set_title(f"{r.case_id} {r.ticker} {r.date} [{r.split[:9]}] run {r.run_days}d",fontsize=7); ax.tick_params(labelsize=5)
            ax.text(0,-.32,textwrap.fill("Q: "+', '.join(Q[w] for w in r.cells_yes.split(';')),95)+f"\nEXIT_V1 {pct(r.v1)} {r.v1_result} (day {'' if pd.isna(r.v1_day) else int(r.v1_day)}{' TP' if r.v1_tp else ''}) ctl {pct(r.ctl_v1)} | 10d {pct(r.h10)} {r.h10_result}\nHow we got here: 21d {pct(r.ret21)} 63d {pct(r.ret63)} {'above' if r.above50 else 'below'} 50dMA, {pct(r.dd_from_63hi)} off 63d hi\ngreen:red 10d {r.g10:.0f}:{r.r10:.0f} 20d {r.g20:.0f}:{r.r20:.0f} 60d {r.g60:.0f}:{r.r60:.0f}" if not pd.isna(r.g60) else f"Q: {', '.join(Q[w] for w in r.cells_yes.split(';'))}\nEXIT_V1 {pct(r.v1)} {r.v1_result} ctl {pct(r.ctl_v1)} | 10d {pct(r.h10)} {r.h10_result}\nHow we got here: 21d {pct(r.ret21)}; price file starts 2020-01-02 so 60/63d windows n/a\ngreen:red 10d {r.g10}:{r.r10} 20d {r.g20}:{r.r20}",transform=ax.transAxes,fontsize=5,va='top',family='monospace')
        for ax in axs.flat[len(F.iloc[p0:p0+6]):]: ax.axis('off')
        fig.subplots_adjust(hspace=.75,top=.96,bottom=.08); pdf.savefig(fig); plt.close(fig)
print('ok',len(F))
