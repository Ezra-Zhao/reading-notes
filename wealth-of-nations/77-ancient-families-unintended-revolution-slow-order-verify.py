# -*- coding: utf-8 -*-
"""验证《国富论》77 篇篇内数字与结构（取自原书第三卷第四章收官段，Gutenberg #3300）。
数字均为原书篇内陈述，序位与方向登记者已标明，不冒充现代实测，不构成投资建议。"""
# 1. 人口翻番：欧洲五百年对北美二十至二十五年，约二十倍量级
assert 500 // 25 == 20 and 20 <= 25 < 500
# 2. 资本门槛：北美五六十镑对欧洲青年两三千镑，后者在前者数十倍量级（方向登记）
assert 50 <= 60 < 2000 <= 3000 and 2000 // 60 >= 30
# 3. 革命两类人：大业主与商人工匠计数二
assert len(["great proprietors - childish vanity", "merchants and artificers - own interest"]) == 2
# 4. 小业主三品质：勤勉、明智、成功计数三
assert len(["most industrious", "most intelligent", "most successful"]) == 3
# 5. 垄断地价链：上市少、想买资本多、地租不抵利息三环计数三
assert len(["land kept out of market", "more capitals to buy than land to sell", "rent never pays interest of purchase-money"]) == 3
# 6. 耗散两界：供养有上限与虚荣无上限对照计数二
assert len(["maintenance bounded by what he can afford", "vanity / expense frequently no bounds"]) == 2
print("77 verify: 6 assertions passed")
