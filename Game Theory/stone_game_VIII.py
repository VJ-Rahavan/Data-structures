from typing import List
from itertools import accumulate
from functools import cache

#Top Down Approach with Memoization
class Solution:
    def stoneGameVIII(self, A: List[int]) -> int:
        n = len(A)

        # Prefix sums
        # s[i] = sum of A[0] ... A[i]
        s = list(accumulate(A))

        @cache
        def maxDiff(i):
            # If we merge everything from 0 to n-1,
            # the game ends and we get the total sum.
            if i == n - 1:
                return s[n - 1]

            # Two choices:
            #
            # 1. Skip this prefix and move to i + 1
            # 2. Take prefix sum s[i], then opponent gets
            #    the state maxDiff(i + 1)
            return max(
                maxDiff(i + 1),
                s[i] - maxDiff(i + 1)
            )

        # First move must take at least 2 stones,
        # so the first valid prefix ends at index 1.
        return maxDiff(1)

#Bottom Up Approach with Tabulation
class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)

        prefix = [0] * n
        prefix[0] = stones[0]

        for i in range(1, n):
            prefix[i] = prefix[i - 1] + stones[i]

        dp = [0] * n

        dp[n - 1] = prefix[n - 1]

        for i in range(n - 2, 0, -1):
            dp[i] = max(
                prefix[i] - dp[i + 1],
                dp[i + 1]
            )

        return dp[1]