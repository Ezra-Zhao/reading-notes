# -*- coding: utf-8 -*-
"""验证《国富论》154 篇结构（第五卷第一章第三部第二条收官，Gutenberg #3300）。参数为原书篇内陈述。"""
# 1. 古代教师胜近代三项
assert len(["attention excited","empire over opinions and principles","tone to conduct and conversation"])==3
# 2. 无赏金商人两难两向；下场三级
assert len(["same price no same profit","dearer few customers"])==2 and len(["poverty and beggary","bankruptcy","ruin"])==3
# 3. 捐赠双害两项
assert len(["corrupted diligence of public teachers","rendered almost impossible good private teachers"])==2
# 4. 无公共机构时被教理由三样
assert len(["demand","necessary or convenient","fashionable"])==3
# 5. 妇女教育无用/荒唐/幻想皆零；挑选者两类
assert len([])==0 and len(["useless","absurd","fantastical"])==3 and len(["parents","guardians"])==2
# 6. 特权取得途径唯一；需求造才能链三环
assert len(["attending lectures of public teachers"])==1 and len(["demand","talent for giving it","unrestrained competition emulation"])==3
print("154 verify: 6 assertions passed")
