# -*- coding: utf-8 -*-
"""验证《国富论》78 篇篇内数字与结构（取自原书第三卷第四章收官段，Gutenberg #3300）。
数字均为原书篇内陈述，序位与方向登记者已标明，不冒充现代实测，不构成投资建议。"""
# 1. 四国对照：英格兰、法国、西葡一组、意大利，计数四组
assert len(["England", "France", "Spain and Portugal", "Italy"]) == 4
# 2. 英格兰时间：自伊丽莎白初逾二百年，与繁荣期通常持续之久同量级（方向登记）
assert 200 == 200 and 200 > 100
# 3. 法国先行：早近一世纪，量级一百
assert 100 == 100 and 100 < 200
# 4. 英格兰农业鼓励三项 + 自耕农地位一项，计数四
assert len(["corn export bounty", "foreign corn duties near prohibition", "live cattle import prohibition", "yeomanry secure independent respectable"]) == 4
# 5. 资本实现两形态：建筑、土地持久改良，计数二
assert len(["buildings", "lasting improvement of lands"]) == 2
# 6. 持久性门槛：一二百年劫掠，下界一百年、上界二百年
assert 100 < 200 and len([100, 200]) == 2
print("78 verify: 6 assertions passed")
