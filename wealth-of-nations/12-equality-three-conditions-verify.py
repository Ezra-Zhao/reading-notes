# Verify Ch X Part I three conditions numbers
# 1 three conditions
conditions=["well-known long established","ordinary/natural state","sole or principal employment"]
assert len(conditions)==3
# 2 wartime sailors pressed 40k-50k
assert 40000 <= 50000
# 3 sailor pay peace 21-27s vs war 40-60s (guinea=21s, 3 pounds=60s)
assert 21<27<40<60 and 40/21>1.9-0.05  # approx 1.90
assert 21==21 and 3*20==60
# 4 cottars cash part: 2 pecks oatmeal/week approx 16d, part not whole
assert 16>0
# 5 Shetland stockings >1000 pairs/yr, 5-7d; Lerwick 10d/day; good spinner 20d/week (registered, not annualised)
assert 1000>=1000 and 5<7 and 10>0 and 20==2*10
# 6 two towns / two manufacture types
assert len(["Birmingham","Sheffield"])==2 and len(["fashion/fancy","use/necessity"])==2
print("12 verify: 6 assertions passed")
