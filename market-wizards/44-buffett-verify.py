# MW44 Buffett verification - all figures from Berkshire Hathaway 2024 shareholder letter (2025-02-22)
# 1 CAGR gap: Berkshire 19.9% vs S&P 500 10.4%, 1965-2024
assert abs((19.9 - 10.4) - 9.5) < 0.01
assert abs(19.9 / 10.4 - 1.91) < 0.01
print("1 CAGR gap 9.50pp, ratio 1.91x")

# 2 overall gain: Berkshire 5,502,284% vs S&P 39,054% (1964-2024)
assert abs(5502284 / 39054 - 140.89) < 0.01
brk_mult = 5502284 / 100 + 1
sp_mult = 39054 / 100 + 1
assert brk_mult == 55023.84 and sp_mult == 391.54
assert abs(brk_mult / sp_mult - 140.53) < 0.01
# $10,000: gain amount vs terminal value differ by the principal itself
assert 10000 * 5502284 / 100 == 550228400.0
assert 10000 * brk_mult == 550238400.0
assert 10000 * sp_mult == 3915400.0
# rounded CAGRs reproduce the overall multiples only approximately (within 3.5%)
assert abs(1.199 ** 60 / brk_mult - 1) < 0.035
assert abs(1.104 ** 60 / sp_mult - 1) < 0.035
print("2 overall gain ratio 140.89x, terminal multiple ratio 140.53x, CAGR rounding gap <3.5%")

# 3 operating earnings 2024 breakdown sums to the reported total; growth vs 2023
parts = [9020, 13670, 5031, 3730, 13072, 1519, 1395]
assert sum(parts) == 47437
assert abs((47437 / 37350 - 1) * 100 - 27.01) < 0.01
print("3 operating earnings sum 47,437, growth +27.01%")

# 4 insurance: underwriting growth and insurance total
assert abs((9020 / 5428 - 1) * 100 - 66.18) < 0.01
assert 9020 + 13670 == 22690 and 5428 + 9567 == 14995
assert abs((22690 / 14995 - 1) * 100 - 51.32) < 0.01
print("4 underwriting +66.18%, insurance total 22,690 vs 14,995 = +51.32%")

# 5 tax visualisation: $1m every 20 minutes through leap year 2024
minutes = 366 * 24 * 60
assert minutes == 527040
checks = minutes // 20
assert checks == 26352
paid = checks * 1_000_000 / 1e9
assert abs(paid - 26.352) < 0.001
assert abs(26.8 - paid - 0.448) < 0.001  # still owed after a full year of checks
assert abs(26.8 / 0.05 - 536.0) < 0.01  # 5% of all US corporate tax implies a $536bn total
print("5 tax checks 26,352 = $26.352bn, shortfall $0.448bn, implied corporate total $536bn")

# 6 sole dividend: Jan 3, 1967, $101,755 at 10 cents per A share
assert 101755 / 0.10 == 1017550.0
print("6 sole dividend implies 1,017,550 A shares at that date")

# 7 float: $46bn to $171bn over two decades; $32bn underwriting profit over the same span
assert abs(171 / 46 - 3.72) < 0.01
assert abs((171 / 46 - 1) * 100 - 271.74) < 0.01
assert 32 / 20 == 1.6
print("7 float 3.72x (+271.74%), underwriting profit averages $1.6bn/yr over 20y")

# 8 Japanese five: cost $13.8bn, market $23.5bn; 2025 dividends $812m vs yen interest $135m
assert abs((23.5 - 13.8) - 9.7) < 0.01
assert abs((23.5 / 13.8 - 1) * 100 - 70.29) < 0.01
assert 812 - 135 == 677
assert abs(812 / 135 - 6.01) < 0.01
assert abs(812 / 13800 * 100 - 5.88) < 0.01
print("8 Japan gain $9.7bn (+70.29%), dividend-interest net $677m, 6.01x cover, 5.88% yield on cost")

# 9 marketable equities: $354bn down to $272bn in 2024
assert 354 - 272 == 82
assert abs((272 / 354 - 1) * 100 - (-23.16)) < 0.01
print("9 marketable equities -$82bn, -23.16%")

# 10 yearly table: 11 negative years out of 60; worst year and widest single-year gap
neg_years = [1966, 1970, 1973, 1974, 1984, 1990, 1999, 2002, 2008, 2011, 2015]
assert len(neg_years) == 11
assert abs(11 / 60 * 100 - 18.33) < 0.01
assert abs(49 / 60 * 100 - 81.67) < 0.01
assert abs((1 / (1 - 0.487) - 1) * 100 - 94.93) < 0.01  # 1974 -48.7% needs +94.93% to recover
assert abs((-19.9 - 21.0) - (-40.9)) < 0.01  # 1999 gap vs S&P
print("10 negative years 11/60 = 18.33%, 1974 recovery +94.93%, 1999 gap -40.90pp")

print("ALL PASSED 10 groups")
