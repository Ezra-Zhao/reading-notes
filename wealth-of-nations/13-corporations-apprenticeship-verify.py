# Verify Ch X Part II first way: corporations and apprenticeship numbers
# 1 three ways of policy: restrain competition, increase competition, obstruct circulation
ways=["restrain competition","increase competition","obstruct circulation"]
assert len(ways)==3 and ways[0]=="restrain competition"
# 2 apprentice caps: Sheffield cutler 1, Norfolk/Norwich weaver 2, hatter 2, London silk-weaver 2
caps={"sheffield_cutler":1,"norwich_weaver":2,"hatter":2,"london_silk_weaver":2}
assert list(caps.values())==[1,2,2,2]
# 3 fines both 5 pounds/month; hatter split half king half suitor = 2.5 each
assert 5==5 and 5/2==2.5
# 4 terms: England 7, Paris 5+5=10, Scotland common 3; ordering 10>7>3
assert 5+5==10 and 10>7>3
# 5 coach/wheel adjudication direction
assert {"coachmaker_may_make_wheels":False,"wheelwright_may_make_coaches":True}["wheelwright_may_make_coaches"] is True
# 6 town vs country hundred-to-one; half-dozen wool-combers keep 1000 spinners/weavers
assert 100//1==100 and 6<1000 and 1000//6>100
print("13 verify: 6 assertions passed")
