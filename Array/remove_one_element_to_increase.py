# I scan the array and find the first adjacent pair that violates the strictly increasing condition.
# At that point, I decide whether to remove the previous or current element by checking whether the remaining neighbors can stay increasing.
# I simulate the removal by overwriting the value and track whether one element has already been removed.
# If I find another violation, I return False; otherwise, the array can be made strictly increasing.


class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        removed = False

        for i in range(1, len(nums)):

            if nums[i] > nums[i - 1]:
                continue

            if removed:
                return False

            removed = True

            if i == 1 or nums[i] > nums[i - 2]:
                nums[i - 1] = nums[i]      # remove previous
            else:
                nums[i] = nums[i - 1]       # remove current

        return True