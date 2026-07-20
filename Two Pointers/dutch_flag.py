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
#Test cases to validate the implementation of sortColors
if __name__ == "__main__":
    nums1 = [2, 0, 2, 1, 1, 0]
    expected_output1 = [0, 0, 1, 1, 2, 2]
    assert sortColors(nums1) == expected_output1, "Test Case 1 Failed"

    nums2 = [0]
    expected_output2 = [0]
    assert sortColors(nums2) == expected_output2, "Test Case 2 Failed"

    nums3 = [1]
    expected_output3 = [1]
    assert sortColors(nums3) == expected_output3, "Test Case 3 Failed"

    nums4 = [2, 0, 1]
    expected_output4 = [0, 1, 2]
    assert sortColors(nums4) == expected_output4, "Test Case 4 Failed"

    nums5 = [0, 0, 0]
    expected_output5 = [0, 0, 0]
    assert sortColors(nums5) == expected_output5, "Test Case 5 Failed"

    print("All test cases passed!")