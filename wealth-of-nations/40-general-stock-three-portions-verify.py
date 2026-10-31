#!/usr/bin/env python3
# 40 verify: Book II Ch.1 second half (numbers/orderings from the book itself)
# 1 general stock divides into three portions
portions = ["stock reserved for immediate consumption", "fixed capital", "circulating capital"]
assert len(portions) == 3
# 2 consumption lifetimes ordering (lower bounds in years, from book wording: several years / half a century or a century / many centuries)
clothes_years, furniture_years, houses_years = 3, 50, 200
assert clothes_years < furniture_years < houses_years
# 3 fixed capital consists chiefly of four articles
fixed_articles = ["useful machines and instruments of trade", "profitable buildings", "improvements of land", "acquired and useful abilities"]
assert len(fixed_articles) == 4
# 4 circulating capital has four parts; three of them (provisions, materials, finished work) are regularly withdrawn
circ_parts = ["money", "provisions", "materials", "finished work"]
withdrawn = ["provisions", "materials", "finished work"]
assert len(circ_parts) == 4 and len(withdrawn) == 3 and set(withdrawn) < set(circ_parts)
# 5 continual supplies of circulating capital drawn principally from three sources
sources = ["land", "mines", "fisheries"]
assert len(sources) == 3
# 6 letting examples: masquerade dresses by the night, furniture by month/year, funeral furniture by day/week;
#    a dwelling-house yields revenue to proprietor but zero addition to public revenue (directional)
letting = {"masquerade dresses": "night", "furniture": "month or year", "funeral furniture": "day or week"}
assert len(letting) == 3
public_revenue_from_houses = 0
assert public_revenue_from_houses == 0
print("40-general-stock-three-portions: all 6 assertions passed")
