# 115. Distinct Subsequences

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)

        # dp[i][j] = number of ways to form
        # first i characters of t using
        # first j characters of s
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # Empty t can be formed in exactly 1 way:
        # choose nothing
        for j in range(m + 1):
            dp[0][j] = 1

        for i in range(1, n + 1):
            for j in range(1, m + 1):

                if t[i - 1] == s[j - 1]:

                    # Two choices:
                    # 1. Use s[j-1]
                    # 2. Skip s[j-1]
                    dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]

                else:

                    # Characters don't match,
                    # so we must skip s[j-1]
                    dp[i][j] = dp[i][j - 1]

        return dp[n][m]