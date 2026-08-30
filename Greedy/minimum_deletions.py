# Removing Minimum and Maximum From Array

# First, find the indices of the minimum and maximum elements. 
# Let left and right be their smaller and larger indices. 
# There are only three possibilities: 
# remove both from the front, remove both from the back, or remove one from each end. 
# Calculate the deletions for all three cases and return the minimum. Time: O(n), Space: O(1).

class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)

        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))

        left = min(min_idx, max_idx)
        right = max(min_idx, max_idx)

        front = right + 1
        back = n - left
        both = (left + 1) + (n - right)

        return min(front, back, both)