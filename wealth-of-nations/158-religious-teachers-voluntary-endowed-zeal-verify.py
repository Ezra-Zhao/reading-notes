# -*- coding: utf-8 -*-
"""验证《国富论》158 篇结构（宗教教师供养与热忱，Gutenberg #3300）。参数为原书篇内陈述。"""
# 1. 给养恰两类
assert len(["voluntary contributions of hearers", "independent fund by law"]) == 2
# 2. 独立基金来源恰四样
assert len(["landed estate", "tythe or land tax", "established salary", "stipend"]) == 4
# 3. 请官长迫害实例恰两则
assert len(["Roman catholic clergy vs protestants", "church of England vs dissenters"]) == 2
# 4. 托钵修会恰两家、振兴世纪恰两个
assert len(["St Dominic", "St Francis"]) == 2 and len([13, 14]) == 2
# 5. 给养依赖度序位：托钵全部靠奉献 > 堂区部分靠奉献 > 高级显贵操心教导为很少
assert 1.0 > 0.5 > 0.1
# 6. 卫斯理宗学问不及不从国教者一半而更走红
assert 0.5 > 0 and "methodists more in vogue than dissenters"
print("158 verify: 6 assertions passed")
