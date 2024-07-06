class Graph:
    def __init__(self):
        self.graph = {}
#         self.graph = defaultdict(list)
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)
#         if v not in self.graph:
    def __str__(self):
        return str(self.graph)

# Create the graph
g = Graph()

# Add edges
edges4 = [
    ('A', 'B'),
    ('B', 'C'), ('B', 'D'),
    ('C', 'E'), ('E', 'D'),
    ('D ', 'A')
]

for u, v in edges4:
    g.add_edge(u, v)

# Print the graph
print("EX2:", end=" ")
print(g)

#part b : Draw the adjacency
adjacency_list = {
   'A': ['B'],
    'B': ['C', 'D'],
    'C': ['E'],
    'D': ['A'],
    'E': ['D']
}

for node, neighbors in adjacency_list.items():
    print(f"{node}: {', '.join(map(str, neighbors))}")
