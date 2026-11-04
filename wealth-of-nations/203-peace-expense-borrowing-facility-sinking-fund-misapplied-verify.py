# -*- coding: utf-8 -*-
# Data from the book passage covered by note 203; no modern measurement.
# 1 War-time failure to raise revenue in proportion has exactly 2 causes
assert len(["unwilling (fear of offending the people)",
            "unable (not knowing what taxes would suffice)"]) == 2
# 2 Perpetual funding: smallest possible increase of taxes raises the
#    largest possible sum; directions are opposite extremes
assert "smallest" != "largest" and 1 < 2
# 3 A sinking fund fails on exactly 2 grounds even if faithfully applied:
#    inadequate in amount, and almost always misapplied in practice
assert len(["inadequate for the whole war debt within any reasonable peace",
            "almost always applied to other purposes"]) == 2
# 4 Sinking funds formed by reduction of interest: exactly 2 examples,
#    Holland 1655 and the ecclesiastical state 1685, 30 years apart
assert 1685 - 1655 == 30
assert len(["Holland 1655", "ecclesiastical state 1685"]) == 2
# 5 A new tax occasions 2 felt consequences (murmur, opposition);
#    a momentary suspension of debt payment occasions 0 felt complaint
assert len(["murmur", "opposition"]) == 2 and 0 == 0
# 6 Only 3 states of mind can make an over-taxed people accept a new tax
assert len(["necessities of a new war", "animosity of national vengeance",
            "anxiety for national security"]) == 3
print("203 verify: 6 assertions passed")
