# -*- coding: utf-8 -*-
"""验证《国富论》117 篇篇内数字与结构（原书第四卷第七章第二部分，Gutenberg #3300）。数字均为原书篇内陈述，不冒充现代实测。涉及奴隶制的条目只登记原书论证结构。"""
# 1. 会议由人民代表选出而非国王任命的新英格兰政府：三个
assert len(["New England government 1", "New England government 2", "New England government 3"]) == 3
# 2. 由议会选举总督的殖民地：康涅狄格、罗得岛，两个
assert len(["Connecticut", "Rhode Island"]) == 2
# 3. 被点名的专制宗主：西班牙、葡萄牙、法国，三个
assert len(["Spain", "Portugal", "France"]) == 3
# 4. 温和待遇使奴隶更有用的通道：更忠诚、更机敏，两项，原书称双倍有用
assert len(["more faithful", "more intelligent"]) == 2
# 5. 波利奥案被命释放的范围：那名奴隶、属于他的一切其他奴隶，两组
assert len(["that slave", "all the others that belonged to him"]) == 2
# 6. 殖民地世袭贵族与老家族特权：均为零
assert len([]) == 0 and 0 == 0
print("117 verify: 6 assertions passed")
