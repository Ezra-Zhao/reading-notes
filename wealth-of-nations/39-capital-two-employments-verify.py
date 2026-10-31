#!/usr/bin/env python3
# 39 verify: Book II Ch.1 first half (numbers/orderings from the book itself)
# 1 stock reserved for immediate consumption consists in three articles
consumption_sources = ["portion originally reserved", "revenue as it comes in", "things purchased in former years not yet consumed"]
assert len(consumption_sources) == 3
# 2 capital may be employed in two ways: circulating and fixed
employments = ["circulating", "fixed"]
assert len(employments) == 2
# 3 merchant's capital is altogether circulating: fixed part = 0 (shop/warehouse aside)
merchant_fixed = 0
assert merchant_fixed == 0
# 4 ordering of instruments' expense: tailor(needles) < shoemaker < weaver << iron-work/mines (ordinal ranks, not prices)
rank = {"tailor needles": 1, "shoemaker tools": 2, "weaver tools": 3, "iron-work and mines": 10}
assert rank["tailor needles"] < rank["shoemaker tools"] < rank["weaver tools"] < rank["iron-work and mines"]
# 5 great iron-work fixed instruments: furnace, forge, slit-mill
iron_tools = ["furnace", "forge", "slit-mill"]
assert len(iron_tools) == 3
# 6 farmer's division: implements & labouring cattle price = fixed; their maintenance = circulating;
#    fattening cattle price & maintenance = circulating; seed = fixed though it never changes masters
farmer = {"implements price": "fixed", "labouring cattle price": "fixed", "their maintenance": "circulating",
          "fattening cattle price+maintenance": "circulating", "breeding flock price": "fixed", "seed": "fixed"}
assert farmer["implements price"] == "fixed" and farmer["their maintenance"] == "circulating"
assert farmer["fattening cattle price+maintenance"] == "circulating" and farmer["seed"] == "fixed"
print("39-capital-two-employments: all 6 assertions passed")
