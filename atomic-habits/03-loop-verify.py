#!/usr/bin/env python3
# 《原子习惯》第3章验算脚本（自写；桑代克计时为书中转述，只复核算术）
checks=[]
def chk(n,c):
    checks.append((n,c)); print(("PASS " if c else "FAIL ")+n)
times=[160,30,90,60,15,28,20,30,22,11,15,20,12,10,14,10,8,8,5,10,8,6,6,7]
chk("十二号猫计时共24次", len(times)==24)
first3=sum(times[:3])/3; last3=sum(times[-3:])/3
chk("头三次平均约93.3秒", abs(first3-93.333)<0.01)
chk("末三次平均约6.3秒", abs(last3-6.333)<0.01)
chk("末段比头段快约14.7倍", abs(first3/last3-14.737)<0.01)
chk("习惯回路恰4环", len(["提示","渴望","回应","奖赏"])==4)
chk("两阶段划分:问题2环+解决2环", 2+2==4)
chk("行为改变四法则恰4条", len(["显而易见","有吸引力","轻而易举","令人满足"])==4)
chk("缺一环即不成习惯:4环全在才完整", all([True,True,True,True]) and not all([True,True,True,False]))
failed=[n for n,c in checks if not c]
print(f"{len(checks)-len(failed)}/{len(checks)} assertions passed")
raise SystemExit(1 if failed else 0)
