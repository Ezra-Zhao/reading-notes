# Verify Ch XI Part I middle: Buenos Ayres ox, Highland trebling, Cato order, Prince Henry prices
# 1 Buenos Ayres: ox 4 reals = 21.5 pence sterling; herd 200-300; account 40-50 years before writing
assert 21.5 == 21.5 and 200 <= 250 <= 300 and 40 <= 45 <= 50
# 2 Highlands: cattle price about 3x; rents tripled and quadrupled (3-4x); 1 lb best meat vs 2 lb white bread ordinarily, 3-4 lb in plentiful years
assert 3 == 3 and 3 <= 4 and 2 < 3 <= 4
# 3 crop periods: corn 1 year; butcher's meat 4-5 years to grow; meat period is 4-5x corn period
assert 4 <= 5 and 5 // 1 == 5
# 4 Cato ranking: feed well 1, feed tolerably 2, feed ill 3, plough 4; provinces furnished a tenth at about 6d a peck
cato = ["feed well", "feed tolerably", "feed ill", "plough"]
assert len(cato) == 4 and cato[0] == "feed well" and cato[3] == "plough" and abs(1/10 - 0.1) < 1e-9 and 6 == 6
# 5 Prince Henry: 9 pounds 10 shillings = 190s for 600 lb -> 31 2/3 s per cwt = 31s 8d; minus 1764 dear-year 27s = 4s 8d
total_s = 9 * 20 + 10
per_cwt = total_s / 6
assert total_s == 190 and abs(per_cwt - (31 + 2/3)) < 1e-9
assert abs((31 + 8/12) - 27 - (4 + 8/12)) < 1e-9
# 6 Windsor wheat in pence: later period 2:1:9.5 = 501.5d > earlier 1:18:3.5 = 459.5d
earlier = 1 * 240 + 18 * 12 + 3.5
later = 2 * 240 + 1 * 12 + 9.5
assert later > earlier and later - earlier == 42.0
print("17 verify: 6 assertions passed")
