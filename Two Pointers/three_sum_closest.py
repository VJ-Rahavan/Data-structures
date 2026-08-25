class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)

        res = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):

            start = i + 1
            end = n - 1

            while start < end:

                summ = nums[i] + nums[start] + nums[end]

                # Exact match
                if summ == target:
                    return target

                # Update closest answer
                if abs(target - summ) < abs(target - res):
                    res = summ

                # Move pointers
                if summ < target:
                    start += 1
                else:
                    end -= 1

        return res