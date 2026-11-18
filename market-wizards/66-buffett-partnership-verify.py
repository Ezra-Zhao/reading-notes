#!/usr/bin/env python3
"""Verify arithmetic in note 66 (Buffett Partnership, Ltd.).

All performance inputs are figures printed in Table 3 of Buffett
(1984), "The Superinvestors of Graham-and-Doddsville", Hermes,
Fall 1984, as reproduced on the Columbia Business School website
and in the appendixes of The Intelligent Investor (4th revised
edition): calendar years 1957-1969, columns Dow (overall results
from Dow, incl. dividends), Partnership Results, Limited
Partners' Results. Stated cumulative 1957-69: Dow +152.6%,
Partnership +2,794.9%, LP +1,502.7%; stated annual compounded
rates: Dow 7.4%, Partnership 29.5%, LP 23.8%. Identity facts are
from Buffett's text (he worked at Graham-Newman 1954-1956;
Table 3 is "the third member of the group who formed Buffett
Partnership in 1957. The best thing he did was to quit in 1969";
all records in the speech "have been audited"). This script only
checks internal arithmetic consistency and derived windows.
Clean-room, self-written.
"""

from math import prod, log

ok = True

def check(name, cond):
    global ok
    print(("PASS" if cond else "FAIL"), name)
    ok = ok and cond

# Rows: (year, Dow %, Partnership %, LP %)
rows = [
    (1957, -8.4, 10.4, 9.3), (1958, 38.5, 40.9, 32.2),
    (1959, 20.0, 25.9, 20.9), (1960, -6.2, 22.8, 18.6),
    (1961, 22.4, 45.9, 35.9), (1962, -7.6, 13.9, 11.9),
    (1963, 20.6, 38.7, 30.5), (1964, 18.7, 27.8, 22.3),
    (1965, 14.2, 47.2, 36.9), (1966, -15.6, 20.4, 16.8),
    (1967, 19.0, 35.9, 28.4), (1968, 7.7, 58.8, 45.6),
    (1969, -11.6, 6.8, 6.6),
]
dow = [r[1] for r in rows]
part = [r[2] for r in rows]
lp = [r[3] for r in rows]
n = len(rows)

def cum(vals):
    return (prod(1 + v / 100 for v in vals) - 1) * 100

def cagr(vals):
    return (prod(1 + v / 100 for v in vals) ** (1 / len(vals)) - 1) * 100

# 1. Thirteen calendar years; partnership never negative; Dow negative 5 years;
#    partnership beat the Dow in all 13 years.
check("1a 13 years", n == 13)
check("1b partnership min year +6.8% (1969), all positive", min(part) == 6.8 and all(v > 0 for v in part))
check("1c Dow negative years = 5", sum(1 for v in dow if v < 0) == 5)
check("1d partnership beat Dow 13/13", all(p > d for p, d in zip(part, dow)))

# 2. Full-period compounding vs stated cumulative (within rounding).
check("2a Dow cum ~+152.6", abs(cum(dow) - 152.6) < 0.15)
check("2b Partnership cum ~+2794.9 (rounding-accumulation gap 1.12pp)", abs(cum(part) - 2794.9) < 1.5)
check("2c LP cum ~+1502.7", abs(cum(lp) - 1502.7) < 0.6)
print(f"   cum: Dow {cum(dow):.2f}  Part {cum(part):.2f}  LP {cum(lp):.2f}")

# 3. CAGR recomputed vs stated annual compounded rates.
check("3a Dow CAGR ~7.4", abs(cagr(dow) - 7.4) < 0.06)
check("3b Partnership CAGR ~29.5", abs(cagr(part) - 29.5) < 0.06)
check("3c LP CAGR ~23.8", abs(cagr(lp) - 23.8) < 0.06)
print(f"   cagr: Dow {cagr(dow):.3f}  Part {cagr(part):.3f}  LP {cagr(lp):.3f}")

# 4. $10,000 terminal values from stated cumulative; ratios.
t_dow, t_part, t_lp = round(10000 * 2.526, 2), round(10000 * 28.949, 2), round(10000 * 16.027, 2)
check("4a terminals 25260 / 289490 / 160270", (t_dow, t_part, t_lp) == (25260.0, 289490.0, 160270.0))
check("4b Part/Dow terminal ratio ~11.46", abs(t_part / t_dow - 11.4596) < 0.01)
check("4c LP/Dow terminal ratio ~6.34", abs(t_lp / t_dow - 6.3447) < 0.01)
print(f"   ratios: Part/Dow {t_part/t_dow:.4f}  LP/Dow {t_lp/t_dow:.4f}")

# 5. Fee drag: LP terminal as share of partnership terminal; CAGR gap.
check("5a LP terminal ~55.36% of partnership terminal", abs(t_lp / t_part * 100 - 55.36) < 0.05)
check("5b CAGR gap Part-LP = 5.7pp", abs((29.5 - 23.8) - 5.7) < 1e-9)
check("5c CAGR gap Part-Dow = 22.1pp", abs((29.5 - 7.4) - 22.1) < 1e-9)

# 6. Dow down years: partnership still averaged ~+14.86% in those 5 years.
down_part = [p for p, d in zip(part, dow) if d < 0]
check("6a down-year partnership values", down_part == [10.4, 22.8, 13.9, 20.4, 6.8])
check("6b down-year partnership mean ~14.86", abs(sum(down_part) / 5 - 14.86) < 0.01)
check("6c Dow worst year -15.6 (1966) vs partnership +20.4 same year",
      min(dow) == -15.6 and part[dow.index(-15.6)] == 20.4)

# 7. Spreads: largest 1968 (+51.1pp), smallest 1958 (+2.4pp).
spreads = [p - d for p, d in zip(part, dow)]
check("7a max spread 51.1 in 1968", abs(max(spreads) - 51.1) < 1e-9 and rows[spreads.index(max(spreads))][0] == 1968)
check("7b min spread 2.4 in 1958", abs(min(spreads) - 2.4) < 1e-9 and rows[spreads.index(min(spreads))][0] == 1958)
print(f"   spreads: {[round(s,1) for s in spreads]}")

# 8. Arithmetic means vs compound rates (volatility drag).
am_dow, am_part, am_lp = sum(dow) / n, sum(part) / n, sum(lp) / n
check("8a arithmetic means ~8.59 / 30.42 / 24.30",
      abs(am_dow - 8.5923) < 0.01 and abs(am_part - 30.4154) < 0.01 and abs(am_lp - 24.30) < 0.01)
check("8b drag Part ~0.87pp, LP ~0.51pp, Dow ~1.21pp",
      abs((am_part - cagr(part)) - 0.87) < 0.06 and abs((am_lp - cagr(lp)) - 0.51) < 0.06 and abs((am_dow - cagr(dow)) - 1.21) < 0.06)
print(f"   means: Dow {am_dow:.4f}  Part {am_part:.4f}  LP {am_lp:.4f}")

# 9. First five years (1957-61) vs stated cumulative rows.
check("9a 1957-61 cum ~74.9 / 251.0 / 181.6",
      abs(cum(dow[:5]) - 74.9) < 0.15 and abs(cum(part[:5]) - 251.0) < 0.3 and abs(cum(lp[:5]) - 181.6) < 0.3)
print(f"   57-61 cum: Dow {cum(dow[:5]):.2f}  Part {cum(part[:5]):.2f}  LP {cum(lp[:5]):.2f}")

# 10. Last four years (1966-69) derived by dividing cumulative factors:
#     partnership still ~+177.5% while Dow ~-4.35% over the same stretch.
seg_part = (1 + cum(part) / 100) / (1 + cum(part[:9]) / 100)
seg_dow = (1 + cum(dow) / 100) / (1 + cum(dow[:9]) / 100)
check("10a 1966-69 partnership ~+177.5%", abs((seg_part - 1) * 100 - 177.5) < 0.4)
check("10b 1966-69 Dow ~-4.35%", abs((seg_dow - 1) * 100 - (-4.35)) < 0.15)
check("10c direct product 1966-69 matches division",
      abs(prod(1 + v / 100 for v in part[9:]) - seg_part) < 1e-9)
print(f"   66-69: Part {(seg_part-1)*100:.2f}%  Dow {(seg_dow-1)*100:.2f}%")

# 11. Doubling times at stated compound rates.
d_part = log(2) / log(1.295)
d_dow = log(2) / log(1.074)
check("11a doubling ~2.68y at 29.5%", abs(d_part - 2.68) < 0.02)
check("11b doubling ~9.71y at 7.4%", abs(d_dow - 9.71) < 0.03)
print(f"   doubling: Part {d_part:.3f}y  Dow {d_dow:.3f}y")

# 12. Timeline arithmetic: formed 1957, quit 1969 (12 years later, 13 result
#     years); Graham-Newman 1954-1956 precedes it; 1984 speech = 1934 + 50.
check("12a 1969-1957 = 12, result years = 13", 1969 - 1957 == 12 and n == 13)
check("12b speech 1984 = Security Analysis 1934 + 50", 1934 + 50 == 1984)
check("12c Graham-Newman stint 1954-1956 ends 1 year before 1957 formation", 1957 - 1956 == 1)

print("ALL PASS" if ok else "SOME FAILED")
raise SystemExit(0 if ok else 1)
