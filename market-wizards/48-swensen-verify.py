#!/usr/bin/env python3
"""Verify arithmetic in note 48 (David Swensen / Yale Endowment).
All inputs are figures stated in the note's cited sources (Yale News
coda 2021-10-22, Yale News obituary 2021-05-06, Yale SOM biography,
Open Yale Courses ECON 252 lecture 9 transcript). This script only
checks internal arithmetic consistency. Clean-room, self-written.
"""
from datetime import date

ok = True

def check(name, cond):
    global ok
    print(("PASS" if cond else "FAIL"), name)
    ok = ok and cond

# 1. Tenure and age: born 1954-01-26, died 2021-05-05 aged 67;
#    CIO 1985 -> 2021 is the 36-year term; 1985 -> 2020 is 35 years.
check("1 age at death 67", (date(2021, 5, 5) - date(1954, 1, 26)).days // 365 == 67)
check("1 started 1985 aged 31", 1985 - 1954 == 31)
check("1 36-year term 1985-2021", 2021 - 1985 == 36)
check("1 35-year window 1985-2020", 2020 - 1985 == 35)

# 2. $1 at 13.7% for 36 years ~ 101.71, close to Yale's "nearly $103"
#    (Yale compounds the actual yearly series; smoothed CAGR is ours).
f36 = 1.137 ** 36
check("2 1.137^36 ~101.71", abs(f36 - 101.71) < 0.05)
check("2 within 2 of Yale 'nearly 103'", abs(f36 - 103) < 2)
# S&P: $1 -> slightly more than $50 implies CAGR ~11.48%.
check("2 S&P implied CAGR ~11.48%", abs((50 ** (1 / 36) - 1) * 100 - 11.48) < 0.05)
check("2 Yale/S&P terminal ratio ~2.06", abs(103 / 50 - 2.06) < 0.01)

# 3. Endowment scale: $1.3B (1985) -> $42.3B (2021-06-30) = 32.54x.
check("3 scale multiple 32.54x", abs(42.3 / 1.3 - 32.54) < 0.01)
# Identity: start + gains - spending = 37.1; residual to 42.3 is 5.2
# (gifts and other net inflows, inferred residual, labelled C).
check("3 1.3+57.6-21.8=37.1", abs((1.3 + 57.6 - 21.8) - 37.1) < 1e-9)
check("3 residual gifts etc 5.2", abs((42.3 - 37.1) - 5.2) < 1e-9)
# Pure no-spending compounding of the start value would be ~132.23B,
# far above the actual 42.3B: the actual multiple is after spending.
check("3 pure compound start ~132.23B", abs(1.3 * f36 - 132.23) < 0.05)

# 4. 36y gaps: average endowment 13.7-3.4=10.3%; 60/40 13.7-4.0=9.7%.
check("4 avg endowment 10.3%", abs((13.7 - 3.4) - 10.3) < 1e-9)
check("4 60/40 implied 9.7%", abs((13.7 - 4.0) - 9.7) < 1e-9)
check("4 $1 at avg endowment ~34.10", abs(1.103 ** 36 - 34.10) < 0.05)
check("4 $1 at 60/40 ~28.02", abs(1.097 ** 36 - 28.02) < 0.05)

# 5. 35y window (obituary, through 2020-06-30): 13.1%; Cambridge mean
#    13.1-3.4=9.7%; 60/40 13.1-4.3=8.8%; gains 45.6, value added 36.0.
check("5 35y Cambridge mean 9.7%", abs((13.1 - 3.4) - 9.7) < 1e-9)
check("5 35y 60/40 implied 8.8%", abs((13.1 - 4.3) - 8.8) < 1e-9)
check("5 value added / gains 78.95%", abs((36.0 / 45.6) * 100 - 78.95) < 0.05)
check("5 35y factor 1.131^35 ~74.33", abs(1.131 ** 35 - 74.33) < 0.05)

# 6. Spending: $45M (~10% of budget, 1985) -> $1.6B (~33% now):
#    35.56x in dollars, 3.3x in budget share; excl. med school 58%.
check("6 spending multiple 35.56x", abs(1600 / 45 - 35.56) < 0.01)
check("6 budget share 10->33 = 3.3x", abs(33 / 10 - 3.3) < 1e-9)
check("6 excl-med share gap 25pp", abs((58 - 33) - 25) < 1e-9)

# 7. Final year +40.2%: 26.5pp above the 36y annualised 13.7%,
#    i.e. 2.93x the long-run yearly rate; $1 -> $1.402 that year.
check("7 final-year gap 26.5pp", abs((40.2 - 13.7) - 26.5) < 1e-9)
check("7 final-year / long-run 2.93x", abs(40.2 / 13.7 - 2.93) < 0.01)

# 8. Earlier snapshot (Yale SOM bio): 27 years at 13.9%, $20.0B.
check("8 27y vs 36y rate diff 0.2pp", abs((13.9 - 13.7) - 0.2) < 1e-9)
check("8 $20.0B -> $42.3B = 2.115x", abs(42.3 / 20.0 - 2.115) < 1e-9)
check("8 Wall Street 3+3=6 years", 3 + 3 == 6)

# 9. Allocation in his own lecture words: mid-1980s typical endowment
#    50% stocks + 40% bonds/cash + 10% alternatives = 100, of which
#    domestic marketable = 90. Yale c.2008: 11+15+4 = 30 traditional.
check("9 1980s mix sums 100", 50 + 40 + 10 == 100)
check("9 domestic marketable 90", 50 + 40 == 90)
check("9 Yale c.2008 traditional 30", 11 + 15 + 4 == 30)

# 10. Legacy counts: 15 alumni went on to lead other institutions;
#     6 of the top-15 endowments (10y) run by Yale alumni = 40%;
#     office built to about 30 professionals.
check("10 alumni-led share 40%", abs((6 / 15) * 100 - 40) < 1e-9)
check("10 two-thirds of 15 ~ 10", round(15 * 2 / 3) == 10)

print("ALL PASSED" if ok else "SOME FAILED")
