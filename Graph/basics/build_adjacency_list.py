n = 6

edges = [
    [0, 1],
    [0, 2],
    [1, 3],
    [4, 5]
]

graph_list = {}


for i in range(n):
    graph_list[i] = []

for node_a, node_b in edges:
    graph_list[node_a].append(node_b)
    graph_list[node_b].append(node_a)

print(graph_list)

# output:
# {
#     0: [1, 2],
#     1: [0, 3],
#     2: [0],
#     3: [1],
#     4: [5],
#     5: [4]
# }