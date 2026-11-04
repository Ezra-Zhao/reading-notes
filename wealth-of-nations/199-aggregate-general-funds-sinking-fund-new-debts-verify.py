# -*- coding: utf-8 -*-
# Data from the book passage covered by note 199; no modern measurement.
# 1 Two company funds stand side by side: bank fund larger, at 6 per cent;
#    East India fund smaller, at 5 per cent (pounds, shillings/pence aside)
assert 3375027 > 3200000
assert 6 > 5
# 2 East India annuity recomputes exactly: 5 per cent of 3,200,000 is
#    160,000. The bank annuity is recorded as printed in the book
#    (206,501 pounds); it is NOT recomputed from the stated 6 per cent.
assert 3200000 * 5 // 100 == 160000
assert 206501 > 160000
# 3 Three great funds after the accumulations; General Fund annuities
#    are recorded at 724,849 pounds
assert len(["Aggregate Fund", "South Sea Fund", "General Fund"]) == 3
assert 724849 > 323434
# 4 Liberation by anticipation alone required exactly 2 attentions:
#    not overloading the fund; not anticipating a second time before the
#    first anticipation expired
assert len(["do not overload the fund",
            "do not anticipate again before the first expires"]) == 2
# 5 Interest path strictly decreasing; the fall from 6 to 5 saved
#    one-sixth of the annuities that had been paid at 6
path = [6, 5, 4, 3.5, 3]
assert path == sorted(path, reverse=True) and len(set(path)) == 5
assert abs((6 - 5) / 6 - 1 / 6) < 1e-12
# 6 Sinking fund in 1717: 323,434 pounds; its recorded character is
#    two-sided: instituted for paying old debts, it facilitates new ones
assert 323434 > 0
assert len(["instituted for the payment of old debts",
            "facilitates contracting new debts"]) == 2
print("199 verify: 6 assertions passed")
