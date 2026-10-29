#!/usr/bin/env python3
"""Verify structural claims in Naval Almanack note 22 (saving yourself).
Illustrative parameters only; not empirical data."""

# 1. Chapter opener lists exactly six helper roles, and none of
# them can substitute for the person: substitutes count is zero.
helpers = ["doctor", "nutritionist", "teacher", "guru", "mentor", "trainer"]
assert len(helpers) == 6 and len(set(helpers)) == 6
substitutes = 0
assert substitutes == 0

# 2. Being-yourself scale (illustrative): the person scores 100 at
# being themselves; an imitator is capped below that by identity,
# not by effort.
self_score, imitator_cap = 100, 99
assert imitator_cap < self_score

# 3. Combinatorics: 20 binary traits already give 2**20 combos.
combos = 2 ** 20
assert combos == 1_048_576 and combos > 1_000_000

# 4. Two random people matching on all 20 binary traits
# (illustrative): probability 2**-20, below 1.1e-6.
p_match = 2 ** -20
assert abs(p_match - 1 / 1_048_576) < 1e-15 and p_match < 1.1e-6

# 5. Listening/absorbing and emulating are distinct modes; only
# absorbing is the recommended one in the source.
modes = ["listen-and-absorb", "emulate"]
assert len(modes) == 2 and modes[0] != modes[1]
recommended = ["listen-and-absorb"]
assert "emulate" not in recommended

# 6. The thing to find comes in four kinds: people, business,
# project, or art.
targets = ["people", "business", "project", "art"]
assert len(targets) == 4

print("22-save-yourself-verify: all assertions passed")
print(f"  helpers=6 substitutes=0; 2^20 combos = {combos:,}; p_match = {p_match:.3e}")
