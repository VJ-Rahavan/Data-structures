#Brute Force

def find_max(arr,k):
    n = len(arr)
    res = []
    cur = []
    
    for i in range(n):
        
        cur.append(arr[i])
        if i >= k - 1:
            d = max(cur)
            res.append(d)
            cur.pop(0)
    
    print(res)

find_max( [9,1, 2, 3, 1, 4, 5, 2, 3, 6],3)

# Optimal solution using deque
from collections import deque

def find_max(arr,k):
    n = len(arr)
    res = []
    dq = deque()
    
    for i in range(n):
        
        if dq and dq[0] <= i - k:
            dq.popleft()
        
        while dq and arr[dq[-1]] < arr[i]:
            dq.pop()
        
        dq.append(i)
        
        
        if i >= k - 1:
            res.append(arr[dq[0]])
        
        
    print(res,dq)

#JS Approach
# function findMax(arr, k) {
#     const res = [];
#     const dq = []; // stores indices
#     let front = 0;

#     for (let i = 0; i < arr.length; i++) {

#         // 1. Remove expired indices from the front
#         while (front < dq.length && dq[front] <= i - k) {
#             front++;
#         }

#         // 2. Remove smaller values from the back
#         while (
#             front < dq.length &&
#             arr[dq[dq.length - 1]] <= arr[i]
#         ) {
#             dq.pop();
#         }

#         // 3. Add current index
#         dq.push(i);

#         // 4. Store maximum after first window is complete
#         if (i >= k - 1) {
#             res.push(arr[dq[front]]);
#         }
#     }

#     return res;
# }

# console.log(
#     findMax([1, 2, 3, 1, 4, 5, 2, 3, 6], 3)
# );
                