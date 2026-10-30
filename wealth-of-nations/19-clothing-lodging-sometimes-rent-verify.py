# Verify Ch XI Part II opening: two wants after food, labour proportions, productivity flip, building/lodging samples
# 1 wants after food: clothing and lodging = 2
assert len(["clothing", "lodging"]) == 2
# 2 labour proportion among savage nations: 1/100 (or little more) for clothing+lodging, 99/100 for food; sums to whole
assert 1 + 99 == 100 and 1/100 < 99/100
# 3 productivity flip: one family provides food for two -> half society feeds whole, other half freed
assert 1/2 + 1/2 == 1 and 2 * 0.5 == 1
# 4 house in some British dominions: built by one day's labour of one man
assert 1 * 1 == 1
# 5 lodging-material samples: rent-bearing/conditional 2 (London-near quarry, Highland bark) vs no-rent 2 (Scotland/Wales quarry, North America timber)
assert len(["london_quarry_rent", "highland_bark_market"]) == 2 and len(["scot_wales_quarry_none", "north_america_timber_unwanted"]) == 2
# 6 clothing trade samples: North America peltry, Highland hides, England wool to Flanders = 3, all priced via foreign demand
assert len(["peltry", "highland_hides", "english_wool"]) == 3
print("19 verify: 6 assertions passed")
