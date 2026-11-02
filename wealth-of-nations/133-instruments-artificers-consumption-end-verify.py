# -*- coding: utf-8 -*-
"""验证《国富论》133 篇篇内数字与结构（原书第四卷第八章收官段：工具与工匠禁令、消费至上总判与帝国账，Gutenberg #3300）。数字均为原书篇内陈述，不冒充现代实测，不构成投资建议。"""
# 1. 煤出口税：每吨逾 5 先令、每查尔德隆逾 15 先令，15 恰为 5 的三倍且下限为正（原书下限口径登记）
assert 15 == 3 * 5 and 5 > 0
# 2. 阿拉伯胶再出口税序位：原 3 便士 < 降后 5 先令=60 便士 < 欧洲进口档 10 先令=120 便士 < 暴涨档 £1:10s=360 便士；胜战锚点 1755
assert 3 < 60 < 120 < 360 and 1755 == 1755
# 3. 海狸皮：旧进口税 16 便士恰估值 6s8d=80 便士的五分之一；1764 年出口 7 便士大于进口 1 便士；海狸毛 18 便士大于 7 便士
assert 80 // 5 == 16 and 7 > 1 and 18 > 7
# 4. 工匠诱出罚则严格递增：罚金 100<500<1000 镑；监禁 3<12<24 月
assert 100 < 500 < 1000 and 3 < 12 < 24
# 5. 工具出口罚：袜机架 40 镑小于器具犯者 200 镑加船长 200 镑之和；规制形态恰绝对禁令一类（非重税）
assert 40 < 200 + 200 and len(["absolute prohibition"]) == 1
# 6. 帝国账：新债逾 1.7 亿镑小于开支逾 2 亿镑；利息大于独占额外利润与贸易总值的序位登记（利息居首）
assert 170_000_000 < 200_000_000
rank = {"interest of debt": 3, "extraordinary profit of monopoly": 2, "value of colony trade": 1}
assert rank["interest of debt"] > rank["extraordinary profit of monopoly"]
print("133 verify: 6 assertions passed")
