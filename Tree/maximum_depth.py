class Solution:
    def check(self, root):
        # Base case
        if not root:
            return 0

        # Find depth of left and right subtrees
        left = self.check(root.left)
        right = self.check(root.right)

        # Current node's depth
        return 1 + max(left, right)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.check(root)