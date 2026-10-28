"""NLP 拆书 27 验证脚本：模型编辑应用（clean-room 自写）
对应教材 5.5 节（书页 220-225，图 5.21-5.24，无公式编号）。
本节是应用节、没有公式，脚本改验五件可算、可复现的事：

1) 结构账：5.5 的三个应用方向、安全一节的两个子项、隐私泄露的三种形式，
   逐项与教材目录/正文计数对齐。
2) DEPN 的核心动作：定位到隐私神经元后把其激活值设为零——玩具向量上
   验证置零后隐私方向的泄漏量归零、非隐私神经元原样保留。
3) 图 5.22 隐私对比的类目账：编辑前回答里出现的个人信息类目集合，
   与编辑后只保留公开渠道、个人类目清零的集合，逐项对照。
   （类目只记名称，不复录教材示例中的任何具体号码/地址。）
4) 祛毒两面：Geva 等人「提升积极概念神经元权重」在玩具 softmax 上确实
   抬高积极词概率；同时词级屏蔽会误伤含敏感词的安全句（如「不制造炸弹」），
   复现教材指出的词级编辑局限。
5) DAMA 的正交投影去偏：把参数向量在偏见方向上的分量投影掉，验证投影后
   偏见方向分量为零、与偏见方向正交的分量逐分量不变。
固定逻辑，无随机性，可复现。
"""
import math

# ---------- 1. 结构账 ----------
print("=== 1. 结构账：三个应用方向 / 安全两子项 / 隐私泄露三形式 ===")
applications = ["精准模型更新（5.5.1）", "保护被遗忘权（5.5.2）", "提升模型安全（5.5.3）"]
safety_items = ["祛除毒性", "减弱偏见"]
leak_forms = [
    "生成时无意泄露个人身份信息",
    "攻击者从输出反推训练数据中的敏感信息",
    "编码敏感信息的参数被不当访问",
]
print(f"  应用方向 {len(applications)} 个：{applications}")
print(f"  安全子项 {len(safety_items)} 个：{safety_items}")
print(f"  隐私泄露形式 {len(leak_forms)} 种")
assert len(applications) == 3 and len(safety_items) == 2 and len(leak_forms) == 3
print("断言通过：5.5 的骨架是三方向，安全方向下辖祛毒与去偏两件事；")
print("教材列的隐私泄露形式是三种，任何一种都够得上被遗忘权要处理的对象。")
print()

# ---------- 2. DEPN：隐私神经元激活置零 ----------
print("=== 2. DEPN：检测器定位隐私神经元，编辑器将其激活置零 ===")
# 玩具激活向量：8 个神经元，其中第 2、5 号被检测器标为隐私神经元
act = [0.8, -0.4, 1.2, 0.3, -0.9, 2.0, 0.5, -0.1]
privacy_idx = [2, 5]
privacy_dir = [1.0 if i in privacy_idx else 0.0 for i in range(len(act))]
def dot(a, b):
    return sum(x * y for x, y in zip(a, b))
leak_before = dot(act, privacy_dir)
edited = [0.0 if i in privacy_idx else v for i, v in enumerate(act)]
leak_after = dot(edited, privacy_dir)
kept = sum(1 for i, v in enumerate(act) if i not in privacy_idx and edited[i] == v)
print(f"  置零前隐私方向泄漏量 = {leak_before:.1f}（隐私神经元激活之和）")
print(f"  置零后隐私方向泄漏量 = {leak_after:.1f}")
print(f"  非隐私神经元 {len(act) - len(privacy_idx)} 个，逐个原样保留：{kept} 个")
assert leak_before == 3.2 and leak_after == 0.0
assert kept == len(act) - len(privacy_idx)
print("断言通过：这正是教材给 DEPN 的两步——先检测定位、再置零编辑；")
print("遗忘的是被定位的那几个神经元，其余处理能力按构造不受影响。")
print("说明：玩具向量只演示置零的代数效果，不冒充 DEPN 在真实模型上的遗忘率。")
print()

# ---------- 3. 图 5.22 隐私对比类目账 ----------
print("=== 3. 图 5.22：编辑前后的个人信息类目账（只记类目名） ===")
before = {"电子邮箱", "电话号码", "个人主页", "身份证号", "出生年代与籍贯",
          "学历与任职机构", "居住小区"}
after_personal = set()               # 编辑后：个人类目一个也不再给出
after_public = {"个人主页（公开渠道）"}  # 只引导去公开主页自行联系
print(f"  编辑前披露类目 {len(before)} 类：{sorted(before)}")
print(f"  编辑后个人类目披露 {len(after_personal)} 类；保留公开渠道：{after_public}")
assert len(before) == 7 and len(after_personal) == 0 and len(after_public) == 1
print("断言通过：编辑不是把人整个抹掉——公开学术渠道保留，私人联系方式与")
print("证件、住址类信息清零，并明确说明经公开渠道联系。这就是被遗忘权落到")
print("一次回答里的样子：删的是私人信息，不是这个人的学术存在。")
print()

# ---------- 4. 祛毒：概念提升有效，但词级屏蔽会误伤 ----------
print("=== 4. 祛毒：提升积极概念概率（有效） vs 词级屏蔽（会误伤） ===")
def softmax(xs):
    m = max(xs)
    es = [math.exp(x - m) for x in xs]
    s = sum(es)
    return [e / s for e in es]
vocab = ["积极回应", "中性回应", "有害回应"]
logits = [1.0, 1.2, 1.6]
p0 = softmax(logits)
# Geva 等人思路的玩具版：给促进积极概念的神经元加权，等价于抬高积极词 logit
logits2 = [1.0 + 1.5, 1.2, 1.6]
p1 = softmax(logits2)
print(f"  提升前 P(积极)={p0[0]:.3f} P(有害)={p0[2]:.3f}")
print(f"  提升后 P(积极)={p1[0]:.3f} P(有害)={p1[2]:.3f}")
assert p1[0] > p0[0] and p1[2] < p0[2]
print("  断言通过：不动有害词本身、只抬积极概念，有害输出的相对概率照样被压下去。")
blocked_words = {"炸弹"}
sentences = {
    "有害句：教人制造炸弹的方法": True,    # 应拦
    "安全句：我们不制造炸弹，也反对暴力": False,  # 不应拦，却含敏感词
}
hits = {s: any(w in s for w in blocked_words) for s in sentences}
print(f"  词级屏蔽命中结果：{hits}")
assert hits["有害句：教人制造炸弹的方法"] is True
assert hits["安全句：我们不制造炸弹，也反对暴力"] is True  # 误伤复现
print("  误伤复现：只认词的屏蔽会把「不制造炸弹」这类安全表述一起拦掉——")
print("  教材据此说，未来的编辑要保住语义层面的安全，而不是只躲敏感词。")
print()

# ---------- 5. DAMA：正交投影去偏 ----------
print("=== 5. DAMA：用正交投影矩阵删掉参数里的偏见方向分量 ===")
# 玩具：偏见方向取单位向量 b；参数向量 w 含偏见分量与正交分量
b = [0.6, 0.8, 0.0]
assert abs(dot(b, b) - 1.0) < 1e-12
w = [3.0, 1.0, 2.0]
coef = dot(w, b)
w_proj = [wi - coef * bi for wi, bi in zip(w, b)]
print(f"  w={w}，偏见方向 b={b}，w 在 b 上的分量 = {coef:.1f}")
print(f"  投影后 w'={[round(x, 3) for x in w_proj]}，w' 在 b 上的分量 = {dot(w_proj, b):.2e}")
assert abs(dot(w_proj, b)) < 1e-9
# 与 b 正交的方向（第三维）逐分量不变
assert w_proj[2] == w[2]
# LSDM 的定位结论（教材原文计数）：被点名的组件恰是两处
lsdm_components = ["底层全连接前馈层", "顶层注意力层"]
print(f"  附记 LSDM 定位结论：因果跟踪点名 {len(lsdm_components)} 处组件：{lsdm_components}")
assert len(lsdm_components) == 2
print("断言通过：正交投影删掉的恰是偏见方向那一份，正交于偏见方向的能力")
print("按构造逐分量保留——这是「减偏见但不伤其他任务」在代数上的兑现方式。")
print()
print("全部断言通过。")
