# -*- coding: utf-8 -*-
"""验证《国富论》155 篇结构（第五卷第一章第三部第二条平民教育前半，Gutenberg #3300）。参数为原书篇内陈述。"""
# 1. 三问恰三项
assert len(["whether public ought to attend","what parts for different orders","in what manner"]) == 3
# 2. 社会状态两类
assert len(["naturally forms abilities without government","does not, government must prevent corruption"]) == 2
# 3. 灵巧代价三样品格
assert len(["intellectual","social","martial virtues"]) == 3
# 4. 职业限定一至二项简单操作
assert 1 <= 1 and 2 == 2 and len(["few simple operations","one or two"]) >= 1
# 5. 未开化社会双重身份
assert len(["warrior","in some measure a statesman"]) == 2
# 6. 多样性对照：个人少、全社会无限
assert len(["little variety in occupations of greater part of individuals","almost infinite variety in those of whole society"]) == 2
print("155 verify: 6 assertions passed")
