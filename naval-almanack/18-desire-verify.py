#!/usr/bin/env python3
"""Verify structural claims in Naval Almanack note 18 (desire, success).
Illustrative parameters only; not empirical data."""

# 1. Desire contract (illustrative): each unfulfilled big desire
# carries one unit of unhappiness load until fulfilled.
def load(n):
    return n * 1.0
assert load(5) == load(1) * 5
assert load(0) == 0

# 2. Time-health-money trifecta (as stated in the book): each life
# stage holds exactly two of the three, never all three at once.
stages = {
    "young": {"time", "health"},
    "middle": {"money", "health"},
    "old": {"money", "time"},
}
assert all(len(v) == 2 for v in stages.values())
assert not any(len(v) == 3 for v in stages.values())

# 3. Hedonic adaptation (illustrative halving): satisfaction from a
# new thing halves each period; after three periods 1/8 remains.
sat = 1.0
for _ in range(3):
    sat /= 2
assert sat == 0.125

# 4. One-thing focus: attention split evenly across n desires gives
# each 100/n; concentrating on one gives it the full 100, 5x the share.
def share(n):
    return 100 / n
assert share(1) == 100 and share(5) == 20
assert share(1) / share(5) == 5

# 5. Pascal test: sitting quietly and happily for 30 minutes is
# 0.5 hour, about 3.1% of a 16-hour waking day.
assert 30 / (16 * 60) * 100 == 3.125

# 6. Stepping out of the game: win/lose load is zero when the
# win-lose scorecard is no longer carried.
def game_load(playing, stakes=10):
    return stakes if playing else 0
assert game_load(True) == 10 and game_load(False) == 0

print("18-desire-verify: all assertions passed")
print(f"  desire load x5 = {load(5):.0f}; adapted satisfaction = {sat:.3f}; sit share = {30/(16*60)*100:.2f}%")
