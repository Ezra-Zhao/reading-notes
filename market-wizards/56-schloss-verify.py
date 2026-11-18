#!/usr/bin/env python3
"""Verify arithmetic in note 56 (Walter J. Schloss / WJS Partnership).

All yearly inputs are figures printed in Table 1 of Buffett (1984),
"The Superinvestors of Graham-and-Doddsville", Hermes, Fall 1984,
p.6, as reproduced in Siddiquee's Schloss study (Table 1, source
line: Buffett 1984, p.6): columns are S&P overall gain incl.
dividends, WJS Limited Partners overall gain, WJS Partnership
overall gain, for 1956-1983 plus 1984 Q1. Stated 28.25-year totals:
S&P +887.2% at 8.4%/yr, LP +6,678.8% at 16.1%/yr, Partnership
+23,104.7% at 21.3%/yr. This script only checks internal arithmetic
consistency and derived windows. Clean-room, self-written.
"""

from datetime import date
from math import prod

ok = True

def check(name, cond):
    global ok
    print(("PASS" if cond else "FAIL"), name)
    ok = ok and cond

# Yearly rows: (S&P, LP, Partnership) in percent
rows = {
    1956: (7.5, 5.1, 6.8), 1957: (-10.5, -4.7, -4.7),
    1958: (42.1, 42.1, 54.6), 1959: (12.7, 17.5, 23.3),
    1960: (-1.6, 7.0, 9.3), 1961: (26.4, 21.6, 28.8),
    1962: (-10.2, 8.3, 11.1), 1963: (23.3, 15.1, 20.1),
    1964: (16.5, 17.1, 22.8), 1965: (13.1, 26.8, 35.7),
    1966: (-10.4, 0.5, 0.7), 1967: (26.8, 25.8, 34.4),
    1968: (10.6, 26.6, 35.5), 1969: (-7.5, -9.0, -9.0),
    1970: (2.4, -8.2, -8.2), 1971: (14.9, 25.5, 28.3),
    1972: (19.8, 11.6, 15.5), 1973: (-14.8, -8.0, -8.0),
    1974: (-26.6, -6.2, -6.2), 1975: (36.9, 42.7, 52.2),
    1976: (22.4, 29.4, 39.2), 1977: (-8.6, 25.8, 34.4),
    1978: (7.0, 36.6, 48.8), 1979: (17.6, 29.8, 39.7),
    1980: (32.1, 23.3, 31.1), 1981: (-6.7, 18.4, 24.5),
    1982: (20.2, 24.1, 32.1), 1983: (22.8, 38.4, 51.2),
}
q1_1984 = (-2.3, 0.8, 1.1)

def compound(vals):
    return prod(1 + v / 100 for v in vals)

sp = [r[0] for r in rows.values()] + [q1_1984[0]]
lp = [r[1] for r in rows.values()] + [q1_1984[1]]
pp = [r[2] for r in rows.values()] + [q1_1984[2]]

# 1. Life dates: born 1916-08-28, died 2012-02-19, age 95;
#    left Graham-Newman in 1955 at 38/39; table starts 1956.
age_days = (date(2012, 2, 19) - date(1916, 8, 28)).days
check("1 age at death 95", 95 * 365 < age_days < 96 * 365 and date(2012, 2, 19).year - 1916 - 1 == 95)
check("1 left Graham-Newman 1955, aged 38-39", 1955 - 1916 == 39)

# 2. Compounding the printed yearly rows reproduces the stated
#    28.25-year gains within rounding of one-decimal yearly inputs.
check("2 S&P compound ~+887.2%", abs((compound(sp) - 1) * 100 - 887.2) < 15)
check("2 LP compound ~+6678.8%", abs((compound(lp) - 1) * 100 - 6678.8) < 120)
check("2 Partnership compound ~+23104.7%", abs((compound(pp) - 1) * 100 - 23104.7) < 500)
print("   compounded:", [round((compound(c) - 1) * 100, 1) for c in (sp, lp, pp)])

# 3. Stated annual rates are consistent with stated totals over
#    28.25 years (geometric check, tolerance 0.15pp).
for total, rate in [(887.2, 8.4), (6678.8, 16.1), (23104.7, 21.3)]:
    implied = ((1 + total / 100) ** (1 / 28.25) - 1) * 100
    check(f"3 total {total}% implies ~{rate}%/yr", abs(implied - rate) < 0.15)

# 4. $10,000 endpoints from stated totals; LP keeps only ~29.21%
#    of the Partnership endpoint; S&P endpoint is ~4.25% of it.
check("4 endpoints 2320470/677880/98720",
      abs(10000 * (1 + 23104.7 / 100) - 2320470) < 1 and abs(10000 * (1 + 6678.8 / 100) - 677880) < 1 and abs(10000 * (1 + 887.2 / 100) - 98720) < 1)
check("4 LP endpoint share ~29.21%", abs(677880 / 2320470 * 100 - 29.21) < 0.01)
check("4 Partnership/LP multiple ~3.42x", abs(2320470 / 677880 - 3.42) < 0.01)
check("4 Partnership/S&P multiple ~23.51x", abs(2320470 / 98720 - 23.51) < 0.01)

# 5. Fee drag in annual-rate terms: 21.3 - 16.1 = 5.2pp; LP still
#    beats S&P by 7.7pp a year; Partnership beats S&P by 12.9pp.
check("5 fee drag 5.2pp, LP edge 7.7pp, gross edge 12.9pp",
      abs(21.3 - 16.1 - 5.2) < 1e-9 and abs(16.1 - 8.4 - 7.7) < 1e-9 and abs(21.3 - 8.4 - 12.9) < 1e-9)

# 6. Negative periods: Partnership loses in 5 of 29 periods
#    (1957, 1969, 1970, 1973, 1974); S&P loses in 10 of 29.
neg_pp = [y for y, r in rows.items() if r[2] < 0]
neg_sp = [y for y, r in rows.items() if r[0] < 0] + [1984]
check("6 partnership negative years = 5", neg_pp == [1957, 1969, 1970, 1973, 1974])
check("6 partnership negative share ~17.24%", abs(len(neg_pp) / 29 * 100 - 17.24) < 0.01)
check("6 S&P negative periods = 10", len(neg_sp) == 10)
check("6 S&P negative share ~34.48%", abs(len(neg_sp) / 29 * 100 - 34.48) < 0.01)

# 7. Worst single years: Partnership -9.0% (1969) vs S&P -26.6%
#    (1974); the S&P worst is about 2.96x deeper.
check("7 worst partnership -9.0, worst S&P -26.6", min(pp) == -9.0 and min(sp) == -26.6)
check("7 depth ratio ~2.96x", abs(26.6 / 9.0 - 2.96) < 0.01)

# 8. The 1973-74 bear market: Partnership compounds to -13.70%
#    (needs +15.88% to recover) vs S&P -37.46% (needs +59.91%).
bear_pp = (1 - 0.08) * (1 - 0.062) - 1
bear_sp = (1 - 0.148) * (1 - 0.266) - 1
check("8 1973-74 partnership ~-13.70%", abs(bear_pp * 100 + 13.70) < 0.01)
check("8 1973-74 S&P ~-37.46%", abs(bear_sp * 100 + 37.46) < 0.01)
check("8 recovery needs ~15.88% vs ~59.91%",
      abs((1 / (1 + bear_pp) - 1) * 100 - 15.88) < 0.01 and abs((1 / (1 + bear_sp) - 1) * 100 - 59.91) < 0.01)

# 9. 1969-70 back-to-back: Partnership -16.46% over two years;
#    and the full 1969-75 path still ends +62.59% over 1968.
two = 0.91 * 0.918 - 1
check("9 1969-70 partnership ~-16.46%", abs(two * 100 + 16.46) < 0.01)
check("9 1969-75 full path ~+62.59% over 1968 level", abs((0.91 * 0.918 * 1.283 * 1.155 * 0.92 * 0.938 * 1.522 - 1) * 100 - 62.59) < 0.02)

# 10. Head-to-head years: Partnership beats S&P in 20 of the 28
#     full years 1956-1983; arithmetic means are ~23.00% (PP),
#     ~17.25% (LP), ~9.94% (S&P) for the full years, each above
#     its geometric rate (volatility drag).
wins = sum(1 for r in rows.values() if r[2] > r[0])
check("10 partnership beats S&P in 22 of 28 full years", wins == 22)
check("10 win share ~78.57%", abs(wins / 28 * 100 - 78.57) < 0.01)
import statistics
check("10 arithmetic means ~23.00/17.25/9.94",
      abs(statistics.mean([r[2] for r in rows.values()]) - 23.00) < 0.02
      and abs(statistics.mean([r[1] for r in rows.values()]) - 17.25) < 0.02
      and abs(statistics.mean([r[0] for r in rows.values()]) - 9.94) < 0.02)

# 11. The closing run: 1975-1983 is nine straight positive
#     Partnership years compounding to about 19.30x (+1,829.65%);
#     no negative Partnership year after 1974 in the table.
run = [rows[y][2] for y in range(1975, 1984)]
check("11 1975-83 all positive, compound ~19.30x", all(v > 0 for v in run) and abs(compound(run) - 19.30) < 0.02)
check("11 no partnership loss after 1974 (incl 1984Q1)", all(rows[y][2] > 0 for y in range(1975, 1984)) and q1_1984[2] > 0)

# 12. Scale arithmetic from the table's footnote: over 800 issues
#     owned across the history, at least 100 positions at most
#     times, about $45M under management -> an average position
#     at 100 holdings is about $450,000, i.e. about 1.00% each.
check("12 avg position at 100 holdings = $450k = 1.00%",
      45_000_000 / 100 == 450_000 and abs(450_000 / 45_000_000 * 100 - 1.00) < 1e-9)
check("12 800 issues over 28.25y ~28.3 new issues/yr", abs(800 / 28.25 - 28.32) < 0.01)

print("ALL PASSED" if ok else "SOME FAILED")
