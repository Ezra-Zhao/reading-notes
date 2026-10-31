#!/usr/bin/env python3
# 41 verify: Book II Ch.2 first part (gross vs neat revenue; numbers/structure from the book itself)
# 1 price of annual produce resolves into the same three parts as a single commodity
parts = ["wages of labour", "profits of stock", "rent of land"]
assert len(parts) == 3
# 2 real wealth is in proportion to neat revenue, not gross (directional)
neat, gross = 80, 100  # illustrative: deductions removed from gross
assert 0 < neat < gross
# 3 neat revenue = gross annual produce minus maintenance of fixed capital first, then circulating capital
gross_produce = 1000
fixed_maint, circ_maint = 120, 80
neat_revenue = gross_produce - fixed_maint - circ_maint
assert neat_revenue == 800 and fixed_maint > 0 and circ_maint > 0
# 4 wages of labour maintaining fixed capital may enter neat revenue, but its materials and produce do not (directional flags)
wage_price_can_enter_neat = True
materials_or_produce_enter_neat = False
assert wage_price_can_enter_neat and not materials_or_produce_enter_neat
# 5 manufactory example: machinery maintenance 1000 a-year reduced to 500 frees 500 for materials and workmen
before, after = 1000, 500
freed = before - after
assert freed == 500 and after == before // 2
# 6 circulating capital has four parts; money is the only one whose maintenance can diminish neat revenue
circ_parts = ["money", "provisions", "materials", "finished work"]
diminishing = ["money"]
assert len(circ_parts) == 4 and diminishing == ["money"]
print("41-gross-neat-revenue: all 6 assertions passed")
