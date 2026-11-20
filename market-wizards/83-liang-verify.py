from decimal import Decimal as D, getcontext
from datetime import date
getcontext().prec=28
ok=[]
def chk(name, cond, detail=""):
    ok.append(cond)
    print(("PASS" if cond else "FAIL"), name, detail)

# 1 tenure: Liang from 2011-07-14; fund effective 2011-06-15; end 2026-09-30
d_ten=(date(2026,9,30)-date(2011,7,14)).days
d_life=(date(2026,9,30)-date(2011,6,15)).days
gap=(date(2011,7,14)-date(2011,6,15)).days
chk("1 tenure", d_ten==5557 and d_life==5586 and gap==29, f"tenure={d_ten}d {d_ten/365.25:.2f}y life={d_life}d share={d_ten/d_life*100:.2f}%")
# 2 since-inception factor vs NAV: A mismatch (register), C exact
fa=D("4.7198"); nava=D("4.008")
fc=D("1.1200"); navc=D("1.120")
chk("2 factor/nav", abs(fa/nava-D("1.1776"))<D("0.001") and fc==navc, f"A ratio={fa/nava:.4f} diff%={(fa/nava-1)*100:.2f} C exact={fc==navc}")
# 3 excess all windows A (7 rows) and C (3 rows)
rowsA=[("-14.32","-20.53","6.21"),("4.46","2.92","1.54"),("14.68","-2.78","17.46"),("44.38","34.94","9.44"),("8.82","1.57","7.25"),("77.98","53.92","24.06"),("371.98","104.24","267.74")]
rowsC=[("-14.44","-20.53","6.09"),("4.19","2.92","1.27"),("12.00","-2.76","14.76")]
chk("3 excess", all(D(a)-D(b)==D(c) for a,b,c in rowsA) and all(D(a)-D(b)==D(c) for a,b,c in rowsC))
# 4 Q2 reverse from 6M and Q3
q2=(D("1.0446")/D("0.8568")-1)*100
bq2=(D("1.0292")/D("0.7947")-1)*100
chk("4 Q2 reverse", abs(q2-D("21.92"))<D("0.02") and abs(bq2-D("29.51"))<D("0.02"), f"fund={q2:.2f} bench={bq2:.2f} excess={q2-bq2:.2f}")
# 5 window splits
seg_7y_first2=(D("1.7798")/D("1.0882")-1)*100
seg_5to3=(D("1.0882")/D("1.4438")-1)*100
seg_3y_first2=(D("1.4438")/D("1.1468")-1)*100
seg_pre7y=(D("4.7198")/D("1.7798")-1)*100
chk("5 splits", abs(seg_7y_first2-D("63.56"))<D("0.05") and abs(seg_5to3-D("-24.62"))<D("0.05") and abs(seg_3y_first2-D("25.90"))<D("0.05") and abs(seg_pre7y-D("165.21"))<D("0.05"), f"7y-first2={seg_7y_first2:.2f} 5to3={seg_5to3:.2f} 3y-first2={seg_3y_first2:.2f} pre7y={seg_pre7y:.2f}")
# 6 recovery prices
rec_q3=(D("1")/D("0.8568")-1)*100
rec_seg=(D("1")/D("0.7538")-1)*100
chk("6 recovery", abs(rec_q3-D("16.72"))<D("0.02"), f"Q3 rec={rec_q3:.2f} seg5to3 rec approx={rec_seg:.2f}")
# 7 profit split A, C, total
a_real=D("168023616.68"); a_prof=D("-426925225.67"); a_float=a_prof-a_real
c_real=D("2066883.69"); c_prof=D("-4746179.18"); c_float=c_prof-c_real
t_real=a_real+c_real; t_prof=a_prof+c_prof; t_float=t_prof-t_real
chk("7 profit", a_float==D("-594948842.35") and c_float==D("-6813062.87") and t_real==D("170090500.37") and t_prof==D("-431671404.85") and t_float==D("-601761905.22"), f"A ratio={abs(a_float/a_real):.2f} tot ratio={abs(t_float/t_real):.2f}")
# 8 shares A, C, total
a_end=D("645393838.13")+D("23966759.07")-D("41663919.59")
c_end=D("18931687.46")+D("115440310.18")-D("2112402.71")
t_start=D("645393838.13")+D("18931687.46"); t_end=a_end+c_end
chk("8 shares", a_end==D("627696677.61") and c_end==D("132259594.93") and t_end==D("759956272.54"), f"A chg={(a_end/D('645393838.13')-1)*100:.2f} C chg={(c_end/D('18931687.46')-1)*100:.2f} tot chg={(t_end/t_start-1)*100:.2f}")
# 9 assets and net assets
tot_assets=D("2312001662.30")+D("358261529.88")+D("1355433.88")
net=D("2515714303.57")+D("148088189.60")
eq_pct=D("2312001662.30")/net*100
chk("9 assets", tot_assets==D("2671618626.06") and net==D("2663802493.17") and abs(eq_pct-D("86.79"))<D("0.01"), f"equity/net={eq_pct:.2f} cash/assets={D('358261529.88')/tot_assets*100:.2f}")
# 10 industries sum and concentration
ind=[D("157836383.96"),D("1656844143.11"),D("549873.82"),D("1782.96"),D("407087526.93"),D("89681951.52")]
manu_it=(D("1656844143.11")+D("407087526.93"))/net*100
chk("10 industries", sum(ind)==D("2312001662.30") and abs(manu_it-D("77.48"))<D("0.01"), f"manu+IT/net={manu_it:.2f} manu/equity={D('1656844143.11')/D('2312001662.30')*100:.2f}")
# 11 top10
top=[D(x) for x in ["6.88","6.06","5.56","5.12","5.12","4.66","4.23","4.21","3.81","3.57"]]
top_val=sum(D(x) for x in ["183399965.10","161425283.10","148130182.08","136463055.12","136423714.85","124230258.00","112764598.16","112033407.33","101432262.29","95162802.00"])
chk("11 top10", sum(top)==D("49.22"), f"top3={sum(top[:3]):.2f} top10/equity={sum(top)/eq_pct*100:.2f} top10 value={top_val}")
# 12 single holder and combined products
holder_end=D("141532539.01")/t_end*100
holder_start=D("141532539.01")/t_start*100
comb=D("8942643011.77")+D("1962353584.21")
chk("12 holder/products", abs(holder_end-D("18.62"))<D("0.01") and abs(holder_start-D("21.30"))<D("0.01") and comb==D("10904996595.98"), f"holder start={holder_start:.2f} end={holder_end:.2f} combined={comb}")
print("ALL PASS" if all(ok) else "SOME FAIL", f"{sum(ok)}/{len(ok)} groups")
