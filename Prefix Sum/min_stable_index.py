# 3904. Smallest Stable Index II

# I precompute a min_suffix array where min_suffix[i] stores the minimum value from i to the end.
# Then, while traversing from left to right, I maintain max_prefix, the maximum value seen so far.
# For each index i, if max_prefix - min_suffix[i] <= k, 
# then all relevant values satisfy the stability condition, so I return i.
# Time complexity is O(n) and space complexity is O(n).

class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        min_suffix = [0] * n

        min_suffix[-1] = nums[-1]

        for i in range(n - 2, -1, -1):
            min_suffix[i] = min(nums[i], min_suffix[i + 1])

        max_prefix = nums[0]

        for i in range(n):
            max_prefix = max(max_prefix, nums[i])

            if max_prefix - min_suffix[i] <= k:
                return i

        return -1
