# MW45 Zhao Feng verification - all figures from Ruiyuan Balanced Value 3Y Holding
# 2026 Q2 report (sent 2026-07-17) and 2026 interim report (sent 2026-08-27)
from datetime import date

# 1 tenure: first manager since contract inception 2020-02-21, still in post at 2026-06-30
days = (date(2026, 6, 30) - date(2020, 2, 21)).days
assert days == 2321
assert abs(days / 365 - 6.36) < 0.01
print("1 tenure 2,321 days = 6.36 years, no departure date in either report")

# 2 inception consistency: unit NAV equals cumulative growth (no distribution adjustment in prints)
assert abs((1.5765 - 1) * 100 - 57.65) < 0.01
assert abs((1.5467 - 1) * 100 - 54.67) < 0.01
assert abs(57.65 - 16.52 - 41.13) < 0.01  # A excess over benchmark, as printed
assert abs(54.67 - 16.52 - 38.15) < 0.01  # C excess over benchmark, as printed
ann = 1.5765 ** (365 / days) - 1
assert abs(ann * 100 - 7.42) < 0.01
print("2 A NAV 1.5765 = +57.65% since inception, excess +41.13pp, mechanical ann. +7.42%")

# 3 five-year window split: past 5y -9.91% with past 3y +22.52% implies the first two years
first2 = (1 - 0.0991) / (1 + 0.2252) - 1
assert abs(first2 * 100 - (-26.47)) < 0.01
prior2 = (1 + 0.2252) / (1 + 0.0993) - 1
assert abs(prior2 * 100 - 11.45) < 0.01
print("3 past-5y split: first 2y -26.47%, last 3y +22.52%; past-3y split: prior 2y +11.45%, last 1y +9.93%")

# 4 H1 2026 (interim report): realised gains vs bottom-line profit, A+C combined
realised = 1001258583.31 + 111514004.14
profit = -547389527.29 + -63274057.24
fv = profit - realised
assert abs(realised - 1112772587.45) < 0.01
assert abs(profit - (-610663584.53)) < 0.01
assert abs(fv - (-1723436171.98)) < 0.01
# Q2 alone (quarterly report): same split
r2 = 159643916.93 + 17584960.86
p2 = -245308533.14 + -29024577.52
assert abs((p2 - r2) - (-451561988.45)) < 0.01
print("4 H1 realised +1,112,772,587.45, profit -610,663,584.53, FV drag -1,723,436,171.98; Q2 FV drag -451,561,988.45")

# 5 Q2 2026 share flows: unlock redemptions vs near-zero subscriptions
open_total = 5027272214.30 + 582621476.02
end_total = 4131360269.03 + 483303197.68
assert abs(open_total - 5609893690.32) < 0.01 and abs(end_total - 4614663466.71) < 0.01
assert abs((end_total / open_total - 1) * 100 - (-17.74)) < 0.01
net_a = 922562685.55 - 26650740.28
assert abs(net_a - 895911945.27) < 0.01
assert abs(922562685.55 / 5027272214.30 * 100 - 18.35) < 0.01
subs_total = 26650740.28 + 2748996.94
assert abs(subs_total / open_total * 100 - 0.52) < 0.01
print("5 total shares -17.74% in Q2; A net redemption 895,911,945.27 (gross 18.35% of opening); subscriptions only 0.52%")

# 6 manager proprietary holding: unchanged all quarter, as printed 3.46% of A
mgr = 142856330.45
assert abs(mgr / 4131360269.03 * 100 - 3.46) < 0.01
assert abs(mgr * 1.5765 - 225213004.95) < 1.0
print("6 manager holds 142,856,330.45 A shares = 3.46%, worth about CNY 225.21m, zero buys/sells in Q2")

# 7 top-10 concentration at 2026-06-30 (percent of NAV, as printed)
top10 = [9.76, 9.30, 9.21, 9.08, 5.24, 4.93, 4.65, 3.90, 3.66, 3.18]
assert abs(sum(top10) - 62.91) < 0.01
assert abs(sum(top10[:4]) - 37.35) < 0.01
print("7 top-10 = 62.91% of NAV; top-4 alone = 37.35%")

# 8 asset mix: equities 89.31% of total assets; HK stocks 38.68% of NAV as printed
assert abs(6569797292.28 / 7356005104.39 * 100 - 89.31) < 0.01
nav_total = 6512912941.94 + 747536656.02
assert abs(2808541465.00 / nav_total * 100 - 38.68) < 0.01
assert abs(3761255827.28 / nav_total * 100 - 51.80) < 0.01
print("8 equities 89.31% of assets; HK 38.68% + domestic 51.80% = 90.48% of NAV in stocks")

# 9 insurance round trip in his own Q2 text: sold near PB 1.2x in early Q1, bought back below 0.8x in Q2
assert abs((0.8 / 1.2 - 1) * 100 - (-33.33)) < 0.01
print("9 buyback PB level at most 66.67% of the sell level, i.e. at least 33.33% lower")

# 10 Q2 and H1 gaps vs benchmark, as printed
assert abs(-4.09 - 3.71 - (-7.80)) < 0.01
assert abs(-7.61 - 0.17 - (-7.78)) < 0.01
print("10 Q2 A -4.09% vs benchmark +3.71% = -7.80pp; H1 A -7.61% vs +0.17% = -7.78pp")

print("ALL PASSED 10 groups")
