# 2265. Count Nodes Equal to Average of Subtree

# I use a **postorder DFS** because the subtree sum and count depend on the left and right subtrees.
# For each node, I get the `(sum, count)` from both children and calculate the current subtree's total sum and count.
# Then I check whether `node.val == total_sum // total_count` and increment the global counter if it matches.
# Finally, I return the current subtree's `(sum, count)` to the parent node.
# The time complexity is **O(n)** and the space complexity is **O(h)** for the recursion stack.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        res = 0
        def dfs(node):
            nonlocal res
            if not node:
                return 0,0
            
            left_sum,left_count = dfs(node.left)
            right_sum,right_count = dfs(node.right)

            tot_sum = left_sum + node.val + right_sum
            count = left_count + 1 + right_count

            if tot_sum//count == node.val:
                res += 1
            
            return tot_sum,count

        dfs(root)
        return res
        