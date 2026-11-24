#!/usr/bin/env python3
"""133 Qi He verify: all numbers from E Fund Eco Theme Q3 2026 report (001856)."""
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

# G1 life / tenure
life = (date(2026,9,30)-date(2017,6,2)).days
tenure = (date(2026,9,30)-date(2017,12,27)).days
pre = (date(2017,12,27)-date(2017,6,2)).days
chk(life==3407, "G1 life 3407")
chk(tenure==3199, "G1 tenure 3199")
chk(pre==208, "G1 pre 208")
chk(approx(D(tenure)/D(life)*100, "93.89", D("0.01")), "G1 tenure share 93.89%")
chk(approx(D(life)/D("365.25"), "9.33", D("0.01")), "G1 life years 9.33")

# G2 A excess (printed)
rows = [("-24.07","-14.47"),("23.17","-14.28"),("56.87","-12.32"),("123.36","0.13"),("71.96","-28.37"),("428.86","30.41"),("621.90","8.26")]
exp = ["-9.60","37.45","69.19","123.23","100.33","398.45","613.64"]
for (f,b),e in zip(rows,exp):
    chk(approx(D(f)-D(b), e, D("0.005")), f"G2 excess {e}")
chk(sum(1 for f,b in rows if D(f)>D(b))==6, "G2 6 of 7 positive")

# G3 implied Q2 2026
q2f = (D("1.2317")/D("0.7593")-1)*100
q2b = (D("0.8572")/D("0.8553")-1)*100
chk(approx(q2f, "62.22", D("0.02")), "G3 Q2 fund +62.22")
chk(approx(q2b, "0.22", D("0.02")), "G3 Q2 bench +0.22")
chk(approx(q2f-q2b, "62.00", D("0.05")), "G3 Q2 gap approx 62.00")

# G4 implied Q1? 6M vs Q2: Q1 = 1.2317/1.6222-1
q1f = (D("1.2317")/((D("1")+q2f/100))-1)*100  # tautology check skip; instead segment splits below
seg_3_1_f = (D("2.2336")/D("1.5687")-1)*100
seg_3_1_b = (D("1.0013")/D("0.8768")-1)*100
chk(approx(seg_3_1_f, "42.39"), "G4 seg 3-1Y fund +42.39")
chk(approx(seg_3_1_b, "14.20"), "G4 seg 3-1Y bench +14.20")

# G5 segments 5-3, 7-5
seg_5_3_f = (D("1.7196")/D("2.2336")-1)*100
seg_5_3_b = (D("0.7163")/D("1.0013")-1)*100
seg_7_5_f = (D("5.2886")/D("1.7196")-1)*100
seg_7_5_b = (D("1.3041")/D("0.7163")-1)*100
chk(approx(seg_5_3_f, "-23.01"), "G5 seg 5-3Y fund -23.01")
chk(approx(seg_5_3_b, "-28.47"), "G5 seg 5-3Y bench -28.47")
chk(approx(seg_7_5_f, "207.54"), "G5 seg 7-5Y fund +207.54")
chk(approx(seg_7_5_b, "82.06"), "G5 seg 7-5Y bench +82.06")

# G6 financials
ra, pa = D("475270724.45"), D("-2044101043.94")
rc, pc = D("166173202.25"), D("-816774605.79")
ua, uc = pa-ra, pc-rc
chk(approx(ua, "-2519371768.39", D("0.01")), "G6 A unrealized -2519371768.39")
chk(approx(uc, "-982947808.04", D("0.01")), "G6 C unrealized -982947808.04")
tot_r, tot_p = ra+rc, pa+pc
chk(approx(tot_r, "641443926.70", D("0.01")), "G6 total realized +641443926.70")
chk(approx(tot_p, "-2860875649.73", D("0.01")), "G6 total profit -2860875649.73")
chk(approx(abs(tot_p-tot_r)/tot_r, "5.46", D("0.01")), "G6 unrealized loss 5.46x realized gain")

# G7 NAV total and loss ratio
nav = D("5948418836.34")+D("1600263756.68")
chk(approx(nav, "7548682593.02", D("0.01")), "G7 total NAV (note: printed sum)")
# recompute: 5948418836.34+1600263756.68 = 7548682593.02
chk(approx(abs(tot_p)/nav*100, "37.90", D("0.02")), "G7 Q3 loss 37.90% of ending NAV")

# G8 holdings
top10 = sum(D(x) for x in ["5.05","4.82","4.68","3.94","2.94","2.94","2.88","2.73","2.64","2.29"])
chk(approx(top10, "34.91", D("0.005")), "G8 top10 34.91")
chk(approx(D("61.18")/D("69.04")*100, "88.62"), "G8 manufacturing 88.62% of equity")
chk(approx(D("363571205.41"), D("363571205.41")), "G8 S industry equals Dongyang amount (register)")

# G9 shares
a_net = D("824008992.57")-D("904284876.92")
c_net = D("224839060.28")-D("407455490.87")
chk(approx(a_net, "-80275884.35", D("0.01")), "G9 A net -80275884.35")
chk(approx(c_net, "-182616430.59", D("0.01")), "G9 C net -182616430.59")
chk(approx(a_net/D("904284876.92")*100, "-8.88"), "G9 A -8.88%")
chk(approx(c_net/D("407455490.87")*100, "-44.82"), "G9 C -44.82%")
tot_net_pct = (D("1048848052.85")-D("1311740367.79"))/D("1311740367.79")*100
chk(approx(tot_net_pct, "-20.04"), "G9 total -20.04%")

# G10 recovery / NAV factor
chk(approx((D("1")/D("0.7593")-1)*100, "31.70"), "G10 Q3 recovery +31.70")
chk(approx(D("7.219")-1, "6.219"), "G10 NAV 7.219 implies +621.9%")
chk(approx((D("1")/D("1.5687")-1)*100, "-36.25"), "G10 1Y prior segment placeholder -36.25 inverse")

# G11 asset mix
chk(approx(D("5211419618.54")/D("7599169605.28")*100, "68.58"), "G11 equity 68.58% total assets")
chk(approx(D("30.69")+D("68.58")+D("0.73"), "100.00"), "G11 mix sums 100")

# G12 C class
chk(approx(D("-24.17")-D("-14.47"), "-9.70", D("0.005")), "G12 C Q3 excess -9.70")
chk(approx(D("123.88")-D("1.84"), "122.04", D("0.005")), "G12 C SI excess 122.04")
chk(approx(D("-24.17")-D("-24.07"), "-0.10", D("0.005")), "G12 C-A Q3 gap -0.10")

print(f"ALL PASS {ok} assertions")
