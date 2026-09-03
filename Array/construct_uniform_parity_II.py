class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        minn = min(nums1)

        if minn % 2 == 1:
            return True

        return all(x % 2 == 0 for x in nums1)