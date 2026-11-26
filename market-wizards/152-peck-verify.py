# -*- coding: utf-8 -*-
"""152 Peck verify: numbers from Baron Asset Fund official fact sheet (BARIX, 2026-09-30).
A = official disclosed figures; C = arithmetic / compounding derived from A."""
from decimal import Decimal as D
from datetime import date

ok = 0
def chk(cond, label):
    global ok
    assert cond, label
    ok += 1
    print("PASS", label)

# Group 1 fund life: 1987-06-12 to 2026-09-30
days = (date(2026,9,30)-date(1987,6,12)).days
chk(days == 14355, f"fund life {days} days")
chk(abs(D(days)/D("365.25") - D("39.30")) < D("0.01"), "about 39.30 years")

# Group 2 tenure split: PM named in 2003 (year only in fact sheet)
lo = (date(2026,9,30)-date(2003,1,1)).days
hi = (date(2026,9,30)-date(2003,12,31)).days
chk(lo == 8673 and hi == 8309, "tenure day range for a 2003 start")
chk(D("57") < D(hi)/D(days)*100 and D(lo)/D(days)*100 < D("61"), "tenure share roughly 58-60 percent")
chk(days - lo > 5600, "predecessor segment over 5600 days, about 15.6 years or more")

fund = {"qtd":D("-6.22"),"ytd":D("2.86"),"1y":D("10.97"),"3y":D("11.50"),"5y":D("2.41"),"10y":D("11.06"),"si":D("11.12")}
mid  = {"qtd":D("-5.84"),"ytd":D("1.01"),"1y":D("-2.73"),"3y":D("15.36"),"5y":D("4.92"),"10y":D("11.86"),"si":D("10.27")}
r3   = {"qtd":D("1.40"),"ytd":D("12.42"),"1y":D("15.13"),"3y":D("22.26"),"5y":D("12.64"),"10y":D("14.73"),"si":D("10.76")}

# Group 3 excess vs Russell Midcap Growth: wins 3 of 7
ex = {k: fund[k]-mid[k] for k in fund}
chk(ex["1y"]==D("13.70") and ex["ytd"]==D("1.85") and ex["si"]==D("0.85"), "vs midcap growth winning windows")
chk(ex["qtd"]==D("-0.38") and ex["3y"]==D("-3.86") and ex["5y"]==D("-2.51") and ex["10y"]==D("-0.80"), "vs midcap growth losing windows")
chk(sum(1 for v in ex.values() if v>0)==3, "vs midcap growth wins 3 of 7")

# Group 4 excess vs Russell 3000: wins only since inception
exr = {k: fund[k]-r3[k] for k in fund}
chk(exr["si"]==D("0.36"), "vs Russell 3000 only SI positive")
chk(sum(1 for v in exr.values() if v>0)==1, "vs Russell 3000 wins 1 of 7")

# Group 5 2026 H1 reverse split
h1 = ((1+fund["ytd"]/100)/(1+fund["qtd"]/100)-1)*100
h1m = ((1+mid["ytd"]/100)/(1+mid["qtd"]/100)-1)*100
chk(D("9.5") < h1 < D("9.9"), f"fund H1 reverse about {h1:.2f} percent")
chk(D("7.1") < h1m < D("7.5"), f"midcap H1 reverse about {h1m:.2f} percent")

def seg(ann_long, yrs_long, ann_short, yrs_short):
    total = (1+ann_long/100)**yrs_long
    short = (1+ann_short/100)**yrs_short
    return ((total/short) ** (D(1)/(yrs_long-yrs_short)) - 1)*100

# Group 6 segment 10 to 5 years ago
s105 = seg(fund["10y"],10,fund["5y"],5)
s105m = seg(mid["10y"],10,mid["5y"],5)
chk(D("20.0") < s105 < D("21.0"), f"10-5y fund about {s105:.2f} per year")
chk(D("18.8") < s105m < D("19.8"), f"10-5y midcap about {s105m:.2f} per year")

# Group 7 segments 5-3 and 3-1 years ago
s53 = seg(fund["5y"],5,fund["3y"],3)
s53m = seg(mid["5y"],5,mid["3y"],3)
chk(D("-10.5") < s53 < D("-9.0"), f"5-3y fund about {s53:.2f} per year")
chk(D("-9.5") < s53m < D("-8.0"), f"5-3y midcap about {s53m:.2f} per year")
s31 = (((1+fund["3y"]/100)**3/(1+fund["1y"]/100)) ** D("0.5") - 1)*100
s31m = (((1+mid["3y"]/100)**3/(1+mid["1y"]/100)) ** D("0.5") - 1)*100
chk(D("11.0") < s31 < D("12.5"), f"3-1y fund about {s31:.2f} per year")
chk(D("24.0") < s31m < D("27.0"), f"3-1y midcap about {s31m:.2f} per year")

# Group 8 ten thousand endpoints
e5 = 10000*(1+fund["5y"]/100)**5
e10 = 10000*(1+fund["10y"]/100)**10
esi = 10000*(1+fund["si"]/100)**(D(days)/D("365.25"))
esim = 10000*(1+mid["si"]/100)**(D(days)/D("365.25"))
chk(D("11000") < e5 < D("11500"), f"5y endpoint about {e5:.0f}")
chk(D("28000") < e10 < D("29000"), f"10y endpoint about {e10:.0f}")
chk(D("600000") < esi < D("660000"), f"SI endpoint about {esi:.0f}")
chk(D("1.30") < esi/esim < D("1.40"), f"SI endpoint about {esi/esim:.2f} times benchmark")

# Group 9 calendar shape 2016-2025: only one negative year
cal = [D("6.51"),D("26.49"),D("0.14"),D("37.96"),D("33.33"),D("14.22"),D("-25.87"),D("17.35"),D("10.77"),D("8.20")]
chk(sum(1 for v in cal if v<0)==1, "only one negative calendar year 2022")
chk(max(cal)==D("37.96"), "best year 2019 +37.96")

# Group 10 2022 recovery arithmetic
need = (1/(1-D("25.87")/100)-1)*100
chk(D("34.5") < need < D("35.5"), f"2022 drop needs about {need:.2f} percent to recover")
net = (1-D("25.87")/100)*(1+D("17.35")/100)*(1+D("10.77")/100)*(1+D("8.20")/100)
chk(D("1.03") < net < D("1.05"), f"2022 drop plus 3 up years ends about {(net-1)*100:.2f} percent above origin")

# Group 11 holdings: top 10 list sums to 62.1 vs printed 62.0 (rounding), SpaceX weight
top = [D("30.5"),D("4.9"),D("3.8"),D("3.8"),D("3.7"),D("3.6"),D("3.4"),D("3.2"),D("2.8"),D("2.4")]
chk(sum(top)==D("62.1"), "top 10 names sum 62.1, printed total 62.0, gap is rounding")
chk(top[0]+top[1]==D("35.4"), "top two sum 35.4 percent")
chk(D("48") < top[0]/sum(top)*100 < D("50"), "SpaceX is about 49 percent of the top 10 total")

# Group 12 Q3 attribution seam: SpaceX detractor -4.01 vs quarter -6.22
chk(D("4.01")/D("6.22") > D("0.6"), "SpaceX detractor equals about 64 percent of the quarter drop magnitude")
chk(D("0.84")+D("0.62")+D("0.46")==D("1.92"), "top 3 contributors sum 1.92 points")

print(f"ALL {ok} ASSERTIONS PASSED")
