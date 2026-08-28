# Count Nodes With Exactly One Child

# I use recursion to traverse the entire binary tree.
# If a node has exactly one child, I add 1 to the count and continue through that child.
# If it has zero or two children, it contributes 0, so I recursively check both subtrees.
# Finally, I add the results from the subtrees to get the total count.

# 0 children → traverse both (both return 0)
# 1 child    → count 1 + traverse existing child
# 2 children → traverse both subtrees

def findChildWithOne(root):

    def check(node):
        if not node:
            return 0

        if not node.left and node.right:
            return 1 + check(node.right)

        if not node.right and node.left:
            return 1 + check(node.left)

        return check(node.left) + check(node.right)

    return check(root)