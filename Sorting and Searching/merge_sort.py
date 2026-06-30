# Merge Sort divides the array until each subarray contains a single element, because a single element is inherently sorted. The sorted subarrays are then merged back together to produce the final sorted array.

# During the divide phase, no sorting happens. We only split the array into smaller and smaller pieces until each piece has one element.

# The actual sorting happens during the merge phase. Each merge combines two already sorted arrays into a larger sorted array, eventually producing the fully sorted array.

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2
    
    leftSort = mergeSort(arr[:mid])
    rightSort = mergeSort(arr[mid:])
    
    return merge(leftSort,rightSort)
    
def merge(left, right):
    res = []
    i = 0
    j = 0
    
    while(i < len(left) and j < len(right)):
        if left[i] <= right[j]:
            res.append(left[i])
            i+=1
        else:
            res.append(right[j])
            j+=1
    res.extend(left[i:])
    res.extend(right[j:])
    
    return res
    
    
    
    
            
            