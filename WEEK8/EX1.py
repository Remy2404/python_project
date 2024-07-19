from collections import defaultdict

graph1 = defaultdict(list)
graph2 = defaultdict(list)

# Add edge to the graph
def add_edge(graph, u, v):
    graph[u].append(v)
    graph[v].append(u)

# DFS function
def DFS(graph, start):
    visited = set()
    stack = [start]  # Stack of nodes to visit
    result = []
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            result.append(node)
            # Sort neighbors in descending order to ensure the correct order of traversal
            for neighbor in sorted(graph[node], reverse=True):  # Sort in descending order
                if neighbor not in visited:
                    stack.append(neighbor)
    
    return result

# Draw the adjacency list
def draw_adjacency_list(graph):
    for node in sorted(graph):  # Ensure nodes are printed in ascending order
        print(f"{node}: {', '.join(map(str, sorted(graph[node])))}")

# Generate graph edges
def generate_graph(graph):
    edges = []
    for node in graph:
        for neighbor in graph[node]:
            if (neighbor, node) not in edges:  # Avoid duplicate edges
                edges.append((node, neighbor))
    return edges

# Create the graph for DFS
add_edge(graph1, 0, 1)
add_edge(graph1, 0, 2)
add_edge(graph1, 0, 3)
add_edge(graph1, 0, 4)
add_edge(graph1, 2, 3)
add_edge(graph1, 2, 4)

# Create the graph for DFS
add_edge(graph2, 0, 1)
add_edge(graph2, 0, 2)
add_edge(graph2, 0, 3)
add_edge(graph2, 0, 4)
add_edge(graph2, 2, 3)
add_edge(graph2, 2, 4)

print("Graph 1 Edges:", generate_graph(graph1))
print("\n----------------------")
print("Graph 1 Adjacency List:")
draw_adjacency_list(graph1)
print("\n----------------------")
print("Graph 2 Edges:", generate_graph(graph2))
print("\n----------------------")
print("Graph 2 Adjacency List:")
draw_adjacency_list(graph2)

# Perform DFS on graph2 starting from node 0
print
