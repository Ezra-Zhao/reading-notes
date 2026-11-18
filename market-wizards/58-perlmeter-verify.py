#!/usr/bin/env python3
"""Verify arithmetic in note 58 (Stan Perlmeter / Perlmeter Investments).

All inputs are figures printed in Table 7 of Buffett (1984),
"The Superinvestors of Graham-and-Doddsville", Hermes, Fall 1984,
as published on Columbia Business School's own site (Chazen Global
Insights reproduction, (c) 1984 Trustees of Columbia University):
columns are PIL Overall (%) and Limited Partner (%), for the stub
period 8/1-12/31/1965, calendar 1966-1975, the stub 1/1-10/31/1976,
and fiscal years ending 10/31 for 1977-1983: 19 periods in total.
Stated totals, 8/1/1965 through 10/31/1983: Partnership +4,277.2%
at 23.0%/yr, Limited Partners +2,309.5% at 19.0%/yr; DJIA about
882 on 7/31/1965 and about 1,225 on 10/31/1983, approximate
compound rate including dividends 7%. This script only checks
internal arithmetic consistency and derived windows. Clean-room,
self-written.
"""

from datetime import date
from math import prod
import statistics

ok = True

def check(name, cond):
    global ok
    print(("PASS" if cond else "FAIL"), name)
    ok = ok and cond

# Period rows: (label, PIL Overall %, Limited Partner %)
rows = [
    ("1965-stub", 40.6, 32.5), ("1966", 6.4, 5.1),
    ("1967", 73.5, 58.8), ("1968", 65.0, 52.0),
    ("1969", -13.8, -13.8), ("1970", -6.0, -6.0),
    ("1971", 55.7, 49.3), ("1972", 23.6, 18.9),
    ("1973", -28.1, -28.1), ("1974", -12.0, -12.0),
    ("1975", 38.5, 38.5), ("1976-stub", 38.2, 34.5),
    ("FY1977", 30.3, 25.5), ("FY1978", 31.8, 26.6),
    ("FY1979", 34.7, 28.9), ("FY1980", 41.8, 34.7),
    ("FY1981", 4.0, 3.3), ("FY1982", 29.8, 25.4),
    ("FY1983", 22.2, 18.4),
]
ov = [r[1] for r in rows]
lp = [r[2] for r in rows]

def compound(vals):
    return prod(1 + v / 100 for v in vals)

# 1. Shape of the table: 19 periods; the window 1965-08-01 to
#    1983-10-31 is 6,665 days, about 18.25 years; the table
#    switches from calendar years to Oct-31 fiscal years after
#    a 10-month stub in 1976 (rows 12-19 are stub + 7 FYs).
days = (date(1983, 10, 31) - date(1965, 8, 1)).days
check("1 19 periods in table", len(rows) == 19)
check("1 window is 6665 days ~18.25y", days == 6665 and abs(days / 365.25 - 18.25) < 0.01)

# 2. Compounding the printed overall rows reproduces the stated
#    total gain +4,277.2% within one-decimal rounding.
check("2 overall compound ~+4277.2%", abs((compound(ov) - 1) * 100 - 4277.2) < 2)
print("   overall compounded:", round((compound(ov) - 1) * 100, 2))

# 3. Compounding the printed LP rows reproduces the stated
#    LP total gain +2,309.5% within one-decimal rounding.
check("3 LP compound ~+2309.5%", abs((compound(lp) - 1) * 100 - 2309.5) < 3)
print("   LP compounded:", round((compound(lp) - 1) * 100, 2))

# 4. Stated annual rates follow from stated totals over 18.25y.
for total, rate in [(4277.2, 23.0), (2309.5, 19.0)]:
    implied = ((1 + total / 100) ** (1 / 18.25) - 1) * 100
    check(f"4 total {total}% implies ~{rate}%/yr", abs(implied - rate) < 0.1)

# 5. $10,000 endpoints from stated totals: overall $437,720,
#    LP $240,950; LP keeps about 55.05% of the overall endpoint,
#    so the overall endpoint is about 1.82x the LP endpoint.
check("5 endpoints 437720/240950",
      abs(10000 * (1 + 4277.2 / 100) - 437720) < 1
      and abs(10000 * (1 + 2309.5 / 100) - 240950) < 1)
check("5 LP endpoint share ~55.05%", abs(240950 / 437720 * 100 - 55.05) < 0.01)
check("5 overall/LP multiple ~1.82x", abs(437720 / 240950 - 1.82) < 0.01)

# 6. Fee drag in annual-rate terms is 4.0pp (23.0 - 19.0), the
#    smallest gap among this series' Superinvestor tables so
#    far; overall beats the Dow's ~7% by 16.0pp, LP by 12.0pp.
check("6 fee drag 4.0pp, edges 16.0pp and 12.0pp",
      abs(23.0 - 19.0 - 4.0) < 1e-9 and abs(23.0 - 7.0 - 16.0) < 1e-9
      and abs(19.0 - 7.0 - 12.0) < 1e-9)

# 7. Losing periods: overall loses in only 4 of 19 periods
#    (1969, 1970, 1973, 1974), i.e. 21.05%; 15 periods are
#    positive (78.95%); the worst single period is -28.1%.
neg = [r[0] for r in rows if r[1] < 0]
check("7 negative periods are 1969/1970/1973/1974",
      neg == ["1969", "1970", "1973", "1974"])
check("7 negative share ~21.05%, positive ~78.95%",
      abs(len(neg) / 19 * 100 - 21.05) < 0.01
      and abs((19 - len(neg)) / 19 * 100 - 78.95) < 0.01)
check("7 worst single period -28.1%", min(ov) == -28.1)

# 8. The 1973-74 bear market: two years compound to -36.73%,
#    needing +58.05% to recover.
bear = (1 - 0.281) * (1 - 0.12) - 1
check("8 1973-74 overall ~-36.73%", abs(bear * 100 + 36.73) < 0.01)
check("8 recovery needs ~+58.05%", abs((1 / (1 + bear) - 1) * 100 - 58.05) < 0.01)

# 9. The first drawdown pair 1969-70 compounds to -18.97%
#    (recovery +23.41%); and the whole six-period stretch
#    1969-1974, two booms included, nets only -1.34%.
two = (1 - 0.138) * (1 - 0.06) - 1
check("9 1969-70 overall ~-18.97%", abs(two * 100 + 18.97) < 0.01)
check("9 recovery needs ~+23.41%", abs((1 / (1 + two) - 1) * 100 - 23.41) < 0.01)
six = compound([-13.8, -6.0, 55.7, 23.6, -28.1, -12.0]) - 1
check("9 1969-74 six periods net ~-1.34%", abs(six * 100 + 1.34) < 0.01)

# 10. After 1974 the table never loses again: the nine periods
#     1975 through FY1983 are all positive and compound to
#     about 10.36x (+935.72%).
run = ov[10:]
check("10 1975-FY83 nine periods all positive", len(run) == 9 and all(v > 0 for v in run))
check("10 1975-FY83 compound ~10.36x", abs(compound(run) - 10.36) < 0.01)
print("   1975-FY83 compounded gain:", round((compound(run) - 1) * 100, 2))

# 11. Arithmetic means (25.06% overall, 20.66% LP) sit above the
#     geometric rates (23.0%, 19.0%): volatility drag again.
#     The opening four periods (1965 stub through 1968) alone
#     compound to +328.26% - the record's head start.
check("11 arithmetic means ~25.06/20.66",
      abs(statistics.mean(ov) - 25.06) < 0.01
      and abs(statistics.mean(lp) - 20.66) < 0.01)
check("11 first four periods compound ~+328.26%",
      abs((compound(ov[:4]) - 1) * 100 - 328.26) < 0.01)

# 12. The Dow comparison in the table is mostly dividends:
#     price alone 882 -> 1,225 is +38.89%, a price-only compound
#     rate of about 1.82%/yr over 18.25y, versus the stated ~7%
#     including dividends. And the LP column equals the overall
#     column in exactly 5 periods - all four losing periods
#     plus 1975 - and is lower in the other 14.
check("12 Dow price-only gain ~+38.89%", abs((1225 / 882 - 1) * 100 - 38.89) < 0.01)
check("12 Dow price-only rate ~1.82%/yr",
      abs(((1225 / 882) ** (1 / 18.25) - 1) * 100 - 1.82) < 0.01)
equal = [r[0] for r in rows if r[1] == r[2]]
check("12 LP equals overall in 5 periods (4 losses + 1975)",
      equal == ["1969", "1970", "1973", "1974", "1975"])
check("12 LP lower in the other 14 periods",
      sum(1 for r in rows if r[2] < r[1]) == 14)

print("ALL PASSED" if ok else "SOME FAILED")
