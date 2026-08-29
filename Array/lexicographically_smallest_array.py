#My approach is to first sort the array and then group the elements based on the limit.
#I then sort each group based on the original indices to maintain the order of elements within the group.
#Finally, I replace the elements in the original array with the sorted values from each group
class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        if not nums:
            return []

        new_arr = []

        for i in range(0, len(nums)):
            new_arr.append((nums[i], i))

        nums_sorted = sorted(new_arr)

        groups = []
        temp = []

        temp.append(nums_sorted[0])

        for i in range(1, len(nums_sorted)):
            if nums_sorted[i][0] - nums_sorted[i - 1][0] <= limit:
                temp.append(nums_sorted[i])
            else:
                groups.append(temp)
                temp = [nums_sorted[i]]
        groups.append(temp)

        for group in groups:
            arr = sorted(group, key=lambda x: x[1])

            for i in range(len(arr)):
                nums[arr[i][1]] = group[i][0]

        return nums

#optimal Solution
class Solution:
    def lexicographicallySmallestArray(
        self, nums: List[int], limit: int
    ) -> List[int]:

        if not nums:
            return []

        pairs = sorted((value, i) for i, value in enumerate(nums))

        start = 0

        while start < len(pairs):
            end = start

            # Find the end of the current group
            while (
                end + 1 < len(pairs)
                and pairs[end + 1][0] - pairs[end][0] <= limit
            ):
                end += 1

            # Original indices of this group
            indices = sorted(pairs[i][1] for i in range(start, end + 1))

            # Values are already sorted because pairs is sorted by value
            for i, index in enumerate(indices):
                nums[index] = pairs[start + i][0]

            start = end + 1

        return nums