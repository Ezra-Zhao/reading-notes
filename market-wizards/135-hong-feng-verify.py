#!/usr/bin/env python3
"""135 Hong Zhi & Feng Hanjie verify: all numbers from GF Balanced Growth Q3 2026 report (010534)."""
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

# G1 life / tenures
life = (date(2026,9,30)-date(2021,1,27)).days
hong = (date(2026,9,30)-date(2021,8,27)).days
pre = (date(2021,8,27)-date(2021,1,27)).days
feng = (date(2026,9,30)-date(2023,11,1)).days
chk(life==2072, "G1 life 2072")
chk(hong==1860, "G1 Hong tenure 1860")
chk(pre==212, "G1 pre-Hong 212")
chk(feng==1064, "G1 Feng tenure 1064")
chk(approx(D(hong)/D(life)*100, "89.77", D("0.01")), "G1 Hong share 89.77%")
chk(approx(D(feng)/D(life)*100, "51.35", D("0.01")), "G1 Feng share 51.35%")
chk(approx(D(life)/D("365.25"), "5.67", D("0.01")), "G1 life years 5.67")

# G2 A excess (printed) - all six positive
rows = [("3.25","-5.67"),("0.89","0.15"),("6.75","0.20"),("25.27","17.52"),("15.38","11.59"),("19.48","10.74")]
exp = ["8.92","0.74","6.55","7.75","3.79","8.74"]
for (f,b),e in zip(rows,exp):
    chk(approx(D(f)-D(b), e, D("0.005")), f"G2 A excess {e}")
chk(all(D(f)>D(b) for f,b in rows), "G2 A all 6 windows positive excess")
chk(max(D(f)-D(b) for f,b in rows)==D("8.92"), "G2 A max excess 8.92")

# G3 implied Q2 2026
q2f = (D("1.0089")/D("1.0325")-1)*100
q2b = (D("1.0015")/D("0.9433")-1)*100
chk(approx(q2f, "-2.29"), "G3 Q2 fund -2.29")
chk(approx(q2b, "6.17"), "G3 Q2 bench +6.17")
chk(approx(q2f-q2b, "-8.46", D("0.05")), "G3 Q2 gap approx -8.46")

# G4 segment 3Y-1Y: near-identical
seg_3_1_f = (D("1.2527")/D("1.0675")-1)*100
seg_3_1_b = (D("1.1752")/D("1.0020")-1)*100
chk(approx(seg_3_1_f, "17.35"), "G4 seg 3-1Y fund +17.35")
chk(approx(seg_3_1_b, "17.29"), "G4 seg 3-1Y bench +17.29")
chk(approx(seg_3_1_f-seg_3_1_b, "0.06", D("0.05")), "G4 seg gap approx +0.06")

# G5 segment 5Y-3Y: both negative
seg_5_3_f = (D("1.1538")/D("1.2527")-1)*100
seg_5_3_b = (D("1.1159")/D("1.1752")-1)*100
chk(approx(seg_5_3_f, "-7.89"), "G5 seg 5-3Y fund -7.89")
chk(approx(seg_5_3_b, "-5.05"), "G5 seg 5-3Y bench -5.05")

# G6 financials: realized and unrealized both positive
ra, pa = D("9202523.35"), D("24607061.74")
rc, pc = D("7094555.47"), D("18418408.35")
chk(approx(pa-ra, "15404538.39", D("0.01")), "G6 A unrealized +15404538.39")
chk(approx(pc-rc, "11323852.88", D("0.01")), "G6 C unrealized +11323852.88")
tot_r, tot_p = ra+rc, pa+pc
chk(approx(tot_r, "16297078.82", D("0.01")), "G6 total realized +16297078.82")
chk(approx(tot_p, "43025470.09", D("0.01")), "G6 total profit +43025470.09")
chk(approx((tot_p-tot_r)/tot_r, "1.64", D("0.01")), "G6 unrealized 1.64x realized")

# G7 NAV total and profit ratio
nav = D("820886978.97")+D("686301764.45")
chk(approx(nav, "1507188743.42", D("0.01")), "G7 total NAV 1507188743.42")
chk(approx(tot_p/nav*100, "2.85"), "G7 Q3 profit 2.85% of ending NAV")

# G8 asset mix: bonds bigger than equity
chk(approx(D("418932352.78")/nav*100, "27.80"), "G8 equity 27.80% of NAV")
chk(approx(D("705316295.04")/nav*100, "46.80"), "G8 bonds 46.80% of NAV")
chk(approx(D("46.52")+D("27.63")+D("17.53")+D("7.91")+D("0.40"), "99.99"), "G8 total-asset mix sums 99.99 (rounding)")
chk(approx(D("705316295.04")/D("418932352.78"), "1.68", D("0.01")), "G8 bonds 1.68x equity amount")

# G9 holdings shape
top10 = sum(D(x) for x in ["1.96","1.91","1.67","1.31","1.27","1.27","1.14","1.02","1.02","0.95"])
chk(approx(top10, "13.52", D("0.005")), "G9 top10 13.52")
coal = D("1.31")+D("1.27")+D("1.27")+D("1.14")
chk(approx(coal, "4.99", D("0.005")), "G9 four coal names 4.99")
chk(approx(D("16.08")/D("27.80")*100, "57.84"), "G9 manufacturing 57.84% of equity")
chk(approx(D("7.43")/D("27.80")*100, "26.73"), "G9 mining 26.73% of equity")

# G10 shares: net inflow in a winning quarter
a_net = D("687050704.04")-D("671184945.87")
c_net = D("582636562.94")-D("504712032.75")
chk(approx(a_net, "15865758.17", D("0.01")), "G10 A net +15865758.17")
chk(approx(c_net, "77924530.19", D("0.01")), "G10 C net +77924530.19")
chk(approx(a_net/D("671184945.87")*100, "2.36"), "G10 A +2.36%")
chk(approx(c_net/D("504712032.75")*100, "15.44"), "G10 C +15.44%")
tot_pct = (D("1269687266.98")-D("1175896978.62"))/D("1175896978.62")*100
chk(approx(tot_pct, "7.98"), "G10 total +7.98%")

# G11 NAV vs since-inception factors
chk(approx(D("1.1948")-1, "0.1948"), "G11 A NAV 1.1948 implies +19.48%")
chk(approx(D("1.1779")-1, "0.1779"), "G11 C NAV 1.1779 implies +17.79%")
chk(approx(D("19.48")-D("17.79"), "1.69", D("0.005")), "G11 A-C SI gap 1.69")

# G12 C class excess
rowsC = [("3.18","-5.67"),("0.76","0.15"),("6.48","0.20"),("24.32","17.52"),("13.95","11.59"),("17.79","10.74")]
expC = ["8.85","0.61","6.28","6.80","2.36","7.05"]
for (f,b),e in zip(rowsC,expC):
    chk(approx(D(f)-D(b), e, D("0.005")), f"G12 C excess {e}")
chk(all(D(f)>D(b) for f,b in rowsC), "G12 C all 6 windows positive excess")
chk(approx(D("3.25")-D("3.18"), "0.07", D("0.005")), "G12 A-C Q3 gap 0.07")

print(f"ALL PASS {ok} assertions")
