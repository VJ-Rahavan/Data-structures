class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for idx, val in enumerate(nums):
            summ = 0

            while val > 0:
                r = val % 10
                summ += r
                val //= 10
            print(summ)
            if summ == idx:
                return idx
        
        return -1
