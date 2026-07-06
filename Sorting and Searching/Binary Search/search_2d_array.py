def search_matrix(arr,target):
    n = len(arr) * len(arr[0])
    start = 0
    end = n - 1
    cols = len(arr[0])
    
    while start <= end:
        mid = (start + end) // 2
        
        i = mid // cols
        j = mid % cols
        
        if arr[i][j] == target:
            return arr[i][j]
        elif arr[i][j] < target:
            start = mid + 1
        else:
            end = mid - 1
    return [-1,-1]

search_matrix([
    [1,  3,  5,  7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
],16)