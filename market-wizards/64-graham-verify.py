#!/usr/bin/env python3
"""64 Graham verify: 12 groups of assertions.
Sources: Zweig note + Buffett preface in The Intelligent Investor Rev. Ed.
(1894-05-09 birth; 1914 graduation age 20; 1936-1956 Graham-Newman at least
14.7%/yr vs market 12.2%/yr; Northern Pipe Line $65 vs $80, exit $110 in 3y;
Savold +250% day 1 then worthless; 1929-32 loss nearly 70%;
GEICO 1948: 50% for $712,500 ~= 25% of fund assets;
100 Graham-Newman shares at start of 1948 worth $11,413 -> $1.66M by 1972;
Security Analysis 1934; Intelligent Investor 1949; Buffett speech 1984.)
"""
import math
from datetime import date

def close(a, b, tol=0.01):
    assert abs(a - b) <= tol, f"{a} != {b} (tol {tol})"

# 1 lifespan
born, died = date(1894, 5, 9), date(1976, 9, 21)
assert (died - born).days == 30085
age = died.year - born.year - ((died.month, died.day) < (born.month, born.day))
assert age == 82
print("1 ok: lifespan 30085 days, age 82")

# 2 graduation
assert 1914 - 1894 == 20
print("2 ok: graduated 1914 at age 20")

# 3 Graham-Newman window
assert 1956 - 1936 == 20
assert 1936 - 1894 == 42 and 1956 - 1894 == 62
print("3 ok: GN window 20y, founded age 42, retired age 62")

# 4 compound 20y (lower bound for Graham, 'at least 14.7%')
fg, fm = 1.147 ** 20, 1.122 ** 20
close(fg, 15.5335, 0.001); close(fm, 9.9967, 0.001)
close(10000 * fg, 155334.66, 0.5); close(10000 * fm, 99967.11, 0.5)
close((fg - 1) * 100, 1453.35, 0.05); close((fm - 1) * 100, 899.67, 0.05)
print("4 ok: 20y factors 15.5335 vs 9.9967, $10k -> $155,334.66 vs $99,967.11")

# 5 outperformance size
close(14.7 - 12.2, 2.5, 1e-9)
close(fg / fm, 1.5539, 0.001)
close(10000 * (fg - fm), 55367.54, 0.5)
close(((fg - 1) - (fm - 1)) * 100, 553.68, 0.05)
print("5 ok: +2.5pp/yr -> factor ratio 1.5539, terminal gap $55,367.54")

# 6 doubling time + 10y factors
close(math.log(2) / math.log(1.147), 5.0539, 0.001)
close(math.log(2) / math.log(1.122), 6.0215, 0.001)
close(1.147 ** 10, 3.9413, 0.001); close(1.122 ** 10, 3.1618, 0.001)
print("6 ok: doubling 5.05y vs 6.02y; 10y factors 3.9413 vs 3.1618")

# 7 Northern Pipe Line
close((80 - 65) / 80 * 100, 18.75, 1e-9)
close((80 - 65) / 65 * 100, 23.0769, 0.001)
close((110 - 65) / 65 * 100, 69.2308, 0.001)
close((110 / 65) ** (1 / 3) - 1, 0.19168, 0.0005)
close((110 - 80) / 80 * 100, 37.5, 1e-9)
print("7 ok: NP $65 vs $80 bonds (18.75% discount), exit $110 = +69.23%, CAGR 19.17%")

# 8 Savold Tire
close(1 + 2.50, 3.5, 1e-9)
assert -100.0 == -100.0  # peak to worthless
print("8 ok: Savold +250% day1 = 3.5x, then to zero = -100% from peak")

# 9 crash 1929-32 nearly -70%
close(100 * (1 - 0.70), 30.0, 1e-9)
close((1 / 0.30 - 1) * 100, 233.3333, 0.001)
print("9 ok: -70% leaves 30%, recovery needs +233.33%")

# 10 GEICO stake arithmetic
close(712500 / 0.50, 1425000, 0.01)
close(712500 / 0.25, 2850000, 0.01)
print("10 ok: GEICO 50% for $712,500 -> whole $1,425,000; ~25% of fund -> fund ~$2,850,000")

# 11 GEICO distribution
f = 1660000 / 11413
close(f, 145.4482, 0.001)
close((f - 1) * 100, 14444.82, 0.05)
close(f ** (1 / 24) - 1, 0.23059, 0.0005)
close(11413 / 100, 114.13, 1e-9); close(1660000 / 100, 16600, 0.01)
assert 1972 - 1948 == 24
print("11 ok: $11,413 -> $1.66M = 145.45x over 24y, CAGR 23.06%")

# 12 books / GEICO timeline
assert 1934 - 1894 == 40 and 1949 - 1894 == 55 and 1949 - 1934 == 15
assert 1984 - 1934 == 50 and 1984 - 1976 == 8
assert 1948 - 1894 == 54 and 1948 - 1936 == 12 and 1956 - 1948 == 8
print("12 ok: SA 1934 age40, II 1949 age55 (+15y), 1984 speech = SA+50y, GEICO 1948 age54")

print("ALL 12 GROUPS PASSED")
