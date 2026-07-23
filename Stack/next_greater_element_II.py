# I use a monotonic decreasing stack and traverse the array twice in reverse to simulate its circular nature. 
# Instead of duplicating the array, I use idx = i % n to wrap around to the beginning. 
# Before processing each element, I remove all smaller or equal elements from the stack, 
# so the top always represents the next greater element. 
# Each element is pushed and popped at most once, resulting in O(n) time and O(n) space complexity.

def next_larger_element_II(arr): 
    
    stack = []
    n = len(arr)
    
    res = [-1] * n
    for i in range(-1, -2 * n, -1):
        idx = i % n
        while stack and stack[-1] <= arr[idx]:
            stack.pop()
        
        if stack:
            res[idx] = stack[-1]
        
        if i >= -n:
            stack.append(arr[idx])
    
    print(res)

next_larger_element_II([1,2,3,4,3])

# Input: nums = [1,2,3,4,3]
# Output: [2,3,4,-1,4]