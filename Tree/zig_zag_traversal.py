from collections import deque
from typing import List, Optional

# We perform a level-order traversal (BFS) using a queue so that we process one level of the tree at a time. 
# For each level, we collect the node values in a temporary list. 
# On odd levels, we append the values as they are. 
# On even levels, we reverse the temporary list before adding it to the result, producing the required zigzag order. 
# After processing a level, we enqueue its left and right children for the next iteration. 
# This visits every node exactly once, resulting in O(n) time and O(n) space complexity.

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque([root])
        res = []
        left_to_right = True

        while queue:
            level = deque()

            for _ in range(len(queue)):
                node = queue.popleft()

                if left_to_right:
                    level.append(node.val)
                else:
                    level.appendleft(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(list(level))
            left_to_right = not left_to_right

        return res