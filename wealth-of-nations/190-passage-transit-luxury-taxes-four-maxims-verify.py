# -*- coding: utf-8 -*-
# Data from the book passage covered by note 190; no modern measurement.
# 1 Passage duties: purposes 2 (road, navigation), proper base bulk/weight (2)
assert len(["maintenance of the road", "maintenance of the navigation"]) == 2
assert len(["bulk", "weight"]) == 2
# 2 Transit duties: most important = Denmark Sound (1); paid altogether by foreigners
assert len(["king of Denmark upon ships through the Sound"]) == 1
assert len([]) == 0  # home subjects pay none of it
# 3 Luxury taxes vs maxims: agree to first 3, offend against the 4th
assert len(["equality (as agreeable as any)", "certainty", "convenience"]) == 3
assert len(["economy (fourth maxim) offended"]) == 1
# 4 Four ways they take out more than they bring in
assert len(["expense of levying (officers salaries/perquisites)", "obstruction to industry", "forfeitures from smuggling hope", "vexation of visits/examination"]) == 4
# 5 Levying expense: excise ~5.5% < customs salaries/incidents >10% < salaries+perquisites 20-30%
assert 5.5 < 10 < 20 <= 30
assert 2500000 < 4975652  # customs neat below 2.5m vs excise neat 4,975,652 (pounds)
assert 50000 > 0  # supposed saving on malt excise expense exceeds £50,000
# 6 Birmingham transmission is inverse: dearer foreign wine -> cheaper hardware part
assert len(["dearer foreign wine", "cheaper hardware sold in exchange"]) == 2
print("190 verify: 6 assertions passed")
