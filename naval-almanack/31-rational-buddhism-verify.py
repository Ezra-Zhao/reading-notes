#!/usr/bin/env python3
"""Verify structural claims in Naval Almanack note 31 (rational Buddhism
and the present). Illustrative parameters only; not empirical data,
not theological, scientific or medical conclusions."""

# 1. Self-verified examples he names: three.
verified = ["meditation_is_good", "clearing_mind_is_good", "base_awareness_below_monkey_mind"]
assert len(verified) == 3

# 2. Named classes he sets aside: two (past-life karma, chakra-style
# nomenclature). Rule: unfalsifiable claims are not treated as
# fundamental truth in his system.
set_aside = ["past_life_karma", "chakra_nomenclature"]
assert len(set_aside) == 2
def is_fundamental(falsifiable):
    return bool(falsifiable)
assert is_fundamental(False) is False
assert is_fundamental(True) is True

# 3. The system has two poles: evolution as the binding principle,
# Buddhism as the internal-state philosophy.
poles = ["evolution_binding_principle", "buddhism_internal_philosophy"]
assert len(poles) == 2

# 4. Human trajectory in order: innocence, corruption, then wisdom
# as discarding vices and returning to virtue by way of knowledge.
trajectory = ["innocence", "corruption", "discard_vices_return_to_virtue"]
assert trajectory[0] == "innocence" and trajectory[-1].startswith("discard")

# 5. Wisdom is defined by long-term consequences, not short-term gain.
definition = {"wisdom": "understanding_long_term_consequences_of_actions"}
assert "long_term" in definition["wisdom"]
assert "short_term" not in definition["wisdom"]

# 6. Time account: reachable past moments and knowable future moments
# are both zero in his framing; only the present is in the real set.
# Inspiration value strictly decays with delay in the illustrative model.
reachable_past, knowable_future = 0, 0
real_set = ["present"]
assert reachable_past == 0 and knowable_future == 0 and len(real_set) == 1
inspiration = [100.0 * (0.5 ** d) for d in range(4)]
assert all(inspiration[i] > inspiration[i + 1] for i in range(3))

print("31-rational-buddhism-verify: all assertions passed")
print("  verified=3; set_aside=2; poles=2; real_set=[present]; inspiration decays")
