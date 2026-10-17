"""Clean-room verification for LLaMA notes (12).
Self-written, numpy + stdlib only, fixed seed.
Demonstrates: RMSNorm vs LayerNorm, RoPE rotation preserves norm / relative position,
SwiGLU gating, GQA sharing KV heads (cache saving), and LLaMA vs GPT data-per-param.
"""
import numpy as np
np.random.seed(42)

print("=== 1. RMSNorm vs LayerNorm ===")
x = np.array([2.0, -1.0, 0.5, 4.0, -3.0])
# LayerNorm: subtract mean, divide std
ln = (x - x.mean()) / np.sqrt(x.var() + 1e-6)
# RMSNorm: no mean centering, divide root-mean-square
rms = x / np.sqrt(np.mean(x**2) + 1e-6)
print(f"x          = {x}")
print(f"LayerNorm  = {np.round(ln,3)}  mean={ln.mean():.3f} (centered)")
print(f"RMSNorm    = {np.round(rms,3)}  mean={rms.mean():.3f} (not centered, keeps sign/direction)")
print(f"RMSNorm RMS = {np.sqrt(np.mean(rms**2)):.3f} (should be ~1)")

print("\n=== 2. RoPE: rotate q/k by position, norm preserved, dot depends on relative distance ===")
def rope(vec, pos, base=10000.0):
    d = len(vec)
    out = vec.copy().astype(float)
    for i in range(0, d, 2):
        theta = pos / (base ** (i / d))
        c, s = np.cos(theta), np.sin(theta)
        a, b = vec[i], vec[i+1]
        out[i] = a*c - b*s
        out[i+1] = a*s + b*c
    return out

v = np.array([1.0, 0.0, 0.5, -0.5])
for pos in [0, 1, 5, 20]:
    r = rope(v, pos)
    print(f"pos={pos:2d} norm before={np.linalg.norm(v):.4f} after={np.linalg.norm(r):.4f}")
# relative property: dot(rope(q,m), rope(k,n)) depends only on m-n for same pair rotation
q = np.array([1.0, 0.2, 0.3, 0.9]); k = np.array([0.4, 1.0, -0.2, 0.5])
for m,n in [(5,3),(10,8),(20,18)]:
    d = float(rope(q,m) @ rope(k,n))
    print(f"dot m={m},n={n} (m-n=2): {d:.4f}")
print("-> same relative distance gives same dot product (RoPE encodes relative position)")

print("\n=== 3. SwiGLU: gated feed-forward ===")
def silu(z): return z / (1 + np.exp(-z))
def swiglu(x_, W, V, W2):
    return (silu(x_ @ W) * (x_ @ V)) @ W2
rng = np.random.default_rng(0)
xin = rng.normal(size=4)
W = rng.normal(size=(4,8)); V = rng.normal(size=(4,8)); W2 = rng.normal(size=(8,4))
out = swiglu(xin, W, V, W2)
gate = silu(xin @ W)
print(f"input dim=4, hidden gate values (first 4) = {np.round(gate[:4],3)}  (SiLU gate: mostly positive, small negatives allowed, acts as a soft switch)")
print(f"SwiGLU output = {np.round(out,3)}")
print("-> one branch proposes content, the other branch gates how much passes: unlike a plain single-branch FFN, the second branch controls how much of the first passes")

print("\n=== 4. GQA: grouped-query attention saves KV cache ===")
def kv_cache(num_heads, groups, seq=1024, dim_head=128, layers=32):
    # MHA: every Q head has own K,V ; GQA: groups share ; MQA: groups=1
    kv_heads = groups
    per_layer = 2 * kv_heads * seq * dim_head  # K and V
    return per_layer * layers
for name, groups in [("MHA (32 Q heads, 32 KV heads)",32), ("GQA (32 Q heads, 8 KV heads)",8), ("MQA (32 Q heads, 1 KV head)",1)]:
    elems = kv_cache(32, groups)
    print(f"{name}: KV elements for seq=1024, 32 layers = {elems:,}  ({elems*2/1e6:.1f} MB in fp16)")
print("-> GQA-8 cuts KV cache to 1/4 of MHA, MQA to 1/32, at small quality cost -- why LLaMA2-70B / LLaMA3 use GQA")

print("\n=== 5. The LLaMA bet: data per parameter ===")
# Tokens and params in billions, from the textbook tables / model cards summarised in the note:
data = [("GPT-3 175B",175,300),("LLaMA1-7B",6.7,1000),("LLaMA1-65B",65.2,1400),("LLaMA2-70B",70,2000),("LLaMA3-8B",8,15000),("LLaMA3-70B",70,15000)]
for name,p,tok in data:
    print(f"{name:14s} params={p:6.1f}B tokens={tok:6d}B  tokens/param={tok/p:6.1f}")
print("-> Chinchilla optimum is ~20 tokens/param; LLaMA deliberately over-trains small models far past it (LLaMA3-8B ~1875 tokens/param) because inference cost is paid forever, training cost only once")
