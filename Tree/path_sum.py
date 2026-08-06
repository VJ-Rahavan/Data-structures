# I use a DFS traversal while maintaining the running sum from the root to the current node. 
# At each node, I add its value to the current sum, and if I reach a leaf node, 
# I compare the accumulated sum with the target. 
# If a valid path is found, I set a shared flag and use an early exit to stop exploring the remaining branches. 
# This visits each node at most once, giving O(n) time complexity and O(h) recursion stack space, where h is the height of the tree.

#My approach using nonlocal variable to track if a valid path has been found.
def path_sum(root, targetSum):
    isMatched = False

    def dfs(current_sum, node):
        nonlocal isMatched

        # Early exit if a valid path is already found
        if isMatched:
            return

        if not node:
            return

        current_sum += node.val

        if (
            current_sum == targetSum
            and not node.left
            and not node.right
        ):
            isMatched = True
            return

        dfs(current_sum, node.left)
        dfs(current_sum, node.right)

    dfs(0, root)

    return isMatched


# I perform a DFS while carrying the running sum from the root to the current node. 
# At each node, I add its value to the current sum. 
# If I reach a leaf node, I compare the accumulated sum with the target and return the result. 
# Otherwise, I recursively check both subtrees and return True 
# if either subtree contains a valid root-to-leaf path. 
# This approach avoids shared state and naturally stops searching once a valid path is found.

#Better Approach
def hasPathSum(root, targetSum):
    def dfs(node, current_sum):
        if not node:
            return False

        current_sum += node.val

        # If it's a leaf, check whether we've reached the target sum
        if not node.left and not node.right:
            return current_sum == targetSum

        return (
            dfs(node.left, current_sum) or
            dfs(node.right, current_sum)
        )

    return dfs(root, 0)