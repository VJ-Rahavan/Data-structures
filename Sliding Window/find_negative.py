
def find_negative(arr,k):
    
    res = []
    cur = []
    
    n = len(arr)
    
    for i in range(len(arr)):
        
        cur.append(arr[i])
        if len(cur) == k:
            start = 0
            while start < len(cur):
                if cur[start] < 0:
                    res.append(cur[start])
                    break
                start+=1
            
            if start == len(cur):
                res.append(0)
                
            cur.pop(0)
        
    print(res,cur)

find_negative([-8, 2,4, 3, -6, 10],3)


#Optimal solution using deque

from collections import deque

def find_negative(arr,k):
    
    res = []
    dq = deque()
    
    for i in range(len(arr)):
        
        if dq and dq[0] <= i - k:
            dq.popleft()
            
        if arr[i] < 0:
            dq.append(i)
        
        
        if i >= k - 1:
            if dq:
                res.append(arr[dq[0]])
            else:
                res.append(0)
    print(res)

find_negative([-8, 2,4, 3, -6, 10],3)