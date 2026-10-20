"""NLP 拆书 15 验证脚本：思维链 CoT（clean-room 自写）
演示四件事：
1) 同一道多步算术题：一步直答的玩具捷径会算错，逐步更新状态的 CoT 算对
2) Zero-Shot CoT 的两阶段：先触发词生成推理，再用固定句式抽取答案
3) Self-Consistency：多条推理路径各自作答，多数投票压过个别算错的路径
4) ToT 迷你版：对 24 点做树搜索——生成候选步、评估、回溯，直到凑出 24
只用标准库，固定数据，可复现。
"""
from collections import Counter
from fractions import Fraction
from itertools import permutations

# ---------- 题目（自编，与教材例题无关） ----------
# 面包房：早上 47 个，卖出 19 个，中午新烤 25 个，下午卖出 31 个，还剩多少？
OPS = [("start", 47), ("卖出", -19), ("新烤", +25), ("卖出", -31)]
TRUTH = 47 - 19 + 25 - 31  # 22

# ---------- 1. 直答捷径 vs CoT 逐步更新 ----------
def direct_shortcut(ops):
    """玩具直答：只看头尾两个数（模拟不展开中间状态时的常见滑步）。"""
    return ops[0][1] + ops[-1][1]

def cot_solve(ops):
    state, trace = 0, []
    for name, delta in ops:
        state = delta if name == "start" else state + delta
        trace.append(f"{name}: 当前 = {state}")
    return state, trace

print("=== 1. 直答 vs CoT ===")
print(f"直答捷径(只看头尾): {direct_shortcut(OPS)}  (正确答案 {TRUTH}) -> 错")
ans, trace = cot_solve(OPS)
for line in trace:
    print("  CoT:", line)
print(f"CoT 最终: {ans} -> {'对' if ans == TRUTH else '错'}")
# 错误传播：中间一步算错，后面全对也救不回来
bad = [("start", 47), ("卖出", -18), ("新烤", +25), ("卖出", -31)]  # 第二步少减 1
bad_ans, _ = cot_solve(bad)
print(f"中间一步差 1 的 CoT: {bad_ans} -> 错（链越长，越要逐步验算）")
print()

# ---------- 2. Zero-Shot CoT 两阶段 ----------
TRIGGER = "让我们一步一步思考。"
EXTRACT = "因此，最终答案为："
reasoning = "；".join(trace)
stage1 = f"问题：面包房还剩多少个面包？\nA：{TRIGGER}{reasoning}。"
stage2_answer = f"{EXTRACT}{ans}"
print("=== 2. Zero-Shot CoT 两阶段 ===")
print("阶段1（触发词+推理生成）:", stage1[:90], "...")
print("阶段2（固定句式抽答案）:", stage2_answer)
print()

# ---------- 3. Self-Consistency 多路径投票 ----------
# 五条路径：换运算结合顺序/验算方式，其中一条中途算错
paths = [
    ("顺序算", [47, -19, +25, -31]),
    ("先加后减", [47, +25, -19, -31]),
    ("卖出合并", [47, +25, -50]),
    ("新烤先行验算", [25, +47, -31, -19]),
    ("中途滑步", [47, -19, +25, -30]),  # 最后一步少减 1 -> 23
]
votes = []
for name, seq in paths:
    total = seq[0] + sum(seq[1:])
    votes.append(total)
    print(f"  路径[{name}]: {'+'.join(str(x) for x in seq)} = {total}")
cnt = Counter(votes)
winner, n = cnt.most_common(1)[0]
print(f"投票结果: {dict(cnt)} -> 多数答案 {winner}（{n}/{len(votes)} 票）"
      f"，与真值一致: {winner == TRUTH}")
print()

# ---------- 4. ToT 迷你版：24 点树搜索 ----------
def search_24(nums, max_nodes=20000):
    """状态 = 一组 Fraction；每步取两数做 + - * / 生成新状态，评估=离 24 的距离。
    返回 (解的表达式, 展开节点数)。带回溯的深度优先搜索，演示 ToT 的生成-评估-搜索骨架。"""
    nodes = 0

    def dfs(state):
        nonlocal nodes
        nodes += 1
        if nodes > max_nodes:
            return None
        if len(state) == 1:
            return state[0][1] if state[0][0] == 24 else None
        # 评估剪枝：只剩两数时直接试全部运算，不再展开更深
        for i in range(len(state)):
            for j in range(len(state)):
                if i == j:
                    continue
                a, ea = state[i]
                b, eb = state[j]
                rest = [state[k] for k in range(len(state)) if k not in (i, j)]
                cands = [(a + b, f"({ea}+{eb})"), (a - b, f"({ea}-{eb})"),
                         (a * b, f"({ea}*{eb})")]
                if b != 0:
                    cands.append((a / b, f"({ea}/{eb})"))
                for val, expr in cands:
                    r = dfs(rest + [(val, expr)])
                    if r:
                        return r
        return None

    start = [(Fraction(x), str(x)) for x in nums]
    return dfs(start), nodes

expr, nodes = search_24([4, 4, 10, 10])
print("=== 4. ToT 迷你版（24 点：4, 4, 10, 10）===")
print(f"搜索展开节点数: {nodes}")
print(f"找到的解: {expr} = {eval(expr.replace('/', '/')) if expr else '无'}")
print("说明: 线性 CoT 只走一条路，错一步全错；ToT 把每步展开成多个候选、")
print("      评估后回溯换路——用搜索的算力换推理的可靠性。")
