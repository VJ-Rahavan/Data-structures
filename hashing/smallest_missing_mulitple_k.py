class Solution:

    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums_set = set(nums)

        num = k

        while num in nums_set:
            num += k

        return num