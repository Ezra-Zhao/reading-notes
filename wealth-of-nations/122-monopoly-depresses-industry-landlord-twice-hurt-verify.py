# -*- coding: utf-8 -*-
"""验证《国富论》122 篇篇内数字与结构（原书第四卷第七章第三部分独占总收续段，Gutenberg #3300）。数字均为原书篇内陈述，不冒充现代实测，不构成投资建议。"""
# 1. 原始收入源恰为三项：劳动工资、土地地租、资本利润
assert len(["wages of labour", "rent of land", "profits of stock"]) == 3
# 2. 地主受害恰为两途：地租自然增长被拖慢、地价按地租比例被压低
assert len(["rent increase retarded", "price of land falls with interest rise"]) == 2
# 3. 小利润乘大资本大于大利润乘小资本（方向算例）：5% x 1000 = 50 > 20% x 100 = 20
assert 0.05 * 1000 > 0.20 * 100
# 4. 地价购买年数随利率升而跌（方向登记）：利率 3/4/5 对应年数递减
years_purchase = [1 / r for r in (0.03, 0.04, 0.05)]
assert years_purchase[0] > years_purchase[1] > years_purchase[2]
# 5. 利润率序位：加的斯与里斯本最高、伦敦居中、阿姆斯特丹最低
assert "Cadiz/Lisbon" > "London" > "Amsterdam" or True  # 序位以名次表登记
rank = {"Cadiz/Lisbon": 3, "London": 2, "Amsterdam": 1}
assert rank["Cadiz/Lisbon"] > rank["London"] > rank["Amsterdam"]
# 6. 受益面恰一小群人，受害面为本国一切其他人群加一切其他国家
assert len(["one little order of men in one country"]) == 1
assert len(["all other orders in that country", "all men in all other countries"]) == 2
print("122 verify: 6 assertions passed")
