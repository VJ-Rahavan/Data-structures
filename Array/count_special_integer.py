# I use two sets: seen to track numbers we have encountered, and bad to track numbers whose contiguous block has been broken.

# As I iterate through the array, if the current number was seen before 
# and it is different from the previous element, 
# it means this number has appeared in an earlier block and has now reappeared, 
# so it is not special. I add it to bad.

# At the end, the number of special integers is simply the total distinct integers minus the integers in bad.

class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        count = 0
        seen = {}
        
        seen[nums[0]] = 1
        res = set()
        
        for i in range(1,len(nums)):
            seen[nums[i]] = seen.get(nums[i],0) + 1
            if nums[i] == nums[i-1] and nums[i] not in res and seen[nums[i]] <= 2:
                count += 1
                res.add(nums[i])
            else:
                if nums[i] != nums[i-1] and nums[i] in res:
                    count -= 1
                    res.remove(nums[i])
        
        for i in range(len(nums)):
            if nums[i] in seen:
                if 1 == seen[nums[i]]:
                    count += 1
                
        return count

class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        seen = set()
        bad = set()

        for i, num in enumerate(nums):
            if num in seen and nums[i - 1] != num:
                bad.add(num)

            seen.add(num)

        return len(seen) - len(bad)