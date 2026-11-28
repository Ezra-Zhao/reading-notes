#!/usr/bin/env python3
# 《原子习惯》第2章验算脚本（自写，演示数字为自设情景）
checks=[]
def chk(n,c):
    checks.append((n,c)); print(("PASS " if c else "FAIL ")+n)
chk("改变三层:结果/过程/身分恰3层", len(["结果","过程","身分认同"])==3)
# 选票模型演示:每天1票、一年365票，好习惯占多数只需183票
chk("365票多数门槛183票", 365//2+1==183)
chk("每周5次一年260次证据", 5*52==260)
chk("每周日上教堂20年约1040次", 52*20==1040)
chk("每天写作1页一年365页成一本书量级", 365*1==365)
# 身分逆推演示:减重40磅目标先问哪种人，非直接节食天数
chk("演示:40磅分20周每周2磅", 40/20==2.0)
chk("两种拒烟说法计数2种", len(["正在戒烟","我不抽烟"])==2)
chk("改变身分两步骤恰2步", len(["决定成为什么样的人","用小胜利证明"])==2)
failed=[n for n,c in checks if not c]
print(f"{len(checks)-len(failed)}/{len(checks)} assertions passed")
raise SystemExit(1 if failed else 0)
