# Bubble Sort repeatedly compares adjacent elements and swaps them if they're in the wrong order, causing the largest unsorted element to bubble up to the end after each pass.

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        isSwapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                isSwapped = True

        if not isSwapped:
            break
# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]
bubbleSort(arr)
print("Sorted array is:", arr)

# Selection Sort repeatedly finds the smallest element from the unsorted
#  portion of the array and places it in its correct position.
def selectionSort(arr):
    for i in range(len(arr)):
        s = i
        for j in range(i+1,len(arr)):
            if arr[s] > arr[j]:
                s = j
        
        print(arr[s])
        
        if s!=i:
            arr[i],arr[s] = arr[s],arr[i]
    
    print(arr)

selectionSort([1,6,3,2,4])