# I maintain three pointers: low, mid, and high. 
# Everything before low is guaranteed to be 0, everything after high is guaranteed to be 2, 
# and mid scans the unknown region. When I see a 0, I swap it to the front and advance both low and mid. 
# When I see a 1, it's already in the correct middle region, so I only advance mid. 
# When I see a 2, I swap it with high and decrement high, 
# but I don't move mid because the element swapped in from the end hasn't been examined yet. 
# This gives an in-place, one-pass solution with O(n) time and O(1) space.

def sortColors(nums):
    low = 0
    mid = 0
    high = len(nums) - 1

    while mid <= high:

        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1

        elif nums[mid] == 1:
            mid += 1

        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

    return nums


nums = [2, 0, 2, 1, 1, 0]
print(sortColors(nums))