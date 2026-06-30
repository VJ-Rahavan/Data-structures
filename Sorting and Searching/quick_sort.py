
# Quick Sort works by choosing a pivot, partitioning the array so that all elements smaller than the pivot are on the left and larger elements are on the right, placing the pivot in its final sorted position, and then recursively sorting the two partitions. It has an average time complexity of O(n log n), worst-case O(n²), is in-place, but not stable.
def quick_sort(arr,low,high):
    
    if low >= high:
        return
    
    pivot_index = partition(arr,low,high)
    
    quick_sort(arr,low,pivot_index-1)
    quick_sort(arr,pivot_index+1,high)
    
    print(arr)
    

def partition(arr,low,high):
    
    pivot = arr[high]
    
    j = low - 1
    
    for i in range(low,high):
        if arr[i] < pivot:
            j+=1
            arr[j],arr[i] = arr[i],arr[j]
    
    arr[j+1],arr[high] = arr[high],arr[j+1]
    return j+1
