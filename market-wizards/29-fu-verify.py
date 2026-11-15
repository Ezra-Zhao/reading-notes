#!/usr/bin/env python3
"""Verify arithmetic for note 29 (Fu Pengbo). All inputs are from public
sources cited in the note: Ruiyuan Growth Value 2026 Q2 report (official
PDF), 2026 interim report, The Paper/Wind Q3 summary, Sina/Tiantian Oct 15
snapshot, Ruiyuan capital-increase announcement 2026-02-10."""
from datetime import date

def close(a, b, tol=0.02):
    return abs(a - b) <= tol

# 1. Q2-end shares: A + C = total
a_sh, c_sh, tot_sh = 7262752709.40, 698206850.80, 7960959560.20
assert close(a_sh + c_sh, tot_sh, 0.01), a_sh + c_sh
print("1 shares sum OK", a_sh + c_sh)

# 2. Q2-end net assets: A + C = 222.01 yi (news base for Q3)
a_na, c_na = 20305061781.14, 1896099853.64
total_yi = (a_na + c_na) / 1e8
assert close(total_yi, 222.01, 0.01), total_yi
print("2 assets sum OK (yi)", round(total_yi, 4))

# 3. Q3-end assets 157.19 yi vs Q2 222.01 yi
chg = 157.19 / 222.01 - 1
assert close(chg * 100, -29.20, 0.05), chg
assert close(222.01 - 157.19, 64.82, 0.01)
print("3 Q3 asset change OK", round(chg * 100, 2), "% shrink 64.82 yi")

# 4. Past-5y +29.14% with past-1y +115.81% implies prior ~4y negative
prior = 1.2914 / 2.1581 - 1
assert close(prior * 100, -40.16, 0.05), prior
print("4 implied prior-period OK", round(prior * 100, 2), "%")

# 5. Outperformance diffs from Q2 report table (A)
assert close(45.79 - 4.72, 41.07, 0.001)
assert close(179.58 - 30.50, 149.08, 0.001)
assert close(115.81 - 15.71, 100.10, 0.001)
print("5 diffs OK 41.07 / 149.08 / 100.10 pp")

# 6. Q2 top-10 concentration (percent of NAV, from Q2 report 5.3)
top10 = [9.73, 8.76, 8.57, 8.51, 7.44, 7.22, 7.08, 5.78, 3.71, 3.06]
assert close(sum(top10), 69.86, 0.01), sum(top10)
print("6 top10 concentration OK", round(sum(top10), 2), "%")

# 7. Q2 A-share flows: subscriptions - redemptions, net rate vs start
start, subs, red = 8604199462.52, 719061979.60, 2060508732.72
net = subs - red
assert close(start + net, a_sh, 0.01)
assert close(net / start * 100, -15.59, 0.02), net / start
print("7 A net flow OK", net, round(net / start * 100, 2), "%")

# 8. Q3 holding increases (wan shares, Q2 report / Wind via news)
zj = 118.69 / 64.78 - 1
gz = 223.48 / 46.61 - 1
lx = 55.50 / 25.86 - 1
assert close(zj * 100, 83.22, 0.05), zj
assert close(gz * 100, 379.42, 0.1), gz
assert close(lx * 100, 114.62, 0.05), lx
print("8 Q3 increases OK", round(zj*100,2), round(gz*100,2), round(lx*100,2))

# 9. Fu stake in Ruiyuan (2026-02-10 capital increase announcement)
stake = 12000000 / 104950000 * 100
assert close(stake, 11.4340, 0.001), stake
print("9 Fu stake OK", round(stake, 4), "%")

# 10. Tenure length + NAV factor identity
d = (date(2026, 6, 30) - date(2019, 3, 26)).days
assert d == 2653, d
assert close(1 + 179.58 / 100, 2.7958, 1e-9)  # NAV A at Q2 end
d2 = (date(2026, 9, 30) - date(2019, 3, 26)).days
assert d2 == 2745, d2
print("10 days OK", d, d2, "NAV factor identity OK")

# 11. Implied fall from 2026-06-30 to 2026-10-15 (Sina inception +76.22%)
fall = 1.7622 / 2.7958 - 1
assert close(fall * 100, -36.97, 0.05), fall
print("11 implied Jun30-Oct15 change OK", round(fall * 100, 2), "%")

# 12. Stock position change Q2 -> Q3
assert close(91.17 - 88.73, 2.44, 0.001)
print("12 position change OK +2.44 pp")

print("ALL 12 ASSERTION GROUPS PASSED")
