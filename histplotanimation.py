# Import libraries
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.animation import FuncAnimation

# Define data
bmi_data = [
     20.04744562, 26.57312925, 20.32443826, 20.2812331, 17.99816345, 22.65625,
    22.03856749, 28.40909091, 15.78083575, 23.30905307, 18.31425598, 18.71094925,
    20.2020202, 22.85714286, 19.15158479, 18.93877551, 27.6816609, 23.38868656,
    17.63085399, 17.63085399, 16.97600724, 22.58270917, 17.57706869, 26.57312925,
    19.83471074, 20.76124567, 18.67093431, 18.93877551, 21.2585034, 29.06592681,
    16.14152893, 19.37716263, 16.16161616, 17.28395062, 17.95918367, 22.34351559,
    20.51913409, 20.54988662, 30.48315806, 23.1206236, 16.80613424, 15.49586777,
    20.04744562, 22.03856749, 15.94387755, 14.69237833, 20.24489796, 22.22906193,
    16.91723323, 16.00365798, 28.47988608, 24.1671624, 17.16550669, 25.59373706,
    15.49586777, 20.06920415, 15.58956916, 16.32653061, 18.19548277, 26.57312925,
    19.26717144, 20.24489796, 20.80856124
]

# Generate random data for height and weight
np.random.seed(42)  # Adding seed for reproducibility
height_data = np.random.normal(170, 10, len(bmi_data))  # mean = 170 cm, std = 10 cm
weight_data = np.random.normal(70, 15, len(bmi_data))  # mean = 70 kg, std = 15 kg

# Create a figure
fig, ax = plt.subplots(figsize=(10, 10))

# Set the title and labels
ax.set_title('BMI vs Height and Weight')
ax.set_xlabel('Height (cm)')
ax.set_ylabel('Weight (kg)')

# Set the color map based on BMI values
cmap = sns.color_palette('RdYlGn', as_cmap=True)
colors = cmap(np.array(bmi_data) / max(bmi_data))  # Convert bmi_data to a numpy array

# Plot the initial scatter plot
scatter = sns.scatterplot(x=height_data, y=weight_data, hue=bmi_data, palette='viridis', s=bmi_data, sizes=(50, 200), ax=ax)
ax.legend(title='BMI', loc='upper left', bbox_to_anchor=(1.05, 1))

# Add a color bar
fig.colorbar(scatter, ax=ax, label='BMI')

# Add some text
avg_bmi = np.mean(bmi_data)
avg_height = np.mean(height_data)
avg_weight = np.mean(weight_data)
ax.text(0.05, 0.95, f'Average BMI: {avg_bmi:.2f}', transform=ax.transAxes, fontsize=14)
ax.text(0.05, 0.90, f'Average Height: {avg_height:.2f} cm', transform=ax.transAxes, fontsize=14)
ax.text(0.05, 0.85, f'Average Weight: {avg_weight:.2f} kg', transform=ax.transAxes, fontsize=14)

def update(frame):
    # Update the data (for example, add some noise to height and weight values)
    updated_height = height_data + np.random.normal(0, 1, len(bmi_data)) * (frame + 1)
    updated_weight = weight_data + np.random.normal(0, 2, len(bmi_data)) * (frame + 1)

    # Update the scatter plot
    scatter.set_offsets(np.column_stack((updated_height, updated_weight)))
    scatter.set_sizes(50 + 4 * bmi_data)  # Adjust size based on BMI

# Set up the animation
animation = FuncAnimation(fig, update, frames=30, interval=200, blit=False)

# Save the animation as GIF
animation.save('animated_bmi_scatter.gif', writer='pillow')

# Show the animation
plt.show()
