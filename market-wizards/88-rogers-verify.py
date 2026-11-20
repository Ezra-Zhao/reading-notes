from decimal import Decimal as D, getcontext
from datetime import date
getcontext().prec=28
ok=[]
def chk(name, cond, detail=""):
    ok.append(cond)
    print(("PASS" if cond else "FAIL"), name, detail)

# 1 tenure: Rogers lead PM since inception 1986-11-06; to 2025-12-31 and to fact-sheet date 2026-03-31
d1=(date(2025,12,31)-date(1986,11,6)).days
d2=(date(2026,3,31)-date(1986,11,6)).days
print("tenure", d1, round(d1/365.25,2), d2, round(d2/365.25,2))
chk("1 tenure", d1==14300 and d2==14390, f"to 2025-12-31 {d1} days ~{d1/365.25:.2f}y = 100% of fund life (since inception); to 2026-03-31 {d2} days")

# 2 calendar 2016-2025 compound vs stated 10y annualized 9.51
cal=[D(x) for x in ["15.57","15.88","-13.67","24.67","10.02","30.36","-18.82","15.81","11.80","14.15"]]
prod=D(1)
for v in cal: prod*=(1+v/100)
ann=(float(prod)**0.1-1)*100
print("10y factor", prod, "ann", ann)
chk("2 calendar compound", abs((prod-1)*100-D("148.03"))<D("0.05") and abs(D(str(ann))-D("9.51"))<D("0.01"), f"factor={prod:.4f} cum={(prod-1)*100:.2f}% ann={ann:.4f}% vs stated 9.51")

# 3 excess vs 3 benchmarks, 4 windows, exact subtraction (prospectus table; SPX 5y uses prospectus 14.42, letter prints 14.43)
rows=[("1y","14.15","12.73","12.59","17.88"),("5y","9.36","10.02","8.88","14.42"),("10y","9.51","9.72","9.27","14.82"),("SI","10.78","10.66","9.96","11.24")]
ex={(w):(D(f)-D(a),D(f)-D(b),D(f)-D(c)) for w,f,a,b,c in rows}
print("excess", ex)
chk("3 excess", ex["SI"]==(D("0.12"),D("0.82"),D("-0.46")) and ex["10y"]==(D("-0.21"),D("0.24"),D("-5.31")) and ex["5y"]==(D("-0.66"),D("0.48"),D("-5.06")) and ex["1y"]==(D("1.42"),D("1.56"),D("-3.73")), "SI beats both value indexes, trails SPX 0.46; 10y trails R2500V and SPX")

# 4 split two 5y windows
p1=D(1)
for v in cal[:5]: p1*=(1+v/100)
p2=D(1)
for v in cal[5:]: p2*=(1+v/100)
a1=(float(p1)**0.2-1)*100; a2=(float(p2)**0.2-1)*100
print("splits", p1, a1, p2, a2)
chk("4 splits", abs(D(str(a1))-D("9.66"))<D("0.01") and abs(D(str(a2))-D("9.36"))<D("0.01"), f"2016-20 ann={a1:.2f}% 2021-25 ann={a2:.2f}% (latter matches stated 5y 9.36)")

# 5 recovery after 2022 -18.82
rec=(D(1)/D("0.8118")-1)*100
two=D("0.8118")*D("1.1581"); three=two*D("1.1180")
print("recovery", rec, two, three)
chk("5 recovery", abs(rec-D("23.18"))<D("0.01") and abs((two-1)*100-(-D("5.99")))<D("0.01") and abs((three-1)*100-D("5.11"))<D("0.01"), f"need +{rec:.2f}%; +15.81% leaves {(two-1)*100:.2f}%; +11.80% reaches {(three-1)*100:.2f}%")

# 6 2020 extremes: best quarter +31.56 (4Q20), worst -35.14 (1Q20), same year; full year +10.02
chk("6 2020 extremes", D("31.56")+D("35.14")==D("66.70"), "spread 66.70pp within one calendar year; year itself +10.02%")

# 7 negative years exactly 2 of 10; single-year best/worst spread
neg=[i for i,v in enumerate(cal) if v<0]
chk("7 neg years", len(neg)==2 and cal[2]==D("-13.67") and cal[6]==D("-18.82") and max(cal)-min(cal)==D("49.18"), "negatives only 2018 -13.67 and 2022 -18.82; best +30.36 (2021) worst -18.82 spread 49.18")

# 8 since-inception terminals (approx, years = 14300/365.25 = 39.15)
yrs=d1/365.25
terms={n:(1+float(r)/100)**yrs for n,r in [("fund","10.78"),("R2500V","10.66"),("R2000V","9.96"),("SPX","11.24")]}
print("terminals", {k:round(v,2) for k,v in terms.items()})
chk("8 SI terminals", abs(terms["fund"]-55.05)<0.3 and abs(terms["SPX"]-64.74)<0.3 and abs(terms["R2500V"]-52.76)<0.3 and abs(terms["R2000V"]-41.15)<0.3, f"fund x{terms['fund']:.2f} vs SPX x{terms['SPX']:.2f} vs R2500V x{terms['R2500V']:.2f} vs R2000V x{terms['R2000V']:.2f} (approx; index inception dates differ, register)")

# 9 after-tax drag at SI: before 10.78, on-dist 9.23, on-dist+sale 9.00; terminals
at1=(1+9.23/100)**yrs; at2=(1+9.00/100)**yrs
print("after-tax terminals", round(at1,2), round(at2,2))
chk("9 after-tax", D("10.78")-D("9.23")==D("1.55") and D("10.78")-D("9.00")==D("1.78") and abs(at1-31.71)<0.3 and abs(at2-29.19)<0.3, f"drag 1.55/1.78pp per year; terminal x{at1:.2f}/x{at2:.2f} vs x{terms['fund']:.2f} before tax")

# 10 top-10 (fact sheet 2026-03-31): rows sum 38.84 vs stated total 38.86 (0.02 rounding)
top=[D(x) for x in ["5.46","4.30","3.84","3.76","3.63","3.62","3.59","3.58","3.54","3.52"]]
print("top10", sum(top), "top1 share", D("5.46")/sum(top)*100)
chk("10 top10", sum(top)==D("38.84") and D("38.86")-sum(top)==D("0.02") and abs(D("5.46")/sum(top)*100-D("14.06"))<D("0.01"), f"rows sum {sum(top)} vs stated 38.86 diff 0.02 rounding; #1 MSGE 5.46 = {D('5.46')/sum(top)*100:.2f}% of top10")

# 11 industries (fact sheet 2026-03-31): top-4 sum; three zero industries vs benchmark; rows sum register
inds=[D(x) for x in ["33.87","17.36","17.25","17.00","3.58","3.54","3.41","2.28","0.00","0.00","0.00","1.89"]]
bench_zero=D("10.00")+D("3.58")+D("4.57")
print("industries sum", sum(inds), "top4", sum(inds[:4]), "bench zero3", bench_zero)
chk("11 industries", sum(inds[:4])==D("85.48") and bench_zero==D("18.15") and sum(inds)==D("100.18"), f"top4={sum(inds[:4])}; Technology+Telecom+Utilities fund 0.00 vs benchmark {bench_zero}; rows sum {sum(inds)} vs 100 diff 0.18 register only (4Q24 sheet rows sum 100.14 likewise)")

# 12 fees exact; expense example gap; turnover two readings; SPX 5y print discrepancy register
chk("12 fees/misc", D("0.58")+D("0.25")+D("0.18")==D("1.01") and D("0.58")+D("0.00")+D("0.12")==D("0.70") and D("1236")-D("871")==D("365") and D("14.43")-D("14.42")==D("0.01"), "Investor 0.58+0.25+0.18=1.01, Institutional 0.58+0+0.12=0.70 exact; 10y expense example 1236 vs 871 diff 365; turnover prospectus FY 17% vs fact-sheet trailing 27.61% different windows register; SPX 5y letter 14.43 vs prospectus 14.42 diff 0.01 register")

print("ALL PASS" if all(ok) else "SOME FAIL", f"{sum(ok)}/{len(ok)} groups")
