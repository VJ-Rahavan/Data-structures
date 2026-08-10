# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
from typing import List, Optional

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = deque()
        res = []
        queue.append(root)

        while queue:
            cur_len = len(queue)
            for i in range(cur_len):
                cur_val = queue.popleft()
                if i == cur_len - 1:
                    res.append(cur_val.val)

                if cur_val.left:
                        queue.append(cur_val.left)
                if cur_val.right:
                    queue.append(cur_val.right)
        
        return res