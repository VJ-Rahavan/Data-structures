#Binary search is a searching algorithm that finds the position of a target value within a sorted array. 
# It works by repeatedly dividing the search interval in half. 
# If the value of the target is less than the item in the middle of the interval, 
# it narrows the interval to the lower half. Otherwise, it narrows it to the upper half. 
# The process continues until the target value is found or the interval is empty.

#Binary Search for a sorted array in ascending order

def binary_search(arr,target):
    start = 0
    end = len(arr) - 1
    
    while(start <= end):
        mid = (start+end)//2
        
        if arr[mid] == target:
            print(mid)
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid -1
    
    return -1


binary_search([1,2,4,5,6],4)

#Binary Search for a sorted array in descending order
def binary_search(arr,target):
    start = 0
    end = len(arr) - 1
    target_index = -1
    
    while(start <= end):
        mid = (start+end)//2
        
        if arr[mid] == target:
            print(mid)
            return mid
        elif arr[mid] > target:
            start = mid + 1
        else:
            end = mid -1
    
    return target_index


binary_search([6,5,4,3,2,1],6)

#Binary Search using Recursion
def binary_search(arr,target,start,end):
    if start > end:
        return - 1
    mid = (start+end)//2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr,target,mid+1,end)
    else:
        return binary_search(arr,target,start,mid-1)
    
binary_search([1,2,3,4,5,6],12,0,5)