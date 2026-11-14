"""Market Wizards 14 Paul Tudor Jones verification script (clean-room, self-written)
Checks six recomputable figures stated in the note; inputs are public-source figures
from the Wikipedia entry and its citations (checked 2026-11-14):
1) 1987 after-fee return 125.9% = 2.259x; popular gross/other-fund claim about 200% = 3.0x,
   gap about 74.1 percentage points - the two must not be mixed;
2) 1990 Japan short return 87.4% = 1.874x;
3) Fees 4% is 2.0x the 2% industry standard; 23% - 20% = 3 percentage points;
4) 1994 SEC fine USD 0.8m = 0.8% of the estimated USD 100m 1987 profit;
5) UVA gifts USD 44m + USD 12m = USD 56m = 56% of USD 100m;
6) Net worth USD 8.1bn / AUM USD 12bn (2022) = 67.5%; Robin Hood 1988 - Tudor 1980 = 8 years;
   founding age 1980 - 1954 = 26.
"""
assert round(1 + 125.9/100, 3) == 2.259
assert round((1 + 200/100) - (1 + 125.9/100), 3) == 0.741
print("1 ok: 1987 after-fee 125.9% = 2.259x; popular 200% = 3.0x; gap 74.1pp")
assert round(1 + 87.4/100, 3) == 1.874
print("2 ok: 1990 return 87.4% = 1.874x")
assert 4/2 == 2.0 and 23-20 == 3
print("3 ok: management fee 4% = 2.0x industry 2%; profit share diff 3pp")
assert round(0.8/100*100, 1) == 0.8
print("4 ok: SEC fine USD 0.8m = 0.8% of USD 100m")
assert 44+12 == 56 and round(56/100*100) == 56
print("5 ok: UVA gifts 44+12 = USD 56m = 56% of USD 100m")
assert round(8.1/12*100, 1) == 67.5 and 1988-1980 == 8 and 1980-1954 == 26
print("6 ok: net worth/AUM = 67.5%; Robin Hood 8 years after founding; founded at 26")
print("All six assertions passed")
