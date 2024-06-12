# Import libraries
import matplotlib.pyplot as plt
import seaborn as sns

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

# Create a figure with 3 subplots
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))

# Plot a histogram on the first subplot
sns.histplot(bmi_data, ax=ax1, kde=True, color='skyblue')  # Added KDE for better distribution visualization
ax1.set_title('Histogram of BMI')
ax1.set_xlabel('BMI')
ax1.set_ylabel('Frequency')

# Plot a box plot on the second subplot
sns.boxplot(y=bmi_data, ax=ax2, color='lightgreen')  # Changed x to y for vertical boxplot
ax2.set_title('Box plot of BMI')
ax2.set_xlabel('')
ax2.set_ylabel('BMI')

# Plot a strip plot on the third subplot
sns.stripplot(y=bmi_data, ax=ax3, color='salmon')  # Changed x to y for vertical stripplot
ax3.set_title('Dot plot of BMI')
ax3.set_xlabel('')
ax3.set_ylabel('BMI')

# Adjust layout to prevent clipping of titles
plt.tight_layout()

# Show the figure
plt.show()
