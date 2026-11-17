from datetime import date
# 1 tenure: 2018-12-05 to 2026-06-30
days = (date(2026,6,30)-date(2018,12,5)).days
assert days == 2764, days
print("1 tenure days", days, "years", round(days/365.25,2))
# 2 Q2 2026 realized vs profit (A+C)
realized = 132657337.10 + 28006899.57
profit = -376230713.26 - 81206372.32
assert realized == 160664236.67, realized
assert profit == -457437085.58, profit
gap = profit - realized
assert gap == -618101322.25, gap
print("2 realized", realized, "profit", profit, "gap", gap)
# 3 Q2 A vs benchmark diff (report stated)
diff = -9.86 - 8.42
assert abs(diff - (-18.28)) < 0.001, diff
print("3 diff", diff)
# 4 since-inception A +162.89% vs unit NAV 2.6289 (start 1.00)
assert abs((1+1.6289) - 2.6289) < 1e-9
print("4 inception factor = unit NAV", 2.6289)
# 5 past 7y vs past 5y implies first two years
first2 = ((1+1.3947)/(1+0.3145)-1)*100
assert abs(first2 - 82.18) < 0.02, first2
print("5 first two years of past seven", first2)
# 6 past 3y vs past 1y implies first two years of past three
f2 = ((1+0.1040)/(1-0.0199)-1)*100
assert abs(f2 - 12.64) < 0.02, f2
print("6 first two of past three", f2)
# 7 top-10 concentration Q2 2026
top10 = 10.19+10.05+9.93+9.64+9.52+7.17+5.25+4.93+3.79+3.69
assert abs(top10 - 74.16) < 0.001, top10
print("7 top10", top10)
# 8 equity / total NAV
tot = 3319020749.67 + 692647108.42
assert tot == 4011667858.09, tot
eq = 3386365286.03/tot*100
assert abs(eq - 84.41) < 0.01, eq
print("8 total NAV", tot, "equity pct", eq)
# 9 Q2 share net redemption
start = 1409910306.87 + 292317691.56
end = 1262525309.09 + 268673636.03
chg = (end/start-1)*100
assert abs(chg - (-10.05)) < 0.01, chg
print("9 shares start", start, "end", end, "chg pct", chg)
# 10 Q2+Q3 compound for A (Q3 +9.33% per Q3 report excerpts) and implied NAV
comp = (0.9014*1.0933-1)*100
assert abs(comp - (-1.45)) < 0.02, comp
nav = 2.6289*1.0933
assert abs(nav - 2.8742) < 0.001, nav
print("10 Q2+Q3 compound", comp, "implied Q3 A NAV", nav)
print("ALL PASSED 10 groups")
