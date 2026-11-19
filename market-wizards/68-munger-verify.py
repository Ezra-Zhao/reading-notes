#!/usr/bin/env python3
"""Verify arithmetic in note 68 (Charles Munger partnership).

All performance inputs are figures printed in Table 5 of Buffett
(1984), "The Superinvestors of Graham-and-Doddsville", Hermes,
Fall 1984 (Columbia Business School), as reproduced in the
appendixes of The Intelligent Investor (4th revised edition):
calendar years 1962-1975, columns Dow (overall), Overall
Partnership, Limited Partners. Stated cumulative 1962-75:
Dow +96.8%, Partnership +1,156.7%, LP +500.1%; stated annual
compounded rates: Dow 5.0%, Partnership 19.8%, LP 13.7%.
Stated intermediate compound row 1962-69: Dow +44.5%,
Partnership +1,046.5%, LP +474.6%. Identity facts are from
Buffett's text introducing Table 5 (a friend of his, a Harvard
Law graduate who set up a major law firm; Buffett ran into him
in about 1960 and told him law was a fine hobby but he could
do better). Two transcription conflicts were resolved by the
stated totals: a secondary table giving 1974 partnership as
-31.9% compounds to +1,149.32% (7.38pp off the stated total),
while -31.5% compounds to +1,156.66% (0.04pp off), so -31.5%
is used for both 1974 partnership columns; the Dow 1966 figure
is -15.7% in the appendix transcription (-15.8% in one
secondary table, -15.6% in Table 3's Dow column) and is
registered as a cross-table discrepancy, not silently fixed.
This script only checks internal arithmetic consistency and
derived windows. Clean-room, self-written.
"""

from math import prod

ok = True

def check(name, cond):
    global ok
    print(("PASS" if cond else "FAIL"), name)
    ok = ok and cond

# Rows: (year, Dow %, Partnership %, LP %)
rows = [
    (1962, -7.6, 30.1, 20.1), (1963, 20.6, 71.7, 47.8),
    (1964, 18.7, 49.7, 33.1), (1965, 14.2, 8.4, 6.0),
    (1966, -15.7, 12.4, 8.3), (1967, 19.0, 56.2, 37.5),
    (1968, 7.7, 40.4, 27.0), (1969, -11.6, 28.3, 21.3),
    (1970, 8.7, -0.1, -0.1), (1971, 9.8, 25.4, 20.6),
    (1972, 18.2, 8.3, 7.3), (1973, -13.1, -31.9, -31.9),
    (1974, -23.1, -31.5, -31.5), (1975, 44.4, 73.2, 73.2),
]
dow = [r[1] for r in rows]
part = [r[2] for r in rows]
lp = [r[3] for r in rows]
n = len(rows)

def cum(vals):
    return (prod(1 + v / 100 for v in vals) - 1) * 100

def cagr(vals):
    return (prod(1 + v / 100 for v in vals) ** (1 / len(vals)) - 1) * 100

# 1. Fourteen calendar years; partnership negative 3 years; Dow negative 5.
check("1a 14 years 1962-1975", n == 14 and rows[0][0] == 1962 and rows[-1][0] == 1975)
check("1b partnership negative years = 3 (1970 -0.1, 1973 -31.9, 1974 -31.5)",
      [r[0] for r in rows if r[2] < 0] == [1970, 1973, 1974])
check("1c Dow negative years = 5", sum(1 for v in dow if v < 0) == 5)
check("1d partnership worst year -31.9, best +73.2", min(part) == -31.9 and max(part) == 73.2)

# 2. Full-period compounding vs stated cumulative.
check("2a Partnership cum ~+1156.7 (gap 0.04pp)", abs(cum(part) - 1156.7) < 0.1)
check("2b LP cum ~+500.1 (gap 0.04pp)", abs(cum(lp) - 500.1) < 0.1)
check("2c Dow cum ~+96.8 (gap 0.40pp, registered)", abs(cum(dow) - 96.8) < 0.5)
print(f"   cum: Dow {cum(dow):.2f}  Part {cum(part):.2f}  LP {cum(lp):.2f}")

# 3. CAGR recomputed vs stated annual compounded rates.
check("3a Partnership CAGR ~19.8", abs(cagr(part) - 19.8) < 0.05)
check("3b LP CAGR ~13.7", abs(cagr(lp) - 13.7) < 0.06)
check("3c Dow CAGR ~5.0", abs(cagr(dow) - 5.0) < 0.08)
print(f"   cagr: Dow {cagr(dow):.3f}  Part {cagr(part):.3f}  LP {cagr(lp):.3f}")

# 4. $10,000 terminal values from stated cumulative; ratios.
t_dow = round(10000 * 1.968, 2)
t_part = round(10000 * 12.567, 2)
t_lp = round(10000 * 6.001, 2)
check("4a terminals 19680 / 125670 / 60010", (t_dow, t_part, t_lp) == (19680.0, 125670.0, 60010.0))
check("4b Part/Dow terminal ratio ~6.39", abs(t_part / t_dow - 6.3857) < 0.01)
check("4c LP/Dow terminal ratio ~3.05", abs(t_lp / t_dow - 3.0493) < 0.01)
print(f"   ratios: Part/Dow {t_part/t_dow:.4f}  LP/Dow {t_lp/t_dow:.4f}")

# 5. Fee drag: LP share of partnership terminal; CAGR gaps.
check("5a LP terminal ~47.75% of partnership terminal", abs(t_lp / t_part * 100 - 47.75) < 0.05)
check("5b CAGR gap Part-LP = 6.1pp", abs((19.8 - 13.7) - 6.1) < 1e-9)
check("5c CAGR gap Part-Dow = 14.8pp", abs((19.8 - 5.0) - 14.8) < 1e-9)

# 6. Head-to-head years vs Dow: partnership wins 9 of 14.
wins = [r[0] for r in rows if r[2] > r[1]]
losses = [r[0] for r in rows if r[2] < r[1]]
check("6a partnership beat Dow 9/14", len(wins) == 9)
check("6b losing years = 1965, 1970, 1972, 1973, 1974", losses == [1965, 1970, 1972, 1973, 1974])

# 7. Excess shape: largest +51.1pp (1963), smallest -18.8pp (1973).
excess = [(r[0], r[2] - r[1]) for r in rows]
check("7a max excess 1963 +51.1pp", abs(max(excess, key=lambda x: x[1])[1] - 51.1) < 1e-9
      and max(excess, key=lambda x: x[1])[0] == 1963)
check("7b min excess 1973 -18.8pp", abs(min(excess, key=lambda x: x[1])[1] - (-18.8)) < 1e-9
      and min(excess, key=lambda x: x[1])[0] == 1973)

# 8. Arithmetic mean vs CAGR: volatility drag.
am_part = sum(part) / n
am_dow = sum(dow) / n
check("8a partnership arithmetic mean ~24.33", abs(am_part - 24.33) < 0.01)
check("8b Dow arithmetic mean ~6.44", abs(am_dow - 6.44) < 0.01)
check("8c partnership drag ~4.51pp vs Dow ~1.50pp",
      abs((am_part - cagr(part)) - 4.51) < 0.03 and abs((am_dow - cagr(dow)) - 1.50) < 0.03)
print(f"   arith: Part {am_part:.3f}  Dow {am_dow:.3f}  drag Part {am_part-cagr(part):.3f} Dow {am_dow-cagr(dow):.3f}")

# 9. The 1973-74 hole: partnership -53.35%, recovery +114.45%; Dow -33.18%, +49.66%.
hole_p = (0.681 * 0.685 - 1) * 100
hole_d = (0.869 * 0.769 - 1) * 100
check("9a partnership 1973-74 combined ~-53.35%", abs(hole_p - (-53.35)) < 0.02)
check("9b recovery needed ~+114.37%", abs((1 / (1 + hole_p / 100) - 1) * 100 - 114.37) < 0.05)
check("9c Dow 1973-74 combined ~-33.18%, recovery ~+49.66%",
      abs(hole_d - (-33.18)) < 0.02 and abs((1 / (1 + hole_d / 100) - 1) * 100 - 49.66) < 0.05)
print(f"   hole: Part {hole_p:.2f} rec {(1/(1+hole_p/100)-1)*100:.2f}  Dow {hole_d:.2f} rec {(1/(1+hole_d/100)-1)*100:.2f}")

# 10. Even after +73.2% in 1975, still below the end-1972 level.
after = (1 + hole_p / 100) * 1.732 - 1
check("10a post-1975 level ~-19.21% vs end-1972", abs(after * 100 - (-19.21)) < 0.05)
print(f"   vs end-1972 after 1975: {after*100:.2f}%")

# 11. Intermediate stated compound row 1962-69 reproduced by first 8 rows.
check("11a first-8y Partnership cum ~+1046.5", abs(cum(part[:8]) - 1046.5) < 0.6)
check("11b first-8y LP cum ~+474.6", abs(cum(lp[:8]) - 474.6) < 0.6)
check("11c first-8y Dow cum ~+44.5 (gap within 0.5pp)", abs(cum(dow[:8]) - 44.5) < 0.5)
print(f"   1962-69 cum: Dow {cum(dow[:8]):.2f}  Part {cum(part[:8]):.2f}  LP {cum(lp[:8]):.2f}")

# 12. Fee pattern: in every negative year LP equals overall (no incentive
#     fee in a loss year); in positive years LP < overall, except the
#     final year 1975 where both print +73.2.
neg_equal = all(r[3] == r[2] for r in rows if r[2] < 0)
pos_less = all(r[3] < r[2] for r in rows if r[2] > 0 and r[0] != 1975)
check("12a LP == overall in all 3 negative years", neg_equal)
check("12b LP < overall in positive years except 1975 (both +73.2)", pos_less and rows[-1][2] == rows[-1][3] == 73.2)

print("ALL OK" if ok else "SOME FAILED")
