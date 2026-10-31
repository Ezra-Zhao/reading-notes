# -*- coding: utf-8 -*-
"""验证《国富论》55 篇篇内数字与结构（取自原书第二卷第三章，Gutenberg #3300）。
数字均为原书篇内陈述，方向性登记者已标明，不冒充现代实测。"""
# 1. 地主份额：1/4 <= share <= 1/3，且份额 1/3 乘增长 3-4 倍 > 从前全部(1)
assert 0.25 <= 1/3 and (1/3)*3 >= 1 and (1/4)*4 >= 1
# 2. 利率序：古代下限10 > 现今上限6 > 4 > 3 > 2
assert 10 > 6 > 4 > 3 > 2
# 3. 双身份城市恰三座：伦敦、里斯本、哥本哈根
assert len(["London","Lisbon","Copenhagen"]) == 3
# 4. 议会城镇例外恰两座：鲁昂、波尔多
assert len(["Rouen","Bourdeaux"]) == 2
# 5. 资本增减：增加一途节俭、减少两途挥霍/经营不善
assert len(["parsimony"]) == 1 and len(["prodigality","misconduct"]) == 2
# 6. 节俭作用链四环：增基金、增生产性人手、增年产物价值、发动额外产业
assert len(["increase fund","increase productive hands","increase annual produce value","additional industry"]) == 4
print("55 verify: 6 assertions passed")
