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