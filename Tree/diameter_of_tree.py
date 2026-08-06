# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# We solve this using a postorder DFS 
# Because the height of a node depends on the heights of its left and right subtrees. 
# The recursive function returns the height of the current subtree. 
# At each node, the longest path passing through it is left_height + right_height, 
# so we update a global diameter with the maximum value seen. 
# Finally, we return 1 + max(left_height, right_height) so the parent can compute its own height.

class Solution:
    def diameterOfBinaryTree(self, root):
        diameter = 0

        def dfs(node):
            nonlocal diameter

            if not node:
                return 0

            left_height = dfs(node.left)
            right_height = dfs(node.right)

            # Diameter passing through the current node
            diameter = max(diameter, left_height + right_height)

            # Return height of current subtree
            return 1 + max(left_height, right_height)

        dfs(root)
        return diameter