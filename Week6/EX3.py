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
edges3 = [
    (0, 1), (0, 2),
    (1, 2), 
    (2, 3), (2, 5),
    (3, 4), (3, 6),
    (4, 6),
    (5, 7),
    (6, 7)
]

for u, v in edges3:
    g.add_edge(u, v)

# Print the graph
print("EX3:", end=" ")
print(g)

#part b : Draw the adjacency
adjacency_list = {
    0: [1, 2],
    1: [2],
    2: [3, 5],
    3: [4, 6],
    4: [6],
    5: [7],
    6: [7],
    7: []
}

for node, neighbors in adjacency_list.items():
    print(f"{node}: {', '.join(map(str, neighbors))}")