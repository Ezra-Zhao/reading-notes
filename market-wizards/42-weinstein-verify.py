# MW42 Weinstein verification - all figures from Schwager, Market Wizards (1989), Weinstein chapter pp.156-165
# 1 first trade: $8,400 account, long corn, out $7,800 in 3 days
rem = 8400 - 7800
loss_pct = 7800 / 8400 * 100
assert rem == 600, rem
assert abs(loss_pct - 92.86) < 0.01, loss_pct
print("1 first trade remaining", rem, "loss pct", round(loss_pct, 2))

# 2 comeback stake: saved ~$24,000 in 6-7 months, $4,000 living, $20,000 trading
assert 4000 + 20000 == 24000
assert abs(4000 / 24000 * 100 - 16.67) < 0.01
assert abs(20000 / 24000 * 100 - 83.33) < 0.01
print("2 stake split living 16.67% trading 83.33%")

# 3 castle: $350,000 price, $50,000/yr upkeep, later said worth $5,000,000
assert abs(50000 / 350000 * 100 - 14.29) < 0.01
mult = 5000000 / 350000
assert abs(mult - 14.29) < 0.01, mult
assert abs((mult - 1) * 100 - 1328.57) < 0.01
print("3 castle upkeep 14.29%/yr of price, value multiple", round(mult, 2))

# 4 soybean disaster: account nearly $1,500,000, losing ~$125,000/day, 5 limit-down days, lost over $600,000
daily_pct = 125000 / 1500000 * 100
assert abs(daily_pct - 8.33) < 0.01, daily_pct  # his words: "nearly 10 percent" - arithmetic on 1.5M is 8.33%
five = 125000 * 5
assert five == 625000 and five > 600000
assert abs(600000 / 1500000 * 100 - 40.00) < 0.01
print("4 daily pct", round(daily_pct, 2), "five-day at daily rate", five, "600k is 40.00% of 1.5M")

# 5 salary yardstick: average annual salary $15,000 at the time
assert abs(125000 / 15000 - 8.33) < 0.01
assert 600000 / 15000 == 40.0
print("5 daily loss = 8.33 annual salaries, total >600k = 40 annual salaries")

# 6 options contest: 47 traders x $5,000 winner-take-all; $100,000 account to over $900,000 in 3 months
pot = 47 * 5000
assert pot == 235000, pot
assert 900000 / 100000 == 9.0
assert (900000 / 100000 - 1) * 100 == 800.0
print("6 contest pot", pot, "account multiple 9.00x, +800.00% (floor, he said over 900k)")

# 7 no-losing streak span: since 1980, interview era 1988 (book May 1989)
months = (1988 - 1980) * 12
weeks = (1988 - 1980) * 52
assert months == 96 and weeks == 416
weeks99 = (1999 - 1980) * 52
assert weeks99 == 988  # TheStreet 1999 reader: "approximately 1,000 perfect weeks" - arithmetic agrees
print("7 1980-1988:", months, "months,", weeks, "weeks; extended to 1999:", weeks99, "weeks")

# 8 last-two-years losers: 17 losers, 9 from quote-machine failure, 3 losing days
assert 17 - 9 == 8
assert abs(9 / 17 * 100 - 52.94) < 0.01
for n in (2000, 3000):
    wr = (n - 17) / n * 100
    print("8 trades", n, "win rate", round(wr, 2))
assert abs((2000 - 17) / 2000 * 100 - 99.15) < 0.01
assert abs((3000 - 17) / 3000 * 100 - 99.43) < 0.01
# Schwager paraphrase "vicinity of 99 percent" requires N >= 1700 for losers <= 1%
assert 17 / 1700 * 100 == 1.0
print("8 machine share of losers 52.94%, non-machine losers 8")

# 9 soybean revenge: watched low $4.75, bought ~$6.18, sold part $7.25, rest $9.92, high $10.46
assert abs((7.25 / 6.18 - 1) * 100 - 17.31) < 0.01
assert abs((9.92 / 6.18 - 1) * 100 - 60.52) < 0.01
assert abs((10.46 / 6.18 - 1) * 100 - 69.26) < 0.01
assert abs((6.18 / 4.75 - 1) * 100 - 30.11) < 0.01  # he bought 30.11% above the low - did not pick the bottom
capture = (9.92 - 6.18) / (10.46 - 6.18) * 100
assert abs(capture - 87.38) < 0.01, capture
print("9 revenge +17.31% / +60.52%, max +69.26%, captured", round(capture, 2), "% of the move")

# 10 the 250,000% figure belongs to Seykota, not Weinstein:
# preface "MIT electrical engineering graduate, computerized, 250,000% over sixteen years"
# Seykota chapter: one customer account $5,000 in 1972, up over 250,000% cash-on-cash as of mid-1988
assert 1988 - 1972 == 16
terminal = 5000 * (1 + 250000 / 100)
assert terminal == 12505000, terminal
print("10 Seykota account terminal >", terminal, "over 16 years - not a Weinstein figure")

print("ALL PASSED 10 groups")
