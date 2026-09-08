# I first count the frequency of each number, so the total value of choosing a number is `number × frequency`.
# Then I process the unique numbers in sorted order, treating them like the House Robber problem: 
# if two numbers are consecutive, I must choose either the current number or the previous best.
# `earn1` stores the best result from two positions back, while `earn2` stores the best result from the previous position.
# If the current number is not consecutive with the previous number,
# I can safely add its value to `earn2` because there is no conflict.
# This gives **O(n log n)** time due to sorting and **O(n)** space for the frequency map.

from collections import Counter


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        freq = Counter(nums)
        nums = sorted(list(set(nums)))

        earn1, earn2 = 0, 0

        for i in range(len(nums)):
            cur = nums[i] * freq[nums[i]]
            if i > 0 and nums[i] == nums[i - 1] + 1:
                temp = max(cur + earn1, earn2)
                earn1 = earn2
                earn2 = temp
            else:
                temp = cur + earn2
                earn1 = earn2
                earn2 = temp
        return earn2
