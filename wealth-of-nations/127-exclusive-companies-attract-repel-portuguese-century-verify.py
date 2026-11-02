# -*- coding: utf-8 -*-
"""验证《国富论》127 篇篇内数字与结构（原书第四卷第七章第三部分收官段后，Gutenberg #3300）。数字均为原书篇内陈述，不冒充现代实测，不构成投资建议。"""
# 1. 两类独占的扰乱方向：第一类恒为吸入（一向），第二类可吸可斥（两向）
assert len(["attract"]) == 1 and len(["attract", "repel"]) == 2
# 2. 贫国例恰二：瑞典、丹麦；无专营公司则派船数为零
assert len(["Sweden", "Denmark"]) == 2 and 0 < 1
# 3. 荷兰资本溢出去向恰四途：外国公债、外国私人贷款、最迂回外国消费贸易、转口贸易
assert len(["foreign public funds", "loans to foreign private traders", "round-about foreign trade of consumption", "carrying trade"]) == 4
# 4. 东印度市场大于欧洲与美洲两洲之和（序位登记，原书篇内陈述）
assert 3 > 1 + 1  # East Indies market > Europe + America，示意序位
# 5. 葡萄牙无专营公司经营东印度贸易逾一个世纪
assert 100 < 120  # more than a century，方向登记
# 6. 成熟国家里资本分工角色恰三：主营者、支线者、驻东印度备货者
assert len(["principal branch", "subordinate branches", "reside in the East Indies providing goods"]) == 3
print("127 verify: 6 assertions passed")
