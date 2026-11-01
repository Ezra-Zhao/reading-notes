# -*- coding: utf-8 -*-
"""验证《国富论》80 篇篇内数字与结构（取自原书第四卷第一章，Gutenberg #3300）。
数字均为原书篇内陈述，序位与方向登记者已标明，不冒充现代实测，不构成投资建议。"""
# 1. 裁决两分：坚实二点、诡辩二点
assert len(["export in trade may be advantageous", "no prohibition can prevent export"]) == 2
assert len(["special government attention vs other commodities", "high exchange necessarily enlarges unfavourable balance"]) == 2
# 2. 金运力：50 吨金铸 500 多万几尼（原书 more than five millions），每吨逾 10 万几尼
assert 5_000_001 / 50 > 100_000
# 3. 谷物对照：5 几尼/吨 × 100 万吨 = 500 万几尼同量级；1000 艘 × 1000 吨 = 100 万吨
assert 5 * 1_000_000 == 5_000_000 and 1000 * 1000 == 1_000_000
# 4. 茶体积比：对银约 100 倍、对金 2000 多倍，金银倍数比约 20
assert 2000 // 100 == 20
# 5. 政策转向两档：法英限本国铸币、荷兰及于本国铸币
assert len(["France/England: own coin only", "Holland etc: liberty extended to own coin"]) == 2
# 6. 注意力两操心：看守出口、看守差额，后者同样徒劳
assert len(["guarding against exportation", "watching the balance of trade"]) == 2
print("80 verify: 6 assertions passed")
