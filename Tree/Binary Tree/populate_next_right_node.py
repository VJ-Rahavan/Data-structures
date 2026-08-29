"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

# BFS approach using a queue to traverse the tree level by level. 
# For each level, I connect the nodes from left to right by setting the `next` pointer of each node to the next node in the queue. 
# The last node in each level points to `None`.
from collections import deque

class Solution:
    def connect(self, root):
        if not root:
            return root

        queue = deque([root])

        while queue:
            size = len(queue)

            for i in range(size):
                node = queue.popleft()

                if i < size - 1:
                    node.next = queue[0]

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return root

#Optimal Approach

# Since the tree is perfect, every parent has exactly two children, so I can connect nodes without using a queue.
# For each parent, I connect its left child to its right child.
# If the parent has a next node, I connect its right child to the next parent's left child.
# I traverse each level using the already-established `next` pointers.
# This gives **O(n) time and O(1) extra space**.

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root

        level = root

        while level.left:
            curr = level

            while curr:
                # Same parent
                curr.left.next = curr.right

                # Different parents
                if curr.next:
                    curr.right.next = curr.next.left

                curr = curr.next

            level = level.left

        return root