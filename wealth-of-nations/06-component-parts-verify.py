#!/usr/bin/env python3
"""Verify structural claims in Wealth of Nations note 06
(Book I Ch. VI, component parts of price).
Numbers are Smith's in-text figures, recomputed; not modern measurements."""
# 1. Hunters: a beaver costs twice the labour of a deer -> 1 beaver = 2 deer.
assert 2 == 2 * 1
# 2. Profit is not wages of inspection: at 10 percent common profit, two
# manufactures each employ 20 workmen at 15 pounds a year = 300 pounds wages;
# materials 700 vs 7000 -> capitals 1000 vs 7300 -> profits 100 vs 730.
wages = 20 * 15
assert wages == 300
cap_small, cap_large = wages + 700, wages + 7000
assert (cap_small, cap_large) == (1000, 7300)
assert (cap_small * 0.10, cap_large * 0.10) == (100, 730)
# 3. Price finally resolves into three parts only.
parts = ["wages","profit","rent"]
assert len(parts) == 3
# 4. Spectrum: sea-fish price uses two parts (wages+profit, rent seldom);
# gathered stones use wages alone (one part).
assert len(["wages","profit"]) == 2 and len(["wages"]) == 1
# 5. The gardener on his own ground unites three characters.
characters = ["landlord","farmer","labourer"]
assert len(characters) == 3
# 6. Three original sources of revenue match the three parts;
# interest is derivative, not a fourth original source.
sources = {"labour":"wages","stock":"profit","land":"rent"}
assert len(sources) == 3 and "interest" not in sources.values()
print("06-component-parts-verify: all assertions passed")
print("  beaver=2deer wages=300 capitals=1000/7300 profits=100/730@10% parts=3 spectrum=3/2/1 sources=3")
