def has_cycle(graph):
    visited = set()

    def dfs(node, parent):
        visited.add(node)

        for neighbor in graph[node]:

            if neighbor == parent:
                continue

            if neighbor in visited:
                return True

            if dfs(neighbor, node):
                return True

        return False

    for node in graph:
        if node not in visited:
            if dfs(node, -1):
                return True

    return False

from collections import deque

def has_cycle(graph):
    visited = set()

    for start in graph:
        if start in visited:
            continue

        queue = deque([(start, -1)])
        visited.add(start)

        while queue:
            node, parent = queue.popleft()

            for neighbor in graph[node]:

                if neighbor == parent:
                    continue

                if neighbor in visited:
                    return True

                visited.add(neighbor)
                queue.append((neighbor, node))

    return False