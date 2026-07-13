# I use a sliding window of size k backed by a hash set. 
# The set stores the last k elements. # As I iterate through the array,
#  I remove the element that falls out of the window.
#  Then I check if the current value is already in the set. 
# If it is, I've found a duplicate within distance k; 
# otherwise, I add the current value and continue.

def contains_duplicate(arr,k):
    seen = set()
    
    for i, value in enumerate(arr):
        if i > k:
            seen.remove(arr[i - k - 1])
        
        if value in seen:
            return True
        
        seen.add(value)
    
    return False


print(contains_duplicate([1,2,3,1],3))