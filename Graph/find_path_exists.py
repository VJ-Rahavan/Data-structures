class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        graph = {}
        for i in range(n):
            graph[i] = []

        for edge in edges:
            node_a, node_b = edge
            graph[node_a].append(node_b)
            graph[node_b].append(node_a)

        visited = set()
        
        def dfs(node):

            visited.add(node)
            if destination == node:
                return True
            
            for i in graph[node]:
                if i not in visited:
                    if dfs(i):
                        return True
                
            return False


        return dfs(source)
