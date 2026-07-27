# I use a monotonic decreasing deque that stores indices, not values. 
# Before processing each element, I remove indices that are outside the current window. 
# Then, I remove all smaller elements from the back because they can never become the maximum while the current larger element is in the window. 
# After adding the current index, the front of the deque always holds the index of the maximum element for the current window. 
# Since every index is added and removed at most once, the overall time complexity is O(n) and the space complexity is O(k).

from collections import deque

def max_sliding_window(arr,k):
    q = deque()
    res = []
    
    for i in range(len(arr)):
        # print(q)
        while q and q[0] <= i - k:
            q.popleft()
            
        while q and arr[q[-1]] < arr[i]:
            q.pop()
        
        
        q.append(i)
        
        if i >= k - 1:
            res.append(arr[q[0]])
        
        
    print(res)

max_sliding_window([1,3,-1,-3,5,3,6,7],3)