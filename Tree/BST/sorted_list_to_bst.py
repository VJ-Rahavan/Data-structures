
# I use the slow and fast pointer technique to find the middle node, 
# which becomes the root of the BST. 
# I keep a prev pointer so I can disconnect the left half from the middle node. 
# Then I recursively build the left subtree from the left half 
# and the right subtree from the nodes after the middle. 
# The base cases handle an empty list and a single-node list.

from typing import Optional
from Tree.symmetric_tree import TreeNode


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:

        if not head:
            return None

        if not head.next:
            return TreeNode(head.val)

        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # Disconnect left half from middle
        prev.next = None

        root = TreeNode(slow.val)

        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)

        return root