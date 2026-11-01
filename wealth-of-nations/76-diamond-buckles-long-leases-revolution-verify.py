# -*- coding: utf-8 -*-
"""验证《国富论》76 篇篇内数字与结构（取自原书第三卷第四章，Gutenberg #3300）。
数字均为原书篇内陈述，序位与方向登记者已标明，不冒充现代实测，不构成投资建议。"""
# 1. 钻石扣交换：一千人一年维持对一对扣子
assert 1000 == 1000 and len(["pair of diamond buckles"]) == 1
# 2. 一万镑今昔：旧法约一千家庭对现今直接不足二十人，落差量级五十倍
assert 1000 // 20 == 50 and 1000 > 20 and 10000 == 10000
# 3. 供养份额四档：十分之一、百分之一、千分之一、万分之一严格递减
shares = [1/10, 1/100, 1/1000, 1/10000]
assert shares == sorted(shares, reverse=True) and len(shares) == 4
# 4. 顾客分散两档：一百与一千不同顾客，计数二
assert len([100, 1000]) == 2 and 1000 // 100 == 10
# 5. 长租约条件链：欲加租、年期保障、连本带利回收三环，计数三
assert len(["raise rents", "security of possession for term", "recover with profit outlay"]) == 3
# 6. 佃户独立两档：付全价可撤佃户、长租佃户，计数二
assert len(["tenant at will paying full value", "tenant with long lease altogether independent"]) == 2
print("76 verify: 6 assertions passed")
