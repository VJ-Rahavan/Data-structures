class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        
        visited = set()

        def dfs(node):
            visited.add(node)

            for i in rooms[node]:
                if i not in visited:
                    dfs(i)

        dfs(0)

        return len(visited) == n
