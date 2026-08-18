from collections import deque


def count_components(graph):
    visited = set()
    components = 0

    # Check every node
    for node in range(n):

        # Found a new component
        if node not in visited:
            components += 1

            queue = deque([node])
            visited.add(node)

            # BFS
            while queue:
                current = queue.popleft()

                for neighbor in graph[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

    return components


def dfs(graph, node, visited):
    visited.add(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


def count_components(graph):
    visited = set()
    components = 0

    for node in range(n):
        if node not in visited:
            components += 1
            dfs(graph, node, visited)

    return components

n = 7

edges = [
    [0, 1],
    [0, 2],
    [3, 4],
    [3, 6]
]


def convertToGraph(edges):
    graph = {}

    # Create every node, including isolated nodes
    for i in range(n):
        graph[i] = []

    # Add edges in both directions
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    return graph


graph_list = convertToGraph(edges)

print(graph_list)
print(count_components(graph_list))