#!/usr/bin/env python3
"""Verify arithmetic for note 32 (Tom Baldwin). Inputs from public
sources cited in the note: Schwager Market Wizards intro (TurtleTrader /
Yumpu reprint), MarketsWiki (tax-court income figures, Crain's 1995
40-under-40 / 5% volume, Granot Loma purchase and restoration),
Granot Loma site reprinting Cigar Aficionado 1997, Chicago Tribune
reporting of the 1989-03-17 loss day carried by a secondary blog,
Wikipedia birth year 1956 (single source, C grade)."""
from datetime import date

def close(a, b, tol=0.02):
    return abs(a - b) <= tol

# 1. Contract face value: T-bond future = $100,000 face per contract
face = 100_000
assert 2_000 * face == 200_000_000
assert 20_000 * face == 2_000_000_000
assert 60_000 * face == 6_000_000_000
print("1 face OK single 2,000 = $200M; typical day 20,000 = $2B; max day 60,000 = $6B")

# 2. Timeline vs birth year 1956 (Wikipedia, C): start 1982, Schwager intro ~1988
assert 1982 - 1956 == 26
assert 1988 - 1956 == 32  # 'early thirties' in the book intro, six years after 1982
assert 1988 - 1982 == 6
assert 1995 - 1956 == 39  # fits Crain's 40 Under 40 in 1995
print("2 timeline OK born 1956 -> 26 at 1982 start, 32 in 1988 (early thirties, 6y in), 39 at 1995 40-under-40")

# 3. Floor tenure and Hall of Fame gap
assert 2000 - 1982 == 18
assert 2009 - 1982 == 27
assert 2009 - 2000 == 9
print("3 tenure OK floor 1982-2000 = 18 years; FIA Hall of Fame 2009-03-12 = 27y after start, 9y after leaving floor")

# 4. 1987 trading income vs 1982 starting stake (magnitude only, not a return)
inc87 = 19_160_059
assert close(inc87 / 20_000, 958.00, 0.01)
print("4 income scale OK 1987 income $19,160,059 / $20,000 start = 958.00x (single-year income vs starting stake)")

# 5. Income decline path (tax-court dispute figures via MarketsWiki)
inc88, inc92 = 7_250_000, 3_045_000
assert close((inc88 / inc87 - 1) * 100, -62.16, 0.02)
assert close(inc92 / inc88, 0.42, 0.0001)
assert close((inc92 / inc88 - 1) * 100, -58.00, 0.02)
assert close((inc92 / inc87 - 1) * 100, -84.11, 0.02)
print("5 decline OK 1987 19.16M -> 1988 7.25M (-62.16%) -> 1992 3.045M (=42.00% of 1988, -58.00%; -84.11% vs 1987)")

# 6. The $5M day (Tribune reporting, secondary): 6,000 contracts, market down 2 points
contracts = 6_000
assert contracts * face == 600_000_000
full_move = contracts * 1_000 * 2  # 1 point = 1% of $100k face = $1,000 per contract
assert full_move == 12_000_000
assert close(5_000_000 / full_move * 100, 41.67, 0.02)
print("6 loss day OK 6,000 contracts = $600M face; full 2-point move = $12.00M; realized $5M = 41.67% (he reversed out progressively)")

# 7. Worst day vs starting stake and vs best day (Cigar Aficionado quote)
assert 5_000_000 / 20_000 == 250
assert close(5_000_000 / 2_000_000, 2.5, 0.001)
print("7 day scale OK worst day -$5M = 250x the $20,000 start; worst/best day = 5M/2M = 2.5x")

# 8. Granot Loma: bought 1987 $4M + similar restoration; asking $19.5M down from $40M
assert 4_000_000 + 4_000_000 == 8_000_000
assert close((19.5 / 40 - 1) * 100, -51.25, 0.02)
assert close(19.5 / 8, 2.4375, 0.0001)
print("8 granot OK cost ~$8M (4M buy + ~4M restore); asking 19.5M vs 40M = -51.25%; asking/cost = 2.4375x")

# 9. Position scale ratios: reported holding up to 60,000 contracts
assert 60_000 / 20_000 == 3
assert 60_000 / 2_000 == 30
print("9 scale OK max holding 60,000 = 3x a typical day's 20,000 traded, 30x a single 2,000 trade")

# 10. Learning hours, illustrative only (his words: six hours a day, every day, in the pit)
hours = 6 * 5 * 50 * 6
assert hours == 9_000
print("10 hours OK illustrative: 6h/day x 5d x 50w x 6y = 9,000 pit hours before the book (assumptions stated, C grade)")

print("ALL PASS")
