from collections import defaultdict
import heapq

import networkx as nx
import matplotlib.pyplot as plt

# Define a constant for infinity

INFINITY = float('infinity')
"""
Defines a constant `INFINITY` as the maximum possible float value, 
representing an infinite distance.
This is used in Dijkstra's algorithm to initialize the distances to all vertices as infinity, 
except for the starting vertex which is set to 0. The `heapq` module is then used to pop the 
vertex with the shortest distance from the priority queue.
"""

# Create the graph with provinces in Cambodia
# Using a dictionary to represent the graph with weights
graph = defaultdict(list)# Create a dictionary to represent the graph with weights
# Array of edges is defined as a list of tuples
edges = [
    ("Phnom Penh", "Kandal", 20),
    ("Phnom Penh", "Kampong Speu", 40),
    ("Phnom Penh", "Takeo", 50),
    ("Kandal", "Prey Veng", 70),
    ("Kandal", "Kampong Cham", 90),
    ("Kampong Speu", "Koh Kong", 120),
    ("Takeo", "Kampot", 60),
    ("Prey Veng", "Svay Rieng", 30),
    ("Kampong Cham", "Kratie", 100),
    ("Koh Kong", "Sihanoukville", 150),
]

# Function to add an edge to the undirected graph
def add_edge(graph, u, v, weight):
    graph[u].append((v, weight))
    graph[v].append((u, weight))

for u, v, weight in edges:# Add edges to the graph
    add_edge(graph, u, v, weight)#call the function to add edges

# Dijkstra's algorithm function
def dijkstra(graph, start):
    # Priority queue to store (distance, vertex)
    pq = [(0, start)]

    # Distances dictionary to store the shortest path to each vertex
    distances = {vertex: INFINITY for vertex in graph}
    distances[start] = 0
    """ Set the distance of the start node to 0 , why we set it to 0? 
    Because we want to represent the distance of the start node as 0.
    The reason is that we want to use the heapq to pop the shortest path
    from the start node. If we set the distance of the start node to 1,	
    the heapq will pop the path with the shortest distance.	
    """
    # Set to track visited vertices
    visited = set()

    while pq:
        #pop the vertex with the shortest distance from the priority queue
        current_distance, current_vertex = heapq.heappop(pq)

        if current_vertex in visited:# If the vertex is already visited, skip it
            continue

        visited.add(current_vertex)# Add the vertex to the visited set
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

# Draw the adjacency list
def draw_adjacency_list(graph):
    for node in sorted(graph):
        neighbors = ", ".join(
            [f"{neighbor} (weight {weight})" for neighbor, weight in sorted(graph[node])]
        )
        print(f"{node}: {neighbors}")

# Create a NetworkX graph for visualization
def create_networkx_graph(graph):
    G = nx.Graph()
    for node in graph:
        G.add_node(node)
    for u, neighbors in graph.items():
        for v, weight in neighbors:
            G.add_edge(u, v, weight=weight)
    return G
# Draw the graph using NetworkX
def draw_graph(graph):
    G = create_networkx_graph(graph)
    pos = nx.spring_layout(G)
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color="Red",
        edge_color = "Black",
        font_size=8,
        node_size=3000,
        font_color="White",
        font_weight="bold",
        font_family="cursive",
        width=1,
        edge_vmin=0,# minimum value of edge
    )
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.axis("off")
    plt.show()

# --- Main Program ---
if __name__ == "__main__":
    draw_graph(graph)

    # Print the adjacency list
    print("\n----------------------")
    print("Graph Adjacency List:")
    draw_adjacency_list(graph)

    # Perform Dijkstra's algorithm
    start_node = "Phnom Penh"
    shortest_paths = dijkstra(graph, start_node)

    # Print the shortest paths from the start node
    print(f"\nShortest paths from {start_node}:")
    for node, distance in sorted(shortest_paths.items(), key=lambda x: x[1]):
        print(f"{node}: {distance}")
