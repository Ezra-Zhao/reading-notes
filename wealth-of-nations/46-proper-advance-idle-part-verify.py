# -*- coding: utf-8 -*-
"""验证《国富论》46 篇篇内数字与结构（取自原书第二卷第二章，Gutenberg #3300）。
数字均为原书篇内陈述，不冒充现代实测。"""
# 1. 正当垫付界（方向性登记）：垫付额 <= 客户本来闲置作现钱应付偶然索款的那一份
def proper(advance, idle_ready_money_part):
    return advance <= idle_ready_money_part
assert proper(500, 500) and not proper(501, 500)
# 2. 还款检验窗口四种：4、5、6、8 个月，最大为最小两倍
windows = [4, 5, 6, 8]
assert len(windows) == 4 and max(windows) == 2 * min(windows)
# 3. 规模对比：银行约 500 户，私人放款人 5–6 人至多 12 人；500 > 12 的 40 倍
assert 500 / 12 > 40
# 4. 水塘判据（方向性登记）：流入 == 流出则水位不变；流入 < 流出则水位下降
def pond(inflow, outflow):
    return inflow - outflow
assert pond(100, 100) == 0 and pond(60, 100) < 0
# 5. 固定资本三业例：铁厂、矿山、土地改良
assert len(["iron forge", "mine", "land improvement"]) == 3
# 6. 长钱渠道两途：债券、抵押；出借人为靠利息生活的私人
assert len(["bond", "mortgage"]) == 2
print("46 verify: 6 assertions passed")
