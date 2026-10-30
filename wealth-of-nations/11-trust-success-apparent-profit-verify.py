# Verify Ch X Part I trust/probability/apparent profit numbers
# 1 law odds 20 to 1; participants 21
assert 20+1==21
# 2 lottery advance 20,30,40 increasing
assert 20<30<40
# 3 uninsured houses 19/20=95%, 99/100=99%
assert 19/20==0.95 and 99/100==0.99
# 4 apothecary cost 30->300 and 40->400 both 1000% markup on cost (10x price)
assert 300/30==10 and 400/40==10
# 5 grocer 100*50%=50 vs wholesale 10000*10%=1000; rate ratio 5, amount ratio 20
assert 100*0.50==50 and 10000*0.10==1000 and 0.50/0.10==5 and 1000/50==20
# 6 sailor max 27s < common labourer monthly min 40s; London-Leith diff 3-4s
assert 27<40 and 3<=4
print("11 verify: 6 assertions passed")
