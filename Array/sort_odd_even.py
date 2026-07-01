def sort_parity(arr):
    end = len(arr) - 1
    start = 0
    
    while start < end:
        if arr[start]%2 != 0:
            arr[end],arr[start] = arr[start],arr[end]
            end-=1
        else:
            start+=1
    
    print(arr)

sort_parity([2,3,4,5])