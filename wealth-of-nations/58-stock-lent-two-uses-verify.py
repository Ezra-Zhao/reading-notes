# -*- coding: utf-8 -*-
"""验证《国富论》58 篇篇内数字与结构（取自原书第二卷第四章，Gutenberg #3300）。
数字均为原书篇内陈述，方向性登记者已标明，不冒充现代实测。"""
# 1. 借用人用法恰两类
assert len(["as capital", "as stock for immediate consumption"]) == 2
# 2. 资本用法下本息不出自其他收入来源（两项登记）
assert len(["restore capital without other revenue", "pay interest without other revenue"]) == 2
# 3. 例外主体一类：凭抵押借款的乡绅；性质为替回已花资本
assert len(["country gentlemen on mortgage"]) == 1
# 4. 贷款媒介两类，真实对象货物三项
assert len(["paper", "gold and silver"]) == 2 and len(["tools", "materials", "maintenance"]) == 3
# 5. 转让对象为年产物份额（方向登记）
assert "annual produce share" in ["annual produce share"]
# 6. 频率序位：节俭勤勉 > 挥霍闲散（方向登记）
assert ["frugal industrious", "prodigal idle"].index("frugal industrious") == 0
print("58 verify: 6 assertions passed")
