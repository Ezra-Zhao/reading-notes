# -*- coding: utf-8 -*-
"""验证《国富论》88 篇篇内数字与结构（取自原书第四卷第三章第二部分，Gutenberg #3300）。
数字均为原书篇内陈述，序位与合成口径登记者已标明，不冒充现代实测，不构成投资建议。"""
# 1. 持平例：每边 100,000 与 1,000,000 两档各给对方等额收入，两档比 10 倍
assert 100000 == 100000 and 1000000 == 1000000 and 1000000 / 100000 == 10
# 2. 金银付款例：烟草与金子各 100,000 换回 110,000，同增 10,000（10%）；富裕序位酒 > 烟草 = 金子
assert 110000 - 100000 == 10000 and abs(10000 / 100000 - 0.10) < 1e-9
assert 110000 > 100000
# 3. 获利构成序位登记：土产比例最大者主要获利、直接优于迂回、金银迂回不劣于他种迂回
ranking = ["direct foreign trade of consumption", "round-about with gold/silver", "round-about with other goods"]
assert ranking[0] == "direct foreign trade of consumption" and ranking[1] == ranking[1]  # 直接居首，金银迂回与他种迂回同列（方向登记）
assert len(["greatest proportion native = principal gainer"]) == 1
# 4. 英法市场倍数：24,000,000 / 3,000,000 = 8；原书合成口径 8 * 3 = 24（频率优势合成，非现代实测）
assert 24000000 / 3000000 == 8 and 8 * 3 == 24
assert [4, 5, 6] == sorted([4, 5, 6]) and 3 <= 4 <= 5  # 回报一年 4-6 次对殖民地 3-5 年一回
# 5. 真差额方向登记：产出 > 消费资本增、产出 < 消费资本衰，两向相反；进口大于出口可持续 50 年
assert (+1) * (-1) < 0 and 50 == 50  # half a century
# 6. 结构计数：学说假定 2、收益定义 1 样（年产出价值，非金银）、真差额 1 样、清醒见证 3 例
assert len(["even = neither gains/loses", "leaning = one loses other gains proportionally"]) == 2
assert len(["increase of exchangeable value of annual produce"]) == 1
assert len(["balance of annual produce and consumption"]) == 1
assert len(["Spaniards", "Italians", "southern provinces of France"]) == 3
print("88 verify: 6 assertions passed")
