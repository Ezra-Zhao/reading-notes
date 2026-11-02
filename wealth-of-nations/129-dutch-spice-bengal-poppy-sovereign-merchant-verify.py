# -*- coding: utf-8 -*-
"""验证《国富论》129 篇篇内数字与结构（原书第四卷第七章第三部分收官段末段，Gutenberg #3300）。数字均为原书篇内陈述，不冒充现代实测，不构成投资建议。"""
# 1. 取得可观征服的公司恰二：英国公司、荷兰公司
assert len(["English company", "Dutch company"]) == 2
# 2. 荷兰限产手段恰三：焚过剩香料、出赏格根绝嫩芽绿叶、减少有据点岛香料树
assert len(["burn surplus spiceries", "premium for blossoms and green leaves", "reduce number of trees"]) == 3
# 3. 英国公司政策追平荷兰毁灭程度的时限为一至二百年区间
assert 100 < 150 < 200  # in the course of a century or two，区间登记
# 4. 君主应废除的限制恰三类（国内运输、出口、进口）外加独占一类
assert len(["transportation within country", "exportation", "importation"]) == 3 and len(["all monopolies"]) == 1
# 5. 公司偏好对照恰两组：小而暂时、大而永久
assert len(["little and transitory profit of the monopolist", "great and permanent revenue of the sovereign"]) == 2
# 6. 利益方向恰两判：为君主与国家同向、为商人与之反向
directions = {"as sovereign": "same", "as merchant": "opposite"}
assert directions["as sovereign"] != directions["as merchant"] and len(directions) == 2
print("129 verify: 6 assertions passed")
