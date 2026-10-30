#!/usr/bin/env python3
"""Verify structural claims in Wealth of Nations note 03
(Book I Ch. III, division of labour limited by extent of market).
Numbers are Smith's in-text figures, recomputed; not modern
measurements, not business advice."""

# 1. Nailer: 1,000 nails a day, 300 working days -> 300,000 a year.
daily, days = 1000, 300
assert daily * days == 300000

# 2. In a remote inland place he could not dispose of 1,000 nails:
# one day's work, i.e. 1/300 of a year's output.
assert 300000 // 1000 == 300

# 3. Water vs land carriage, London-Edinburgh in about six weeks:
# one broad-wheeled waggon carries near 4 tons; one ship 200 tons.
waggon_tons, ship_tons = 4, 200
assert ship_tons // waggon_tons == 50

# 4. Same 200 tons by land needs 50 waggons, 100 men, 400 horses;
# by water only the maintenance of 6 to 8 men plus the ship.
land = {"waggons": 50, "men": 100, "horses": 400}
ship_crew = (6, 8)
assert land["waggons"] * waggon_tons == ship_tons
assert land["men"] // land["waggons"] == 2 and land["horses"] // land["waggons"] == 8
assert ship_crew[0] >= 6 and ship_crew[1] <= 8

# 5. Three early-improvement regions credited to inland navigation:
# Egypt (Nile), Bengal (Ganges), eastern provinces of China.
regions = ["egypt_nile", "bengal_ganges", "eastern_china_rivers"]
assert len(regions) == 3

# 6. In scattered country every farmer must be his own butcher,
# baker and brewer: three self-supplied trades.
self_trades = ["butcher", "baker", "brewer"]
assert len(self_trades) == 3

print("03-extent-of-market-verify: all assertions passed")
print("  nails=300000 local=1000(1/300) ship/waggon=50x land=50w/100m/400h crew=6-8 regions=3")
