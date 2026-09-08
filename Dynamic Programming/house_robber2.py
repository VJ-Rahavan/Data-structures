class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.loot_max(nums[1:]), self.loot_max(nums[:-1]))

    def loot_max(self, nums: List[int]) -> int:
        house1, house2 = 0, 0

        for house in nums:
            temp = max(house + house1, house2)
            house1 = house2
            house2 = temp

        return house2
