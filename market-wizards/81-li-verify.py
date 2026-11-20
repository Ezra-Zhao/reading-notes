from decimal import Decimal as D, getcontext
from datetime import date
getcontext().prec=28
ok=[]
def chk(name, cond, detail=""):
    ok.append(cond)
    print(("PASS" if cond else "FAIL"), name, detail)

# 1 tenure
d1=(date(2026,9,30)-date(2018,7,5)).days
chk("1 tenure Li", d1==3009, f"days={d1} years={d1/365.25:.2f}")
d2=(date(2026,9,30)-date(2019,9,20)).days
chk("1b tenure Zhang", d2==2567, f"days={d2} years={d2/365.25:.2f}")
# 2 since inception vs NAV
f=D("3.1350"); nav=D("2.8609")
chk("2 factor/nav", abs(f/nav-D("1.0958"))<D("0.001"), f"ratio={f/nav:.4f} diff%={(f/nav-1)*100:.2f}")
# 3 A excess all windows
rows=[("-13.86","-7.12","-6.74"),("6.79","-1.20","7.99"),("-8.45","-4.11","-4.34"),("18.99","23.92","-4.93"),("-14.83","1.96","-16.79"),("116.94","21.84","95.10"),("213.50","29.10","184.40")]
chk("3 A excess", all(D(a)-D(b)==D(c) for a,b,c in rows))
rowsC=[("-13.99","-7.12","-6.87"),("6.47","-1.20","7.67"),("-9.00","-4.11","-4.89"),("16.96","23.92","-6.96"),("-19.66","1.90","-21.56")]
chk("3b C excess", all(D(a)-D(b)==D(c) for a,b,c in rowsC))
# 4 Q2 reverse
q2=(D("1.0679")/D("0.8614")-1)*100
bq2=(D("0.9880")/D("0.9288")-1)*100
chk("4 Q2 reverse", abs(q2-D("23.97"))<D("0.02") and abs(bq2-D("6.37"))<D("0.02"), f"fund={q2:.2f} bench={bq2:.2f} excess={q2-bq2:.2f}")
# 5 window splits
earliest2_7y=(D("2.1694")/D("0.8517")-1)*100
first2_3y=(D("1.1899")/D("0.9155")-1)*100
chk("5 splits", abs(earliest2_7y-D("154.71"))<D("0.05") and abs(first2_3y-D("29.97"))<D("0.05"), f"7y-earliest2={earliest2_7y:.2f} 3y-first2={first2_3y:.2f}")
# 6 recovery
rec=(D("1")/D("0.8614")-1)*100
chk("6 recovery Q3", abs(rec-D("16.09"))<D("0.02"), f"{rec:.2f}")
# also 5y recovery
rec5=(D("1")/D("0.8517")-1)*100
print("  5y recovery", f"{rec5:.2f}")
# 7 profit split
a_real=D("70163513.64"); a_prof=D("-328495616.29"); a_float=a_prof-a_real
c_real=D("25022958.55"); c_prof=D("-130757206.19"); c_float=c_prof-c_real
tot_real=a_real+c_real; tot_prof=a_prof+c_prof; tot_float=tot_prof-tot_real
chk("7 profit", a_float==D("-398659129.93") and c_float==D("-155780164.74") and tot_real==D("95186472.19") and tot_prof==D("-459252822.48"), f"tot_float={tot_float} ratio={abs(tot_float/tot_real):.2f}")
# 8 shares
a_end=D("743430607.85")+D("10891084.07")-D("51109598.24")
c_end=D("293123619.83")+D("1277514.29")-D("5930064.25")
tot_start=D("743430607.85")+D("293123619.83"); tot_end=a_end+c_end
chk("8 shares", a_end==D("703212093.68") and c_end==D("288471069.87") and tot_end==D("991683163.55"), f"Achg={(a_end/D('743430607.85')-1)*100:.2f} Cchg={(c_end/D('293123619.83')-1)*100:.2f} totchg={(tot_end/tot_start-1)*100:.2f}")
# 9 assets
tot_assets=D("2581991724.79")+D("24201053.07")+D("221277179.54")+D("76359844.70")
net=D("2011848027.17")+D("802273528.29")
chk("9 assets", tot_assets==D("2903829802.10") and net==D("2814121555.46"), f"equity/net={(D('2581991724.79')/net)*100:.2f}")
# 10 industries
dom=D("275741532.96")+D("1141639951.84")+D("549873.82")+D("35927.49")+D("149483468.64")+D("8045.28")
hk=D("249337338.48")+D("85383181.38")+D("211303508.09")+D("468508896.81")
chk("10 industries", dom==D("1567458800.03") and hk==D("1014532924.76") and dom+hk==D("2581991724.79"), f"dom%={dom/net*100:.2f} hk%={hk/net*100:.2f}")
# 11 top10
top=[D(x) for x in ["9.97","8.81","8.07","7.84","5.44","5.31","5.05","5.00","3.93","3.23"]]
semi=D("9.97")+D("8.81")+D("7.84")
chk("11 top10", sum(top)==D("62.65") and semi==D("26.62"), f"top10/equity%={sum(top)/(D('2581991724.79')/net*100)*100:.2f}")
# 12 bonds + single holder
bonds=D("22192818.00")+D("2008235.07")
holder=D("217785950.94")/tot_end*100
chk("12 bonds/holder", bonds==D("24201053.07") and abs(holder-D("21.96"))<D("0.01"), f"holder%={holder:.2f}")
print("ALL PASS" if all(ok) else "SOME FAIL", f"{sum(ok)}/{len(ok)} groups")
