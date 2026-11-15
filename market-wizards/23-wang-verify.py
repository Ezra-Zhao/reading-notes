# -*- coding: utf-8 -*-
"""23 Wang Yawei verification: arithmetic checks only, sources in note."""
from datetime import date

def approx(a,b,tol=0.02): return abs(a-b) <= tol

# 1 cumulative NAV: start 1.001 to 11.472
growth = 11.472/1.001 - 1
assert approx(growth*100, 1046.05, 0.05), growth
print(f"1 cumulative unit NAV growth {growth*100:.2f}% == 1046.05% OK; multiple {11.472/1.001:.4f}x")

# 2 adjusted NAV growth 1198.91% and benchmark 132.78%
assert approx(1+1198.91/100, 12.9891, 1e-9)
assert approx(1+132.78/100, 2.3278, 1e-9)
ratio = 12.9891/2.3278
print(f"2 adjusted multiple 12.9891x, benchmark 2.3278x, terminal ratio {ratio:.2f}x OK")

# 3 yearly chain 2006-2009
chain = (1+1.5449)*(1+2.2624)*(1-0.3488)*(1+1.1619)
print(f"3 2006-2009 chain multiple {chain:.3f}x (growth {(chain-1)*100:.1f}%)")
assert 11.0 < chain < 12.0

# 4 2007 gaps
sse07 = 226.24-129.58
assert approx(sse07, 96.66, 0.01)
second = 226.24-35.0
print(f"4 2007 SSE implied {sse07:.2f}%, second place implied {second:.2f}% OK")

# 5 2008: SSE drop from points, gap to first
drop = 1820.81/5265.01-1
print(f"5 2008 SSE point drop {drop*100:.2f}% (text 65.39%, rounding diff {abs(drop*100+65.39):.2f}pp); gap to first {-32.28-(-34.88):.2f}pp")
assert approx(-32.28-(-34.88), 2.60, 0.01)

# 6 early funds outperformance
assert approx(90.48-18.79, 71.69, 0.01)
assert approx(13.22-(-28.5), 41.72, 0.01)
print("6 Xinghua adjusted excess 71.69pp; Huaxia Growth excess 41.72pp OK")

# 7 tenure and age
days = (date(2012,5,4)-date(2005,12,31)).days
age = 2012-1971 - ((5,4) < (9,11))
print(f"7 Large Cap tenure {days} days = {days/365.25:.2f} years; age at resignation {age}")
assert days == 2316 and age == 40

# 8 2010 ranks context: large cap 24.24 vs strategy 29.50 diff
assert approx(29.50-24.24, 5.26, 0.01)
print("8 2010 strategy-large cap gap 5.26pp OK")
print("ALL 8 ASSERTION GROUPS PASSED")
