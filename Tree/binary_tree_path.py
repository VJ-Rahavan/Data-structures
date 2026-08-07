# I perform a DFS while maintaining the current root-to-node path in a list. 
# At each node, I append its value to the path. 
# When I reach a leaf, I join the path using "->" and add it to the result. 
# After exploring both children, I remove the current node from the path to restore the state before returning (backtracking).

#My Approach
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        path = []
        res = []

        def dfs(node):
            if not node:
                return

            path.append(str(node.val))

            if not node.left and not node.right:
                res.append("->".join(path))
            else:
                dfs(node.left)
                dfs(node.right)

            path.pop()

        dfs(root)
        return res
    


#Better Approach
from typing import List,Optional


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []

        def dfs(node, path):
            if not node:
                return

            if path:
                path += "->"
            path += str(node.val)

            if not node.left and not node.right:
                res.append(path)
                return

            dfs(node.left, path)
            dfs(node.right, path)

        dfs(root, "")
        return res