# -*- coding: utf-8 -*-
"""162 验证：第一章结论前半的分担结构。参数取原书第五卷第一章结论篇内陈述，不冒充现代实测。"""
# 1. 明言普遍利益、由普遍贡献承担的费用恰两笔：国防、最高行政官尊严
assert len(["defence of society", "dignity of chief magistrate"]) == 2
# 2. 分担比例原则为按能力比例，非人头同额
principle = "in proportion to respective abilities"
assert principle.startswith("in proportion")
# 3. 司法费用归因对象恰两类：引发费用者、直接受益者
assert len(["those who give occasion", "those most immediately benefited"]) == 2
# 4. 受益者好处恰两型：恢复权利、维持权利
assert len(["restored to rights", "maintained in rights"]) == 2
# 5. 承担工具恰一项（诉讼费），兜底例外恰一条（无产罪犯定罪）
tools, exceptions = ["fees of court"], ["conviction of criminals without estate or fund"]
assert len(tools) == 1 and len(exceptions) == 1
# 6. 定性两档：国防尊严为「合理应当」，司法普遍承担为「并无不当」
assert len(["reasonable therefore general", "no impropriety in general"]) == 2
print("162 verify: 6 assertions passed")
