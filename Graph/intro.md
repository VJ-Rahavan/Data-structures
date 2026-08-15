# Graph DSA Notes

## 1. What is a Graph?

A **graph** is a data structure used to represent relationships between objects.

- **Vertex / Node** → object
- **Edge** → connection between two nodes

Example:

```text
    1
   / \
  2---3
   \
    4
```

Vertices = `{1, 2, 3, 4}`
Edges = `{1-2, 1-3, 2-3, 2-4}`

---

# 2. Types of Graphs

### Undirected Graph

Edges have no direction.

```text
1 ---- 2
```

If `1 → 2`, then `2 → 1` is also possible.

### Directed Graph

Edges have direction.

```text
1 ----> 2
```

`1 → 2` does **not** mean `2 → 1`.

### Weighted Graph

Edges have a cost/weight.

```text
1 --5-- 2
```

The cost of going from `1` to `2` is `5`.

### Unweighted Graph

All edges are considered equal.

### Cyclic Graph

Contains at least one cycle.

```text
1
| \
|  \
2---3
```

### Acyclic Graph

Contains no cycles.

A **DAG** = Directed Acyclic Graph.

---

# 3. Important Graph Terminology

| Term      | Meaning                                |
| --------- | -------------------------------------- |
| Vertex    | Node                                   |
| Edge      | Connection                             |
| Degree    | Number of edges connected to a node    |
| Indegree  | Incoming edges                         |
| Outdegree | Outgoing edges                         |
| Path      | Sequence of connected vertices         |
| Cycle     | Path that returns to starting node     |
| Connected | Every node can be reached from another |
| Component | Connected group of nodes               |
| Neighbor  | Directly connected node                |

For a directed graph:

```text
1 → 2 → 3
    ↑
    |
    4
```

For node `2`:

- Indegree = 2 (`1`, `4`)
- Outdegree = 1 (`3`)

---

# 4. Graph Representation

## Adjacency Matrix

For:

```text
1 --- 2
|
3
```

We can represent it as:

```text
    1 2 3
1   0 1 1
2   1 0 0
3   1 0 0
```

Good when the graph has **many edges**.

---

## Adjacency List ⭐

Most commonly used in DSA interviews.

```python
graph = {
    1: [2, 3],
    2: [1],
    3: [1]
}
```

For a weighted graph:

```python
graph = {
    1: [(2, 5), (3, 10)],
    2: [(1, 5)],
    3: [(1, 10)]
}
```

**Interview default:** Think **adjacency list** first.

---

# 5. Building an Undirected Graph

```python
graph = [[] for _ in range(n)]

for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)
```

Why both?

Because:

```text
u ---- v
```

means we can travel:

```text
u → v
v → u
```

For a directed graph:

```python
graph[u].append(v)
```

Only one direction.

---

# 6. BFS — Breadth First Search ⭐⭐⭐

BFS explores the graph **level by level**.

```text
       1
      / \
     2   3
    / \
   4   5
```

BFS from `1`:

```text
1 → 2 → 3 → 4 → 5
```

Use a **queue**.

```python
from collections import deque

queue = deque([start])
visited = {start}

while queue:
    node = queue.popleft()

    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)
```

### BFS is especially useful for:

- Shortest path in **unweighted graphs**
- Level-order exploration
- Minimum number of steps
- Connected components
- Grid problems
- Bipartite checking

---

# 7. DFS — Depth First Search ⭐⭐⭐

DFS goes as deep as possible before backtracking.

```text
       1
      / \
     2   3
    / \
   4   5
```

Possible DFS:

```text
1 → 2 → 4 → 5 → 3
```

### Recursive DFS

```python
def dfs(node):
    visited.add(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor)
```

### Iterative DFS

Use a stack:

```python
stack = [start]
visited = {start}

while stack:
    node = stack.pop()

    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            stack.append(neighbor)
```

### DFS is especially useful for:

- Cycle detection
- Connected components
- Path existence
- Topological sorting
- Backtracking
- Number of islands
- Graph traversal

---

# 8. BFS vs DFS

| BFS                               | DFS                  |
| --------------------------------- | -------------------- |
| Queue                             | Stack / recursion    |
| Level by level                    | Goes deep            |
| Shortest path in unweighted graph | Cycle detection      |
| Minimum steps                     | Components           |
| Often iterative                   | Often recursive      |
| Good for distance                 | Good for exploration |

### Interview rule

If the question says:

> "minimum number of edges/steps"

Think **BFS**.

If it says:

> "explore all possibilities / detect cycle / components"

Think **DFS**.

---

# 9. Visited Array ⭐

The most important graph concept.

Without `visited`, you can repeatedly traverse the same nodes.

Example:

```text
1 ---- 2
 \    /
   3
```

You could keep doing:

```text
1 → 2 → 3 → 1 → 2 → 3 ...
```

So:

```python
visited = set()
```

Then:

```python
if neighbor not in visited:
    visited.add(neighbor)
```

---

# 10. Disconnected Graphs

Consider:

```text
1 --- 2       3 --- 4
```

Starting DFS from `1` only visits:

```text
1, 2
```

To visit the **entire graph**:

```python
for node in range(n):
    if node not in visited:
        dfs(node)
```

This pattern is extremely important.

It is used for:

- Number of connected components
- Number of provinces
- Number of islands
- Graph traversal

---

# 11. Connected Components ⭐

Example:

```text
1 --- 2       3 --- 4       5
```

There are **3 connected components**.

Pattern:

```python
components = 0

for node in range(n):
    if node not in visited:
        components += 1
        dfs(node)
```

Every new DFS/BFS represents one component.

---

# 12. Cycle Detection — Undirected Graph

Important idea:

When traversing from `node` to `neighbor`, if the neighbor is already visited **and it isn't the parent**, a cycle exists.

```python
def dfs(node, parent):
    visited.add(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            if dfs(neighbor, node):
                return True

        elif neighbor != parent:
            return True

    return False
```

Example:

```text
1 --- 2
 \   /
   3
```

`1 → 2 → 3 → 1`

Cycle exists.

---

# 13. Cycle Detection — Directed Graph ⭐

For directed graphs, use **two states**.

```text
0 = unvisited
1 = currently visiting
2 = completely processed
```

If we encounter a node with state `1`, we've found a cycle.

```python
def dfs(node):
    state[node] = 1

    for neighbor in graph[node]:
        if state[neighbor] == 1:
            return True

        if state[neighbor] == 0:
            if dfs(neighbor):
                return True

    state[node] = 2
    return False
```

This concept is important for:

- Course Schedule
- Dependency graphs
- Build systems
- Package dependencies

---

# 14. Topological Sort ⭐⭐⭐

Used for a **Directed Acyclic Graph (DAG)**.

Example:

```text
A → B → D
A → C → D
```

Possible ordering:

```text
A → B → C → D
```

Meaning:

> A must happen before B/C, and B/C before D.

Common applications:

- Course prerequisites
- Build dependencies
- Task scheduling
- Package installation

---

# 15. Topological Sort — Kahn's Algorithm

Uses **BFS + indegree**.

```python
from collections import deque

queue = deque()

for node in range(n):
    if indegree[node] == 0:
        queue.append(node)

order = []

while queue:
    node = queue.popleft()
    order.append(node)

    for neighbor in graph[node]:
        indegree[neighbor] -= 1

        if indegree[neighbor] == 0:
            queue.append(neighbor)
```

### Important

If:

```python
len(order) != n
```

then the graph contains a cycle.

---

# 16. Shortest Path

### Unweighted Graph

Use **BFS**.

```text
1 --- 2 --- 4
 \         /
  ---- 3 --
```

BFS finds the minimum number of edges.

### Weighted Graph

Choice depends on weights:

| Situation               | Algorithm                     |
| ----------------------- | ----------------------------- |
| Unweighted              | BFS                           |
| Positive weights        | Dijkstra                      |
| Negative weights        | Bellman-Ford                  |
| All-pairs shortest path | Floyd-Warshall                |
| DAG shortest path       | Topological sort + relaxation |

---

# 17. Dijkstra's Algorithm ⭐⭐⭐

Used for shortest path when edge weights are **non-negative**.

Example:

```text
A --4-- B
|       |
2       1
|       |
C --3-- D
```

Core idea:

> Always process the currently known closest node.

Uses a **min heap / priority queue**.

Python:

```python
import heapq

dist = [float("inf")] * n
dist[start] = 0

heap = [(0, start)]

while heap:
    current_dist, node = heapq.heappop(heap)

    if current_dist > dist[node]:
        continue

    for neighbor, weight in graph[node]:
        new_dist = current_dist + weight

        if new_dist < dist[neighbor]:
            dist[neighbor] = new_dist
            heapq.heappush(heap, (new_dist, neighbor))
```

### Critical interview point

**Dijkstra does NOT work correctly with negative edge weights.**

---

# 18. Bellman-Ford

Handles **negative edge weights**.

It repeatedly relaxes all edges.

Useful when:

```text
edge weight < 0
```

It can also detect a **negative cycle**.

You don't need to prioritize this before BFS/DFS/Dijkstra for most interview preparation.

---

# 19. Minimum Spanning Tree

A **Minimum Spanning Tree (MST)** connects all vertices with:

- No cycles
- Minimum total edge weight

Two major algorithms:

### Kruskal's Algorithm

Uses:

- Sort edges by weight
- Union-Find / DSU

### Prim's Algorithm

Uses:

- Priority queue
- Greedy expansion

---

# 20. Union-Find / DSU ⭐⭐

Useful for efficiently managing connected components.

Operations:

```text
find(x)
union(x, y)
```

Typical applications:

- Cycle detection
- Kruskal's MST
- Number of connected components
- Dynamic connectivity

Key optimization:

```text
Path Compression
+
Union by Rank/Size
```

---

# 21. Bipartite Graph ⭐⭐

A graph is bipartite if we can divide nodes into **two groups** such that no edge connects nodes within the same group.

Example:

```text
1 ---- 2
|      |
4 ---- 3
```

Can color:

```text
Group A: 1, 3
Group B: 2, 4
```

Use BFS/DFS coloring:

```python
color = [-1] * n

for start in range(n):
    if color[start] != -1:
        continue

    color[start] = 0
    queue = deque([start])

    while queue:
        node = queue.popleft()

        for neighbor in graph[node]:
            if color[neighbor] == -1:
                color[neighbor] = 1 - color[node]
                queue.append(neighbor)

            elif color[neighbor] == color[node]:
                return False
```

### Key observation

A graph containing an **odd-length cycle** is not bipartite.

---

# 22. Grid Problems Are Graph Problems

This is extremely important for interviews.

Example:

```text
1 1 0
0 1 0
1 0 1
```

Each cell can be treated as a node.

Neighbors:

```text
↑
↓
←
→
```

Sometimes diagonals too.

Typical problems:

- Number of Islands
- Flood Fill
- Rotten Oranges
- Surrounded Regions
- Pacific Atlantic Water Flow
- Shortest Path in Grid

---

# 23. Number of Islands Pattern ⭐⭐⭐

Think:

> Every unvisited land cell starts a new DFS/BFS.

```python
for r in range(rows):
    for c in range(cols):

        if grid[r][c] == "1":
            islands += 1
            dfs(r, c)
```

DFS explores the entire island.

---

# 24. Graph Problem Recognition

When you see:

### "Can I reach X from Y?"

→ DFS / BFS

### "Minimum number of steps?"

→ BFS

### "How many groups/components?"

→ DFS / BFS / DSU

### "Does a cycle exist?"

→ DFS / DSU depending on graph type

### "Prerequisites/dependencies?"

→ Topological Sort

### "Shortest path with positive weights?"

→ Dijkstra

### "Negative weights?"

→ Bellman-Ford

### "Connect everything with minimum cost?"

→ MST

### "Can split into two groups?"

→ Bipartite checking

### "Grid with connected cells?"

→ DFS / BFS

---

# 25. Graph Interview Roadmap

For your DSA preparation, I would learn them in this order:

```text
1. Graph representation
       ↓
2. BFS
       ↓
3. DFS
       ↓
4. Connected Components
       ↓
5. Cycle Detection - Undirected
       ↓
6. Cycle Detection - Directed
       ↓
7. Number of Islands / Grid DFS
       ↓
8. Bipartite Graph
       ↓
9. Topological Sort
       ↓
10. Course Schedule
       ↓
11. Shortest Path - BFS
       ↓
12. Dijkstra
       ↓
13. Union-Find / DSU
       ↓
14. Kruskal / Prim
       ↓
15. Bellman-Ford
       ↓
16. Advanced Graph Problems
```

### The **core interview set**

If your goal is interview readiness rather than becoming a graph specialist, master these first:

**BFS → DFS → Components → Cycle Detection → Grid Problems → Bipartite → Topological Sort → Dijkstra → DSU.**

Those are the patterns you should be able to recognize and implement without hesitation.
