"""Market Wizards 11 Ge Weidong verification script (clean-room, self-written)
Checks six recomputable figures stated in the note; inputs are public-report figures:
1) 2019 GigaDevice private placement: 5.035m shares x 75.47 yuan = about CNY 380m;
2) 2020 placement: 7.3609m shares x 203.78 yuan = about CNY 1.50bn;
3) GigaDevice peak 846.66 (2026-06-29 intraday) to 257.80 (2026-10-30 close) = -69.6%, recovery needs +228.4%;
4) Holding chain: 17.0267m end-2025 - 0.7651m Q1 reduction = 16.2616m; +0.1851m Q3 = 16.4467m;
5) Ge + Wang Ping GigaDevice: 16.4467m + 8.5999m = 25.0466m shares; reported value CNY 8.864bn implies 353.9 yuan/share;
6) Haiguang pre-IPO: 44.590909m shares x 11.21 yuan = about CNY 499.9m; IPO price 36 yuan = 3.21x cost price.
"""
assert round(503.5 * 75.47, 1) == 37999.1
print("1 ok: 2019 placement 503.5w x 75.47 = 37999.1w yuan (~3.80yi)")
assert round(736.09 * 203.78, 1) == 150000.4
print("2 ok: 2020 placement 736.09w x 203.78 = 150000.4w yuan (~15.00yi)")
assert round((257.80 - 846.66) / 846.66 * 100, 1) == -69.6
assert round((846.66 / 257.80 - 1) * 100, 1) == 228.4
print("3 ok: peak to Oct30 = -69.6%, recovery needs +228.4%")
assert round(1702.67 - 76.51, 2) == 1626.16 and round(1626.16 + 18.51, 2) == 1644.67
print("4 ok: 1702.67 - 76.51 = 1626.16; + 18.51 = 1644.67 (wan shares)")
assert round(1644.67 + 859.99, 2) == 2504.66
assert round(88.64 * 10000 / 2504.66, 1) == 353.9
print("5 ok: Ge+Wang = 2504.66w shares; 88.64yi implies 353.9 yuan/share")
assert round(4459.0909 * 11.21, 1) == 49986.4
assert round(36 / 11.21, 2) == 3.21
print("6 ok: Haiguang cost ~49986.4w yuan (~4.99yi); IPO price = 3.21x cost")
print("All six assertions passed")
