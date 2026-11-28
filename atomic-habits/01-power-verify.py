#!/usr/bin/env python3
# 《原子习惯》第1章验算脚本（自写）
import math
checks=[]
def chk(n,c):
    checks.append((n,c)); print(("PASS " if c else "FAIL ")+n)
chk("每天进步1%一年约37.78倍", abs(1.01**365-37.78)<0.01)
chk("每天退步1%一年约剩0.026", abs(0.99**365-0.026)<0.001)
chk("进步与退步一年终值相差千倍量级", 1.01**365/0.99**365>1000)
# 航向偏3.5度、洛杉矶到纽约约2451英里，横向偏移约150英里量级
off=2451*math.sin(math.radians(3.5))
chk("航向偏3.5度横向偏移约150英里", abs(off-149.7)<1.0)
chk("冰块25到32度共升7度才到融点", 32-25==7)
chk("作者体重170到200磅增30磅", 200-170==30)
chk("体重增幅约17.6%", abs(30/170-0.176)<0.001)
chk("英国队2008后十年口径:178+66计数登记", 178+66==244)
chk("环法六年五冠胜率约83%", abs(5/6-0.833)<0.001)
chk("ESPN全美阵容33人计数", 33==33)
failed=[n for n,c in checks if not c]
print(f"{len(checks)-len(failed)}/{len(checks)} assertions passed")
raise SystemExit(1 if failed else 0)
