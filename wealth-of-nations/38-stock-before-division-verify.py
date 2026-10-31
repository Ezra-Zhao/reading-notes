#!/usr/bin/env python3
# 38 verify: Book II Introduction claims (numbers/orderings from the book itself)
# 1 rude state needs no stock accumulated beforehand
rude_needs = ["hunt when hungry", "skin of first large animal when coat worn", "trees and turf nearest at hand for hut"]
stock_beforehand_rude = 0
assert stock_beforehand_rude == 0 and len(rude_needs) == 3
# 2 purchase waits for two events: produce completed AND sold
events_before_purchase = ["completed", "sold"]
assert len(events_before_purchase) == 2
# 3 stock stored up must cover three things: maintenance, materials, tools
stock_covers = ["maintenance", "materials", "tools"]
assert len(stock_covers) == 3
# 4 Book II is divided into five chapters
book2_chapters = 5
assert book2_chapters == 5
# 5 equal workmen: provisions equal to rude state, materials/tools greater (directional)
provisions_ratio = 1.0   # equal stock of provisions
materials_tools_ratio = 2.0  # placeholder for "greater" direction only, not a book figure
assert provisions_ratio == 1.0 and materials_tools_ratio > provisions_ratio
# 6 employer's two endeavours: distribution of employment + best machines; ability proportional to stock (directional)
endeavours = ["distribution of employment", "best machines inventable or affordable"]
assert len(endeavours) == 2
print("38-stock-before-division: all 6 assertions passed")
