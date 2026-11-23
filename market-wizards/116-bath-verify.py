#!/usr/bin/env python3
"""116 Bath (Diamond Hill Large Cap Composite) verification.
Source: Diamond Hill Large Cap Composite Fact Sheet, as of 30 Sep 2026 (official PDF).
All returns net of fees unless labelled gross. Benchmark = Russell 1000 Value Index.
"""
from decimal import Decimal as D
from datetime import date

ok = 0
def chk(cond, label):
    global ok
    assert cond, label
    ok += 1
    print("PASS", label)

def r2(x): return x.quantize(D("0.01"))
def r1(x): return x.quantize(D("0.1"))

# Group 1: life span
life = (date(2026, 9, 30) - date(2001, 6, 30)).days
chk(life == 9223, "life 9223 days")
chk(r2(D(life) / D("365.25")) == D("25.25"), "life approx 25.25 years")

# Printed annualized returns (%): SI, 20Y, 15Y, 10Y, 5Y, 3Y, 1Y, YTD, 3Q26
net  = [D("8.88"), D("8.61"), D("11.78"), D("9.80"), D("5.81"), D("11.13"), D("5.52"), D("4.16"), D("3.18")]
gross= [D("9.62"), D("9.31"), D("12.47"), D("10.47"), D("6.45"), D("11.80"), D("6.15"), D("4.63"), D("3.33")]
val  = [D("8.43"), D("8.60"), D("12.98"), D("11.43"), D("11.92"), D("20.07"), D("23.81"), D("19.27"), D("2.61")]
core = [D("9.62"), D("11.16"), D("15.50"), D("15.04"), D("13.01"), D("22.48"), D("15.01"), D("12.30"), D("1.80")]

# Group 2: excess vs value index per window (pp)
excess = [r2(n - v) for n, v in zip(net, val)]
chk(excess == [D("0.45"), D("0.01"), D("-1.20"), D("-1.63"), D("-6.11"), D("-8.94"), D("-18.29"), D("-15.11"), D("0.57")], "excess all windows")
chk(sum(1 for e in excess if e > 0) == 3, "only 3 of 9 windows positive excess")

# Group 3: Q3 win, YTD split into H1
chk(r2(net[8] - val[8]) == D("0.57"), "Q3 excess +0.57")
h1_net = r2(((1 + net[7] / 100) / (1 + net[8] / 100) - 1) * 100)
h1_val = r2(((1 + val[7] / 100) / (1 + val[8] / 100) - 1) * 100)
chk(h1_net == D("0.95"), "H1 net +0.95")
chk(h1_val == D("16.24"), "H1 value +16.24")
chk(r2(h1_net - h1_val) == D("-15.29"), "H1 gap -15.29pp")

# Group 4: 1Y split into prior 9 months
p9_net = r2(((1 + net[6] / 100) / (1 + net[8] / 100) - 1) * 100)
p9_val = r2(((1 + val[6] / 100) / (1 + val[8] / 100) - 1) * 100)
chk(p9_net == D("2.27"), "prior9 net +2.27")
chk(p9_val == D("20.66"), "prior9 value +20.66")

# Group 5: since-inception $10,000 mechanical endpoints (25.25y)
yrs = D("25.25")
end_net = (10000 * (1 + net[0] / 100) ** yrs).quantize(D("1"))
end_val = (10000 * (1 + val[0] / 100) ** yrs).quantize(D("1"))
end_core = (10000 * (1 + core[0] / 100) ** yrs).quantize(D("1"))
chk(abs(end_net - D("85692")) <= 5, "endpoint net approx 85692")
chk(abs(end_val - D("77183")) <= 5, "endpoint value approx 77183")
chk(abs(end_core - D("101676")) <= 5, "endpoint core approx 101676")

# Group 6: cumulative windows
def cum(r, n): return r2(((1 + r / 100) ** n - 1) * 100)
chk(cum(net[3], 10) == D("154.70"), "10Y cum net +154.70")
chk(cum(val[3], 10) == D("195.14"), "10Y cum value +195.14")
chk(cum(net[4], 5) == D("32.63"), "5Y cum net +32.63")
chk(cum(val[4], 5) == D("75.61"), "5Y cum value +75.61")
chk(cum(net[5], 3) == D("37.24"), "3Y cum net +37.24")
chk(cum(val[5], 3) == D("73.10"), "3Y cum value +73.10")

# Group 7: segment splits
def seg(rl, yl, rs, ys): return r2((((1 + rl / 100) ** yl) / ((1 + rs / 100) ** ys) - 1) * 100)
chk(seg(net[3], 10, net[4], 5) == D("92.04"), "seg 5-10y ago net +92.04")
chk(seg(val[3], 10, val[4], 5) == D("68.07"), "seg 5-10y ago value +68.07")
chk(seg(net[4], 5, net[5], 3) == D("-3.36"), "seg 3-5y ago net -3.36")
chk(seg(val[4], 5, val[5], 3) == D("1.45"), "seg 3-5y ago value +1.45")
chk(seg(net[1], 20, net[2], 15) == D("-1.84"), "seg 15-20y ago net -1.84")
chk(seg(val[1], 20, val[2], 15) == D("-16.52"), "seg 15-20y ago value -16.52")

# Group 8: calendar years 2011-2025 net vs value, win count
cal_net = [D(x) for x in ["2.87","12.61","36.89","10.86","-0.82","14.57","20.37","-9.36","32.16","9.33","25.74","-13.35","13.68","12.06","5.55"]]
cal_val = [D(x) for x in ["0.39","17.51","32.53","13.45","-3.83","17.34","13.66","-8.27","26.54","2.80","25.16","-7.54","11.46","14.37","15.91"]]
wins = sum(1 for a, b in zip(cal_net, cal_val) if a > b)
chk(wins == 8, "calendar wins 8 of 15")
chk(len(cal_net) - wins == 7, "calendar losses 7 of 15")
chk(sum(1 for a in cal_net if a < 0) == 3, "net negative calendar years 3")

# Group 9: top-10 holdings sum vs printed total
top = [D(x) for x in ["7.0","5.8","4.8","4.1","3.5","2.9","2.8","2.7","2.7","2.5"]]
chk(r1(sum(top)) == D("38.8"), "top10 rows sum 38.8 (printed 38.9, diff 0.1 registered)")
chk(top[0] == D("7.0"), "largest position 7.0 at guideline max")

# Group 10: sector allocation sum
sec = [D(x) for x in ["20.9","15.2","15.1","12.4","10.0","8.4","7.5","2.5","2.2","1.8","1.0"]]
chk(r1(sum(sec)) == D("97.0"), "sectors ex-cash 97.0")
chk(r1(sum(sec) + D("3.1")) == D("100.1"), "sectors plus cash 100.1 (diff 0.1 registered)")

# Group 11: contributors
best = [D("1.8"), D("0.8"), D("0.6"), D("0.6"), D("0.5")]
worst = [D("-0.4"), D("-0.4"), D("-0.3"), D("-0.3"), D("-0.3")]
chk(r1(sum(best)) == D("4.3"), "best five contribution +4.3")
chk(r1(sum(worst)) == D("-1.7"), "worst five contribution -1.7")
chk(r2(sum(best) + sum(worst)) == D("2.60"), "listed ten net +2.60 vs gross Q3 3.33")

# Group 12: fee drag, characteristics, catch-up
chk(r2(gross[0] - net[0]) == D("0.74"), "SI gross-net drag 0.74/yr")
chk(r2(gross[8] - net[8]) == D("0.15"), "Q3 gross-net drag 0.15")
chk(r2(D("82.9") / D("14.7")) == D("5.64"), "median mkt cap 5.64x benchmark")
chk(r2(((1 + val[6] / 100) / (1 + net[6] / 100) - 1) * 100) == D("17.33"), "catch-up needed +17.33 to match value 1Y endpoint")
chk(gross[0] == core[0] == D("9.62"), "gross SI equals core index SI 9.62 (registered coincidence)")

print(f"ALL {ok} ASSERTIONS PASSED")
