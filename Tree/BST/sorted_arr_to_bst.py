# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Find the middle element and make it the root.
# Recursively use the left half to build the left subtree.
# Recursively use the right half to build the right subtree.
# This guarantees the BST is height-balanced.

from typing import List, Optional
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
            
        middle = len(nums)//2

        root = TreeNode(nums[middle])

        root.left = self.sortedArrayToBST(nums[:middle])
        root.right = self.sortedArrayToBST(nums[middle+1:])

        return root
        