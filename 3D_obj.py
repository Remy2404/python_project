import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.animation import FuncAnimation

# Define cube vertices
vertices = np.array([[0, 0, 0],
                      [1, 0, 0],
                      [1, 1, 0],
                      [0, 1, 0],
                      [0, 0, 1],
                      [1, 0, 1],
                      [1, 1, 1],
                      [0, 1, 1]])

# Define cube faces
faces = [[vertices[0], vertices[1], vertices[2], vertices[3]],
         [vertices[4], vertices[5], vertices[6], vertices[7]],
         [vertices[0], vertices[1], vertices[5], vertices[4]],
         [vertices[2], vertices[3], vertices[7], vertices[6]],
         [vertices[1], vertices[2], vertices[6], vertices[5]],
         [vertices[4], vertices[7], vertices[3], vertices[0]]]

# Create a figure and axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Initialize the cube
cube = Poly3DCollection(faces, facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25)
ax.add_collection3d(cube)

# Define the update function for the animation
def update(angle):
    ax.view_init(elev=20, azim=angle)
    return cube,

# Create the animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 360, 2), interval=50, blit=True)

plt.show()
