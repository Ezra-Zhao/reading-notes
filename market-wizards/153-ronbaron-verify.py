# -*- coding: utf-8 -*-
"""153 Ron Baron verify: numbers from Baron Generational Growth Fund (formerly Baron Growth Fund)
official fact sheet (BGRIX, 2026-09-30).
A = official disclosed figures; C = arithmetic / compounding derived from A."""
from decimal import Decimal as D
from datetime import date

ok = 0
def chk(cond, label):
    global ok
    assert cond, label
    ok += 1
    print("PASS", label)

# Group 1 fund life: 1994-12-31 to 2026-09-30
days = (date(2026,9,30)-date(1994,12,31)).days
chk(days == 11596, f"fund life {days} days")
chk(abs(D(days)/D("365.25") - D("31.75")) < D("0.01"), "about 31.75 years")

# Group 2 tenure: Ron Baron PM since 1994 = whole fund life; Rosenberg named PM in 2018 (year only)
lo = (date(2026,9,30)-date(2018,1,1)).days
hi = (date(2026,9,30)-date(2018,12,31)).days
chk(lo == 3194 and hi == 2830, "co-manager era day range for a 2018 start")
chk(D("24") < D(hi)/D(days)*100 and D(lo)/D(days)*100 < D("28"), "Rosenberg era roughly 24-28 percent of fund life")

fund = {"qtd":D("2.13"),"ytd":D("-12.44"),"1y":D("-14.79"),"3y":D("-5.27"),"5y":D("-5.58"),"10y":D("6.96"),"si":D("10.87")}
r2   = {"qtd":D("-9.39"),"ytd":D("10.71"),"1y":D("12.05"),"3y":D("17.55"),"5y":D("4.72"),"10y":D("9.90"),"si":D("8.22")}
r3   = {"qtd":D("1.40"),"ytd":D("12.42"),"1y":D("15.13"),"3y":D("22.26"),"5y":D("12.64"),"10y":D("14.73"),"si":D("11.15")}

# Group 3 excess vs Russell 2000 Growth: wins 2 of 7 (QTD and since inception)
ex = {k: fund[k]-r2[k] for k in fund}
chk(ex["qtd"]==D("11.52") and ex["si"]==D("2.65"), "vs small growth winning windows")
chk(ex["1y"]==D("-26.84") and ex["3y"]==D("-22.82") and ex["5y"]==D("-10.30"), "vs small growth deep losing windows")
chk(sum(1 for v in ex.values() if v>0)==2, "vs small growth wins 2 of 7")

# Group 4 excess vs Russell 3000: wins only QTD
exr = {k: fund[k]-r3[k] for k in fund}
chk(exr["qtd"]==D("0.73") and exr["si"]==D("-0.28"), "vs Russell 3000 QTD win, SI near tie negative")
chk(sum(1 for v in exr.values() if v>0)==1, "vs Russell 3000 wins 1 of 7")

# Group 5 2026 H1 reverse split: fund down hard, index up hard
h1 = ((1+fund["ytd"]/100)/(1+fund["qtd"]/100)-1)*100
h1r = ((1+r2["ytd"]/100)/(1+r2["qtd"]/100)-1)*100
chk(D("-14.6") < h1 < D("-13.9"), f"fund H1 reverse about {h1:.2f} percent")
chk(D("21.8") < h1r < D("22.6"), f"small growth H1 reverse about {h1r:.2f} percent")

def seg(ann_long, yrs_long, ann_short, yrs_short):
    total = (1+ann_long/100)**yrs_long
    short = (1+ann_short/100)**yrs_short
    return ((total/short) ** (D(1)/(yrs_long-yrs_short)) - 1)*100

# Group 6 segment 10 to 5 years ago: the sharp segment
s105 = seg(fund["10y"],10,fund["5y"],5)
s105r = seg(r2["10y"],10,r2["5y"],5)
chk(D("20.6") < s105 < D("21.7"), f"10-5y fund about {s105:.2f} per year")
chk(D("14.8") < s105r < D("15.9"), f"10-5y index about {s105r:.2f} per year")

# Group 7 segments 5-3 and 3-1 years ago
s53 = seg(fund["5y"],5,fund["3y"],3)
s53r = seg(r2["5y"],5,r2["3y"],3)
chk(D("-6.6") < s53 < D("-5.5"), f"5-3y fund about {s53:.2f} per year")
chk(D("-12.5") < s53r < D("-11.4"), f"5-3y index about {s53r:.2f} per year")
s31 = (((1+fund["3y"]/100)**3/(1+fund["1y"]/100)) ** D("0.5") - 1)*100
s31r = (((1+r2["3y"]/100)**3/(1+r2["1y"]/100)) ** D("0.5") - 1)*100
chk(D("-0.7") < s31 < D("0.5"), f"3-1y fund about {s31:.2f} per year")
chk(D("19.9") < s31r < D("20.9"), f"3-1y index about {s31r:.2f} per year")

# Group 8 ten thousand endpoints
e5 = 10000*(1+fund["5y"]/100)**5
e10 = 10000*(1+fund["10y"]/100)**10
esi = 10000*(1+fund["si"]/100)**(D(days)/D("365.25"))
esir = 10000*(1+r2["si"]/100)**(D(days)/D("365.25"))
chk(D("7400") < e5 < D("7600"), f"5y endpoint about {e5:.0f}")
chk(D("19400") < e10 < D("19800"), f"10y endpoint about {e10:.0f}")
chk(D("260000") < esi < D("270000"), f"SI endpoint about {esi:.0f}")
chk(D("2.10") < esi/esir < D("2.22"), f"SI endpoint about {esi/esir:.2f} times benchmark")

# Group 9 calendar shape 2016-2025: three negative years
cal = [D("6.31"),D("27.35"),D("-2.67"),D("40.50"),D("33.06"),D("20.15"),D("-22.40"),D("14.97"),D("5.02"),D("-14.18")]
chk(sum(1 for v in cal if v<0)==3, "three negative calendar years: 2018, 2022, 2025")
chk(max(cal)==D("40.50"), "best year 2019 +40.50")
chk(cal[-1]-D("13.01")==D("-27.19"), "2025 calendar excess vs index -27.19 points")

# Group 10 2022 recovery arithmetic: still below origin at end of 2025
need = (1/(1-D("22.40")/100)-1)*100
chk(D("28.4") < need < D("29.4"), f"2022 drop needs about {need:.2f} percent to recover")
net = (1-D("22.40")/100)*(1+D("14.97")/100)*(1+D("5.02")/100)*(1-D("14.18")/100)
chk(D("0.79") < net < D("0.82"), f"2022 drop plus 2023-2025 ends about {(net-1)*100:.2f} percent vs origin")

# Group 11 holdings: top 10 names sum exactly to printed 106.8 (over 100 percent of net assets)
top = [D("19.8"),D("19.7"),D("14.9"),D("11.5"),D("9.2"),D("8.3"),D("7.1"),D("6.1"),D("5.1"),D("5.1")]
chk(sum(top)==D("106.8"), "top 10 names sum 106.8, equals printed total")
chk(top[0]+top[1]==D("39.5"), "top two sum 39.5 percent of net assets")
chk(D("36") < (top[0]+top[1])/sum(top)*100 < D("38"), "top two are about 37 percent of the top 10 total")

# Group 12 Q3 attribution: top contributor alone exceeds the whole quarter gain
chk(D("2.39")+D("1.75")+D("1.04")==D("5.18"), "top 3 contributors sum 5.18 points")
chk(D("-1.54")+D("-0.76")+D("-0.66")==D("-2.96"), "top 3 detractors sum -2.96 points")
chk(D("2.39") > fund["qtd"], "Gartner contribution 2.39 exceeds whole QTD return 2.13")

print(f"ALL {ok} ASSERTIONS PASSED")
