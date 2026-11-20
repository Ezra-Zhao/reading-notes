from decimal import Decimal as D, getcontext
from datetime import date
getcontext().prec=28
ok=[]
def chk(name, cond, detail=""):
    ok.append(cond)
    print(("PASS" if cond else "FAIL"), name, detail)

# 1 tenure: Wu from 2011-12-28; fund effective 2008-10-10; end 2026-09-30
d_ten=(date(2026,9,30)-date(2011,12,28)).days
d_life=(date(2026,9,30)-date(2008,10,10)).days
gap=(date(2011,12,28)-date(2008,10,10)).days
print("tenure days", d_ten, "life", d_life, "gap", gap, "share", round(d_ten/d_life*100,2), "tenure yrs", round(d_ten/365.25,2), "gap yrs", round(gap/365.25,2))
chk("1 tenure", d_ten>5000, f"tenure={d_ten} life={d_life} gap={gap}")

# 2 since-inception factor vs NAV
fa=D("6.7336"); nava=D("1.2006")
fc=D("1.4579"); navc=D("1.3812")
print("A factor/nav", fa/nava, "C nav/factor", navc/fc)
chk("2 factor/nav", fa/nava>D("5.6") and navc<fc, f"A ratio={fa/nava:.4f} C ratio={navc/fc:.4f} C short={(1-navc/fc)*100:.2f}%")

# 3 excess all windows
rowsA=[("5.93","-9.67","15.60"),("-0.53","-1.35","0.82"),("7.52","-3.98","11.50"),("36.34","17.40","18.94"),("41.23","-2.17","43.40"),("100.94","20.76","80.18"),("172.44","40.76","131.68"),("573.36","133.92","439.44")]
rowsC=[("5.77","-9.67","15.44"),("-0.84","-1.35","0.51"),("6.89","-3.98","10.87"),("45.79","23.93","21.86")]
chk("3 excess", all(D(a)-D(b)==D(c) for a,b,c in rowsA) and all(D(a)-D(b)==D(c) for a,b,c in rowsC), "A 8 windows + C 4 windows all excess positive and exact")

# 4 Q2 reverse from 6M and Q3
q2=(D("0.9947")/D("1.0593")-1)*100
bq2=(D("0.9865")/D("0.9033")-1)*100
print("Q2 fund", q2, "Q2 bench", bq2, "Q2 excess", q2-bq2)
chk("4 Q2 reverse", abs(q2-(-D("6.10")))<D("0.05") and abs(bq2-D("9.21"))<D("0.05"), f"fund={q2:.2f} bench={bq2:.2f} excess={q2-bq2:.2f}")

# 5 window splits
s_10_first5=(D("2.7244")/D("1.4123")-1)*100
s_7to5=(D("2.0094")/D("1.4123")-1)*100
s_5to3=(D("1.4123")/D("1.3634")-1)*100
s_3to1=(D("1.3634")/D("1.0752")-1)*100
s_pre10=(D("6.7336")/D("2.7244")-1)*100
print("splits", s_10_first5, s_7to5, s_5to3, s_3to1, s_pre10)
chk("5 splits", s_10_first5>D("92") and s_5to3<D("4") and s_pre10>D("147"), f"10y-first5={s_10_first5:.2f} 7to5={s_7to5:.2f} 5to3={s_5to3:.2f} 3to1={s_3to1:.2f} pre10={s_pre10:.2f}")

# 6 recovery prices
rec_q2=(D("1")/ (D("1")+q2/100) -1)*100
print("Q2 recovery needed", rec_q2, "Q3 actual 5.93, half-year factor", D("0.9947"))
chk("6 recovery", abs(rec_q2-D("6.50"))<D("0.05"), f"Q2 loss recovery={rec_q2:.2f} vs Q3 gain 5.93")

# 7 profit split
a_real=D("20954226.82"); a_prof=D("55094724.11"); a_float=a_prof-a_real
c_real=D("1352453.21"); c_prof=D("2720069.79"); c_float=c_prof-c_real
t_real=a_real+c_real; t_prof=a_prof+c_prof; t_float=t_prof-t_real
print("floats", a_float, c_float, t_float, "ratios", a_float/a_real, t_float/t_real)
chk("7 profit", a_float==D("34140497.29") and c_float==D("1367616.58") and t_real==D("22306680.03") and t_prof==D("57814793.90") and t_float==D("35508113.87"), f"A ratio={a_float/a_real:.2f} tot ratio={t_float/t_real:.2f}")

# 8 shares
a_end=D("773065988.03")+D("142315733.79")-D("54975813.11")
c_end=D("50151254.98")+D("42057366.11")-D("33236601.45")
t_start=D("773065988.03")+D("50151254.98"); t_end=a_end+c_end
print("shares", a_end, c_end, t_end, "chg A", (a_end/D("773065988.03")-1)*100, "C", (c_end/D("50151254.98")-1)*100, "tot", (t_end/t_start-1)*100)
chk("8 shares", a_end==D("860405908.71") and c_end==D("58972019.64") and t_end==D("919377928.35"), f"A chg={(a_end/D('773065988.03')-1)*100:.2f} C chg={(c_end/D('50151254.98')-1)*100:.2f} tot chg={(t_end/t_start-1)*100:.2f}")

# 9 assets
tot_assets=D("1005163108.97")+D("112532099.83")+D("599927.92")
net=D("1033022076.34")+D("81454839.08")
eq_pct=D("1005163108.97")/net*100
print("assets", tot_assets, net, eq_pct, D("112532099.83")/tot_assets*100)
chk("9 assets", tot_assets==D("1118295136.72") and net==D("1114476915.42") and abs(eq_pct-D("90.19"))<D("0.01"), f"equity/net={eq_pct:.2f} cash/assets={D('112532099.83')/tot_assets*100:.2f}")

# 10 industries
ind=[D("109794038.96"),D("495929084.91"),D("31976658.00"),D("9805548.00"),D("31182448.24"),D("326475330.86")]
fin_pct=D("326475330.86")/net*100
manu_pct=D("495929084.91")/net*100
print("industries sum", sum(ind), "fin", fin_pct, "manu", manu_pct, "fin+manu", fin_pct+manu_pct)
chk("10 industries", sum(ind)==D("1005163108.97") and abs(fin_pct-D("29.29"))<D("0.01") and abs(manu_pct-D("44.50"))<D("0.01"), f"fin+manu/net={fin_pct+manu_pct:.2f}")

# 11 top10
top=[D(x) for x in ["8.35","7.62","6.28","5.04","4.86","4.22","3.70","3.63","3.62","3.43"]]
fin_top=D("8.35")+D("7.62")+D("5.04")+D("3.70")
print("top10", sum(top), "top3", sum(top[:3]), "fin top", fin_top, "top10/equity", sum(top)/eq_pct*100)
chk("11 top10", sum(top)==D("50.75") and fin_top==D("24.71"), f"top3={sum(top[:3]):.2f} fin-names={fin_top:.2f} top10/equity={sum(top)/eq_pct*100:.2f}")

# 12 combined products and manager holding
comb=D("3680061526.11")+D("9384150296.38")
hold_a=D("8717523.98")/D("860405908.71")*100
hold_t=D("8717523.98")/t_end*100
priv_share=D("9384150296.38")/comb*100
print("combined", comb, "hold/A", hold_a, "hold/total", hold_t, "private share", priv_share)
chk("12 products/holding", comb==D("13064211822.49") and abs(hold_a-D("1.01"))<D("0.01"), f"hold/A={hold_a:.2f} hold/total={hold_t:.2f} private share={priv_share:.2f}")

print("ALL PASS" if all(ok) else "SOME FAIL", f"{sum(ok)}/{len(ok)} groups")
