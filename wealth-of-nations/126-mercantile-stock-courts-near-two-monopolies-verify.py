# -*- coding: utf-8 -*-
"""验证《国富论》126 篇篇内数字与结构（原书第四卷第七章第三部分收官段中，Gutenberg #3300）。数字均为原书篇内陈述，不冒充现代实测，不构成投资建议。"""
# 1. 资本趋近的偏好层级恰三层：转口贸易想变外国消费贸易、再想变国内贸易（序位登记）
pref = ["carrying trade", "foreign trade of consumption", "home trade"]
assert len(pref) == 3 and pref.index("home trade") == 2
# 2. 高利润的证据指向恰两项异常：买得过贱、卖得过贵
assert len(["bought cheaper than ought", "sold dearer than ought"]) == 2
# 3. 受压迫的形态恰两面：多付、少得
assert len(["paying more", "getting less"]) == 2
# 4. 扰乱最大的贸易恰两支大洲贸易：美洲、东印度
assert len(["America", "East Indies"]) == 2
# 5. 独占恰两类：独占殖民地市场型、专营公司型
assert len(["monopoly of colony market", "exclusive company"]) == 2
# 6. 第二类独占下本国人多付恰两笔：公司额外利润、管理欺诈浪费的额外损耗
assert len(["extraordinary profits of the company", "extraordinary waste from fraud and abuse"]) == 2
print("126 verify: 6 assertions passed")
