from math import gcd
from typing import List

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)

        # Precompute every subset's LCM and its sign (+/-)
        subsets = []

        def lcm(a, b):
            return a * b // gcd(a, b)

        def dfs(idx, curr_lcm, bits):
            if idx == n:
                if bits > 0:
                    sign = 1 if bits % 2 == 1 else -1
                    subsets.append((curr_lcm, sign))
                return

            # Skip current coin
            dfs(idx + 1, curr_lcm, bits)

            # Take current coin
            if bits == 0:
                new_lcm = coins[idx]
            else:
                new_lcm = lcm(curr_lcm, coins[idx])

            dfs(idx + 1, new_lcm, bits + 1)

        dfs(0, 1, 0)

        def count(x):
            total = 0
            for l, sign in subsets:
                total += sign * (x // l)
            return total

        left = min(coins)
        right = min(coins) * k

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left