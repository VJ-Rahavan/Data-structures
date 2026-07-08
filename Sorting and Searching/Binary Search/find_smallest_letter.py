# > I use binary search to find the first letter strictly greater than the target 
# by discarding half of the search space in each iteration.
# > If no greater letter exists, I use modulo to wrap around and 
# return the first letter in the array.


def find_smallest_letter(arr,target):
    
    start = 0
    end = len(arr) - 1
    
    while start <= end:
        mid = (start + end) // 2
        
        if arr[mid] <= target:
            start = mid + 1
        else:
            end = mid - 1
    
    return arr[start % len(arr)]

#Alternative implementation
def findSmallestLetter(arr,target):
    
    start = 0
    end = len(arr) - 1
    ans = 0
    while start <= end:
        mid = (start + end) // 2
        
        if arr[mid] <= target:
            start = mid + 1
        else:
            ans = mid
            end = mid - 1
    
    return arr[ans]

print(findSmallestLetter(['a','c','f'],'c'))