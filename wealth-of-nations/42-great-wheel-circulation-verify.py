#!/usr/bin/env python3
# 42 verify: Book II Ch.2 middle (money resembles fixed capital; wheel vs goods)
# 1 resemblance has three points
resemblances = ["expense to erect/collect and to support is a deduction from neat revenue",
                "makes no part of gross or neat revenue",
                "every saving in that expense improves neat revenue"]
assert len(resemblances) == 3
# 2 in computing revenue, the whole value of money must be deducted: revenue = goods only, money adds zero
goods, money = 5000, 900
revenue = goods + money - money
assert revenue == goods and revenue != goods + money
# 3 two senses of a sum of money (book examples): England circulating money computed at 18 millions (metal sense);
#   a man worth 50 or 100 pounds a-year (goods/purchasing-power sense)
england_metal_millions = 18
income_examples = [50, 100]
assert england_metal_millions == 18 and income_examples == [50, 100]
# 4 guinea pension: revenue equals the guinea's worth (goods), counted once, never guinea plus its worth
guinea, guineas_worth = 1, 1
weekly_revenue = guineas_worth
assert weekly_revenue == 1 and weekly_revenue != guinea + guineas_worth
# 5 same guinea pays three pensions on three successive days: metal stock 1 serves revenue payments of 3
payments = ["day1 pension A", "day2 pension B", "day3 pension C"]
metal_pieces = 1
assert len(payments) == 3 and metal_pieces < len(payments)
# 6 capital split: while whole capital is unchanged, the smaller the fixed part the greater the circulating part
whole = 1000
for fixed in (600, 400, 200):
    circulating = whole - fixed
    assert fixed + circulating == whole
assert (whole - 200) > (whole - 600)
print("42-great-wheel-circulation: all 6 assertions passed")
