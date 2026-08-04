# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# We recursively visit each node in the tree. 
# At every node, we swap its left and right children, 
# then recursively invert the left and right subtrees. 
# The base case is when the current node is None, where recursion stops. 
# Since every node is processed once, the time complexity is O(n).
from collections import deque

#BFS Approach
class Solution:
    def invertTree(self, root):
        if not root:
            return None

        q = deque([root])

        while q:
            node = q.popleft()

            node.left, node.right = node.right, node.left

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return root

#DFS Approach
class Solution:
    def invertTree(self, root):
        if not root:
            return

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root