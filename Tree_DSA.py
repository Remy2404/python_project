import matplotlib.pyplot as plt
import networkx as nx

# Initialize the graph
G = nx.DiGraph()

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

# Add a root node to represent the university
root = "RUPP"

# Add edges from the root node to each faculty/institute
edges = [(root, node) for node in nodes]

# Add the nodes and edges to the graph
G.add_node(root)
G.add_nodes_from(nodes)
G.add_edges_from(edges)

# Define the layout for the tree
pos = nx.spring_layout(G)

# Draw the nodes and edges
plt.figure(figsize=(12, 8))
nx.draw(G, pos, with_labels=True, node_size=3000, node_color="skyblue", font_size=10, font_weight="bold", arrows=True)
plt.title("RUPP Faculties and Institutes Tree Structure", size=15)
plt.show()
