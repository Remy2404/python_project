import networkx as nx
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))

cambodia_graph = Graph()

edges = [
    ("Phnom Penh", "Siem Reap", 314),
    ("Phnom Penh", "Battambang", 291),
    ("Phnom Penh", "Kampot", 148),
    ("Phnom Penh", "Kampong Cham", 124),
    ("Phnom Penh", "Kratie", 315),
    ("Phnom Penh", "Mondul Kiri", 521),
    ("Phnom Penh", "Preah Vihear", 294),
    ("Phnom Penh", "Ratanakiri", 588),
    ("Phnom Penh", "Sihanoukville", 230),
    ("Phnom Penh", "Svay Rieng", 122),
    ("Phnom Penh", "Takeo", 78),
    ("Phnom Penh", "Kampong Speu", 48),
    ("Phnom Penh", "Koh Kong", 271),
    ("Phnom Penh", "Kandal", 11),
    ("Phnom Penh", "Banteay Meanchey", 359),
    ("Phnom Penh", "Prey Veng", 90),
    ("Phnom Penh", "Pailin", 371),
    ("Phnom Penh", "Pursat", 189),
    ("Phnom Penh", "Stung Treng", 455),
    ("Phnom Penh", "Oddar Meanchey", 469),
    ("Phnom Penh", "Kampong Thom", 167),
    ("Phnom Penh", "Kampong Chhnang", 91),
    ("Phnom Penh", "Kep", 174),
]

for u, v, weight in edges:
    cambodia_graph.add_edge(u, v, weight)

def MST_algorithm_step(graph, start):
    visited = set([start])
    edges = []
    while len(visited) < len(graph.graph):
        min_edge = None
        for v in visited:
            for neighbor, weight in graph.graph[v]:
                if neighbor not in visited:
                    if min_edge is None or weight < min_edge[2]:
                        min_edge = (v, neighbor, weight)
        if min_edge:
            edges.append(min_edge)
            visited.add(min_edge[1])
            yield min_edge[1], list(visited), edges

def get_initial_map_data():
    markers = {
        'Phnom Penh': [11.56245, 104.91601],
        'Banteay Meanchey': [13.58588, 102.97369],
        'Battambang': [13.10271, 103.19822],
        'Kampong Cham': [11.99339, 105.4635],
        'Kampong Chhnang': [12.25, 104.66667],
        'Kampong Speu': [11.4600, 104.5247],
        'Kampong Thom': [12.71121, 104.89108],
        'Kampot': [10.61041, 104.18145],
        'Kandal': [11.2016, 105.2096],
        'Koh Kong': [11.6089, 103.0787],
        'Kratie': [12.4880, 106.0190],
        'Mondul Kiri': [12.8000, 107.2000],
        'Oddar Meanchey': [14.18175, 103.51761],
        'Pailin': [12.84895, 102.60928],
        'Preah Vihear': [13.7911, 104.9830],
        'Prey Veng': [11.48682, 105.32533],
        'Pursat': [12.53878, 103.9192],
        'Ratanakiri': [13.73939, 106.98727],
        'Siem Reap': [13.36179, 103.86056],
        'Stung Treng': [13.52586, 105.9683],
        'Svay Rieng': [11.08785, 105.79935],
        'Takeo': [10.99081, 104.78498],
        'Kep': [10.4833, 104.3167],
        'Sihanoukville': [10.60932, 103.52958],
    }
    
    G = nx.Graph()
    for u, v, weight in edges:
        G.add_edge(u, v, weight=weight)
    
    return {
        'markers': markers,
        'edges': list(G.edges())
    }

# The following functions are kept for compatibility with existing code,
# but they are not used in the new dynamic implementation

def create_networkx_graph(custom_graph):
    G = nx.Graph()
    for node, edges in custom_graph.graph.items():
        for edge, weight in edges:
            G.add_edge(node, edge, weight=weight)
    return G

def draw_graph_step(graph, distances, visited, current_vertex, parent, pos):
    # This function is not used in the new implementation
    pass

def create_MST_map(start, end):
    # This function is not used in the new implementation
    pass

def update_map_colors(feature_group, current_vertex, visited, markers, step):
    # This function is not used in the new implementation
    pass