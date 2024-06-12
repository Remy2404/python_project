import graphviz as pgv
import matplotlib.pyplot as plt

# Create a new graph
graph = pgv.Digraph(strict=True)

# Define the nodes and add them to the graph
start = graph.node("Start")
process = graph.node("Perform calculation")
decision = graph.node("Is result correct?")
output_yes = graph.node("Display result")
output_no = graph.node("Error message")
end = graph.node("End")

# Define the edges and add them to the graph
graph.edge(start, process)
graph.edge(process, decision)
graph.edge(decision, output_yes, label='Yes')
graph.edge(decision, output_no, label='No')
graph.edge(output_yes, end)
graph.edge(output_no, process)

# Set plot parameters for visualization
plt.figure(figsize=(8, 6))
layout = graph.pipe(format='png')

# Plot the graph
plt.title("Flowchart")
plt.axis('off')
plt.tight_layout()
plt.subplots_adjust(top=1.4)
plt.margins(0)
plt.imshow(layout, aspect='equal')

# Show the flowchart
plt.show()