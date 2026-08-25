# I first scan from right to left to find the first index where nums[i] < nums[i+1]; that's my pivot. 
# The suffix after this pivot is in decreasing order. 
# I then scan from the right to find the first element greater than the pivot and swap them. 
# Finally, I reverse the suffix to put it into its smallest possible order. 
# If no pivot exists, the array is already the largest permutation, 
# so reversing the entire array gives the smallest permutation. 
# The algorithm runs in O(n) time and O(1) space.


def rev(left,right,nums):
    while left < right:
        nums[left],nums[right] = nums[right], nums[left]
        left+=1
        right -= 1

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        pivot = n - 2

        while pivot >= 0 and nums[pivot] >= nums[pivot + 1]:
                pivot -= 1

        if pivot >= 0:
            large = n - 1

            while nums[large] <= nums[pivot]:
                large -= 1

            nums[pivot], nums[large] = nums[large], nums[pivot]

        rev(pivot+1,n-1,nums)
