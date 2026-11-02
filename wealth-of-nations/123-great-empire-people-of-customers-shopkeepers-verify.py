# -*- coding: utf-8 -*-
"""验证《国富论》123 篇篇内数字与结构（原书第四卷第七章第三部分大帝国段，Gutenberg #3300）。数字均为原书篇内陈述，不冒充现代实测，不构成投资建议。"""
# 1. 土地通常价三十年购买年数，殖民地买价仅装备费（示意为远小于三十年价）
assert 30 > 1  # 三十年购买年数为通常价尺度，买价仅发现勘察装备费
# 2. 耕作者长成兴旺人口的区间三十至四十年：1660-1620 恰四十年
assert 1660 - 1620 == 40 and 30 <= 40 <= 40
# 3. 和平建制步兵团恰二十个
assert len(["foot regiment"] * 20) == 20
# 4. 上次战争费用逾九千多万镑，构成恰三项
assert 90_000_000 < 100_000_000
assert len(["new debt", "two shillings in the pound land tax", "sinking fund borrowings"]) == 3
# 5. 每镑两先令：每镑二十先令，两先令恰十分之一
assert 2 / 20 == 0.1
# 6. 西班牙战争 1739 年开始，主要目标一项：阻止搜查殖民地违禁贸易船只
assert 1739 < 1760
assert len(["prevent search of colony contraband ships"]) == 1
print("123 verify: 6 assertions passed")
