"""Market Wizards 10 Druckenmiller verification script (clean-room, self-written)
Checks six recomputable figures stated in the note; all inputs are public-report figures, not audited accounts:
1) 30% a year for 30 years compounds to about 2620x (USD 10,000 to about USD 26.2m);
2) Closing AUM about USD 12bn vs starting about USD 0.9m is about 13,333x;
3) Initial pound short USD 1.5bn on a USD 7bn fund is about 21.4% of the fund;
4) A USD 200m internet short losing USD 600m is a loss of 3x the position size;
5) USD 6bn of tech stocks losing USD 3bn is a 50% loss;
6) Quantum assets from USD 1bn to USD 20bn is 20x.
"""
assert round(1.30 ** 30, 1) == 2620.0
print("1 ok: 30% x 30y = 2620.0x")
assert round(12000 / 0.9, 1) == 13333.3
print("2 ok: 12bn / 0.9m = 13333.3x AUM growth")
assert round(1.5 / 7 * 100, 1) == 21.4
print("3 ok: initial pound short = 21.4% of fund")
assert 600 / 200 == 3
print("4 ok: 600m loss = 3x the 200m short")
assert 3 / 6 == 0.5
print("5 ok: 3bn / 6bn = 50% loss")
assert 20 / 1 == 20
print("6 ok: Quantum 1bn to 20bn = 20x")
print("All six assertions passed")
