import os
import folium
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib import use
use('Agg')
from collections import defaultdict

# Define the Graph class and add edges
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))

# Initialize the graph and add edges
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

# Create a NetworkX graph from the custom Graph class
def create_networkx_graph(custom_graph):
    G = nx.Graph()
    for node, edges in custom_graph.graph.items():
        for edge, weight in edges:
            G.add_edge(node, edge, weight=weight)
    return G

def draw_graph_step(graph, distances, visited, current_vertex, parent, pos):
    G = create_networkx_graph(graph)
    node_colors = ['orange' if node == current_vertex else 'green' if node in visited else 'red' for node in G.nodes()]
    edge_colors = ['green' if u in visited and v in visited else 'red' for u, v in G.edges()]

    plt.figure(figsize=(12, 8))
    nx.draw(G, pos, with_labels=True, node_color=node_colors, edge_color=edge_colors, node_size=700, font_size=10)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    
    # Create a 'templates' directory if it doesn't exist
    if not os.path.exists('templates'):
        os.makedirs('templates')
    
    # Save the figure in the templates folder
    plt.savefig('templates/graph_step.png')
    plt.close()

# Create a map centered on Cambodia
m = folium.Map(location=[12.5657, 104.991], zoom_start=7)

# Add markers with correct coordinates and popups
def add_marker(m):
    markers = {}
    markers['Phnom Penh'] = folium.Marker([11.56245, 104.91601], popup='Phnom Penh').add_to(m)
    markers['Banteay Meanchey'] = folium.Marker([13.58588, 102.97369], popup='Banteay Meanchey').add_to(m)
    markers['Battambang'] = folium.Marker([13.10271, 103.19822], popup='Battambang').add_to(m)
    markers['Kampong Cham'] = folium.Marker([11.99339, 105.4635], popup='Kampong Cham').add_to(m)
    markers['Kampong Chhnang'] = folium.Marker([12.25, 104.66667], popup='Kampong Chhnang').add_to(m)
    markers['Kampong Speu'] = folium.Marker([11.4600, 104.5247], popup='Kampong Speu').add_to(m)
    markers['Kampong Thom'] = folium.Marker([12.71121, 104.89108], popup='Kampong Thom').add_to(m)
    markers['Kampot'] = folium.Marker([10.61041, 104.18145], popup='Kampot').add_to(m)
    markers['Kandal'] = folium.Marker([11.2016, 105.2096], popup='Kandal').add_to(m)
    markers['Koh Kong'] = folium.Marker([11.6089, 103.0787], popup='Koh Kong').add_to(m)
    markers['Kratie'] = folium.Marker([12.4880, 106.0190], popup='Kratie').add_to(m)
    markers['Mondul Kiri'] = folium.Marker([12.8000, 107.2000], popup='Mondul Kiri').add_to(m)
    markers['Oddar Meanchey'] = folium.Marker([14.18175, 103.51761], popup='Oddar Meanchey').add_to(m)
    markers['Pailin'] = folium.Marker([12.84895, 102.60928], popup='Pailin').add_to(m)
    markers['Preah Vihear'] = folium.Marker([13.7911, 104.9830], popup='Preah Vihear').add_to(m)
    markers['Prey Veng'] = folium.Marker([11.48682, 105.32533], popup='Prey Veng').add_to(m)
    markers['Pursat'] = folium.Marker([12.53878, 103.9192], popup='Pursat').add_to(m)
    markers['Ratanakiri'] = folium.Marker([13.73939, 106.98727], popup='Ratanakiri').add_to(m)
    markers['Siem Reap'] = folium.Marker([13.36179, 103.86056], popup='Siem Reap').add_to(m)
    markers['Stung Treng'] = folium.Marker([13.52586, 105.9683], popup='Stung Treng').add_to(m)
    markers['Svay Rieng'] = folium.Marker([11.08785, 105.79935], popup='Svay Rieng').add_to(m)
    markers['Takeo'] = folium.Marker([10.99081, 104.78498], popup='Takeo').add_to(m)
    markers['Kep'] = folium.Marker([10.4833, 104.3167], popup='Kep').add_to(m)
    markers['Sihanoukville'] = folium.Marker([10.60932, 103.52958], popup='Sihanoukville').add_to(m)
    return markers

# Create a NetworkX graph
G = create_networkx_graph(cambodia_graph)

# Add lines for connections between provinces
markers = add_marker(m)

for edge in G.edges():
    start = markers[edge[0]]
    end = markers[edge[1]]
    folium.PolyLine(
        locations=[start.location, end.location],
        weight=3,
        color='red'
    ).add_to(m)

# Save the map
m.save("cambodia_map3.1.html")
pos = nx.spring_layout(G)  # You can use other layouts like nx.kamada_kawai_layout(G)
draw_graph_step(cambodia_graph, {}, [], 'Phnom Penh', None, pos)

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

mst_step_generator = MST_algorithm_step(cambodia_graph, 'Phnom Penh')


def create_MST_map(start, end):
    m = folium.Map(location=[12.5657, 104.991], zoom_start=7)
    markers = add_marker(m)
    
    feature_group = folium.FeatureGroup(name="MST Steps")
    m.add_child(feature_group)
    
    for step, (current_vertex, visited, distances) in enumerate(MST_algorithm_step(cambodia_graph, start, end)):
        update_map_colors(feature_group, current_vertex, visited, markers, step)
    
    folium.LayerControl().add_to(m)
    return m

def update_map_colors(feature_group, current_vertex, visited, markers, step):
    for node, marker in markers.items():
        color = 'red'
        if node == current_vertex:
            color = 'orange'
        elif node in visited:
            color = 'green'
        
        folium.CircleMarker(
            location=marker.location,
            radius=10,
            popup=f"Step {step}: {node}",
            color=color,
            fill=True,
            fillColor=color
        ).add_to(feature_group)
