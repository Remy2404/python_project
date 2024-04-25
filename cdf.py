import pygraphviz as pgv
import matplotlib.pyplot as plt

# Create a new graph
graph = pgv.AGraph(directed=True, strict=True)

# Define the nodes and add them to the graph
start = graph.add_node("Start")
process = graph.add_node("Perform calculation")
decision = graph.add_node("Is result correct?")
output_yes = graph.add_node("Display result")
output_no = graph.add_node("Error message")
end = graph.add_node("End")

# Define the edges and add them to the graph
graph.add_edge(start, process)
graph.add_edge(process, decision)
graph.add_edge(decision, output_yes, label='Yes')
graph.add_edge(decision, output_no, label='No')
graph.add_edge(output_yes, end)
graph.add_edge(output_no, process)

# Set plot parameters for visualization
plt.figure(figsize=(8, 6))
layout = graph.layout(prog='dot')

# Plot the graph
plt.title("Flowchart")
plt.axis('off')
plt.tight_layout()
plt.subplots_adjust(top=1.4)
plt.margins(0)
plt.plot(layout, with_labels=True, node_size=0)

# Show the flowchart
plt.show()