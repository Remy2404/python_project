import numpy as np
import matplotlib.pyplot as plt

# Define the function f(Y) = Y - t
def f(Y, t):
    return Y - t

# Create a grid of t and Y values
t = np.linspace(-4, 4, 20)
Y = np.linspace(-4, 4, 20)
T, Y = np.meshgrid(t, Y)

# Calculate the derivatives for the vector field
dT = np.ones_like(T)
dY = f(Y, T)

# Plot the vector field
plt.quiver(T, Y, dT, dY, color='red', scale=10)

# Plot the curve (1/3) * (3 - np.exp(t) + 3 * t)
curve_t = np.linspace(-4, 4, 100)
curve_Y = (1/3) * (3 - np.exp(curve_t) + 3 * curve_t)
plt.plot(curve_t, curve_Y, color='blue')

# Set labels and show the plot
plt.xlabel('t')
plt.ylabel('Y')
plt.grid()
plt.show()
