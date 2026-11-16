#!/usr/bin/env python3
"""Verify arithmetic for note 34 (Tony Saliba). Inputs from public
sources cited in the note: Schwager Market Wizards chapter intro and
interview as reprinted/summarised by TurtleTrader and Macro Ops,
Gary Sinise Foundation biography (career start 1979, three years on
CBOE board, founder list), TurtleTrader biography (Kelley 1977,
27 traders by 1987, board 1987-1990, ITI 1989, LiquidPoint 1999 sold
to ConvergEx 2007), Novel Investor on the Teledyne 1984 tender
($200, about $30 above market, stock $302 by September)."""
from datetime import date

def close(a, b, tol=0.02):
    return abs(a - b) <= tol

# 1. Grubstake path spring 1979 (Schwager interview via Macro Ops)
assert close((75_000 / 50_000 - 1) * 100, 50.00, 0.01)
assert close((15_000 / 75_000 - 1) * 100, -80.00, 0.01)
assert close((15_000 / 50_000 - 1) * 100, -70.00, 0.01)
assert 50_000 - 15_000 == 35_000
print("1 stake OK 50k -> 75k in ~2 weeks = +50.00%; -> 15k in ~6 weeks = -80.00% from peak, -70.00% from stake, $35,000 gone")

# 2. The $300-a-day rebuild target (floor advice quoted in the interview)
assert 300 * 250 == 75_000
print("2 daily OK $300/day x 250 trading days = $75,000/year (250-day year is the quote's own arithmetic)")

# 3. Seventy consecutive months: length, and the ambiguous $100,000 wording
assert 70 // 12 == 5 and 70 % 12 == 10
assert close(70 / 12, 5.83, 0.01)
assert 70 * 100_000 == 7_000_000
print("3 streak OK 70 months = 5y10m = 5.83y; Schwager intro wording, if read as >$100k per month, implies >$7,000,000 total -- later blurbs say only 'profitable months', so the per-month reading is registered, not adopted")

# 4. Teledyne build-up path (interview): 160 -> 138 -> 150 -> halt 155
assert close((138 / 160 - 1) * 100, -13.75, 0.01)
assert close((150 / 138 - 1) * 100, 8.70, 0.01)
assert close((155 / 150 - 1) * 100, 3.33, 0.01)
print("4 teledyne path OK 160 -> 138 = -13.75%; 138 -> 150 = +8.70%; 150 -> 155 halt = +3.33%")

# 5. Teledyne tender premium and the $180 calls' intrinsic value
assert close((200 / 155 - 1) * 100, 29.03, 0.01)
assert 200 - 155 == 45
assert 200 - 30 == 170  # Novel Investor: $200 was about $30 above the market -> implies ~$170, a different moment than the $155 halt
assert 200 - 180 == 20 and 300 - 180 == 120 and 120 // 20 == 6
print("5 tender OK $200 vs $155 halt = +29.03% ($45 premium); Novel Investor's 'about $30 above market' implies ~$170 -- a different pricing moment, registered not merged; $180 call intrinsic $20 at tender, $120 at $300 = 6x")

# 6. Teledyne eventual top: interview $300 vs Novel Investor $302 by September
assert close((300 / 155 - 1) * 100, 93.55, 0.01)
assert close((302 / 155 - 1) * 100, 94.84, 0.01)
assert close((302 / 300 - 1) * 100, 0.67, 0.01)
print("6 top OK 155 -> 300 = +93.55% (interview); 155 -> 302 = +94.84% (Novel Investor, September, highest-priced NYSE stock); the two tops differ by only 0.67%")

# 7. Arrival-year conflict and board tenure
assert 1979 - 1978 == 1
assert 1990 - 1987 == 3  # TurtleTrader bio line: board 1987-1990; Sinise bio: three years on the board -- consistent
assert 1979 - 1977 == 2  # Kelley graduation 1977 (TurtleTrader) to CBOE start 1979 (Sinise)
print("7 timeline OK Schwager intro arrival 1978 vs later bios' 1979 start = 1y conflict, registered; board 1987-1990 spans 3 years, matching the Sinise bio's 'three years'; Kelley 1977 -> CBOE 1979 = 2y")

# 8. Team scale by 1987 (TurtleTrader)
assert 1987 - 1979 == 8 and 1987 - 1978 == 9
print("8 team OK clerk to 27 traders working under him by 1987 = 8y after a 1979 start, 9y after a 1978 start (both registered with the arrival conflict)")

# 9. October 1987: puts at parity, and the 95% hold
assert 30 - 30 == 0  # puts 30 points in the money trading at $30: time value = 0
assert 100 - 95 == 5
print("9 crash OK puts 30 points ITM quoted at $30 = parity, time value $0 (his stated reason for not covering); he held 95% at Monday's close, so at most 5% had been covered")

# 10. Institution building (TurtleTrader; $250M sale figure via Liquid Mercury interview)
assert 1989 - 1979 == 10
assert 2007 - 1999 == 8
assert 250_000_000 // 1_000_000 == 250
print("10 firms OK ITI founded 1989 = 10y after 1979 start; LiquidPoint 1999 -> sold to ConvergEx 2007 = 8y; sale reported at $250M in the Liquid Mercury interview, a nine-figure sum consistent in order with TurtleTrader's 'mid-nine-figure' wording")

print("ALL PASS")
