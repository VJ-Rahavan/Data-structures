# I perform a DFS while maintaining the current path and the running sum. 
# At each node, I add its value to both. 
# If I reach a leaf and the sum equals the target, 
# I append a copy of the current path to the result. 
# After exploring the left and right subtrees, 
# I remove the current node from the path to restore the state before returning. 
# This is the backtracking step.


def path_sum_II(root, targetSum):
    result = []
    path = []

    def dfs(node, current_sum):
        if not node:
            return

        path.append(node.val)
        current_sum += node.val

        if not node.left and not node.right:
            if current_sum == targetSum:
                result.append(path[:])
        else:
            dfs(node.left, current_sum)
            dfs(node.right, current_sum)

        path.pop()

    dfs(root, 0)
    return result