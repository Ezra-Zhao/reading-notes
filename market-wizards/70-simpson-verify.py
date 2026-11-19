#!/usr/bin/env python3
"""70 Simpson verify: Berkshire Hathaway 2004 annual report, Portrait of a
Disciplined Investor table (GEICO equities vs S&P, 1980-2004)."""
from decimal import Decimal

G = [Decimal(x) for x in ("23.7","5.4","45.8","36.0","21.8","45.8","38.7","-10.0","30.0","36.1",
                           "-9.9","56.5","10.8","4.6","13.4","39.8","29.2","24.6","18.6","7.2",
                           "20.9","5.2","-8.1","38.3","16.9")]
S = [Decimal(x) for x in ("32.3","-5.0","21.4","22.4","6.1","31.6","18.6","5.1","16.6","31.7",
                           "-3.1","30.5","7.6","10.1","1.3","37.6","23.0","33.4","28.6","21.0",
                           "-9.1","-11.9","-22.1","28.7","10.9")]
REL = [Decimal(x) for x in ("-8.6","10.4","24.4","13.6","15.7","14.2","20.1","-15.1","13.4","4.4",
                             "-6.8","26.0","3.2","-5.5","12.1","2.2","6.2","-8.8","-10.0","-13.8",
                             "30.0","17.1","14.0","9.6","6.0")]
Y = list(range(1980, 2005))

def cum(xs):
    f = Decimal(1)
    for v in xs: f *= 1 + v / 100
    return f

def approx(a, b, tol):
    return abs(a - b) <= Decimal(str(tol))

# 1: 25 rows, relative column is exactly GEICO minus S&P every year
assert len(G) == len(S) == 25
assert all(G[i] - S[i] == REL[i] for i in range(25))

# 2: yearly compounding reproduces the table's average annual gains
cg, cs = cum(G), cum(S)
assert approx((cg - 1) * 100, Decimal("10060.55"), "0.05")
assert approx((cs - 1) * 100, Decimal("2269.53"), "0.05")
assert approx(((float(cg) ** (1/25)) - 1) * 100, 20.30, 0.01)
assert approx(((float(cs) ** (1/25)) - 1) * 100, 13.50, 0.01)

# 3: terminal values for $10,000 and their ratio
tg, ts = 10000 * float(cg), 10000 * float(cs)
assert approx(tg, 1016054.68, 1.0) and approx(ts, 236953.40, 1.0)
assert approx(tg / ts, 4.29, 0.01)

# 4: arithmetic averages and volatility drag
ag, as_ = float(sum(G)) / 25, float(sum(S)) / 25
assert approx(ag, 21.65, 0.01) and approx(as_, 14.69, 0.01)
assert approx(ag - 20.30, 1.35, 0.01) and approx(as_ - 13.50, 1.19, 0.01)

# 5: win/lose count vs S&P and relative extremes
wins = sum(1 for i in range(25) if REL[i] > 0)
assert wins == 18 and 25 - wins == 7
assert max(REL) == Decimal("30.0") and Y[REL.index(max(REL))] == 2000
assert min(REL) == Decimal("-15.1") and Y[REL.index(min(REL))] == 1987

# 6: negative years: GEICO 3 (worst -10.0), S&P 5 (worst -22.1)
neg_g = [(Y[i], G[i]) for i in range(25) if G[i] < 0]
neg_s = [(Y[i], S[i]) for i in range(25) if S[i] < 0]
assert neg_g == [(1987, Decimal("-10.0")), (1990, Decimal("-9.9")), (2002, Decimal("-8.1"))]
assert len(neg_s) == 5 and min(S) == Decimal("-22.1")
assert approx(100 * (1 / 0.90 - 1), 11.11, 0.01)  # recovery from -10.0%

# 7: no two consecutive GEICO down years; worst consecutive pair is 2001-02 at -3.32%
pairs = [((float(cum(G[i:i+2])) - 1) * 100, Y[i]) for i in range(24)]
worst = min(pairs)
assert approx(worst[0], -3.32, 0.01) and worst[1] == 2001

# 8: 1980s split
assert approx((float(cum(G[:10])) - 1) * 100, 913.99, 0.05)
assert approx((float(cum(S[:10])) - 1) * 100, 399.14, 0.05)
assert approx(((float(cum(G[:10])) ** 0.1) - 1) * 100, 26.07, 0.01)
assert approx(((float(cum(S[:10])) ** 0.1) - 1) * 100, 17.44, 0.01)

# 9: 1990s split is essentially a tie (GEICO fractionally behind)
assert approx((float(cum(G[10:20])) - 1) * 100, 430.26, 0.05)
assert approx((float(cum(S[10:20])) - 1) * 100, 433.15, 0.05)
assert approx(((float(cum(G[10:20])) ** 0.1) - 1) * 100, 18.15, 0.01)
assert approx(((float(cum(S[10:20])) ** 0.1) - 1) * 100, 18.22, 0.01)

# 10: 2000-2004 split and the 2000-2002 bear-market trio
assert approx((float(cum(G[20:])) - 1) * 100, 88.97, 0.05)
assert approx((float(cum(S[20:])) - 1) * 100, -10.96, 0.05)
assert approx((float(cum(G[20:23])) - 1) * 100, 16.88, 0.05)
assert approx((float(cum(S[20:23])) - 1) * 100, -37.62, 0.05)

# 11: 1997-99 three straight relative losses while making +58.42%
assert all(REL[i] < 0 for i in (17, 18, 19))
assert approx((float(cum(G[17:20])) - 1) * 100, 58.42, 0.05)
assert approx((float(cum(S[17:20])) - 1) * 100, 107.58, 0.05)

# 12: longest relative win streak is 6 (1981-86); a $200-300m purchase is
# 8-12% of the ~$2.5bn portfolio the letter says he managed
streak = cur = 0
for r in REL:
    cur = cur + 1 if r > 0 else 0
    streak = max(streak, cur)
assert streak == 6
assert approx(200 / 2500 * 100, 8.0, 0.001) and approx(300 / 2500 * 100, 12.0, 0.001)

print("ALL 12 ASSERTION GROUPS PASS")
print(f"cum GEICO +{(float(cg)-1)*100:.2f}%  S&P +{(float(cs)-1)*100:.2f}%  "
      f"CAGR 20.30/13.50  $10k -> {tg:,.0f} vs {ts:,.0f}")
