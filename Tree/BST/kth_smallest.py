def kthSmallest(root, k):
    count = 0

    def inorder(node):
        nonlocal count

        # 1. If there is no node, stop this path
        if node is None:
            return None

        # 2. Go LEFT first
        result = inorder(node.left)

        # 3. If the answer was already found on the left,
        #    pass it upward and stop
        if result is not None:
            return result

        # 4. Process CURRENT node
        count += 1

        if count == k:
            return node.val

        # 5. Go RIGHT
        return inorder(node.right)

    return inorder(root)