# -*- coding: utf-8 -*-
"""169 验证：固定估值地租税的结构、铸币算例与格言合拍账。
参数全部取自《国富论》第五卷第二章第二部第一条首段的篇内陈述，
只做结构/计数/算术复算断言，不冒充现代实测。纯标准库。"""

# 一、地租税设法恰两种：固定估值规程、随真实地租涨落。
canons = ["固定估值规程", "随真实地租涨落"]
assert len(canons) == 2

# 二、格言合拍账：违背恰一条（平等），合拍恰三条（确定、便利、经济）。
offends = ["平等"]
agreeable = ["确定", "便利", "经济"]
assert len(offends) == 1 and len(agreeable) == 3 and not set(offends) & set(agreeable)

# 三、铸币算例复算：一盎司银 5s.2d=62 便士；2s.7d=31 便士恰一半；10s.4d=124 便士恰两倍。
def to_pence(shillings, pence):
    return shillings * 12 + pence
base = to_pence(5, 2)
assert base == 62 and to_pence(2, 7) == base // 2 == 31 and to_pence(10, 4) == base * 2 == 124

# 四、垫付链：实际纳税人唯一（地主）；佃户垫付、地主在租中让回，链长两环。
chain = [("佃户", "垫付"), ("地主", "实际承担并在租中让回")]
assert len(chain) == 2 and chain[-1][0] == "地主"

# 五、税官比较：固定估值土地税所用税官在同收入级税中取最小序位。
officers_rank = {"固定估值土地税": 1, "其他同收入级税甲": 2, "其他同收入级税乙": 3}
assert min(officers_rank, key=officers_rank.get) == "固定估值土地税"

# 六、恒久性判据：应适配者恰一类（必然恒常）；不应适配者恰三类（暂时、偶然、意外）。
fit = ["必然恒常"]
unfit = ["暂时", "偶然", "意外"]
assert len(fit) == 1 and len(unfit) == 3

print("169 verify: 6 assertions passed")
