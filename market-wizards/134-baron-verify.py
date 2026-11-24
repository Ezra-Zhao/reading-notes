#!/usr/bin/env python3
"""134 Ron Baron verify: all numbers from Baron Generational Growth Fund fact sheet (BGRIX, 2026-09-30)."""
from decimal import Decimal as D
from datetime import date

ok = 0
def chk(cond, label):
    global ok
    assert cond, f"FAIL {label}"
    ok += 1
    print(f"PASS {label}")

def approx(a, b, tol=D("0.02")):
    return abs(D(str(a)) - D(str(b))) <= tol

# G1 life / tenure: inception 1994-12-31 to 2026-09-30
life = (date(2026,9,30)-date(1994,12,31)).days
chk(life==11596, "G1 life 11596 days")
chk(approx(D(life)/D("365.25"), "31.75", D("0.01")), "G1 life 31.75 years")
chk(2026-1994==32, "G1 calendar span 32nd year")
# Rosenberg named PM in 2018 (year only): solo span 1994->2018 = 24 calendar years approx
chk(2018-1994==24, "G1 solo approx 24 years before co-manager year")

# Annualized (BGRIX): windows 1,3,5,10,SI
F = {"1":D("-14.79"),"3":D("-5.27"),"5":D("-5.58"),"10":D("6.96"),"SI":D("10.87")}
R2 = {"1":D("12.05"),"3":D("17.55"),"5":D("4.72"),"10":D("9.90"),"SI":D("8.22")}
R3 = {"1":D("15.13"),"3":D("22.26"),"5":D("12.64"),"10":D("14.73"),"SI":D("11.15")}

# G2 excess vs Russell 2000 Growth
exp2 = {"1":"-26.84","3":"-22.82","5":"-10.30","10":"-2.94","SI":"2.65"}
for k,e in exp2.items():
    chk(approx(F[k]-R2[k], e, D("0.005")), f"G2 excess vs R2000G {k} {e}")
chk(sum(1 for k in F if F[k]>R2[k])==1, "G2 only 1 of 5 windows positive vs R2000G")

# G3 excess vs Russell 3000
exp3 = {"1":"-29.92","3":"-27.53","5":"-18.22","10":"-7.77","SI":"-0.28"}
for k,e in exp3.items():
    chk(approx(F[k]-R3[k], e, D("0.005")), f"G3 excess vs R3000 {k} {e}")
chk(sum(1 for k in F if F[k]>R3[k])==0, "G3 zero windows positive vs R3000")

# G4 non-annualized QTD / YTD
chk(approx(D("2.13")-D("-9.39"), "11.52", D("0.005")), "G4 QTD excess vs R2000G +11.52")
chk(approx(D("2.13")-D("1.40"), "0.73", D("0.005")), "G4 QTD excess vs R3000 +0.73")
chk(approx(D("-12.44")-D("10.71"), "-23.15", D("0.005")), "G4 YTD excess vs R2000G -23.15")
chk(approx(D("-12.44")-D("12.42"), "-24.86", D("0.005")), "G4 YTD excess vs R3000 -24.86")

# G5 implied H1 2026 (YTD stripped of Q3)
h1f = (D("0.8756")/D("1.0213")-1)*100
h1r2 = (D("1.1071")/D("0.9061")-1)*100
h1r3 = (D("1.1242")/D("1.0140")-1)*100
chk(approx(h1f, "-14.27"), "G5 H1 fund -14.27")
chk(approx(h1r2, "22.18"), "G5 H1 R2000G +22.18")
chk(approx(h1r3, "10.87"), "G5 H1 R3000 +10.87")

# G6 $10,000 endpoints over 31.75 years
def endpt(a): return D("10000")*( (D("1")+D(str(a))/100) ** D("31.75") )
chk(approx(endpt("10.87"), "264756", D("150")), "G6 fund endpoint ~264756")
chk(approx(endpt("8.22"), "122819", D("150")), "G6 R2000G endpoint ~122819")
chk(approx(endpt("11.15"), "286831", D("150")), "G6 R3000 endpoint ~286831")
chk(approx(endpt("10.87")/endpt("8.22"), "2.16", D("0.01")), "G6 fund/R2000G 2.16x")
chk(approx(endpt("10.87")/endpt("11.15"), "0.92", D("0.01")), "G6 fund/R3000 0.92x")

# G7 segment splits (annualized segment between windows)
def seg(long_a, long_y, short_a, short_y):
    la = (D("1")+D(str(long_a))/100) ** D(str(long_y))
    sa = (D("1")+D(str(short_a))/100) ** D(str(short_y))
    return ((la/sa) ** (D("1")/D(str(long_y-short_y))) - 1) * 100
chk(approx(seg("6.96",10,"-5.58",5), "21.17", D("0.05")), "G7 fund 10-5y segment +21.17")
chk(approx(seg("9.90",10,"4.72",5), "15.34", D("0.05")), "G7 R2000G 10-5y segment +15.34")
chk(approx(seg("-5.58",5,"-5.27",3), "-6.04", D("0.05")), "G7 fund 5-3y segment -6.04")
chk(approx(seg("-5.27",3,"-14.79",1), "-0.12", D("0.05")), "G7 fund 3-1y segment -0.12")
chk(approx(seg("17.55",3,"12.05",1), "20.40", D("0.05")), "G7 R2000G 3-1y segment +20.40")

# G8 early segment: SI stripped of last 10 years (21.75 years)
chk(approx(seg("10.87",31.75,"6.96",10), "12.72", D("0.05")), "G8 fund early segment +12.72")
chk(approx(seg("8.22",31.75,"9.90",10), "7.46", D("0.05")), "G8 R2000G early segment +7.46")
chk(approx(seg("11.15",31.75,"14.73",10), "9.54", D("0.05")), "G8 R3000 early segment +9.54")

# G9 cumulative windows and recovery
def cum(a,y): return ((D("1")+D(str(a))/100) ** D(str(y)) - 1) * 100
chk(approx(cum("6.96",10), "95.98", D("0.05")), "G9 fund cum10 +95.98")
chk(approx(cum("-5.58",5), "-24.96", D("0.05")), "G9 fund cum5 -24.96")
chk(approx(cum("4.72",5), "25.94", D("0.05")), "G9 R2000G cum5 +25.94")
chk(approx(cum("-5.27",3), "-14.99", D("0.05")), "G9 fund cum3 -14.99")
chk(approx((D("1")/D("0.8521")-1)*100, "17.36", D("0.02")), "G9 recovery after 1Y +17.36")
chk(approx((D("1")/D("0.8756")-1)*100, "14.21", D("0.02")), "G9 recovery after YTD +14.21")

# G10 calendar years 2016-2025 win counts
cal_f = [D(x) for x in ("6.31","27.35","-2.67","40.50","33.06","20.15","-22.40","14.97","5.02","-14.18")]
cal_r2 = [D(x) for x in ("11.32","22.17","-9.31","28.48","34.63","2.83","-26.36","18.66","15.15","13.01")]
cal_r3 = [D(x) for x in ("12.74","21.13","-5.24","31.02","20.89","25.66","-19.21","25.96","23.81","17.15")]
chk(sum(1 for a,b in zip(cal_f,cal_r2) if a>b)==5, "G10 vs R2000G 5 wins of 10")
chk(sum(1 for a,b in zip(cal_f,cal_r3) if a>b)==4, "G10 vs R3000 4 wins of 10")
chk(all(cal_f[i]<cal_r2[i] for i in (7,8,9)), "G10 last three calendar years all lose to R2000G")

# G11 holdings shape
top10 = [D(x) for x in ("19.8","19.7","14.9","11.5","9.2","8.3","7.1","6.1","5.1","5.1")]
chk(approx(sum(top10), "106.8", D("0.01")), "G11 top10 sum 106.8")
chk(approx(top10[0]+top10[1], "39.5", D("0.01")), "G11 top2 sum 39.5")
chk(approx(D("100")/D("0.93"), "107.53", D("0.01")), "G11 implied holding 107.53 years from 0.93% turnover")
chk(approx(D("17.57")/D("7.35"), "2.39", D("0.01")), "G11 weighted/median cap 2.39x")

# G12 retail vs institutional (BGRFX vs BGRIX)
ret = {"QTD":D("2.06"),"YTD":D("-12.60"),"1":D("-15.01"),"3":D("-5.52"),"5":D("-5.82"),"10":D("6.68"),"SI":D("10.71")}
inst = {"QTD":D("2.13"),"YTD":D("-12.44"),"1":D("-14.79"),"3":D("-5.27"),"5":D("-5.58"),"10":D("6.96"),"SI":D("10.87")}
for k in ret:
    chk(ret[k] < inst[k], f"G12 retail below institutional {k}")
chk(approx(inst["SI"]-ret["SI"], "0.16", D("0.005")), "G12 SI gap 0.16/yr")

print(f"ALL {ok} ASSERTIONS PASSED")
