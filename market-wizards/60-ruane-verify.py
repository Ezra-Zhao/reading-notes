#!/usr/bin/env python3
"""Verify arithmetic in note 60 (Bill Ruane / Sequoia Fund).

All performance inputs are figures printed in Table 4 of Buffett
(1984), "The Superinvestors of Graham-and-Doddsville", Hermes,
Fall 1984, as reproduced in the appendixes of The Intelligent
Investor (4th revised edition): columns are Sequoia Fund, Inc.
annual percentage change and S&P 500 Index, for the stub period
from 1970-07-15, calendar 1971-1983, and 1984 Q1. Stated totals:
entire period Sequoia +775.3% at 17.2%/yr compound, S&P +270.0%
at 10.0%/yr; gross investment return 18.2% after adding back the
1% management fee. Identity dates are from public biographical
records (born 1925-10-24, died 2005-10-04) and the fund's SEC
shareholder report (shares first offered 1970-07-15). This script
only checks internal arithmetic consistency and derived windows.
Clean-room, self-written.
"""

from datetime import date
from math import prod

ok = True

def check(name, cond):
    global ok
    print(("PASS" if cond else "FAIL"), name)
    ok = ok and cond

# Rows: (label, Sequoia %, S&P 500 %)
rows = [
    ("1970-stub", 12.1, 20.6), ("1971", 13.5, 14.3),
    ("1972", 3.7, 18.9), ("1973", -24.0, -14.8),
    ("1974", -15.7, -26.4), ("1975", 60.5, 37.2),
    ("1976", 72.3, 23.6), ("1977", 19.9, -7.4),
    ("1978", 23.9, 6.4), ("1979", 12.1, 18.2),
    ("1980", 12.6, 32.3), ("1981", 21.5, -5.0),
    ("1982", 31.2, 21.4), ("1983", 27.3, 22.4),
    ("1984Q1", -1.6, -2.4),
]
seq = [r[1] for r in rows]
sp = [r[2] for r in rows]

def compound(vals):
    return prod(1 + v / 100 for v in vals)

# 1. Life and launch dates: born 1925-10-24, died 2005-10-04 at
#    79, twenty days short of his 80th birthday; Sequoia shares
#    were first offered 1970-07-15, when he was 44 (16,335 days).
check("1 died aged 79, 20 days before 80th birthday",
      (date(2005, 10, 4) - date(1925, 10, 24)).days == 29200
      and (date(2005, 10, 24) - date(2005, 10, 4)).days == 20)
check("1 age at fund launch 16335 days ~44.72y",
      (date(1970, 7, 15) - date(1925, 10, 24)).days == 16335
      and abs(16335 / 365.25 - 44.72) < 0.01)

# 2. Table shape: 15 rows (1970 stub + 13 full years + 1984 Q1);
#    the window 1970-07-15 to 1984-03-31 is 5,008 days, about
#    13.71 years.
days = (date(1984, 3, 31) - date(1970, 7, 15)).days
check("2 15 rows in table", len(rows) == 15)
check("2 window 5008 days ~13.71y",
      days == 5008 and abs(days / 365.25 - 13.71) < 0.01)

# 3. Compounding all 15 printed rows reproduces the stated entire
#    period totals within one-decimal rounding: Sequoia +775.3%,
#    S&P +270.0%.
check("3 Sequoia compound ~+775.3%",
      abs((compound(seq) - 1) * 100 - 775.3) < 0.05)
print("   Sequoia compounded:", round((compound(seq) - 1) * 100, 2))
check("3 S&P compound ~+270.0%",
      abs((compound(sp) - 1) * 100 - 270.0) < 0.05)
print("   S&P compounded:", round((compound(sp) - 1) * 100, 2))

# 4. Endpoints on USD 10,000 from the stated totals: Sequoia
#    USD 87,530 against S&P USD 37,000, a ratio of about 2.37x.
check("4 endpoints 87530 / 37000",
      abs(10000 * (1 + 775.3 / 100) - 87530) < 1
      and abs(10000 * (1 + 270.0 / 100) - 37000) < 1)
check("4 endpoint ratio ~2.37x", abs(87530 / 37000 - 2.37) < 0.01)

# 5. Stated compound rates: 17.2% against 10.0% is a 7.2pp gap;
#    the gross line 18.2% is exactly the net line plus the stated
#    1.0% fee; Buffett's bar for Ruane was +4pp a year, so the
#    delivered gap is 1.80x the bar.
check("5 net gap 7.2pp", abs(17.2 - 10.0 - 7.2) < 1e-9)
check("5 gross = net + 1.0 fee", abs(18.2 - 17.2 - 1.0) < 1e-9)
check("5 delivered gap is 1.80x the 4pp bar", abs(7.2 / 4.0 - 1.80) < 1e-9)

# 6. The first four rows all lag the index: yearly gaps are
#    -8.5, -0.8, -15.2 and -9.2pp. Cumulatively over those rows
#    Sequoia gained only about +0.28% while the S&P gained
#    about +39.64%.
gaps4 = [a - b for a, b in zip(seq[:4], sp[:4])]
check("6 first four gaps all negative",
      all(g < 0 for g in gaps4)
      and abs(gaps4[0] + 8.5) < 0.01 and abs(gaps4[2] + 15.2) < 0.01)
check("6 first-four cumulative ~+0.28% vs ~+39.64%",
      abs((compound(seq[:4]) - 1) * 100 - 0.28) < 0.01
      and abs((compound(sp[:4]) - 1) * 100 - 39.64) < 0.01)

# 7. After five rows (through 1974) the fund was still under
#    water: about -15.47% cumulatively, while the S&P was about
#    +2.78%. The celebrated record began below zero.
check("7 first-five cumulative ~-15.47% vs ~+2.78%",
      abs((compound(seq[:5]) - 1) * 100 + 15.47) < 0.01
      and abs((compound(sp[:5]) - 1) * 100 - 2.78) < 0.01)

# 8. The 1973-74 drawdown: Sequoia compounded about -35.93%,
#    slightly shallower than the S&P at about -37.29%; breaking
#    even needed about +56.08% against +59.47%.
check("8 1973-74 drawdown ~-35.93% vs ~-37.29%",
      abs((compound(seq[3:5]) - 1) * 100 + 35.93) < 0.01
      and abs((compound(sp[3:5]) - 1) * 100 + 37.29) < 0.01)
check("8 recovery needs ~+56.08% vs ~+59.47%",
      abs((1 / compound(seq[3:5]) - 1) * 100 - 56.08) < 0.01
      and abs((1 / compound(sp[3:5]) - 1) * 100 - 59.47) < 0.01)

# 9. The 1975-76 rebound: two years compounded about +176.54%
#    for Sequoia against about +69.58% for the S&P.
check("9 1975-76 rebound ~+176.54% vs ~+69.58%",
      abs((compound(seq[5:7]) - 1) * 100 - 176.54) < 0.01
      and abs((compound(sp[5:7]) - 1) * 100 - 69.58) < 0.01)

# 10. The nine full years 1975-1983 were all positive for
#     Sequoia and compounded to about +952.28% (a 10.52x
#     multiple): the whole legend sits in this stretch.
check("10 1975-83 all nine years positive",
      all(v > 0 for v in seq[5:14]))
check("10 1975-83 compound ~+952.28%",
      abs((compound(seq[5:14]) - 1) * 100 - 952.28) < 0.05)
print("   1975-83 factor:", round(compound(seq[5:14]), 4))

# 11. Scoreboard over all 15 rows: Sequoia beat the S&P in 9
#     rows (60.00%); it printed only 3 negative rows against the
#     index's 5; its worst row (-24.0% in 1973) was shallower
#     than the index's worst (-26.4% in 1974).
wins = sum(1 for a, b in zip(seq, sp) if a > b)
check("11 wins 9 of 15 = 60.00%",
      wins == 9 and abs(wins / 15 * 100 - 60.00) < 0.01)
check("11 negative rows 3 vs 5, worst -24.0 vs -26.4",
      sum(1 for v in seq if v < 0) == 3
      and sum(1 for v in sp if v < 0) == 5
      and min(seq) == -24.0 and min(sp) == -26.4)

# 12. Two separations. (a) Recomputing compound rates from the
#     compounded factors over 13.71 years gives about 17.14% and
#     about 10.01%, close to the stated 17.2% / 10.0% (the small
#     gap is the stub-and-quarter weighting). (b) The fund kept
#     compounding long after its founder: it closed to new
#     investors in 1982, twelve years after launch, and reopened
#     in 2008, three years after Ruane died in 2005, so neither
#     the reopening nor the post-2005 record is his.
yrs = days / 365.25
check("12 recomputed CAGR ~17.14% vs ~10.01%",
      abs((compound(seq) ** (1 / yrs) - 1) * 100 - 17.14) < 0.01
      and abs((compound(sp) ** (1 / yrs) - 1) * 100 - 10.01) < 0.01)
check("12 close 12y after launch, reopen 3y after death",
      1982 - 1970 == 12 and 2008 - 2005 == 3)

print("ALL PASSED" if ok else "SOME FAILED")
