from collections import defaultdict
import heapq
import networkx as nx
import matplotlib.pyplot as plt

# Define a constant for infinity
INFINITY = float('infinity')

# Create the graph with provinces in Cambodia
graph = defaultdict(list)  # Create a dictionary to represent the graph with weights

# Array of edges defined as a list of tuples
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

# Add edges to the graph
for u, v, weight in edges:
    add_edge(graph, u, v, weight)

# Dijkstra's algorithm function with simulation
def dijkstra(graph, start, pos):
    pq = [(0, start)]  # Priority queue to store (distance, vertex)
    distances = {vertex: INFINITY for vertex in graph}  # Initialize distances
    distances[start] = 0  # Set distance of start node to 0
    visited = set()  # Set to track visited vertices
    parent = {start: None}  # To reconstruct paths

    step = 0

    while pq:
        current_distance, current_vertex = heapq.heappop(pq)

        if current_vertex in visited:  # If vertex is already visited, skip it
            continue

        visited.add(current_vertex)  # Add vertex to visited set
        print(f"Step {step}: Visit {current_vertex}, distance = {current_distance}")
        step += 1
        draw_graph_step(graph, distances, visited, current_vertex, parent, pos)

        for neighbor, weight in graph[current_vertex]:# For each neighbor of the current vertex...
            distance = current_distance + weight# Calculate the distance to the neighbor
            if distance < distances[neighbor]:
                distances[neighbor] = distance# Update the distance if it's shorter
                heapq.heappush(pq, (distance, neighbor))# Add the neighbor to the priority queue
                parent[neighbor] = current_vertex# Update the parent of the neighbor

    return distances, parent

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
    for u, neighbors in graph.items():
        for v, weight in neighbors:
            G.add_edge(u, v, weight=weight)
    return G

# Draw the graph at each step of Dijkstra's algorithm
def draw_graph_step(graph, distances, visited, current_vertex, parent, pos):
    G = create_networkx_graph(graph)

    node_colors = []
    for node in G.nodes():
        if node == current_vertex:
            node_colors.append("orange")
        elif node in visited:
            node_colors.append("green")
        else:
            node_colors.append("red")

    edge_colors = []
    for u, v in G.edges():
        if u in visited and v in visited:
            edge_colors.append("green")
        else:
            edge_colors.append("black")

    plt.clf()  # Clear the current figure
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color=node_colors,
        edge_color=edge_colors,
        font_size=8,
        node_size=3000,
        width=3,
        node_shape="o",
        font_family="sans-serif",
        font_color="white",
        font_weight="bold",
        arrows=True,
    )

    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, label_pos=0.3)
    plt.title(f"Current Vertex: {current_vertex}")
    plt.axis("off")
    plt.pause(3)  # Pause to allow the plot to update

# Function to reconstruct the path
def reconstruct_path(parent, start, end):
    path = []
    current = end
    while current != start:
        path.append(current)
        current = parent[current]
    path.append(start)
    return path[::-1]

# --- Main Program ---
def main():
    print("Dijkstra's Algorithm with Simulation")
    print("-------------------------------")
    plt.ion()  # Enable interactive mode
    G = create_networkx_graph(graph)
    pos = {
        "Phnom Penh": (0, 0),
        "Kandal": (1, 1),
        "Kampong Speu": (-1, -1),
        "Takeo": (-2, 0),
        "Prey Veng": (2, 1),
        "Kampong Cham": (3, 0),
        "Koh Kong": (-3, -1),
        "Kampot": (-3, 1),
        "Svay Rieng": (3, 2),
        "Kratie": (4, -1),
        "Sihanoukville": (-4, -2),
    }  # Constant positions for nodes

    draw_graph_step(graph, {}, set(), None, {}, pos)  # Initial empty graph

    # Print the adjacency list
    print("\n----------------------")
    print("Graph Adjacency List:")
    draw_adjacency_list(graph)

    # Perform Dijkstra's algorithm with simulation
    start_node = "Phnom Penh"
    shortest_paths, parent = dijkstra(graph, start_node, pos)

    # Print the shortest paths from the start node
    print(f"\nShortest paths from {start_node}:")
    for node, distance in sorted(shortest_paths.items(), key=lambda x: x[1]):
        path = reconstruct_path(parent, start_node, node)
        print(f"{node}: Distance = {distance}, Path = {' -> '.join(path)}")

    plt.ioff()  # Disable interactive mode
    plt.show()  # Display the final plot

if __name__ == "__main__":
    main()