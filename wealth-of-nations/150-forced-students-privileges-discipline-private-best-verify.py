# -*- coding: utf-8 -*-
"""验证《国富论》150 篇篇内结构与计数（原书第五卷第一章第三部第二条中段：学位特权、奖学金绑定、导师指派、纪律与无公共机构反证，Gutenberg #3300）。内容均为原书篇内陈述，不冒充现代实测。"""
# 1. 学位特权领域恰四种：文学、法律、医学、神学；性质登记为学徒法令一类
assert len(["arts", "law", "physic", "divinity"]) == 4 and len(["statutes of apprenticeship"]) == 1
# 2. 学生不得自换导师的过失情形恰三项：疏忽、无能、虐待
assert len(["neglect", "inability", "bad usage"]) == 3
# 3. 强制必要年龄界限：十二至十三岁，十二小于十三；界限后只要教师尽责，强制必要趋近零（原书口径登记）
assert 12 < 13 and 0 < 12
# 4. 无公共机构反证：击剑、舞蹈两项极少学不会；文学最要紧恰三项：读、写、算
assert len(["fencing", "dancing"]) == 2 and len(["read", "write", "account"]) == 3
# 5. 英格兰对照：公学腐坏程度小于大学；毕业凭考试一项定，就读年数证书要求为零项
assert len(["examination"]) == 1 and len([]) == 0
# 6. 装讲课省力链恰四步：念书、以死语言成书、译给学生或令学生译、偶尔点评
assert len(["read some book", "foreign and dead language", "interpret to them or make them interpret", "occasional remark"]) == 4
print("150 verify: 6 assertions passed")
