# 940. Distinct Subsequences II

# I use DP where `dp` represents the number of distinct subsequences so far, including the empty subsequence.
# For each character, every existing subsequence can either take or skip it, so we initially double `dp`.
# If the character appeared before, some of the newly created subsequences are duplicates, 
# So I subtract `last[c]`, which stores the DP value before its previous occurrence.
# I update `last[c]` with the old `dp` and take modulo `10^9 + 7` to prevent the values from becoming too large.
# Finally, I subtract `1` to remove the empty subsequence since the problem asks for non-empty subsequences.


class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7

        dp = 1
        last = {}

        for c in s:
            old_dp = dp

            dp = (2 * dp - last.get(c, 0)) % MOD

            last[c] = old_dp

        return (dp - 1) % MOD