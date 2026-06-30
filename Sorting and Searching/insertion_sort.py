def insertionSort(arr):
    
    for i in range(1,len(arr)):
        key = arr[i]
        start = i - 1
        while(key < arr[start] and start >= 0):
            arr[start+1] = arr[start]
            start -= 1
        
        arr[start+1] = key
    print(arr)


insertionSort([3,4,5,1,6,2])

# Insertion Sort maintains a sorted portion of the array and inserts each new element into its correct position by shifting larger elements to the right.