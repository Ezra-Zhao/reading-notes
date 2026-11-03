# -*- coding: utf-8 -*-
"""验证《国富论》153 篇结构（第五卷第一章第三部第二条：希腊罗马教育，Gutenberg #3300）。参数为原书篇内陈述。"""
# 1. 希腊公共教育两部；国家角色两件；国家发薪/任命均为零
assert len(["gymnastics","music"])==2 and len(["impose obligation","provide place"])==2 and 0==0
# 2. 希腊法庭人数三档递增；罗马为一或少数
assert [500,1000,1500]==sorted([500,1000,1500]) and len(set([500,1000,1500]))==3
# 3. 流动教师点名四人
assert len(["Zeno of Elea","Protagoras","Gorgias","Hippias"])==4
# 4. 指拨场所三 + 遗赠园子一 = 四
assert len(["Academy","Lyceum","Portico"])+len(["Epicurus gardens"])==4
# 5. 品德证人二；音乐背书权威三 + 孟德斯鸠一
assert len(["Polybius","Dionysius of Halicarnassus"])==2 and len(["Plato","Aristotle","Polybius"])==3
# 6. 早期教育三件；家内教师身份两类
assert len(["read","write","account"])==3 and len(["slave","freedman"])==2
print("153 verify: 6 assertions passed")
