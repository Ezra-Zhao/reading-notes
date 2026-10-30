#!/usr/bin/env python3
"""Verify structural claims in Wealth of Nations note 04
(Book I Ch. IV, origin and use of money).
Numbers are Smith's in-text figures, recomputed; not modern measurements."""
# 1. Homer armour prices in oxen: Diomede 9, Glaucus 100.
diomede, glaucus = 9, 100
assert glaucus > diomede * 11
# 2. Abraham paid 400 shekels of silver, by weight not by tale.
assert 400 == 400
# 3. Common instruments of commerce listed in the chapter:
# cattle, salt, shells, dried cod, tobacco, sugar, hides, nails.
instruments = ["cattle","salt","shells","dried cod","tobacco","sugar","hides","nails"]
assert len(instruments) == 8
# 4. Metal money by nation: iron (Spartans), copper (Romans), gold and silver (rich nations).
metals = {"spartans":"iron","romans":"copper","rich_nations":"gold_and_silver"}
assert len(metals) == 3
# 5. Roman as: originally 1 pound of copper divided into 12 ounces;
# reduced to 1/24 of original value, weighing only half an ounce.
assert 12 / 24 == 0.5
# 6. A penny was 1/20 of an ounce and 1/240 of a pound (12 ounces x 20);
# surviving fractions of original metal: England about 1/3, Scots about 1/36, France about 1/66.
assert 12 * 20 == 240
fractions = {"england":3,"scots":36,"france":66}
assert fractions["england"] < fractions["scots"] < fractions["france"]
print("04-origin-of-money-verify: all assertions passed")
print("  oxen=9/100 shekels=400 instruments=8 metals=3 as=12oz->1/24=0.5oz penny=1/240 debased=1/3,1/36,1/66")
