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