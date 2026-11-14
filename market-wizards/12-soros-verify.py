"""Market Wizards 12 Soros verification script (clean-room, self-written)
Checks six recomputable figures stated in the note; inputs are public-source figures:
1) Quantum 1969-1980 +3365% = 34.65x vs S&P +47% = 1.47x, ratio about 23.6x;
2) USD 1,000 invested in 1969, dividends reinvested, about USD 2.15m in 1995 = 2150x;
3) ERM central rate DM 2.9500, floor DM 2.7780: room from central to floor 5.8%;
   a fall of about 15% is about 2.6x that room (asymmetry illustration, my calculation);
4) 1992 short position about USD 10bn, reported profit about USD 1bn = 10.0% of notional;
5) 1981: USD 400m fund, -22% loss year = USD 312m before redemptions, then redemptions to about USD 200m;
6) 1998 Russia loss about USD 2bn = 2.0x the reported 1992 profit of about USD 1bn;
   2013 gain USD 5.5bn is 13.75% of the USD 40bn cumulative since 1973 inception (reported 2013).
"""
assert round(1 + 3365 / 100, 2) == 34.65 and round(1 + 47 / 100, 2) == 1.47
assert round(34.65 / 1.47, 1) == 23.6
print("1 ok: 1969-1980 Quantum 34.65x vs S&P 1.47x, ratio 23.6x")
assert round(2150000 / 1000) == 2150
print("2 ok: USD 1,000 in 1969 to about USD 2.15m in 1995 = 2150x")
room = (2.95 - 2.778) / 2.95 * 100
assert round(room, 1) == 5.8
assert round(15 / room, 1) == 2.6
print("3 ok: ERM central-to-floor room 5.8%; a 15% fall is about 2.6x that room")
assert round(1 / 10 * 100, 1) == 10.0
print("4 ok: profit USD 1bn on about USD 10bn notional = 10.0%")
assert round(400 * (1 - 0.22), 0) == 312
print("5 ok: USD 400m after -22% = USD 312m before redemptions (then to about USD 200m)")
assert round(2 / 1, 1) == 2.0
assert round(5.5 / 40 * 100, 2) == 13.75
print("6 ok: Russia loss USD 2bn = 2.0x 1992 profit; 2013 USD 5.5bn = 13.75% of USD 40bn cumulative")
print("All six assertions passed")
