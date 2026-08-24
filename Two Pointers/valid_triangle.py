# First, I sort the array so I can use the two-pointer technique.
# I fix k as the largest side and use i and j to find pairs where nums[i] + nums[j] > nums[k]. 
# If the condition is satisfied, since the array is sorted,
# every index between i and j can form a valid triangle with j and k, 
# so I add j - i at once and move j left. Otherwise, I move i right to increase the sum. 
# The time complexity is O(n²) after sorting, and the extra space is O(1).

from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        count = 0
        
        for k in range(n - 1, 1, -1):
            i = 0
            j = k -1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    count += j - i
                    j -= 1
                
                else:
                    i += 1
        
        return count