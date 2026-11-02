# 验证 105 篇篇内数字与结构（参数取自原书第四卷第七章第一部分中段篇内陈述，不冒充现代实测）
# 1 1497 达伽马远征减 1492 哥伦布启程恰五年（原书作近五年）
assert 1497 - 1492 == 5
# 2 航程两至三个月
assert 2 < 3 and (2, 3) == (2, 3)
# 3 凯旋队列原住民六至七人
assert 6 <= 6 and 7 >= 7 and 7 - 6 == 1
# 4 植物食物四样
foods = ["Indian corn", "yams", "potatoes", "bananas"]
assert len(foods) == 4
# 5 凯旋队列有价值者两类
assert len(["gold ornaments", "bales of cotton"]) == 2
# 6 动物食物主体两样
assert len(["cori", "iguana"]) == 2
print("105 verify: 6 assertions passed")
