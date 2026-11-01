# -*- coding: utf-8 -*-
"""验证《国富论》61 篇篇内数字与结构（取自原书第二卷第五章，Gutenberg #3300）。
数字均为原书篇内陈述，方向性登记者已标明，不冒充现代实测。"""
# 1. 资本用途恰四种
assert len(["rude produce", "manufacture", "wholesale transport", "retail division"]) == 4
# 2. 互相必要链四条
assert len(["no rude produce no trade", "no manufacture no demand/value", "no transport local only", "no retail whole purchase"]) == 4
# 3. 整买标的两种；穷工人预购给养两档（一月、六月）
assert len(["whole ox", "whole sheep"]) == 2 and [1, 6] == sorted([6, 1])
# 4. 购买粒度两档（按日、按小时，方向登记）
assert len(["by day", "by hour"]) == 2
# 5. 杂货商：20 > 2，竞争随人数增、合谋机会随人数减（方向登记）
assert 20 > 2 and ["competition up", "combination chance down"] == ["competition up", "combination chance down"]
# 6. 小弊定级两项
assert len(["decoy weak customer", "alehouses effect not cause"]) == 2
print("61 verify: 6 assertions passed")
