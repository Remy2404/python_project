from collections import defaultdict

graph = defaultdict(list)

def add_edge(graph, u, v):
    graph[u].append(v)
    graph[v].append(u)

def draw_adjacency_List(graph):
    for node in graph:
        print(f"{node}: {', '.join(map(str, graph[node]))}")

def remove_edge(graph, u, v):
    graph[u].remove(v)
    graph[v].remove(u)

def generate_adjacency_matrix(graph):
    max_node = max(graph.keys())# Find the maximum node number to determine the size of the matrix
    adjacency_matrix = [[0] * (max_node + 1) for _ in range(max_node + 1)]# Initialize the adjacency matrix with zeros

    for node in graph:
        for neighbour in graph[node]:
            adjacency_matrix[node][neighbour] = 1
            adjacency_matrix[neighbour][node] = 1  # Since the graph is undirected
    
    return adjacency_matrix

def generate_graph(graph):
    add_edge = []
    for node in graph:
        for neighbor in graph[node]:
            add_edge.append((node, neighbor))
    return add_edge

# Create the graph based on the given image
add_edge(graph, 0, 1)
add_edge(graph, 0, 2)
add_edge(graph, 0, 3)
add_edge(graph, 1, 2)

# Display the graph and adjacency matrix
print("Original Adjacency List:")
draw_adjacency_List(graph)

print("\nOriginal Adjacency Matrix:")
adjacency_matrix = generate_adjacency_matrix(graph)
for row in adjacency_matrix:
    print(row)

# Remove edge (1, 2) and print the updated adjacency list and matrix
remove_edge(graph, 1, 2)

print("\nAdjacency List after removing edge (1, 2):")
draw_adjacency_List(graph)

print("\nAdjacency Matrix after removing edge (1, 2):")
adjacency_matrix = generate_adjacency_matrix(graph)
for row in adjacency_matrix:
    print(row)


