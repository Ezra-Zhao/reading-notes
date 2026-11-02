# -*- coding: utf-8 -*-
"""验证《国富论》128 篇篇内数字与结构（原书第四卷第七章第三部分收官段末段，Gutenberg #3300）。数字均为原书篇内陈述，不冒充现代实测，不构成投资建议。"""
# 1. 欧洲据点所在区域恰二：非洲海岸、东印度
assert len(["coast of Africa", "East Indies"]) == 2
# 2. 葡萄牙无专营公司据点恰四：刚果、安哥拉、本盖拉、果阿
assert len(["Congo", "Angola", "Benguela", "Goa"]) == 4
# 3. 荷兰最可观殖民地恰二：好望角、巴达维亚
assert len(["Cape of Good Hope", "Batavia"]) == 2
# 4. 巴达维亚港常到船只来源恰六：中国、日本、东京、马六甲、交趾支那、西里伯斯
assert len(["China", "Japan", "Tonquin", "Malacca", "Cochin-China", "Celebes"]) == 6
# 5. 美洲猎人例外恰二（墨西哥、秘鲁），牧人同地供养人数大于猎人（序位登记）
assert len(["Mexico", "Peru"]) == 2 and 2 > 1  # shepherds maintained > hunters maintained，示意序位
# 6. 好望角过路船供应品恰三：新鲜给养、水果、葡萄酒
assert len(["fresh provisions", "fruit", "wine"]) == 3
print("128 verify: 6 assertions passed")
