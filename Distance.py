import matplotlib.pyplot as plt
import numpy as np

# Define the points
points = np.array([[-1, 0], [-1, -1], [4, 1], [2, 0.5], [3.5, 2],
                   [3, 1.5], [-1.5, 4], [5.5, 4]])

# Function to calculate distance between two points
def distance(p1, p2):
    return np.sqrt(np.sum((p1 - p2)**2))

# Find the farthest points
farthest_distance = 0
farthest_pair = None
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        current_distance = distance(points[i], points[j])
        if current_distance > farthest_distance:
            farthest_distance = current_distance
            farthest_pair = (points[i], points[j])

# Extract the farthest points
p1, p2 = farthest_pair

# Plot the points and the line connecting the farthest points
plt.scatter(points[:, 0], points[:, 1], label='Points')
plt.plot([p1[0], p2[0]], [p1[1], p2[1]], color='red', label='Farthest Points')

# Label the axes and add a title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Farthest Points Visualization')



# Add legend
plt.legend()

# Show the plot
plt.grid(True)
plt.show()

print("Farthest Points:", p1, "and", p2)
print("Distance:", farthest_distance)