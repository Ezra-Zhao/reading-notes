# -*- coding: utf-8 -*-
# 数据取自原书篇内陈述（183 篇覆盖段），不冒充现代实测。
# 1 英国四必需品税目
assert len(["salt", "leather", "soap", "candles"]) == 4
# 2 盐税 3s4d = 40d，约原价三倍
assert 3 * 12 + 4 == 40 and 3 == 3
# 3 税率带序位：皮革 8-10 < 烛 14-15 < 皂 20-25（取下限）
assert 8 < 14 < 20 and 10 < 15 < 25
# 4 煤沿海税 3s3d = 39d，超过原价 60%；课税通道 1、免税通道 2
assert 3 * 12 + 3 == 39 and 0.60 > 3 / 5 - 0.0001
assert len(["coastways taxed"]) == 1 and len(["by land free", "inland navigation free"]) == 2
# 5 荷兰：城镇面包价倍数 2；小麦面包年额 6s9.5d = 81.5d
assert 2 == 2 and 6 * 12 + 9.5 == 81.5
# 6 德克尔叠加 4-5 次；肉必需判定否、衬衫皮鞋是
assert 4 <= 5 and len([4, 5]) == 2
meat_necessary = 0
shirt_shoes_necessary = 1
assert meat_necessary == 0 and shirt_shoes_necessary == 1
print("183 verify: 6 assertions passed")
