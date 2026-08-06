# I use a post-order DFS because a node can only determine 
# whether it is balanced after knowing the heights of its left and right subtrees. 
# At each node, I compare the height difference using abs(left - right). 
# If the difference exceeds 1, I mark the tree as unbalanced. 
# Finally, I return 1 + max(left, right) so the parent can compute its own height.

def isBalanced(root):
    is_balanced = True

    def dfs(node):
        nonlocal is_balanced

        if not node:
            return 0

        left = dfs(node.left)
        right = dfs(node.right)

        if abs(left - right) > 1:
            is_balanced = False

        return 1 + max(left, right)

    dfs(root)

    return is_balanced