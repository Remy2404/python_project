import heapq

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = {}

    def add_edge(self, start, end, distance):
        self.add_vertex(start)
        self.add_vertex(end)
        self.vertices[start][end] = distance
        self.vertices[end][start] = distance  # Assuming undirected graph

    def display_connections(self):
        for vertex, neighbors in self.vertices.items():
            print(f"{vertex}: {neighbors}")

    def prim_mst(self, start):
        mst = []
        visited = {start}
        edges = [(cost, start, to) for to, cost in self.vertices[start].items()]
        heapq.heapify(edges)

        while edges:
            cost, frm, to = heapq.heappop(edges)
            if to not in visited:
                visited.add(to)
                mst.append((frm, to, cost))
                for next_to, next_cost in self.vertices[to].items():
                    if next_to not in visited:
                        heapq.heappush(edges, (next_cost, to, next_to))

        return mst

# Create graph and add edges
cambodia_graph = Graph()

# Adding edges based on the provided data
cambodia_graph.add_edge("Phnom Penh", "Angkor Wat", 321)
cambodia_graph.add_edge("Phnom Penh", "Bokor", 189)
cambodia_graph.add_edge("Phnom Penh", "Kirirum", 117)
cambodia_graph.add_edge("Phnom Penh", "Kampot", 148)
cambodia_graph.add_edge("Phnom Penh", "Krong Kep", 174)
cambodia_graph.add_edge("Phnom Penh", "Sihanoukville", 230)
cambodia_graph.add_edge("Phnom Penh", "Kampong Chnang", 91)
cambodia_graph.add_edge("Phnom Penh", "Pursat", 189)
cambodia_graph.add_edge("Phnom Penh", "Battambong", 291)
cambodia_graph.add_edge("Phnom Penh", "Pailin", 371)
cambodia_graph.add_edge("Phnom Penh", "Banteay Meanchey", 359)
cambodia_graph.add_edge("Phnom Penh", "Siem Reap", 314)
cambodia_graph.add_edge("Phnom Penh", "Kampong Thom", 167)
cambodia_graph.add_edge("Phnom Penh", "Kampong Cham", 124)
cambodia_graph.add_edge("Phnom Penh", "Prey Veng", 90)
cambodia_graph.add_edge("Phnom Penh", "Svay Rieng", 122)
cambodia_graph.add_edge("Phnom Penh", "Takeo", 78)
cambodia_graph.add_edge("Phnom Penh", "Kandal", 11)
cambodia_graph.add_edge("Phnom Penh", "Kampong Speu", 48)
cambodia_graph.add_edge("Phnom Penh", "Kratie", 315)
cambodia_graph.add_edge("Phnom Penh", "Steong Treng", 455)
cambodia_graph.add_edge("Phnom Penh", "Mondol Kiri", 521)
cambodia_graph.add_edge("Phnom Penh", "Preah Vihear", 294)
cambodia_graph.add_edge("Phnom Penh", "Ratanakiri", 588)
cambodia_graph.add_edge("Phnom Penh", "Koh Kong", 271)
cambodia_graph.add_edge("Phnom Penh", "Oddar Meanchey", 469)

print("Connections between provinces:")
cambodia_graph.display_connections()

print("\nMinimum Spanning Tree (starting from Phnom Penh):")
mst = cambodia_graph.prim_mst("Phnom Penh")

for edge in mst:
    print(f"{edge[0]} - {edge[1]}: {edge[2]} km")

total_distance = sum(edge[2] for edge in mst)
print(f"\nTotal minimum distance to connect all provinces: {total_distance} km")