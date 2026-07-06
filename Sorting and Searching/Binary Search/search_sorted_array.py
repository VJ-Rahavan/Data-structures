# I use modified binary search because, in a rotated sorted array, at least one half is always sorted.
# I identify the sorted half and check whether the target lies within its range, then discard the other half.
# This continues until the target is found, giving O(log n) time complexity and O(1) space complexity.


def search_sorted_array(arr,target):
    start = 0
    end = len(arr) - 1
    
    while start <= end:
        mid = (start + end) // 2
        
        if arr[mid] == target:
            return mid
        if arr[start] <= arr[mid]:
            if arr[start] <= target < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if arr[mid] < target <= arr[end]:
                start = mid + 1
            else:
                end = mid - 1
    return -1
print(search_sorted_array([4,5,6,7,0,1,2],0))