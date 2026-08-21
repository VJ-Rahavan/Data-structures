class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        low = 1
        high = len(nums) - 1

        while low < high:
            mid = (low+high)//2
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1
            if count > mid:
                high = mid
            else:
                low = mid + 1
        
        return low

# Since every number lies between 1 and n, I binary search on the value range instead of the array indices. 
# For each middle value, I count how many elements are less than or equal to it. 
# If that count exceeds mid, then there are more numbers than distinct values available in the range 1...mid. 
# By the Pigeonhole Principle, a duplicate must exist in that left half, so I move high to mid.
# Otherwise, the duplicate must be in the right half, so I move low to mid + 1. 
# I continue until low equals high, and that value is the duplicate. 
# The algorithm runs in O(n log n) time because each binary search step scans the array once, while using only O(1) extra space.