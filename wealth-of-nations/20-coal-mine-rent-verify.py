# Verify Ch XI Part II coal: three classes, wood ceiling, rent shares, purchase years, lowest price
from fractions import Fraction
# 1 three classes by (profit, rent): barren (no, no), barely (profit, no rent, landlord-worked), fertile-but-remote (would-be profit, unsold)
classes = {"barren": (False, False), "barely_landlord_worked": (True, False), "fertile_remote_unsold": (True, False)}
assert len(classes) == 3 and classes["barren"] == (False, False)
# 2 ceiling: at consumption place coal expense generally somewhat less than wood expense; coal price cannot rise above wood parity
wood, coal_typical = Fraction(1,1), Fraction(9,10)
assert coal_typical < wood  # direction only: coal < wood per text, 9/10 is a placeholder for "somewhat less", not a text figure
# 3 rent shares descending: surface estate commonly 1/3 > coal very great rent 1/5 > coal common rent 1/10
assert Fraction(1,3) > Fraction(1,5) > Fraction(1,10)
# 4 purchase years: land 30 years considered moderate, coal mine 10 years a good price; ratio 3
assert 30 // 10 == 3
# 5 most fertile neighbourhood mine regulates price by underselling: its price < neighbours' price
assert Fraction(99,100) < 1
# 6 lowest long-run price components: stock replacement + ordinary profits = 2 components, rent component = 0 at such a mine
components = ["replace_stock", "ordinary_profits"]
assert len(components) == 2 and "rent" not in components
print("20 verify: 6 assertions passed")
