#!/usr/bin/env python3
"""Verify structural claims in Wealth of Nations note 01
(Introduction and Plan + Book I Ch. I, division of labour).
Numbers are Adam Smith's in-text workshop observations (1776),
recomputed here; not modern measurements, not business advice."""

# 1. Pin factory: 10 men, about 12 pounds a day, upwards of 4,000
# middling pins per pound -> upwards of 48,000 pins, 4,800 each.
workers, pounds, per_pound = 10, 12, 4000
total = pounds * per_pound
assert total == 48000 and total // workers == 4800

# 2. Working alone: at most 20 pins, perhaps not 1; ratios to 4,800
# are 1/240 and 1/4800 as Smith states.
assert 4800 // 20 == 240 and 4800 // 1 == 4800

# 3. Making a pin is divided into about eighteen operations.
pin_operations = 18
assert pin_operations == 18

# 4. Nail-making dexterity ladder: occasional smith at most 200-300,
# habitual but not specialist 800-1,000, specialist boys over 2,300.
nails = [300, 1000, 2300]
assert nails == sorted(nails) and len(set(nails)) == 3

# 5. Three causes of the productivity gain from division of labour.
causes = ["dexterity", "saving_switching_time", "invention_of_machines"]
assert len(causes) == 3

# 6. The five-book plan in fixed order.
books = ["distribution", "capital", "progress_of_opulence",
         "systems_of_political_economy", "revenue_of_sovereign"]
assert len(books) == 5 and books[0] == "distribution" and books[-1] == "revenue_of_sovereign"

print("01-division-of-labour-verify: all assertions passed")
print("  pins=48000 per_worker=4800 ratios=1/240,1/4800 ops=18 nails=300<1000<2300 causes=3 books=5")
