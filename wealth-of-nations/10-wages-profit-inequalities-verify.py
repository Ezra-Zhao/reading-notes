# Verify Ch X Part I first three circumstances numbers (from Smith text)
# 1 five circumstances, this piece covers first three
circumstances=["agreeableness","learning","constancy","trust","probability"]
assert len(circumstances)==5 and circumstances[:3]==["agreeableness","learning","constancy"]
# 2 masons vs common: midpoints within 1.5-2x
for common, mason in [(4.5,7.5),(6,9.5),(9.5,16.5)]:
    r=mason/common; assert 1.5 <= r <= 2.0, r
# 3 London tailor half-a-crown 30d vs common 18d
assert 30/18 == 5/3
# 4 collier 2x Newcastle, 3x Scotland; coal-heavers 4-5x increasing
assert 2 < 3 < 4 <= 5
# 5 coal-heaver 6s=72d is 4x 18d; upper 10s
assert 6*12==72 and 72/18==4 and 10*12==120
# 6 smith 12h vs collier 8h
assert 12>8 and 12/8==1.5
print("10 verify: 6 assertions passed")
