from collections import defaultdict, deque

graph = defaultdict(list)

def add_undirected_edge(graph, u, v):
    graph[u].append(v)
    graph[v].append(u)

def draw_adjacency_list(graph):
    for node in graph:
        print(f"{node}: {', '.join(map(str, graph[node]))}")

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    bfs_order = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            bfs_order.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
    
    return bfs_order

# Part a: Create adjacency list for the undirected graph
add_undirected_edge(graph, 0, 1)
add_undirected_edge(graph, 0, 2)
add_undirected_edge(graph, 0, 3)
add_undirected_edge(graph, 1, 4)
add_undirected_edge(graph, 2, 3)
add_undirected_edge(graph, 3, 4)

# Print adjacency list
print("Adjacency List for the Undirected Graph:")
draw_adjacency_list(graph)

# Part b: Execute BFS starting from node 3
bfs_result = bfs(graph, 3)
print("\nBFS starting from node 3:", bfs_result)

# Part c: Complete execution of BFS code
print("\nComplete BFS Execution:")
print(bfs(graph, 3))
