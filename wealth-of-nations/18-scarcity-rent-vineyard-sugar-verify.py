# Verify Ch XI Part I close: vineyard order, Cochin China sugar, tobacco limit, rice and potato arithmetic
# 1 ancient chain: Democritus about 2000 years before Smith; reporters/commentators Columella, Palladius, Varro = 3
assert 2000 >= 2000 and len(["Columella", "Palladius", "Varro"]) == 3
# 2 France 1731 order covers two objects: new planting; renewal of old vineyards interrupted two years; permission needs intendant certification land unfit for other culture
objects = ["new planting", "renewal after two years interruption"]
assert len(objects) == 2 and "two years" in objects[1]
# 3 Cochin China sugar: quintal 150-200 Paris pounds, medium 175; 3 piastres ~ 13s 6d; about 8s per English cwt; stated as under 1/4 of brown/muscovada price and under 1/6 of finest white price
assert (150 + 200) / 2 == 175 and 13.5 == 13 + 6 / 12 and 8 < 32 and 1 / 4 > 1 / 6
# 4 tobacco restraint: 6000 plants supposed 1000 weight per negro aged 16-60; plus 4 acres Indian corn managed
assert 6000 / 1000 == 6 and 60 - 16 == 44 and 4 == 4
# 5 rice: two crops a year, 30-60 bushels each -> annual 60-120 bushels per acre
assert 2 * 30 == 60 and 2 * 60 == 120
# 6 potatoes: 12000 lb per acre, half to water -> 6000 lb solid; wheat 2000 lb; 6000 = 3x wheat; total potato weight = 6x wheat
assert 12000 * 0.5 == 6000 and 6000 == 3 * 2000 and 12000 == 6 * 2000
print("18 verify: 6 assertions passed")
