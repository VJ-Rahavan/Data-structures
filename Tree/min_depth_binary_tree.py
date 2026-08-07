# I perform a depth-first search while keeping track of the current depth. 
# Whenever I reach a leaf node (a node with no left or right child), 
# I compare its depth with the minimum depth found so far and update the answer if needed. 
# I continue exploring both subtrees recursively until all root-to-leaf paths have been checked. 
# Finally, I return the smallest depth recorded.

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        res = float("inf")

        def dfs(node, depth):
            nonlocal res

            if not node:
                return

            if not node.left and not node.right:
                res = min(res, depth)
                return

            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 1)
        return res