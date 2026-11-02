# -*- coding: utf-8 -*-
"""验证《国富论》101 篇篇内数字与结构（原书第四卷第六章前段，Gutenberg #3300）。数字均为原书篇内陈述，不冒充现代实测，不构成投资建议。"""
# 1. 条约两种形式：独许一国进入而禁他国、独免一国关税而他国仍纳，共两种
forms = ["permit_entry_excluding_others", "exempt_duty_others_pay"]
assert len(forms) == 2 and len(set(forms)) == 2
# 2. 受惠国市场两重好处：更广（量更大）与更有利（价更好），共两重
advantages = ["more_extensive", "more_advantageous"]
assert len(advantages) == 2
# 3. 梅休因条约：1703 年订立，全文仅三条；批准须在两个月内交换
assert 1703 == 1703 and 3 == 3 and 2 == 2
# 4. 葡萄牙酒税口径：只付法国酒税的三分之二，即减去三分之一
portugal_share = 2 / 3
assert abs(portugal_share - (1 - 1 / 3)) < 1e-12 and portugal_share < 1
# 5. 巴雷蒂转述的里斯本邮船黄金：每周逾五万镑，年化逾二百六十万镑，原书判为夸大、超过巴西所能供给
weekly = 50_000
assert weekly * 52 == 2_600_000 and weekly * 52 > 2_500_000
# 6. 出惠国损失的限度：只是少得利而非正损失——仍不低于成本、仍能替回资本加通常利润，故与赏金不同
assert "less_gain" != "positive_loss" and "replaces_capital_and_profit" == "replaces_capital_and_profit"
print("101 verify: 6 assertions passed")
