from collections import defaultdict

graph = defaultdict(list)

def add_edge(graph, u, v):
    graph[u].append(v)
    graph[v].append(u)

# Draw adjacency List:
def draw_adjacency_List(graph):
    for node in graph:
        print(f"{node}: {', '.join(map(str, graph[node]))}")

# Function to generate the adjacency matrix
def generate_adjacency_matrix(graph):
    # Find the maximum node number to determine the size of the matrix
    max_node = max(graph.keys())
    # Initialize the adjacency matrix with zeros
    adjacency_matrix = [[0] * (max_node + 1) for _ in range(max_node + 1)]
    
    # Fill the adjacency matrix
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
#Edges: (1-2), (1-5), (2-3), (2-4), (2-5), (3-4), (4-5)
add_edge(graph, 1, 2)
add_edge(graph, 1, 5)
add_edge(graph, 2, 3)
add_edge(graph, 2, 4)
add_edge(graph, 2, 5)
add_edge(graph, 3, 4)
add_edge(graph, 4, 5)
# Display the graph

print(generate_graph(graph))
print("", end="")

# Draw the adjacency List:
print("Adjacency List:")
draw_adjacency_List(graph)

# Generate the adjacency matrix
print("Adjacency Matrix:")
adjacency_matrix = generate_adjacency_matrix(graph)

# Print the adjacency matrix
for row in adjacency_matrix[1:]:  # Skip the 0th row for clarity
    print(row[1:])  # Skip the 0th column for clarity



