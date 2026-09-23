class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        n = len(nums)
        total = sum(nums)
        target = total - x

        if target == 0:
            return n
        if target < 0:
            return -1

        longest = -1
        left = 0
        cur = 0

        for right in range(n):
            cur += nums[right]

            while left < right and cur > target:
                cur -= nums[left]
                left += 1
            
            if cur == target:
                longest = max(longest, right - left + 1)
            
        return -1 if longest == -1 else n - longest