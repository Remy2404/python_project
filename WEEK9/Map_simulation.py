from collections import defaultdict
import heapq
import networkx as nx
import matplotlib.pyplot as plt

INFINITY = float('infinity')

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))

cambodia_graph = Graph()

# Adding edges based on the provided data
cambodia_graph.add_edge("Phnom Penh", "Bokor", 189)
cambodia_graph.add_edge("Phnom Penh", "Kirirom", 117)
cambodia_graph.add_edge("Phnom Penh", "Kampot", 148)
cambodia_graph.add_edge("Phnom Penh", "Krong Kep", 174)
cambodia_graph.add_edge("Phnom Penh", "Sihanoukville", 230)
cambodia_graph.add_edge("Phnom Penh", "Kampong Chhnang", 91)
cambodia_graph.add_edge("Phnom Penh", "Pursat", 189)
cambodia_graph.add_edge("Phnom Penh", "Battambang", 291)
cambodia_graph.add_edge("Phnom Penh", "Pailin", 371)
cambodia_graph.add_edge("Phnom Penh", "Banteay Meanchey", 359)
cambodia_graph.add_edge("Phnom Penh", "Kampong Thom", 167)
cambodia_graph.add_edge("Phnom Penh", "Kampong Cham", 124)
cambodia_graph.add_edge("Phnom Penh", "Prey Veng", 90)
cambodia_graph.add_edge("Phnom Penh", "Svay Rieng", 122)
cambodia_graph.add_edge("Phnom Penh", "Takeo", 78)
cambodia_graph.add_edge("Phnom Penh", "Kandal", 11)
cambodia_graph.add_edge("Phnom Penh", "Kampong Speu", 48)
cambodia_graph.add_edge("Phnom Penh", "Kratie", 315)
cambodia_graph.add_edge("Phnom Penh", "Stung Treng", 455)
cambodia_graph.add_edge("Phnom Penh", "Mondulkiri", 521)
cambodia_graph.add_edge("Phnom Penh", "Preah Vihear", 294)
cambodia_graph.add_edge("Phnom Penh", "Ratanakiri", 588)
cambodia_graph.add_edge("Phnom Penh", "Koh Kong", 271)
cambodia_graph.add_edge("Phnom Penh", "Oddar Meanchey", 469)

# Define node positions for each province in Cambodia
provinces = {
    "Banteay Meanchey": (1, 5),
    "Oddar Meanchey": (2, 6),
    "Preah Vihear": (4, 6),
    "Stung Treng": (5, 7),
    "Ratanakiri": (6, 7),
    "Mondulkiri": (7, 6),
    "Kratie": (6, 5),
    "Kampong Thom": (5, 4),
    "Kampong Cham": (6, 3),
    "Phnom Penh": (7, 2),
    "Kandal": (7, 1),
    "Prey Veng": (8, 2),
    "Svay Rieng": (9, 2),
    "Takeo": (7, 0),
    "Kampot": (6, 0),
    "Koh Kong": (4, 0),
    "Pailin": (2, 4),
    "Battambang": (3, 4),
    "Pursat": (4, 3),
    "Kampong Chhnang": (5, 2),
    "Kampong Speu": (6, 1),
    "Sihanoukville": (5, 0),
    "Kep": (6, -1),
    "Bokor": (5.5, -0.5),
    "Kirirom": (5, 1),
    "Krong Kep": (6, -1)
}


def dijkstra(graph, start, pos):
    pq = [(0, start)]
    distances = {vertex: INFINITY for vertex in graph.graph}
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
        draw_graph_step(graph.graph, distances, visited, current_vertex, parent, pos)

        for neighbor, weight in graph.graph[current_vertex]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
                parent[neighbor] = current_vertex

    return distances, parent

def draw_adjacency_list(graph):
    for node in sorted(graph.graph):
        neighbors = ", ".join([f"{neighbor} (weight {weight})" for neighbor, weight in sorted(graph.graph[node])])
        print(f"{node}: {neighbors}")

def create_networkx_graph(graph):
    G = nx.Graph()
    for u, neighbors in graph.graph.items():
        for v, weight in neighbors:
            G.add_edge(u, v, weight=weight)
    return G

def draw_graph_step(graph, distances, visited, current_vertex, parent, pos):
    G = create_networkx_graph(Graph())
    for u, neighbors in graph.items():
        for v, weight in neighbors:
            G.add_edge(u, v, weight=weight)
    
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

    if distances:
        for node, distance in distances.items():
            if distance != INFINITY:
                plt.text(pos[node][0], pos[node][1] + 0.15, str(distance), fontsize=8, ha='center', va='center')

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
    G = create_networkx_graph(cambodia_graph)
    pos = provinces  # Use the predefined positions

    draw_graph_step(cambodia_graph.graph, {}, set(), None, {}, pos)

    print("\n----------------------")
    print("Graph Adjacency List:")
    draw_adjacency_list(cambodia_graph)

    start_node = "Phnom Penh"
    shortest_paths, parent = dijkstra(cambodia_graph, start_node, pos)

    print(f"\nShortest paths from {start_node}:")
    for node, distance in sorted(shortest_paths.items(), key=lambda x: x[1]):
        path = reconstruct_path(parent, start_node, node)
        print(f"{node}: Distance = {distance}, Path = {' -> '.join(path)}")

    plt.ioff()
    plt.show()

if __name__ == "__main__":
    main()
