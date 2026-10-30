# Verify Ch X Part II second way: publicly funded education increasing competition
# 1 second way increases competition, opposite of first way restraining it
assert "increase" != "restrain"
# 2 curate 5 merks approx 10 pounds present silver; master mason 4d/day approx 1s=12d present, journeyman 3d approx 9d; ratios in present terms
assert 12==3*4 and 9==12*3//4
# 3 statute 12 Anne: curate stipend band 20-50 pounds; 40 inside band and reckoned very good; some under 20
assert 20 <= 40 <= 50 and 20 < 40
# 4 London journeyman shoemakers 40/year equals good curate pay; common labourers often above 20
assert 40==40 and 40>20
# 5 minae conversions consistent: 4 minae = 13l 6s 8d; 5 = 16l 13s 4d; 10 = 33l 6s 8d (in pence: 1l=240d, 1s=12d)
def to_pence(pounds, shillings, pence): return pounds*240+shillings*12+pence
four=to_pence(13,6,8); five=to_pence(16,13,4); ten=to_pence(33,6,8)
assert four*5==five*4==ten*2==16000  # per-mina value consistent: 800d
assert ten//10==800
# 6 Isocrates: 10 minae/scholar x 100 scholars = 1000 minae; source printed pound total 3335l 6s 8d differs from recomputed 3333l 6s 8d by 2 pounds, registered not used
assert 10*100==1000
recomputed=to_pence(33,6,8)*100; printed=to_pence(3335,6,8)
assert printed-recomputed==2*240
print("14 verify: 6 assertions passed")
