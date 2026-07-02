#Binary Search(Recursion)
def find_occurrence(arr,target,find_first):
    start = 0
    end = len(arr)-1
    
    target_index = -1
    
    while start <= end:
        mid = (start+end)//2
        
        if arr[mid] == target:
            target_index = mid
            if find_first:
                end = mid - 1
            else:
                start = mid + 1
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    
    return target_index

def search_range(arr,target):
    first_occurrence = find_occurrence(arr,target,True)
    second_occurrence = find_occurrence(arr,target,False)
    print(first_occurrence,second_occurrence)
    return [first_occurrence,second_occurrence]


search_range([1,3,4,6,6,8,9],6)
    
    
#Recursive Binary Search to find first and last occurrence of a target in a sorted array
def find_occurrence(arr, target, find_first, start=0, end=None):
    if end is None:
        end = len(arr) - 1
    if start > end:
        return -1
    
    mid = (start + end) // 2
    
    if arr[mid] == target:
        if find_first:
            left_result = find_occurrence(arr, target, True, start, mid - 1)
            return left_result if left_result != -1 else mid
        else:
            right_result = find_occurrence(arr, target, False, mid + 1, end)
            return right_result if right_result != -1 else mid
    elif arr[mid] > target:
        return find_occurrence(arr, target, find_first, start, mid - 1)
    else:
        return find_occurrence(arr, target, find_first, mid + 1, end)