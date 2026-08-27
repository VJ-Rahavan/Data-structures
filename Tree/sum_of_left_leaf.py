# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#global variable approach
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        cur = 0
        def find(node,is_left):
            nonlocal cur
            if not node:
                return 0

            if is_left and not node.left and not node.right:
                cur = cur + node.val

            left = find(node.left,True)
            right = find(node.right,False)

        find(root,False)
        

        return cur
    
#recursive approach returning value
def f(root, isLeft=False):
    if not root: return 0
    if not root.left and not root.right and isLeft: return root.val
    return f(root.left, True)+f(root.right, False)