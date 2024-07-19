from collections import defaultdict

# Define the graph using an adjacency list
graph = defaultdict(list)

def add_edge(graph, u, v):
    graph[u].append(v)

def generate_graph(graph):
    edges = []
    for node in graph:
        for neighbour in graph[node]:
            edges.append((node, neighbour))
    return edges

# Add edges to the graph
add_edge(graph, 1, 2)
add_edge(graph, 1, 3)
add_edge(graph, 2, 4)
add_edge(graph, 2, 5)
add_edge(graph, 3, 6)
add_edge(graph, 4, 7)
add_edge(graph, 5, 7)

# Print the edges of the graph
print(generate_graph(graph))
# Define the adjacency list
graph = {
    1: [2, 3],
    2: [4, 5],
    3: [6],
    4: [7],
    5: [7],
    6: [],
    7: []
}

# Print the adjacency list
for node, edges in graph.items():
    print(f"{node} has edges: {edges}")
