from collections import defaultdict
import heapq
import networkx as nx
import matplotlib.pyplot as plt

INFINITY = float('infinity')

graph = defaultdict(list)

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

def add_edge(graph, u, v, weight):
    graph[u].append((v, weight))
    graph[v].append((u, weight))

for u, v, weight in edges:
    add_edge(graph, u, v, weight)

def dijkstra(graph, start, pos):
    pq = [(0, start)]
    distances = {vertex: INFINITY for vertex in graph}
    distances[start] = 0
    visited = set()
    parent = {start: None}
    step = 0

    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        if current_vertex in visited:
            continue
        visited.add(current_vertex)
        print(f"Step {step}: Visit {current_vertex}, distance = {current_distance}")
        step += 1
        draw_graph_step(graph, distances, visited, current_vertex, parent, pos)

        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
                parent[neighbor] = current_vertex

    return distances, parent

def draw_adjacency_list(graph):
    for node in sorted(graph):
        neighbors = ", ".join([f"{neighbor} (weight {weight})" for neighbor, weight in sorted(graph[node])])
        print(f"{node}: {neighbors}")

def create_networkx_graph(graph):
    G = nx.Graph()
    for u, neighbors in graph.items():
        for v, weight in neighbors:
            G.add_edge(u, v, weight=weight)
    return G

def draw_graph_step(graph, distances, visited, current_vertex, parent, pos):
    G = create_networkx_graph(graph)
    node_colors = ['orange' if node == current_vertex else 'green' if node in visited else 'red' for node in G.nodes()]
    edge_colors = ['green' if u in visited and v in visited else 'black' for u, v in G.edges()]

    plt.clf()
    nx.draw(G, pos, with_labels=True, node_color=node_colors, edge_color=edge_colors, font_size=8, node_size=3000, width=3, node_shape="o", font_family="sans-serif", font_color="white", font_weight="bold", arrows=True)
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, label_pos=0.3)
    plt.title(f"Current Vertex: {current_vertex}")
    plt.tight_layout()
    plt.axis("off")
    plt.pause(3)
    plt.show(block=False)
    plt.draw()


    # Display calculated distances on the plot
    if distances:
        for node, distance in distances.items():
            if distance != INFINITY:# If the distance is not infinity, display it on the plot
                plt.text(pos[node][0], pos[node][1] + 0.15, str(distance), fontsize=8, ha='center', va='center')# Add text to the plot
#function parent
def parent(graph, start, end, pos):
    distances, parent = dijkstra(graph, start, pos)
    path = reconstruct_path(parent, start, end)
    print(f"Shortest path from {start} to {end}: {path}")
    print(f"Shortest distance from {start} to {end}: {distances[end]}")
    return path


def reconstruct_path(parent, start, end):
    path = []
    current = end
    while current != start:
        path.append(current)
        current = parent[current]
    path.append(start)
    return path[::-1]

def main():
    print("Dijkstra's Algorithm with Simulation")
    print("-------------------------------")
    plt.ion()
    G = create_networkx_graph(graph)
    pos = {
        "Phnom Penh": (0, 0), "Kandal": (1, 1), "Kampong Speu": (-1, -1),
        "Takeo": (-2, 0), "Prey Veng": (2, 1), "Kampong Cham": (3, 0),
        "Koh Kong": (-3, -1), "Kampot": (-3, 1), "Svay Rieng": (3, 2),
        "Kratie": (4, -1), "Sihanoukville": (-4, -2),
    }

    draw_graph_step(graph, {}, set(), None, {}, pos)

    print("\n----------------------")
    print("Graph Adjacency List:")
    draw_adjacency_list(graph)

    start_node = "Phnom Penh"
    shortest_paths, parent = dijkstra(graph, start_node, pos)

    print(f"\nShortest paths from {start_node}:")
    for node, distance in sorted(shortest_paths.items(), key=lambda x: x[1]):
        path = reconstruct_path(parent, start_node, node)
        print(f"{node}: Distance = {distance}, Path = {' -> '.join(path)}")

    plt.ioff()
    plt.show()

if __name__ == "__main__":
    main()
