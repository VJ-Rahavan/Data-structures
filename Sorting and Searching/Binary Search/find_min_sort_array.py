def find_min_sorted_arr(arr):
    
    start = 0
    end = len(arr) - 1
    
    while start < end:
        mid = (start + end) // 2
        
        if arr[mid] > arr[end]:
            start = mid + 1
        else:
            end = mid
    
    return arr[start]