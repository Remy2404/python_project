#EX1:
#part a:
from collections import defaultdict

graph = defaultdict(list)

def add_edge(graph, u, v):
    graph[u].append(v)
    graph[v].append(u)

def generate_graph(graph):
    add_edge = []
    for node in graph:
        for neighbour in graph[node]:
            add_edge.append((node, neighbour))
    return add_edge

add_edge(graph, 0, 1)
add_edge(graph, 0, 2)
add_edge(graph, 1, 3)
add_edge(graph, 2, 3)
add_edge(graph, 3, 4)
add_edge(graph, 4, 0)

print(generate_graph(graph))
print("", end="")


#part b : Draw the adjacency list:
#Draws an adjcency list:
graph = {
    0: [1, 2, 3],
    1: [3, 4],
    2:[3],
    3: [4],
    4:[]
}
for node, edges in graph.items():
    print("EX1:", end=" ")
    print(f"{node} has edges: {edges}")

#EX2:
#part a :
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
edges1 = [
    (1, 2), (1, 3),
    (2, 4), (2, 5),
    (3, 6),
    (4, 7),
    (5, 6), (5, 7),
    (6, 7)
]

for u, v in edges1:
    g.add_edge(u, v)

# Print the graph
print("EX2:", end=" ")
print(g)

#part b : Draw the adjacency
adjacency_list = {
    1: [2, 3],
    2: [4, 5],
    3: [6],
    4: [7],
    5: [6, 7],
    6: [7],
    7: []
}

for node, neighbors in adjacency_list.items():
    print(f"{node}: {', '.join(map(str, neighbors))}")

