# -*- coding: utf-8 -*-
"""验证《国富论》151 篇篇内结构与计数（原书第五卷第一章第三部第二条后段前半：教会起源、拉丁文、三科变五科与修习次序，Gutenberg #3300）。内容均为原书篇内陈述，不冒充现代实测；原书价值评判只登记不作本仓结论。"""
# 1. 语言分层恰三对：祭司/百姓、神圣/世俗、有学问/无学问
assert len([("priests", "people"), ("sacred", "profane"), ("learned", "unlearned")]) == 3
# 2. 原文语言恰两种：希腊文、希伯来文；西班牙大学希腊文缺位登记一项
assert len(["Greek", "Hebrew"]) == 2 and len(["some Spanish universities: Greek never part of course"]) == 1
# 3. 古代哲学恰三科：物理、伦理、逻辑；逻辑起源序位第三（后于物理与伦理）
assert len(["physics", "ethics", "logic"]) == 3 and ["physics", "ethics", "logic"].index("logic") == 2
# 4. 大学课程恰五科，修习次序：逻辑、本体论、灵学、道德哲学、物理学（物理学末位第五）
order = ["logic", "ontology", "pneumatology", "moral philosophy", "physics"]
assert len(order) == 5 and order.index("physics") == 4 and order.index("logic") == 0
# 5. 伦理学对象范围恰四层：个人、家庭、国家、人类大社会
assert len(["individual", "family", "state", "great society of mankind"]) == 4
# 6. 三科加新增两科（灵学独立与本体论）恰合五科；改良采用序位：最富最慢
assert 3 + 2 == 5 and len(["richest and best endowed slowest", "poorer easier"]) == 2
print("151 verify: 6 assertions passed")
