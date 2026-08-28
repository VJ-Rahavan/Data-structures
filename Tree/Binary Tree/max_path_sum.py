# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# I use postorder DFS to calculate the maximum path from each node's children first.
# At each node, I calculate `left + node + right` as a candidate path and update the global maximum.
# For the parent, I return only `node + max(left, right)` because a path can continue through only one child.
# I use `max(0, child)` to ignore negative contributions, 
# while initializing the global maximum to `-inf` to handle all-negative trees.


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxx = float("-inf")

        def dfs(node):
            nonlocal maxx
            if not node:
                return 0

            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            summ = left + right + node.val
            maxx = max(maxx, summ)

            return node.val + max(left, right)

        dfs(
            root,
        )
        return maxx
