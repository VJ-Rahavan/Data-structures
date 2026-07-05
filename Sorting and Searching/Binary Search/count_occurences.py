#Count occurrences of element in sorted array
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
    
def count_occurrence(arr,target):
    
    first_occurrence = find_occurrence(arr,target,True)
    
    if first_occurrence == -1:
        return 0
    
    last_occurrence = find_occurrence(arr,target,False)
    
    return last_occurrence - first_occurrence + 1
