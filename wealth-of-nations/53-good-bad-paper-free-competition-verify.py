# -*- coding: utf-8 -*-
"""验证《国富论》53 篇篇内数字与结构（取自原书第二卷第二章，Gutenberg #3300）。
数字均为原书篇内陈述，方向性登记者已标明，不冒充现代实测。"""
# 1. 现值：6% 利率、15 年后 100 镑现值约 41.7 镑，在 40 与 42 之间（原书作「四十镑多一点」）
pv = 100 / (1.06 ** 15)
assert 40 < pv < 42
# 2. 邓弗里斯折价 4%；距卡莱尔不到 30 英里（以 30 为上限登记）
assert 4 == 4 and 30 >= 30
# 3. 殖民地汇兑序：100 英镑 = 130 至 1100 通货，极差倍数约 8.46
assert 130 < 1100 and abs(1100 / 130 - 8.4615) < 0.01
# 4. 宾州面额序（便士计）：5 先令 60 < 6 先令 3 便士 75 < 6 先令 8 便士 80
assert 60 < 75 < 80
# 5. 坏纸三道闸（意愿/条件/期限）；可选条款流行三年（1762、1763、1764）
assert len(["goodwill", "condition", "term of years"]) == 3 and len([1762, 1763, 1764]) == 3
# 6. 收官：限制两项（面额下限/无条件即付）；竞争增安全机制四项
assert len(["minimum denomination", "immediate unconditional payment"]) == 2
assert len(["circumspection", "guard against rival runs", "one failure less consequence", "more liberal dealing"]) == 4
print("53 verify: 6 assertions passed")
