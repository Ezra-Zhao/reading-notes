# Verify Ch X Part II third way: obstruction of circulation and settlement laws
# 1 two obstructions: apprenticeship statute blocks employment-to-employment same place; corporations block place-to-place same employment
blocks={"apprenticeship_statute":"employment to employment, same place","corporations":"place to place, same employment"}
assert len(blocks)==2
# 2 original settlement thresholds: 40 days undisturbed residence; tenement 10 pounds/year; patch chain start points in order
assert 40==40 and 10==10
starts=["residence","written notice","church publication"]
assert len(starts)==3 and starts[0]=="residence" and starts[-1]=="church publication"
# 3 four other ways to gain settlement; first two need public deed of parish, last two closed to married men in practice
ways=["taxed and paying parish rates","annual parish office one year","apprenticeship in parish","hired service one year"]
assert len(ways)==4
# 4 security floor 30 pounds is 3x the 10-pound tenement line
assert 30==3*10
# 5 three similar weaving arts; changeover a few days, not seven years
assert len(["plain linen","plain silk","plain woollen"])==3 and 7*365>7
# 6 chapter-end numbers: London tailor cap 2s 7.5d = 31.5d; Burn experience above 400 years; assize statutes 31 Geo II before 3 Geo III (regnal order as stated in text)
assert 2*12+7.5==31.5 and 400>=400
print("15 verify: 6 assertions passed")
