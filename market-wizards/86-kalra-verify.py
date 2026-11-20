#!/usr/bin/env python3
"""86 Kalra verify: 12 assertion groups, Decimal arithmetic.
Sources: Fidelity Blue Chip Growth Fund Class K summary prospectus
2026-09-29 (periods ended 2025-12-31) + Fidelity fund fact sheet
(FIIS_FS_58916, data as of 2026-10-31 / 2026-09-30)."""
from decimal import Decimal as D, getcontext
from datetime import date
getcontext().prec = 28

def approx(a, b, tol):
    return abs(a - b) <= tol

# G1 tenure
start = date(2009, 7, 1); end = date(2025, 12, 31)
tenure_days = (end - start).days + 1  # inclusive? house style uses diff; check both
tenure_diff = (end - start).days
fund_start = date(1987, 12, 31)
fund_life = (end - fund_start).days
class_start = date(2008, 5, 9)
gap_class = (start - class_start).days
print(f"G1 tenure_diff={tenure_diff} days={tenure_diff/365.25:.2f}yr fund_life={fund_life} share={tenure_diff/fund_life*100:.2f}% gap_after_class={gap_class}d tenure_to_20261031={(date(2026,10,31)-start).days}d")
assert approx(D(tenure_diff) / D(fund_life) * 100, D('43.5'), D('0.6'))

# G2 calendar 10y compound
cal = [D('1.71'), D('36.20'), D('1.16'), D('33.56'), D('62.38'),
       D('22.81'), D('-38.40'), D('55.76'), D('39.80'), D('19.99')]
prod = D(1)
for r in cal:
    prod *= (1 + r / 100)
ann = (float(prod) ** 0.1 - 1) * 100
print(f"G2 product={prod:.6f} cum={(prod-1)*100:.2f}% annualized={ann:.2f}% vs stated 19.64")
assert approx(D(str(ann)), D('19.64'), D('0.05'))

# G3 $10k endpoints from stated annualized
f10 = (D('1.1964')) ** 10; rg10 = (D('1.1813')) ** 10; r10 = (D('1.1459')) ** 10
print(f"G3 fund x{f10:.4f} ${10000*f10:,.0f} | RG x{rg10:.4f} ${10000*rg10:,.0f} | R1000 x{r10:.4f} ${10000*r10:,.0f} | ratio RG {f10/rg10:.4f} R1000 {f10/r10:.4f} | calendar endpoint ${10000*prod:,.0f}")
assert approx(f10, prod, D('0.01'))

# G4 excess
rows = [(D('19.99'), D('18.56'), D('17.37')), (D('14.60'), D('15.32'), D('13.59')), (D('19.64'), D('18.13'), D('14.59'))]
for i, (f, g, r) in enumerate(rows):
    print(f"G4 row{i+1} vsRG {f-g:+.2f}pp vsR1000 {f-r:+.2f}pp")
assert rows[1][0] - rows[1][1] == D('-0.72') and rows[2][0] - rows[2][2] == D('5.05')

# G5 halves
p1 = D(1)
for r in cal[:5]:
    p1 *= (1 + r / 100)
p2 = prod / p1
a1 = (float(p1) ** 0.2 - 1) * 100; a2 = (float(p2) ** 0.2 - 1) * 100
print(f"G5 2016-20 x{p1:.6f} cum={(p1-1)*100:.2f}% ann={a1:.2f}% | 2021-25 x{p2:.6f} cum={(p2-1)*100:.2f}% ann={a2:.2f}% vs stated 5yr 14.60")
assert approx(D(str(a2)), D('14.60'), D('0.05'))

# G6 2022 recovery
need = (1 / (1 - D('0.3840')) - 1) * 100
two = (1 - D('0.3840')) * (1 + D('0.5576'))
three = two * (1 + D('0.3980'))
print(f"G6 recovery need +{need:.2f}% | 2022-23 factor {two:.6f} ({(two-1)*100:+.2f}%) | 2022-24 factor {three:.6f} ({(three-1)*100:+.2f}%)")
assert approx(need, D('62.34'), D('0.01'))

# G7 extremes
neg = sum(1 for r in cal if r < 0)
print(f"G7 negative years={neg}/10 best 2020 +62.38 worst 2022 -38.40 range {D('62.38')+D('38.40')}pp | quarters +37.85/-27.28 spread {D('37.85')+D('27.28')}pp")
assert neg == 1

# G8 2020-2022 boom-bust
bb = (1 + D('0.6238')) * (1 + D('0.2281')) * (1 - D('0.3840'))
print(f"G8 2020-22 factor {bb:.6f} cum {(bb-1)*100:+.2f}%")
assert approx((bb - 1) * 100, D('22.85'), D('0.05'))

# G9 last 3 calendar years
l3 = (1 + D('0.5576')) * (1 + D('0.3980')) * (1 + D('0.1999'))
print(f"G9 2023-25 factor {l3:.6f} cum {(l3-1)*100:+.2f}% ann {((float(l3)**(1/3)-1)*100):.2f}%")
assert approx((l3 - 1) * 100, D('161.31'), D('0.1'))

# G10 top10 issuers
t10 = [D('15.06'), D('10.46'), D('7.65'), D('6.04'), D('3.97'), D('3.79'), D('3.63'), D('3.53'), D('3.42'), D('2.32')]
s = sum(t10)
print(f"G10 top10 sum={s} (stated 59.87) top2={t10[0]+t10[1]} top5={sum(t10[:5])} NVDA share of top10={t10[0]/s*100:.2f}%")
assert s == D('59.87')

# G11 scale
pa = D('97889.67'); ck = D('7409.79')
print(f"G11 ClassK share of portfolio assets={ck/pa*100:.2f}% holdings 391 issuers 311 diff={391-311}")
assert 391 - 311 == 80

# G12 fees/turnover/sector
print(f"G12 expense 0.65=0.65+0.00 | turnover 37 vs 36.67 diff={D('37')-D('36.67')}pp | IT sector 54.94-54.88={D('54.94')-D('54.88')}pp | example 66/208/362/810")
assert D('37') - D('36.67') == D('0.33')

print("ALL 12 GROUPS PASS")
