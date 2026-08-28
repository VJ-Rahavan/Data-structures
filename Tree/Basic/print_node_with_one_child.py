# I recursively traverse the entire binary tree and check each node’s children.
# I use a logic to identify whether exactly one child is missing, which means the node has exactly one child.
# If such a node is found, I print its value and continue traversing both subtrees.
# Finally, if no node was found, I print -1.

def findChildWithOne(root):

    def check(node):
        if not node:
            return False

        found = False

        if (node.left is None) != (node.right is None):
            print(node.val)
            found = True

        left_found = check(node.left)
        right_found = check(node.right)

        return found or left_found or right_found

    if not check(root):
        print(-1)