# I preprocess nums2 using a monotonic decreasing stack.
# I traverse from right to left because I need information about elements to the right. 
# For each element, I remove all smaller elements from the stack 
# since they can never be the next greater element for the current element or any element further left.
# After popping, if the stack is not empty, its top is the next greater element; 
# otherwise, the answer is -1. I store this in a hash map. 
# Finally, I iterate through nums1 and look up each answer from the hash map."

class Solution:
    def nextGreaterElement(self, nums: List[int], arr: List[int]) -> List[int]:
        stack = []
        hash_map = {}
        res = []
        for value in reversed(arr):
            while stack and stack[-1] < value:
                stack.pop()
            
            if stack and stack[-1] > value:
                hash_map[value] = stack[-1]
            else:
                hash_map[value] = -1
            
            stack.append(value)
        
        for i in nums:
            res.append(hash_map[i])

        return res