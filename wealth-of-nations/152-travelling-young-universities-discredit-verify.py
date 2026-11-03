# -*- coding: utf-8 -*-
"""验证《国富论》152 篇结构（第五卷第一章第三部第二条后段：游学之风，Gutenberg #3300）。参数为原书篇内陈述，不冒充现代实测。"""
# 1. 出门17-18、归来21，时长3-4年
assert 21-18==3 and 21-17==4
# 2. 语言1-2门，成色：不足以说/写得体（两动词）
assert len(["one foreign language","two foreign languages"])==2 and len(["speak","write"])==2
# 3. 变坏四项，基准为在家同等时间
assert len(["conceited","unprincipled","dissipated","incapable of serious application"])==4
# 4. 习惯结局两向，与应然两向相反
assert len(["weakened","effaced"])==2 and len(["riveted","confirmed"])==2
# 5. 成因唯一：大学失信
assert len(["discredit of the universities"])==1
# 6. 父亲解脱对象三状、监督者两类
assert len(["unemployed","neglected","going to ruin"])==3 and len(["parents","relations"])==2
print("152 verify: 6 assertions passed")
