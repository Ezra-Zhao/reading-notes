# -*- coding: utf-8 -*-
"""168 验证：税收四格言后两条（便利、经济）与多掏四方式的结构与计数。
参数全部取自《国富论》第五卷第二章第二部格言三、四及过渡句的篇内陈述，
只做结构/计数/关系断言，不冒充现代实测。纯标准库。"""

# 一、格言三正面例子恰两类；奢侈品消费税随买随缴、零星分付、购买自愿。
maxim3_examples = ["地租与房租税随付租期征收", "奢侈品消费税由消费者最终支付"]
assert len(maxim3_examples) == 2
luxury = {"支付方式": "零星分付", "购买": "自愿可不买"}
assert luxury["支付方式"] == "零星分付" and luxury["购买"] == "自愿可不买"

# 二、多掏（入国库之外漏损）方式恰四种，各有独立条目。
burden_ways = ["税官薪俸与规费", "阻碍产业并毁纳税基金", "没收罚金与走私诱惑", "税吏查访的烦恼压迫"]
assert len(burden_ways) == 4 and len(set(burden_ways)) == 4

# 三、走私逻辑链：罚则随诱惑增大而加重（单调），且诱惑由税制造在先。
temptation = [1, 2, 3, 4]
penalty = [2, 4, 6, 8]  # 随诱惑成比例加重（示意原书"成比例"陈述）
assert all(penalty[i] < penalty[i + 1] for i in range(len(penalty) - 1))
sequence = ["税制造诱惑", "人屈服", "法律惩罚"]
assert sequence.index("税制造诱惑") < sequence.index("法律惩罚")

# 四、烦恼估值：烦恼非严格开支，但等值于人愿付的赎免代价。
vexation = {"严格开支": False, "赎免等值": True}
assert vexation["严格开支"] is False and vexation["赎免等值"] is True

# 五、四格言总目恰四条，本篇覆盖后两条。
maxims = ["平等", "确定", "便利", "经济"]
assert len(maxims) == 4 and maxims[2:] == ["便利", "经济"]

# 六、过渡句：各国力求的四性质恰四项，与四格言一一对应。
endeavoured = ["平等", "确定", "时间与方式上便利", "与收入相比少累民"]
assert len(endeavoured) == 4

print("168 verify: 6 assertions passed")
