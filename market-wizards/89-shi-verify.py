from decimal import Decimal as D, getcontext
from datetime import date
getcontext().prec=28
ok=[]
def chk(name, cond, detail=""):
    ok.append(cond)
    print(("PASS" if cond else "FAIL"), name, detail)

# 1 tenure: Shi Cheng PM since fund inception 2019-11-18 (Q3 2026 report 4.1); to 2026-09-30
d1=(date(2026,9,30)-date(2019,11,18)).days
print("tenure", d1, round(d1/365.25,2))
chk("1 tenure", d1==2508, f"2019-11-18 to 2026-09-30 = {d1} days ~{d1/365.25:.2f}y = 100% of fund life (first PM since inception, no predecessor segment)")

# 2 A-class excess all 6 windows exact; C-class excess all 6 windows exact
A=[("-30.03","-18.13"),("-10.35","-17.38"),("-6.21","-14.30"),("18.70","4.11"),("-42.85","-36.29"),("119.21","46.82")]
Aex=[D(f)-D(b) for f,b in A]
C=[("-30.10","-18.13"),("-10.53","-17.38"),("-6.59","-14.30"),("17.29","4.11"),("-43.98","-36.29"),("113.28","46.82")]
Cex=[D(f)-D(b) for f,b in C]
print("A excess", Aex); print("C excess", Cex)
chk("2 excess", Aex==[D(x) for x in ["-11.90","7.03","8.09","14.59","-6.56","72.39"]] and Cex==[D(x) for x in ["-11.97","6.85","7.71","13.18","-7.69","66.46"]], "A excess matches report in all 6 windows; only 3M and 5Y negative; C same pattern")

# 3 Q2 2026 single quarter reverse-derived from 6M and Q3 (A and benchmark)
q2=(D("0.8965")/D("0.6997")-1)*100
q2b=(D("0.8262")/D("0.8187")-1)*100
print("Q2 fund", q2, "Q2 bench", q2b, "excess", q2-q2b)
chk("3 Q2 reverse", abs(q2-D("28.13"))<D("0.01") and abs(q2b-D("0.92"))<D("0.01") and abs((q2-q2b)-D("27.21"))<D("0.02"), f"Q2 2026 fund approx +{q2:.2f}%, benchmark approx +{q2b:.2f}%, excess approx +{q2-q2b:.2f}pp; then Q3 -30.03% leaves 6M at -10.35%")

# 4 window splits: SI/5Y first segment; 5Y/3Y segment; 3Y/1Y segment; 1Y earlier half
seg1=(D("2.1921")/D("0.5715")-1)*100
seg2=(D("0.5715")/D("1.1870")-1)*100
seg3=(D("1.1870")/D("0.9379")-1)*100
seg4=(D("0.9379")/D("0.8965")-1)*100
print("splits", seg1, seg2, seg3, seg4)
chk("4 splits", abs(seg1-D("283.57"))<D("0.05") and abs(seg2-(-D("51.85")))<D("0.01") and abs(seg3-D("26.56"))<D("0.01") and abs(seg4-D("4.62"))<D("0.01"), f"inception to -5y approx +{seg1:.2f}%; -5y to -3y approx {seg2:.2f}%; -3y to -1y approx +{seg3:.2f}%; earlier half of past 1y approx +{seg4:.2f}%")

# 5 recovery prices: 5Y -42.85 and Q3 -30.03
r5=(D(1)/D("0.5715")-1)*100
r3=(D(1)/D("0.6997")-1)*100
print("recovery", r5, r3)
chk("5 recovery", abs(r5-D("74.98"))<D("0.01") and abs(r3-D("42.92"))<D("0.01"), f"past-5y -42.85% needs +{r5:.2f}% to recover; Q3 -30.03% alone needs +{r3:.2f}%")

# 6 Q3 profit split: realized vs profit vs unrealized, A+C combined
ra,pa=D("-50985178.34"),D("-585389401.46")
rc,pc=D("-32928982.68"),D("-362990483.16")
ua,uc=pa-ra,pc-rc
tot_r,tot_p,tot_u=ra+rc,pa+pc,ua+uc
ratio=abs(tot_u)/abs(tot_r)
print("profit split", tot_r, tot_p, tot_u, ratio)
chk("6 profit split", tot_r==D("-83914161.02") and tot_p==D("-948379884.62") and tot_u==D("-864465723.60") and abs(ratio-D("10.30"))<D("0.01"), f"combined realized {tot_r} yuan, profit {tot_p} yuan, unrealized {tot_u} yuan = approx {ratio:.2f}x the realized loss")

# 7 shares: start/end by class and total; net change
a0,a1=D("674333813.77"),D("655809229.85")
c0,c1=D("422572389.44"),D("417151037.50")
t0,t1=a0+c0,a1+c1
print("shares", t0, t1, (a1-a0)/a0*100, (c1-c0)/c0*100, (t1-t0)/t0*100)
chk("7 shares", t1==D("1072960267.35") and a1+c1==t1 and abs((a1-a0)/a0*100-(-D("2.75")))<D("0.01") and abs((c1-c0)/c0*100-(-D("1.28")))<D("0.01") and abs((t1-t0)/t0*100-(-D("2.18")))<D("0.01"), f"A net {(a1-a0)/a0*100:.2f}%, C net {(c1-c0)/c0*100:.2f}%, total {t0} to {t1} net {(t1-t0)/t0*100:.2f}% in a -30% quarter; end total matches section 2")

# 8 NAV and asset mix: combined NAV; equity share of total assets and of NAV; A unit NAV x shares rounding
nav=D("1349040496.40")+D("834872465.07")
eq=D("2039491980.00"); ta=D("2191084850.86")
diff=D("2.0571")*a1-D("1349040496.40")
print("NAV", nav, "eq/TA", eq/ta*100, "eq/NAV", eq/nav*100, "A nav diff", diff)
chk("8 NAV/assets", nav==D("2183912961.47") and abs(eq/ta*100-D("93.08"))<D("0.01") and abs(eq/nav*100-D("93.39"))<D("0.01") and abs(diff)<D("30000"), f"combined NAV {nav} yuan; equity {eq/ta*100:.2f}% of total assets and {eq/nav*100:.2f}% of NAV; A unit NAV x shares exceeds reported A NAV by approx {diff:.0f} yuan (rounding, register)")

# 9 industry: manufacturing 93.36% of NAV; domestic total 93.39; manufacturing share of domestic equity; HK stocks negligible
man=D("2038824944.20"); dom=D("2039467929.52")
print("industry", man/dom*100)
chk("9 industry", abs(man/dom*100-D("99.97"))<D("0.01") and D("93.39")-D("93.36")==D("0.03"), f"manufacturing 2,038,824,944.20 yuan = 93.36% of NAV and approx {man/dom*100:.2f}% of domestic equity; all other domestic industries sum to 0.03pp; HK stocks 24,050.48 yuan approx 0.00% of NAV")

# 10 top-10 holdings: pct sum, value sum, #1 share of top-10, top-3 sum
pct=[D(x) for x in ["9.41","8.49","7.21","7.18","6.43","6.07","5.87","5.73","5.42","5.22"]]
val=[D(x) for x in ["205517400.00","185449053.24","157539637.80","156708009.60","140359343.73","132471585.30","128274888.00","125140395.45","118306464.00","114098934.00"]]
print("top10 pct", sum(pct), "val", sum(val), "top1 share", pct[0]/sum(pct)*100, "top3", sum(pct[:3]))
chk("10 top10", sum(pct)==D("67.03") and sum(val)==D("1463865711.12") and abs(pct[0]/sum(pct)*100-D("14.04"))<D("0.01") and sum(pct[:3])==D("25.11"), f"top-10 sum {sum(pct)}% of NAV, values sum {sum(val)} yuan; #1 Fangzheng Tech 9.41% = approx {pct[0]/sum(pct)*100:.2f}% of top-10; top-3 sum 25.11%")

# 11 since-inception factor vs unit NAV ratio, A and C (register only)
ra_si=D("2.1921")/D("2.0571"); rc_si=D("2.1328")/D("2.0014")
print("SI ratios", ra_si, rc_si)
chk("11 SI factor vs NAV", abs(ra_si-D("1.0656"))<D("0.0002") and abs(rc_si-D("1.0657"))<D("0.0002"), f"A cumulative factor 2.1921 / unit NAV 2.0571 = approx {ra_si:.4f}; C 2.1328 / 2.0014 = approx {rc_si:.4f}; near-identical ratios, register only (distributions etc.), no inference")

# 12 bond book is a single convertible; volatility gap A vs benchmark
bond=D("210003.22")/nav*100
print("bond pct", bond, "std ratio", D("3.91")/D("1.31"))
chk("12 bond/vol", abs(bond-D("0.01"))<D("0.005") and abs(D("3.91")/D("1.31")-D("2.98"))<D("0.01"), f"sole bond holding Aoshi convertible 210,003.22 yuan = approx {bond:.4f}% of NAV (report rounds to 0.01%); A 3M NAV std 3.91% is approx {D('3.91')/D('1.31'):.2f}x benchmark std 1.31%; std excess exact in all windows (2.60/2.00/1.61/1.12/1.01/0.91)")

print("ALL PASS" if all(ok) else "SOME FAIL", f"{sum(ok)}/{len(ok)} groups")
