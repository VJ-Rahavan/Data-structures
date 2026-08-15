### Interview Explanation — Lowest Common Ancestor of BST

# > “Since this is a Binary Search Tree, I can use its ordering property. 
# If both `p` and `q` are smaller than the current node, their LCA must be in the left subtree. 
# If both are greater, it must be in the right subtree. 
# Otherwise, the current node is where their paths split, so it is the lowest common ancestor. 
# I use an iterative approach to move down the tree.”

# **Complexity:** `O(h)` time and `O(1)` space, where `h` is the height of the tree.


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        curr = root

        while curr:
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left

            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right

            else:
                return curr
            