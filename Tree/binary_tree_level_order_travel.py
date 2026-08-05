from collections import deque
from typing import List, Optional 

# My approach is to use a queue to do a level order traversal of the binary tree. 
# I will keep track of the level of each node and store the values of the nodes at each level in a dictionary. 
# Finally, I will return the values as a list of lists.

class Solution:
    def levelOrder(self, root: Optional[TreeNode]):
        
        if not root:
            return []
            
        queue = deque()
        h = {}
        
        queue.append((1,root))
        
        while queue:
            level,node = queue.popleft()
            
            if level in h:
               h[level].append(node.val)
            else:
                h[level] = [node.val]
            
            if node.left:
                queue.append((level+1,node.left))
    
            if node.right:
                queue.append((level+1,node.right))
        
        return list(h.values())

#optimal Solution
# I'm using Breadth-First Search (BFS) with a queue. 
# At the start of each iteration, len(queue) gives the number of nodes in the current level. 
# I process exactly those nodes, collect their values into a level list, 
# and enqueue their children for the next level. 
# After finishing the current level, I append level to the final answer.
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        if not root:
            return res
        
        q = collections.deque()
        q.append(root)
    
        while q:
            same_level = []

            for _ in range(len(q)):
                node = q.popleft()
                same_level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            res.append(same_level)
        
        return res