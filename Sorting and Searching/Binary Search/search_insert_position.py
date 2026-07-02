#If the target isn't found, start ends at the correct insertion index 
# because it points to the first element greater than or equal to the target.

def search_insert_position(arr,target):
    start = 0
    end = len(arr) - 1
    mid = -1
    
    while(start <= end):
        mid = (start+end)//2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid -1
    
    return start
   

print(search_insert_position([1,2,5,7],4))