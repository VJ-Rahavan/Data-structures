from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#optimal Approach
class Solution:
    def leftHeight(self, node):
        height = 0
        while node:
            height += 1
            node = node.left
        return height

    def rightHeight(self, node):
        height = 0
        while node:
            height += 1
            node = node.right
        return height

    def countNodes(self, root):
        if not root:
            return 0

        left = self.leftHeight(root)
        right = self.rightHeight(root)

        # Perfect binary tree
        if left == right:
            return (1 << left) - 1

        # Otherwise recurse
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

#Brute Force Approach - DFS
class Solution:    
    def countNodes(self,node):
        if node is None:
            return 0

        left = self.countNodes(node.left)
        right = self.countNodes(node.right)
        

        return left + right + 1

#Brute Force Approach - BFS
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        queue.append(root)
        c = 1
        while queue:
            d = queue.popleft()
            
            if d.left:
                queue.append(d.left)
                c +=1
            
            if d.right:
                queue.append(d.right)
                c+=1
        print(c)