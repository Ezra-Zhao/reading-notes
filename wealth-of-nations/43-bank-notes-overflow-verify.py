#!/usr/bin/env python3
# 43 verify: Book II Ch.2 bank notes, overflow of gold and silver (all figures from the book itself)
# 1 one banker: notes in circulation 100,000; 20,000 gold/silver often sufficient reserve; 80,000 spared
notes, reserve = 100_000, 20_000
assert notes - reserve == 80_000 and reserve * 5 == notes
# 2 hypothetical country: channel holds 1,000,000; banks issue 1,000,000 notes reserving 200,000;
#   gold left in circulation 800,000; paper+money poured in 1,800,000; overflow 800,000
channel = 1_000_000
issued, kept = 1_000_000, 200_000
gold_left = channel - kept
poured = gold_left + issued
overflow = poured - channel
assert gold_left == 800_000 and poured == 1_800_000 and overflow == 800_000
# paper cannot go abroad, so the overflow leaves as gold and silver (directional)
overflow_metal = "gold and silver"
assert overflow_metal == "gold and silver" and overflow == gold_left
# 3 industry is set in motion by three requisites; money is neither material nor tool
requisites = ["materials to work upon", "tools to work with", "wages or recompence"]
assert len(requisites) == 3 and "money" not in requisites
# 4 authors' computed proportions of circulating money to annual produce: a fifth, tenth, twentieth, thirtieth
props = [5, 10, 20, 30]
assert props == sorted(props) and props[0] == 5 and props[-1] == 30
# 5 paper reduces gold needed to about a fifth; the other four-fifths is the fund potentially added to industry
former_gold = 5
needed_after_paper = 1
assert needed_after_paper * 5 == former_gold and former_gold - needed_after_paper == 4
print("43-bank-notes-overflow: all 6 assertions passed")
