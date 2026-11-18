#!/usr/bin/env python3
"""Verify arithmetic in note 62 (Tweedy, Browne Partners / Tom Knapp).

All performance inputs are figures printed in Table 2 of Buffett
(1984), "The Superinvestors of Graham-and-Doddsville", Hermes,
Fall 1984, as reproduced in the appendixes of The Intelligent
Investor (4th revised edition): fiscal years ended September 30,
1968 (nine months) through 1983, columns Dow Jones, S&P 500,
TBK Overall and TBK Limited Partners. Stated totals for the
15 3/4 years: Dow +191.8%, S&P +238.5%, TBK Overall +1,661.2%,
TBK Limited Partners +936.4%; stated compound rates: S&P 7.0%
(as printed), TBK LP 16.0%, TBK Overall 20.0%. Identity facts are
from Buffett's text (Knapp worked at Graham-Newman from 1954;
in 1968 Knapp and Ed Anderson formed Tweedy, Browne Partners).
This script only checks internal arithmetic consistency and
derived windows. Clean-room, self-written.
"""

from math import prod

ok = True

def check(name, cond):
    global ok
    print(("PASS" if cond else "FAIL"), name)
    ok = ok and cond

# Rows: (label, Dow %, S&P %, TBK Overall %, TBK LP %)
rows = [
    ("1968-9m", 6.0, 8.8, 27.6, 22.0), ("1969", -9.5, -6.2, 12.7, 10.0),
    ("1970", -2.5, -6.1, -1.3, -1.9), ("1971", 20.7, 20.4, 20.9, 16.1),
    ("1972", 11.0, 15.5, 14.6, 11.8), ("1973", 2.9, 1.0, 8.3, 7.5),
    ("1974", -31.8, -38.1, 1.5, 1.5), ("1975", 36.9, 37.8, 28.8, 22.0),
    ("1976", 29.6, 30.1, 40.2, 32.8), ("1977", -9.9, -4.0, 23.4, 18.7),
    ("1978", 8.3, 11.9, 41.0, 32.1), ("1979", 7.9, 12.7, 25.5, 20.5),
    ("1980", 13.0, 21.1, 21.4, 17.3), ("1981", -3.3, 2.7, 14.4, 11.6),
    ("1982", 12.5, 10.1, 10.2, 8.2), ("1983", 44.5, 44.3, 35.0, 28.2),
]
dow = [r[1] for r in rows]
sp = [r[2] for r in rows]
ov = [r[3] for r in rows]
lp = [r[4] for r in rows]

def compound(vals):
    return prod(1 + v / 100 for v in vals)

# 1. Table shape and identity dates: 16 rows (1968 nine-month stub
#    plus fifteen fiscal years to 1983), stated span 15 3/4 years;
#    the partnership was formed in 1968, fourteen years after
#    Knapp started at Graham-Newman in 1954.
check("1 16 rows, span 15.75y", len(rows) == 16)
check("1 formed 1968, 14y after 1954", 1968 - 1954 == 14)

# 2. Three of the four columns compound exactly to their stated
#    totals within one-decimal rounding: Dow +191.8%, TBK Overall
#    +1,661.2%, TBK Limited Partners +936.4%.
check("2 Dow compound ~+191.8%",
      abs((compound(dow) - 1) * 100 - 191.8) < 0.05)
check("2 Overall compound ~+1661.2%",
      abs((compound(ov) - 1) * 100 - 1661.2) < 0.05)
check("2 LP compound ~+936.4%",
      abs((compound(lp) - 1) * 100 - 936.4) < 0.05)
print("   Dow/Overall/LP compounded:",
      round((compound(dow) - 1) * 100, 2),
      round((compound(ov) - 1) * 100, 2),
      round((compound(lp) - 1) * 100, 2))

# 3. The S&P column does NOT reconcile: compounding its printed
#    rows gives about +257.30%, not the stated +238.5% (a gap of
#    about 18.80pp), and the stated 7.0% compound rate matches
#    neither (the stated total implies about 8.05%, the rows
#    about 8.42%; 7.0% is in fact the Dow's implied rate, about
#    7.04%). Registered, not silently corrected.
sp_comp = (compound(sp) - 1) * 100
check("3 S&P rows compound ~+257.30%, gap ~18.80pp vs stated",
      abs(sp_comp - 257.30) < 0.05 and abs(sp_comp - 238.5 - 18.80) < 0.05)
check("3 implied CAGRs: stated-total ~8.05%, rows ~8.42%, Dow ~7.04%",
      abs(((1 + 238.5 / 100) ** (1 / 15.75) - 1) * 100 - 8.05) < 0.01
      and abs((compound(sp) ** (1 / 15.75) - 1) * 100 - 8.42) < 0.01
      and abs((compound(dow) ** (1 / 15.75) - 1) * 100 - 7.04) < 0.01)

# 4. The TBK stated compound rates do reconcile: recomputing over
#    15.75 years gives about 19.98% (stated 20.0%) and about
#    16.01% (stated 16.0%).
check("4 Overall CAGR ~19.98% vs stated 20.0%",
      abs((compound(ov) ** (1 / 15.75) - 1) * 100 - 19.98) < 0.01)
check("4 LP CAGR ~16.01% vs stated 16.0%",
      abs((compound(lp) ** (1 / 15.75) - 1) * 100 - 16.01) < 0.01)

# 5. Endpoints on USD 10,000 from the stated totals: Overall
#    USD 176,120, LP USD 103,640, S&P (stated total) USD 33,850;
#    the Overall endpoint is about 1.70x the LP endpoint, and
#    the fee-and-share drag is 1,661.2 - 936.4 = 724.8pp.
check("5 endpoints 176120 / 103640 / 33850",
      abs(10000 * (1 + 1661.2 / 100) - 176120) < 1
      and abs(10000 * (1 + 936.4 / 100) - 103640) < 1
      and abs(10000 * (1 + 238.5 / 100) - 33850) < 1)
check("5 Overall/LP endpoint ratio ~1.70x, drag 724.8pp",
      abs(176120 / 103640 - 1.70) < 0.01
      and abs(1661.2 - 936.4 - 724.8) < 1e-9)

# 6. Only one negative row: TBK Overall fell in just 1 of 16 rows
#    (-1.3% in fiscal 1970), and TBK LP likewise in just 1; the
#    S&P printed 4 negative rows and the Dow 5.
check("6 negative rows Overall 1, LP 1, S&P 4, Dow 5",
      sum(1 for v in ov if v < 0) == 1 and ov[2] == -1.3
      and sum(1 for v in lp if v < 0) == 1
      and sum(1 for v in sp if v < 0) == 4
      and sum(1 for v in dow if v < 0) == 5)

# 7. Worst rows: TBK Overall's worst row is -1.3%; the S&P's
#    worst printed row is -38.1% (fiscal 1974), 36.8pp deeper.
check("7 worst rows -1.3 vs -38.1, gap 36.8pp",
      min(ov) == -1.3 and min(sp) == -38.1
      and abs(abs(min(sp)) - abs(min(ov)) - 36.8) < 1e-9)

# 8. The 1973-74 bear market, fiscal years: while the S&P
#    compounded about -37.48% over the two rows, TBK Overall
#    compounded about +9.92% (rows +8.3% and +1.5%); the single
#    fiscal-1974 gap alone is 39.6pp (+1.5 against -38.1).
check("8 1973-74 Overall ~+9.92% vs S&P ~-37.48%",
      abs((compound(ov[5:7]) - 1) * 100 - 9.92) < 0.01
      and abs((compound(sp[5:7]) - 1) * 100 + 37.48) < 0.01)
check("8 fiscal-1974 single-row gap 39.6pp",
      abs(ov[6] - sp[6] - 39.6) < 1e-9)

# 9. Scoreboard: TBK Overall beat the S&P in 13 of 16 rows
#    (81.25%); it also beat the Dow in 13 of 16 rows.
wins_sp = sum(1 for a, b in zip(ov, sp) if a > b)
wins_dow = sum(1 for a, b in zip(ov, dow) if a > b)
check("9 wins vs S&P 13/16 = 81.25%, vs Dow 13/16",
      wins_sp == 13 and abs(wins_sp / 16 * 100 - 81.25) < 0.01
      and wins_dow == 13)

# 10. The start: over the first three rows (1968 stub through
#     fiscal 1970) TBK Overall compounded about +41.94% while
#     the S&P compounded about -4.17% -- the record opened by
#     not falling, in the years the index went nowhere.
check("10 first-three Overall ~+41.94% vs S&P ~-4.17%",
      abs((compound(ov[:3]) - 1) * 100 - 41.94) < 0.01
      and abs((compound(sp[:3]) - 1) * 100 + 4.17) < 0.01)

# 11. Fiscal 1969: the index fell (-6.2%) and TBK Overall rose
#     +12.7%, a single-row gap of 18.9pp; the partnership's
#     second year already showed the pattern of row 8.
check("11 fiscal-1969 gap 18.9pp",
      abs(ov[1] - sp[1] - 18.9) < 1e-9)

# 12. Separation: this table ends at fiscal 1983; Tweedy,
#     Browne's later mutual-fund record (the firm survives, the
#     partnership table does not extend) is a different account
#     and is not credited to Knapp's partnership here. The table
#     window 1968-1983 inclusive is 16 fiscal rows over a stated
#     15 3/4 years because the first row is nine months.
check("12 16 rows = 0.75 + 15 full years",
      abs(0.75 + 15 - 15.75) < 1e-9 and 1983 - 1968 + 1 == 16)

print("ALL PASSED" if ok else "SOME FAILED")
