from collections import defaultdict
import heapq

graph = defaultdict(list)

# Add edge to the graph
def add_edge(graph, u, v, weight):
    graph[u].append((v, weight))
    graph[v].append((u, weight))  # Since the graph is undirected

# Dijkstra's algorithm function
def dijkstra(graph, start):
    # Priority queue to store (distance, vertex)
    pq = [(0, start)]
    # Distances dictionary to store the shortest path to each vertex
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    # Set to track visited vertices
    visited = set()

    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        
        if current_vertex in visited:
            continue
        
        visited.add(current_vertex)

        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances

# Draw the adjacency list
def draw_adjacency_list(graph):
    for node in sorted(graph):  # Ensure nodes are printed in ascending order
        print(f"{node}: {', '.join([f'{neighbor} (weight {weight})' for neighbor, weight in sorted(graph[node])])}")

# Generate graph edges
def generate_graph(graph):
    edges = []
    for node in graph:
        for neighbor, weight in graph[node]:
            if (neighbor, node, weight) not in edges:  # Avoid duplicate edges
                edges.append((node, neighbor, weight))
    return edges

# Create the graph based on the image provided
add_edge(graph, 0, 1, 2)
add_edge(graph, 0, 2, 6)
add_edge(graph, 0, 3, 8)
add_edge(graph, 1, 3, 5)
add_edge(graph, 2, 3, 8)
add_edge(graph, 3, 4, 10)
add_edge(graph, 3, 5, 15)
add_edge(graph, 4, 5, 6)
add_edge(graph, 4, 6, 2)
add_edge(graph, 5, 6, 6)

print("Graph Edges:", generate_graph(graph))
print("\n----------------------")
print("Graph Adjacency List:")
draw_adjacency_list(graph)

# Perform Dijkstra's algorithm on the graph starting from node 0
start_node = 0
shortest_paths = dijkstra(graph, start_node)

print(f"\nShortest paths from node {start_node}:")
for node, distance in shortest_paths.items():
    print(f"Node {node}: {distance}")
