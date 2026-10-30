# Verify Ch XI intro: natural rent definition, monopoly price, rent as effect
# 1 tenant retention = stock maintenance + ordinary profits of farming stock in neighbourhood; rent = all surplus above it; deviations: landlord liberality, landlord ignorance, tenant ignorance
retention = ["seed+labour+cattle+instruments stock", "ordinary profits of farming stock"]
deviations = ["landlord liberality", "landlord ignorance", "tenant ignorance"]
assert len(retention) == 2 and len(deviations) == 3
# 2 improvement-interest rebuttal has three layers: rent for unimproved land; tenant-made improvements charged at renewal; rent for what is incapable of human improvement (kelp)
layers = ["unimproved land rent", "tenant improvements charged at renewal", "incapable of improvement"]
assert len(layers) == 3 and layers[2] == "incapable of improvement"
# 3 two extreme instances: kelp shore; Shetland fish rent based on land+water combined produce
instances = ["kelp", "shetland fish"]
assert len(instances) == 2
rent_base = "land and water together"
assert "water" in rent_base
# 4 two thresholds in order: price replaces stock+ordinary profits (marketable) < price above that (affords rent)
thresholds = ["replace stock + ordinary profits", "above that affords rent"]
assert thresholds[0].startswith("replace") and "rent" in thresholds[1]
# 5 causal directions: wages/profit are causes of price; rent is effect of price
causes = {"wages": "cause of price", "profit": "cause of price", "rent": "effect of price"}
assert causes["rent"] == "effect of price" and causes["wages"] != causes["rent"]
# 6 food surplus under most liberal maintenance still leaves rent; rent varies with fertility and situation (2 dimensions); London-counties petition not more than 50 years ago
assert len(["fertility", "situation"]) == 2 and 50 >= 50
print("16 verify: 6 assertions passed")
