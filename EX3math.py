import numpy as np
import matplotlib.pyplot as plt

# Define the equations in the form ax + by = c
def equation1(x):
    return (x + 3) / 2

def equation2(x):
    return (3*x + 3) / 6

# Generate x values
x_values = np.linspace(-5, 5, 100)

# Plot the lines
plt.plot(x_values, equation1(x_values), label='x - 2y = -3')
plt.plot(x_values, equation2(x_values), label='-3x + 6y = 1')

# Add labels and legend
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt._draw_all_if_interactive()

# Show the plot
plt.show()
