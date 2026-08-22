class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        seen = {}
        count = 0
        for num in nums:
            diff = num - k 
            summ = num + k
            if diff in seen:
                count += seen[diff]
            if summ in seen:
                count += seen[summ]

            seen[num] = seen.get(num, 0) + 1
        print(seen)
        return count
