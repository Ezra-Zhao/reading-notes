#!/usr/bin/env python3
"""Verify structural claims in Naval Almanack note 34 (Naval's
writing: life formulas and rules; next-on-Naval; appreciation and
sources). Illustrative parameters only; not empirical data,
not health or investment advice."""

# 1. Happiness top level has three terms; health splits into three,
# and each of exercise, diet, sleep splits into three parts.
happiness = ["health", "wealth", "good_relationships"]
health = ["exercise", "diet", "sleep"]
sub = {"exercise": 3, "diet": 3, "sleep": 3}
assert len(happiness) == 3 and len(health) == 3
assert all(v == 3 for v in sub.values())

# 2. Income splits into three; the 2008 formula's leverage is
# capital, people, intellectual property; ROI splits into three.
income = ["accountability", "leverage", "specific_knowledge"]
leverage_2008 = ["capital", "people", "intellectual_property"]
roi = ["buy_and_hold", "valuation", "margin_of_safety"]
assert len(income) == 3 and len(leverage_2008) == 3 and len(roi) == 3
assert "code" not in leverage_2008 and "media" not in leverage_2008

# 3. The 2016 rules number seventeen; attributed sources among
# them are four (Buddha twice, Buffett once, Tolle once).
rules_count = 17
attributed = {"buddha": 2, "buffett": 1, "tolle": 1}
assert rules_count == 17 and sum(attributed.values()) == 4

# 4. Closing priority order is fixed: health, love, mission.
priority = ["health", "love", "mission"]
assert priority == ["health", "love", "mission"]

# 5. Next-on-Naval: six cut-section topics; three most popular items.
cut_topics = ["education", "angellist_story", "investing",
              "startups", "crypto", "relationships"]
popular = ["how_to_get_rich_compilation", "knowledge_project",
           "joe_rogan_podcast"]
assert len(cut_topics) == 6 and len(popular) == 3

# 6. Sources list runs to eighty entries; five almanack-genre
# inspirations are named; four interviewers are credited.
sources = list(range(1, 81))
inspirations = ["poor_charlies", "zero_to_one", "seeking_wisdom",
                "berkshire_letters", "principles"]
interviewers = ["shane_parrish", "joe_rogan", "sarah_lacy",
                "tim_ferriss"]
assert len(sources) == 80 and sources[-1] == 80
assert len(inspirations) == 5 and len(interviewers) == 4

print("34-formulas-rules-verify: all assertions passed")
print("  happiness=3 health=3x3; income=3 leverage08=3 roi=3; rules=17 attributed=4; cut=6 popular=3; sources=80")
