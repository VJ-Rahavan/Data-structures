from collections import deque

#BFS
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_deque = deque([p])
        q_deque = deque([q])

        while p_deque and q_deque:
            p_value = p_deque.popleft()
            q_value = q_deque.popleft()

            if not p_value and not q_value:
                continue

            if not p_value or not q_value:
                return False

            if p_value.val != q_value.val:
                return False

            p_deque.append(p_value.left)
            p_deque.append(p_value.right)

            q_deque.append(q_value.left)
            q_deque.append(q_value.right)

        return not p_deque and not q_deque


#DFS
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and \
               self.isSameTree(p.right, q.right)