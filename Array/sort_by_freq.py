# Sort array by frequency of elements

def sort_by_freq(arr):
    hash_map = {}
    for i in arr:
        if i in hash_map:
            hash_map[i] +=1
        else:
            hash_map[i] = 1
    
    sorted_items = sorted(arr,key=lambda item: item[1])
    
    res = []
    
    for key,value in sorted_items:
        res.extend([key]*value)
    
    print(res)

sort_by_freq([3,5,1,3,4,2,5,1,1])