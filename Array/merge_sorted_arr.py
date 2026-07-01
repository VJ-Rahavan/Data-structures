def merge_sorted_arr(arr1,arr2):
    arr1_len = len(arr1) 
    arr2_len = len(arr2)
    
    i = j = 0
    res = []
    while i < arr1_len and j < arr2_len:
        if arr1[i] <= arr2[j]:
            res.append(arr1[i])
            i+=1
        else:
            res.append(arr2[j])
            j+=1
    
    res.extend(arr1[i:])
    res.extend(arr2[j:])
    
    print(res)

merge_sorted_arr([2,3,],[1,4,5])