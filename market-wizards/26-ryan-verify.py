# -*- coding: utf-8 -*-
"""David Ryan 篇验算：早期账户、锦标赛三年连乘、洛杉矶时报两年度账户、买点延伸与仓位风险。"""
def close(a,b,tol=0.15): return abs(a-b) <= tol

# 1 早期账户 20000 -> 52000 -> 16000
up=(52000-20000)/20000*100; dd=(16000-52000)/52000*100; net=(16000-20000)/20000*100; rec=(52000/16000-1)*100
assert close(up,160.0,0.01) and close(dd,-69.23,0.05) and close(net,-20.0,0.01) and close(rec,225.0,0.1)
print(f"1 早期账户 20000->52000 +{up:.1f}%; ->16000 自高点{dd:.2f}% 对起点{net:.1f}%; 回到52000需+{rec:.1f}% OK")

# 2 三年连乘对 Schwager 自报 1379%：161% / 160% / 约118%
chain=2.61*2.60*2.18
assert close((chain-1)*100,1379.0,1.0), chain
print(f"2 连乘 2.61x2.60x2.18={chain:.4f} -> +{(chain-1)*100:.2f}% vs Schwager 1379% OK")

# 3 由总连乘反推第三年
third=14.79/(2.61*2.60)
assert close((third-1)*100,117.95,0.2)
print(f"3 总倍数14.79 / (2.61x2.60) = 第三年倍数{third:.4f} -> +{(third-1)*100:.2f}% 约118% OK")

# 4 第三年若按流传的155%版，总连乘对不上
alt=2.61*2.60*2.55
assert close((alt-1)*100,1630.43,0.5) and not close((alt-1)*100,1379.0,10.0)
print(f"4 第三年155%版连乘 +{(alt-1)*100:.2f}% 与1379%差{(alt-1)*100-1379:.1f}个百分点 不成立 OK")

# 5 洛杉矶时报两年度账户 43000 -> 295000：报道578%，复算586.05%
gain=(295000-43000)/43000*100; implied=43000*(1+5.78)
assert close(gain,586.05,0.1) and close(implied,291540,1)
print(f"5 43000->295000 复算 +{gain:.2f}% (报道578%对应终值{implied:.0f}美元 差{295000-implied:.0f}美元) OK")

# 6 买点延伸：突破点50、退出48 对 追高到55
r_on_time=(50-48)/50*100; r_late=(55-48)/55*100
assert close(r_on_time,4.0,0.01) and close(r_late,12.73,0.05) and close(r_late/r_on_time,3.18,0.02)
print(f"6 准时买风险{r_on_time:.1f}% 追高买风险{r_late:.2f}% 为准时买的{r_late/r_on_time:.2f}倍 OK")

# 7 仓位风险：10%仓位吃8%止损 = 账户0.8%
risk=0.10*0.08*100
assert close(risk,0.8,0.01)
print(f"7 仓位10% x 止损8% = 账户风险{risk:.1f}% 对自述单笔风险约1%上限 OK")

# 8 起步仓位到赢家仓位的倍数区间：5-10% -> 20-25%
assert close(20/10,2.0,0.01) and close(25/5,5.0,0.01)
print("8 赢家仓位/起步仓位 倍数区间 2.0-5.0倍 OK")

# 9 每周扫图量级：约4000张/周
assert 4000*52==208000
print("9 约4000张/周 x 52周 = 约208000张/年 只作量级 OK")
print("ALL PASS")
