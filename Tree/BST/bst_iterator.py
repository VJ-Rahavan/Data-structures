# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


### Interview Explanation

# * I use a **stack to simulate inorder traversal** of the BST, because inorder traversal gives values in sorted order.
# * During initialization, I push the **entire left path** from the root into the stack.
# * In `next()`, I pop the smallest node, then move to its right subtree and push that subtree's **left path**.
# * `hasNext()` simply checks whether the stack is non-empty.
# * This gives **O(h) space**, where `h` is the tree height, and `next()` takes **O(h) worst-case** but **O(1) amortized** time.

from typing import Optional

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        cur = root
        while cur:
            self.stack.append(cur)
            cur = cur.left

    def next(self) -> int:
        node = self.stack.pop()

        # Go to the right subtree,
        # then keep going left.
        cur = node.right

        while cur:
            self.stack.append(cur)
            cur = cur.left

        return node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()