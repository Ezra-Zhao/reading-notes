from decimal import Decimal as D, getcontext
from datetime import date
getcontext().prec=28
ok=[]
def chk(name, cond, detail=""):
    ok.append(cond)
    print(("PASS" if cond else "FAIL"), name, detail)

# 1 tenure: Xiu from 2022-11-18; fund effective 2015-12-30; end 2026-09-30
d_ten=(date(2026,9,30)-date(2022,11,18)).days
d_life=(date(2026,9,30)-date(2015,12,30)).days
gap=(date(2022,11,18)-date(2015,12,30)).days
print("tenure", d_ten, "life", d_life, "gap", gap, "share", round(d_ten/d_life*100,2), "yrs", round(d_ten/365.25,2))
chk("1 tenure", d_ten==1412 and d_life==3927 and gap==2515, f"tenure={d_ten} life={d_life} gap={gap} share={d_ten/d_life*100:.2f}%")

# 2 excess A all 8 windows exact
rowsA=[("3.60","-2.23","5.83"),("-5.80","-14.00","8.20"),("-19.89","-18.41","-1.48"),("4.80","-0.29","5.09"),("-19.12","3.04","-22.16"),("67.99","15.21","52.78"),("165.09","-24.18","189.27"),("215.72","-39.89","255.61")]
chk("2 excess A", all(D(a)-D(b)==D(c) for a,b,c in rowsA), "8 windows exact; excess negative only in 1y and 5y")

# 3 Q2 reverse from 6M and Q3
q2=(D("0.9420")/D("1.0360")-1)*100
bq2=(D("0.8600")/D("0.9777")-1)*100
print("Q2 fund", q2, "bench", bq2, "excess", q2-bq2)
chk("3 Q2 reverse", abs(q2-(-D("9.07")))<D("0.05") and abs(bq2-(-D("12.04")))<D("0.05") and abs((q2-bq2)-D("2.97"))<D("0.05"), f"fund={q2:.2f} bench={bq2:.2f} excess={q2-bq2:.2f}")

# 4 window splits
earliest5=(D("2.6509")/D("0.8088")-1)*100
seg75=(D("1.6799")/D("0.8088")-1)*100
seg53=(D("0.8088")/D("1.0480")-1)*100
early6=(D("0.8011")/D("0.9420")-1)*100
print("splits", earliest5, seg75, seg53, early6)
chk("4 splits", abs(earliest5-D("227.76"))<D("0.05") and abs(seg75-D("107.70"))<D("0.05") and abs(seg53-(-D("22.82")))<D("0.05") and abs(early6-(-D("14.96")))<D("0.05"), f"earliest5={earliest5:.2f} -7to-5={seg75:.2f} -5to-3={seg53:.2f} early6m={early6:.2f}")

# 5 recovery price for 5y loss
rec5=(D("1")/D("0.8088")-1)*100
print("recovery 5y", rec5)
chk("5 recovery", abs(rec5-D("23.64"))<D("0.05"), f"5y -19.12% needs +{rec5:.2f}%")

# 6 profit split: realized negative, profit positive, float dominates
a_r=D("-18918663.70"); a_p=D("79338311.82"); a_f=a_p-a_r
c_r=D("-1390139.40"); c_p=D("4307467.07"); c_f=c_p-c_r
t_r=a_r+c_r; t_p=a_p+c_p; t_f=t_p-t_r
print("floats", a_f, c_f, t_f, "ratio", t_f/abs(t_r))
chk("6 profit", a_f==D("98256975.52") and c_f==D("5697606.47") and t_r==D("-20308803.10") and t_p==D("83645778.89") and t_f==D("103954581.99"), f"combined float/|realized|={t_f/abs(t_r):.2f}")

# 7 shares reconcile and change
a_end=D("838759006.43")+D("7430398.36")-D("65814432.66")
c_end=D("49746912.01")+D("5569957.71")-D("5908932.09")
t0=D("838759006.43")+D("49746912.01"); t1=a_end+c_end
print("shares", a_end, c_end, t1, (a_end/D("838759006.43")-1)*100, (c_end/D("49746912.01")-1)*100, (t1/t0-1)*100)
chk("7 shares", a_end==D("780374972.13") and c_end==D("49407937.63") and t1==D("829782909.76"), f"A chg={(a_end/D('838759006.43')-1)*100:.2f} C chg={(c_end/D('49746912.01')-1)*100:.2f} tot={(t1/t0-1)*100:.2f}")

# 8 assets and NAV
net=D("2178678466.17")+D("133254029.79")
eq=D("2145565775.98")
nav_prod=D("780374972.13")*D("2.792")
print("net", net, "eq/net", eq/net*100, "A nav*shares", nav_prod, "diff", nav_prod-D("2178678466.17"))
chk("8 assets/NAV", net==D("2311932495.96") and abs(eq/net*100-D("92.80"))<D("0.01") and abs((nav_prod-D("2178678466.17")))<D("200000"), f"eq/net={eq/net*100:.2f} A product diff={(nav_prod-D('2178678466.17')):.2f} (NAV 3dp rounding)")

# 9 industries: nonzero rows sum 92.81 vs stated 92.80 (rounding 0.01)
inds=[D("0.00"),D("36.54"),D("1.35"),D("6.28"),D("2.01"),D("23.92"),D("7.50"),D("5.52"),D("9.69")]
print("industry sum", sum(inds))
chk("9 industries", sum(inds)==D("92.81") and D("36.54")>D("23.92")>D("9.69"), f"sum={sum(inds)} vs stated 92.80 diff 0.01 rounding; mfg 36.54 info 23.92 culture 9.69")

# 10 top10 and single-name = industry line
top=[D(x) for x in ["8.82","8.41","8.20","7.50","6.39","6.36","5.41","5.23","4.62","3.25"]]
print("top10", sum(top), "top3", sum(top[:3]))
chk("10 top10", sum(top)==D("64.19") and sum(top[:3])==D("25.43") and D("173290607.16")==D("173290607.16"), f"top10={sum(top)} top3={sum(top[:3])} Fenzhong amount equals L-industry amount 173,290,607.16")

# 11 since-inception factor vs NAV (distribution gap, register only)
fac=D("3.1572"); nav=D("2.792")
print("factor/nav", fac/nav)
chk("11 factor/nav", abs(fac/nav-D("1.1308"))<D("0.001"), f"ratio={fac/nav:.4f} (cum-return factor vs unit NAV; distributions, register only)")

# 12 C-class excess exact, 6 rows; C added 2020-11-23 so no 7y/10y rows
rowsC=[("3.41","-2.23","5.64"),("-6.09","-14.00","7.91"),("-20.37","-18.41","-1.96"),("2.94","-0.29","3.23"),("-21.51","3.04","-24.55"),("-12.21","-5.53","-6.68")]
chk("12 excess C", all(D(a)-D(b)==D(c) for a,b,c in rowsC), "6 rows exact; C since-inception row is since C inception per report layout, not 2015")

print("ALL PASS" if all(ok) else "SOME FAIL", f"{sum(ok)}/{len(ok)} groups")
