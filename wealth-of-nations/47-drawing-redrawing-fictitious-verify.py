# -*- coding: utf-8 -*-
"""验证《国富论》47 篇篇内数字与结构（取自原书第二卷第二章，Gutenberg #3300）。
数字均为原书篇内陈述，不冒充现代实测。"""
# 1. 佣金下限 0.5% x 6 次 = 3%，加年息 5% = 8%；重复多于六次故成本 >8%
assert abs(0.5 * 6 + 5.0 - 8.0) < 1e-9 and 0.5 * 7 + 5.0 > 8.0
# 2. 脚注变体一：汇兑 3% x 4 次 = 12%，加佣金 0.5% x 4 = 2%，合计至少 14%
assert abs(3.0 * 4 + 0.5 * 4 - 14.0) < 1e-9
# 3. 两月期票一年滚续 6 次；法定利息 5%
assert 12 // 2 == 6
# 4. 普通利润区间 6-10%，下限 6 < 抽单成本下限 8（方向登记）
assert 6 < 8 <= 10
# 5. 虚构偿付判据（方向登记）：新票金额 > 旧票且偿付依赖新票贴现
def fictitious(new_bill, old_bill, payment_depends_on_new):
    return new_bill > old_bill and payment_depends_on_new
assert fictitious(101, 100, True) and not fictitious(100, 100, True)
# 6. 责任链主体三类：出票人、承兑人、背书人
assert len(["drawer", "acceptor", "indorser"]) == 3
print("47 verify: 6 assertions passed")
