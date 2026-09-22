from collections import defaultdict


class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        graph = defaultdict(list)

        for edge in edges:
            node_a, node_b = edge
            graph[node_a].append(node_b)
            graph[node_b].append(node_a)

        visited = set()
        visited.add(source)
        
        def dfs(node):

            if destination == node:
                return True
            
            for i in graph[node]:
                if i not in visited:
                    visited.add(i)
                    if dfs(i):
                        return True
                
            return False


        return dfs(source)

#BFS approach


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)

        for edge in edges:
            node_a, node_b = edge
            graph[node_a].append(node_b)
            graph[node_b].append(node_a)

        queue = deque([source])
        visited = {source}

        while queue:
            current = queue.popleft()
            if current == destination:
                return True

            for neighbor in graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return False    