from datetime import date
def pct(x): return round(x,2)
# 1 two-year boom and three-year check
boom = (1.7136*1.7252-1)*100
three = (1.7136*1.7252*0.8881-1)*100
assert abs(boom-195.61) < 0.05, boom
assert abs(three-162.56) < 0.05, three
print("1 boom", boom, "three", three)
# 2 2021 realized vs profit
gap = -3702167146.10 - 2770951953.07
assert gap == -6473119099.17, gap
print("2 gap", gap)
# 3 peak unit to 2026Q3
dd = (2.79/5.274-1)*100
rec = (5.274/2.79-1)*100
assert abs(dd - (-47.10)) < 0.02, dd
assert abs(rec - 89.03) < 0.02, rec
print("3 drawdown", dd, "recover", rec)
# 4 assets peak to now, shares 2021 to now
a_dd = (10108528770.35/34709674276.38-1)*100
s_dd = (3622644694.68/6629477557.41-1)*100
assert abs(a_dd - (-70.88)) < 0.02, a_dd
assert abs(s_dd - (-45.36)) < 0.02, s_dd
print("4 assets", a_dd, "shares", s_dd)
# 5 implied first five years of past ten
first5 = ((1+1.0440)/(1-0.3874)-1)*100
assert abs(first5-233.66) < 0.05, first5
print("5 first5", first5)
# 6 tenure
days = (date(2026,9,30)-date(2012,9,28)).days
assert days == 5115, days
yrs = days/365.25
print("6 days", days, "years", round(yrs,2))
# 7 concentration
top10 = 9.96+9.48+8.64+8.62+8.02+6.84+6.09+5.61+5.35+3.84
assert abs(top10-72.45) < 0.001, top10
print("7 top10", top10)
# 8 Q3 2026 fair value and share net
fv = 474792324.55-110072968.99
net = (3622644694.68-3651045943.73)/3651045943.73*100
assert fv == 364719355.56, fv
assert abs(net - (-0.78)) < 0.01, net
print("8 fv", fv, "net shares pct", net)
# 9 assets 2019->2020 growth
g = (34709674276.38/20529301497.74-1)*100
assert abs(g-69.07) < 0.02, g
print("9 assets growth 19-20", g)
# 10 unit 2021 end to 2026Q3
d2 = (2.79/4.684-1)*100
assert abs(d2 - (-40.44)) < 0.02, d2
print("10 unit 21-26", d2)
print("ALL PASSED 10 groups")
