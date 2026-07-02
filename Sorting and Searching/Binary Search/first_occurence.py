def binary_search(arr,target):
    start = 0
    end = len(arr) - 1
    target_index = -1
    
    while(start <= end):
        mid = (start+end)//2
        
        if arr[mid] == target:
            target_index = mid
            end = mid - 1
            print(target_index)
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid -1
    
    return target_index