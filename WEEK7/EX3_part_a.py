from collections import defaultdict

graph1 = defaultdict(list)
graph2 = defaultdict(list)

def add_directed_edge(graph, u, v):
    graph[u].append(v)

def add_undirected_edge(graph, u, v):
    graph[u].append(v)
    graph[v].append(u)

def draw_adjacency_list(graph):
    for node in graph:
        print(f"{node}: {', '.join(map(str, graph[node]))}")

def remove_directed_edge(graph, u, v):
    graph[u].remove(v)

def remove_undirected_edge(graph, u, v):
    graph[u].remove(v)
    graph[v].remove(u)

def generate_adjacency_matrix(graph):
    max_node = max(graph.keys())
    adjacency_matrix = [[0] * (max_node + 1) for _ in range(max_node + 1)]
    for node in graph:
        for neighbour in graph[node]:
            adjacency_matrix[node][neighbour] = 1
    return adjacency_matrix

def generate_edges(graph):
    edges = []
    for node in graph:
        for neighbor in graph[node]:
            edges.append((node, neighbor))
    return edges

# Part a: Create adjacency list for both graphs
# Graph 1: Directed
add_directed_edge(graph1, 1, 2)
add_directed_edge(graph1, 1, 3)
add_directed_edge(graph1, 2, 3)
add_directed_edge(graph1, 3, 4)

# Graph 2: Undirected
add_undirected_edge(graph2, 1, 2)
add_undirected_edge(graph2, 1, 3)
add_undirected_edge(graph2, 2, 3)
add_undirected_edge(graph2, 3, 4)

# Print adjacency lists
print("Adjacency List for Graph 1 (Directed):")
draw_adjacency_list(graph1)

print("\nAdjacency List for Graph 2 (Undirected):")
draw_adjacency_list(graph2)

# Part b: Generate edges for both graphs
print("\nEdges for Graph 1 (Directed):")
print(generate_edges(graph1))

print("\nEdges for Graph 2 (Undirected):")
print(generate_edges(graph2))
