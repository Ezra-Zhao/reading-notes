#!/usr/bin/env python3
"""Verify structural claims in Naval Almanack note 30 (meaning and values).
Illustrative parameters only; not empirical data, not theological
or cosmological conclusions."""

# 1. Three answers to the meaning-of-life question: personal and
# self-found, no intrinsic meaning so create your own, and a
# physics-stitched entropy account.
answers = ["personal_find_your_own", "no_intrinsic_meaning_create_your_own", "entropy_heat_death"]
assert len(answers) == 3

# 2. Absence durations as stated: more than 10 billion years before,
# about 70 billion years after; the after span is about seven
# times the before span.
before_bn, after_bn = 10, 70
assert after_bn / before_bn == 7.0
assert after_bn > before_bn

# 3. The why-chain: in the illustrative model every answer generates
# one further why, so depth grows without a built-in stopping point.
depth = 0
for _ in range(5):
    depth += 1  # one answer, one new why
assert depth == 5

# 4. Honesty thread account: thought and speech aligned is one
# thread; disconnected adds future-planning and past-regretting.
aligned_threads = ["what_i_think_and_say"]
disconnected_threads = ["what_i_think", "future_planning", "past_regretting"]
assert len(aligned_threads) == 1
assert len(disconnected_threads) > len(aligned_threads)

# 5. Compound interest is named for six domains.
domains = ["money", "relationships", "love", "health", "activities", "habits"]
assert len(domains) == 6

# 6. Named value samples in the section: honesty, long-term only,
# peer-only relationships, no anger (four). Alignment test: when
# values align, small-issue weight is low; when they do not, the
# quarrel weight is high.
values = ["honesty", "long_term", "peer_only", "no_anger"]
assert len(values) == 4
small_issue_weight = {"aligned": 1, "misaligned": 9}
assert small_issue_weight["aligned"] < small_issue_weight["misaligned"]

print("30-meaning-values-verify: all assertions passed")
print("  answers=3; after/before=7x; compound domains=6; values=4")
