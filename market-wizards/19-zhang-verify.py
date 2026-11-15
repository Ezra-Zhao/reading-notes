#!/usr/bin/env python3
"""Self-written verification for note 19 (Zhang Kun). All inputs are
public figures taken from 2026 Q3 fund-report coverage (Cailianshe /
The Paper via 21jingji, Sina Fund, 10jqka/Wind tables)."""
from datetime import date

# 1. Q3 2026 AUM sum: 189.33 + 66.84 + 36.90 = 293.07 (100m CNY)
total = 189.33 + 66.84 + 36.90
assert abs(total - 293.07) < 0.01, total

# 2. Decline from mid-2021 peak 1344.78 to 293.07
peak, now = 1344.78, 293.07
drop = peak - now
assert abs(drop - 1051.71) < 0.01, drop
assert abs(drop / peak * 100 - 78.21) < 0.05, drop / peak * 100
assert abs(now / peak * 100 - 21.79) < 0.05

# 3. Blue-chip fund shrinkage Q2->Q3: 204.16 -> 189.33
assert abs((204.16 - 189.33) - 14.83) < 0.01
assert abs((189.33 - 204.16) / 204.16 * 100 + 7.26) < 0.05

# 4. Tenure lengths
d1 = (date(2026, 9, 30) - date(2018, 9, 5)).days  # blue chip, since inception
assert d1 == 2947, d1
y1 = d1 / 365.25
assert abs(y1 - 8.07) < 0.02, y1
d2 = (date(2026, 9, 30) - date(2014, 4, 8)).days  # Asia select
assert d2 == 4558, d2
y2 = d2 / 365.25
assert abs(y2 - 12.48) < 0.02, y2
d3 = (date(2026, 9, 30) - date(2012, 9, 28)).days  # first fund (110011 lineage)
assert d3 == 5115, d3

# 5. Tenure returns -> multiples and mechanical annualised (illustrative)
m_blue = 1 + 38.06 / 100
assert abs(m_blue - 1.3806) < 1e-9
ann_blue = m_blue ** (1 / y1) - 1
assert abs(ann_blue * 100 - 4.07) < 0.15, ann_blue * 100
m_asia = 1 + 100.26 / 100
assert abs(m_asia - 2.0026) < 1e-9
ann_asia = m_asia ** (1 / y2) - 1
assert abs(ann_asia * 100 - 5.72) < 0.15, ann_asia * 100

# 6. Q3 position changes imply Q2 share counts
xin_yi_sheng_q2 = 113.21 / (1 + 1.7621)  # +176.21%
assert abs(xin_yi_sheng_q2 - 41.0) < 0.1, xin_yi_sheng_q2
chuan_tou_q2 = 2902.49 / (1 + 0.2094)  # +20.94%
assert abs(chuan_tou_q2 - 2400.0) < 1.0, chuan_tou_q2
moutai_chg = (95.85 - 96.85) / 96.85 * 100  # blue-chip Moutai shares
assert abs(moutai_chg + 1.03) < 0.02, moutai_chg

# 7. Solo-managed share of AUM and equity-position lifts
assert abs(36.90 / 293.07 * 100 - 12.59) < 0.05
assert abs((86.55 - 75.00) - 11.55) < 0.01   # blue chip equity pp lift
assert abs((92.11 - 78.97) - 13.14) < 0.01   # Asia select equity pp lift
# Q3 excess returns
assert abs((-4.58) - (-4.02) + 0.56) < 1e-9  # blue chip vs benchmark
assert abs((-2.32) - (-2.42) - 0.10) < 1e-9  # Asia select vs benchmark

print("19-zhang-verify: 7 assertion groups passed")
print(f" blue-chip tenure {d1}d/{y1:.2f}y ann~{ann_blue*100:.2f}% | asia {d2}d/{y2:.2f}y ann~{ann_asia*100:.2f}%")
print(f" peak decline {drop:.2f} = {drop/peak*100:.2f}% | solo share {36.90/293.07*100:.2f}%")
