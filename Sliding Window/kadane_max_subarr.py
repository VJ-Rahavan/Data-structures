# I maintain two variables:
#  cur stores the maximum subarray sum ending at the current index, 
# and res stores the overall maximum seen so far. 
# At each element, I decide whether it's better to extend the previous subarray or 
# start a new subarray from the current element. 
# Then I update the global maximum.

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6

def max_subarr(arr):
    if not arr:
        return False
    
    res = arr[0]
    cur = res
    start = 0
    
    for i in range(1,len(arr)):
        cur = max(cur+arr[i], arr[i])
        res = max(cur,res)
    
    print(res)

max_subarr([-2,1,-3,4,-1,2,1,-5,4])