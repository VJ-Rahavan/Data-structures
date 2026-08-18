def bfs(graph, start):
    queue = deque([start])
    visited = {start}

    while queue:
        node = queue.popleft()
        print(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

#Alternative BFS Implementation:

def bfs():
    queue = deque()
    visited = set()
    queue.append(0)

    while queue:
        node = queue.popleft()

        if node in visited:
            continue

        visited.add(node)
        print(node)

        for i in graph[node]:
            if i not in visited:
                queue.append(i)