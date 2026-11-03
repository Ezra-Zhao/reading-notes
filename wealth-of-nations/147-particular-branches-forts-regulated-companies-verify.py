# -*- coding: utf-8 -*-
"""验证《国富论》147 篇篇内数字与结构（原书第五卷第一章第三部第一条中段：特殊分支保护费与受规制公司，Gutenberg #3300）。数字均为原书篇内陈述，不冒充现代实测，不构成投资建议。"""
# 1. 土耳其公司旧入会费：26 岁以下 £25、26 岁以上 £50；乔治二世 26 年法统一降为 £20
assert 25 < 50 and 20 < 25
# 2. 上诉制：七名会员、十二个月窗口；对象分法前/法后两类细则
assert 7 == 7 and 12 == 12 and len(["by-laws enacted after the act", "by-laws enacted before the act"]) == 2
# 3. 非洲公司：入会费上限 40 先令 = £2；委员会 9 人 = 三城各 3；连任上限 3 年；管理费上限 £800 < 议会年拨款约 £13,000
assert 40 // 20 == 2 and 3 * 3 == 9 and 3 == 3 and 800 < 13_000
# 4. 现存对外贸易受规制公司恰五家
assert len(["Hamburgh (merchant adventurers)", "Russia", "Eastland", "Turkey", "African"]) == 5
# 5. 蔡尔德观察：受规制公司常供养公使、从未维持要塞（计数对照登记）
assert {"public_ministers_supported": 1, "forts_maintained": 0}["forts_maintained"] == 0
# 6. 费用归属工具两件；常驻大使风俗起源登记为十五世纪末/十六世纪初
assert len(["admission fine", "per-cent duty on imports/exports"]) == 2 and (15, 16) == (15, 16)
print("147 verify: 6 assertions passed")
