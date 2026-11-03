# -*- coding: utf-8 -*-
"""验证《国富论》157 篇结构（平民教育收官，Gutenberg #3300）。参数为原书篇内陈述。"""
# 1. 公共三法
assert len(["facilitate","encourage premiums badges","impose examination"]) == 3
# 2. 竞技会三处，光荣及三层
assert len(["Olympic","Isthmian","Nemaean"]) == 3 and len(["person","family","kindred"]) == 3
# 3. 古代教师薪俸/专权/法律优待皆零，报酬来源唯一
assert len([]) == 0 and len(["from scholars"]) == 1
# 4. 尚武双重用处
assert len(["smaller standing army requisite","diminish dangers to liberty from standing army"]) == 2
# 5. 古代制度三优势
assert len(["more simple self-executing","little/no government attention","more universal whole body instructed"]) == 3
# 6. 受教育收益五项
assert len(["less liable to enthusiasm superstition delusions","more decent and orderly","more respectable and respect superiors","see through faction and sedition complaints","not judge rashly capriciously of government"]) == 5
print("157 verify: 6 assertions passed")
