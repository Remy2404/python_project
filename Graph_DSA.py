import matplotlib.pyplot as plt
import networkx as nx

# Initialize the graph
G = nx.Graph()

# Add nodes (faculties and institutes)
nodes = [
    "Faculty of Agriculture",
    "Faculty of Arts",
    "Faculty of Economics and Management",
    "Faculty of Education",
    "Faculty of Engineering",
    "Faculty of Environmental Science",
    "Faculty of Geosciences",
    "Faculty of Law and Public Affairs",
    "Faculty of Science",
    "Institute of Foreign Languages",
    "Institute of International Relations",
    "Institute of Technology",
    "Institute of Graduate Studies"
]

# Add edges (connections) between nodes
edges = [
    ("Faculty of Agriculture", "Faculty of Environmental Science"),
    ("Faculty of Economics and Management", "Faculty of Law and Public Affairs"),
    ("Faculty of Education", "Institute of Graduate Studies"),
    ("Faculty of Engineering", "Institute of Technology"),
    ("Faculty of Science", "Faculty of Engineering"),
    ("Institute of Foreign Languages", "Institute of International Relations"),
    ("Faculty of Arts", "Faculty of Education")
]

# Add the nodes and edges to the graph
G.add_nodes_from(nodes)
G.add_edges_from(edges)

# Define the layout for the graph
pos = nx.kamada_kawai_layout(G)

# Draw the graph
plt.figure(figsize=(15, 10))
nx.draw_networkx_nodes(G, pos, node_color='skyblue', node_size=3000, edgecolors='black')
nx.draw_networkx_edges(G, pos, width=2, alpha=0.6, edge_color='gray')
nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif', font_weight='bold')

# Adjust text positions
for node, (x, y) in pos.items():
    plt.text(x, y+0.05, s=node, bbox=dict(facecolor='white', alpha=0.6), horizontalalignment='center', fontsize=10, fontweight='bold')

# Customize the plot
plt.title("RUPP Faculties and Institutes Graph Structure", size=20)
plt.axis('off')  # Hide the axes
plt.show()
