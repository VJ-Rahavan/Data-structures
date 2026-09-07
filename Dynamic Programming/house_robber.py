
# This is a 1D DP problem. At each house, I have two choices: rob the current house or skip it. 
# If I rob the current house, I cannot rob the previous house, so the value is nums[i] + dp[i-2]. 
# If I skip it, I keep dp[i-1]. Therefore, dp[i] = max(nums[i] + dp[i-2], dp[i-1]).
# I only need the previous two DP values, so I optimize the space from O(n) to O(1) using rob1 and rob2.

class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for i in nums:
            temp = max(i + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        
        return rob2
            