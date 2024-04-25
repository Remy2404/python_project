import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # Import seaborn for color palettes

# Create a DataFrame with your BMI, Height, and Weight data
data = {
    'BMI': [
        16.97959184, 26.57312925, 20.32443826, 20.2812331, 17.99816345,
        22.65625, 22.03856749, 28.40909091, 15.78083575, 23.30905307,
        18.31425598, 18.71094925, 20.2020202, 22.85714286, 19.15158479,
        18.93877551, 27.6816609, 23.38868656, 17.63085399, 17.63085399,
        16.97600724, 22.58270917, 17.57706869, 26.57312925, 19.83471074,
        20.76124567, 18.67093431, 18.93877551, 21.2585034, 29.06592681,
        16.14152893, 19.37716263, 16.16161616, 17.28395062, 17.95918367,
        22.34351559, 20.51913409, 20.54988662, 30.48315806, 23.1206236,
        16.80613424, 15.49586777, 20.04744562, 22.03856749, 15.94387755,
        14.69237833, 20.24489796, 22.22906193, 16.91723323, 16.00365798,
        28.47988608, 24.1671624, 17.16550669, 25.59373706, 15.49586777,
        20.06920415, 15.58956916, 16.32653061, 18.19548277, 26.57312925,
        19.26717144, 20.24489796, 20.80856124
    ],
    'Height': [
        1.75, 1.68, 1.63, 1.72, 1.65, 1.6, 1.65, 1.76, 1.78, 1.55,
        1.55, 1.73, 1.65, 1.75, 1.77, 1.75, 1.7, 1.73, 1.65, 1.65,
        1.88, 1.63, 1.72, 1.68, 1.65, 1.7, 1.62, 1.75, 1.68, 1.74,
        1.76, 1.7, 1.65, 1.8, 1.75, 1.77, 1.71, 1.68, 1.62, 1.74,
        1.69, 1.76, 1.73, 1.65, 1.68, 1.65, 1.75, 1.71, 1.77, 1.62,
        1.59, 1.64, 1.79, 1.63, 1.76, 1.7, 1.68, 1.75, 1.59, 1.68,
        1.72, 1.75, 1.74
    ],
    'Weight': [
        52, 75, 54, 60, 49, 58, 60, 88, 50, 56, 44, 56, 55, 70, 60, 58,
        80, 70, 48, 48, 60, 60, 52, 75, 54, 60, 49, 58, 60, 88, 50, 56,
        44, 56, 55, 70, 60, 58, 80, 70, 48, 48, 60, 60, 45, 40, 62, 65,
        53, 42, 72, 65, 55, 68, 48, 58, 44, 50, 46, 75, 57, 62, 63
    ]
}

df = pd.DataFrame(data)

# Categorize BMI
df['Categorize BMI'] = pd.cut(df['BMI'],
    bins=[-float('inf'), 16, 17, 18.5, 25, 30, 35, 40, float('inf')],
    labels=['Severe Thinness', 'Moderate Thinness', 'Mild Thinness', 'Normal', 'Overweight', 'Obese Class I', 'Obese Class II', 'Obese Class III']
)

# Count the occurrences of each category
category_counts = df['Categorize BMI'].value_counts()

# Define a color palette for the BMI categories
palette = sns.color_palette("viridis", n_colors=len(category_counts))

# Create a bar chart with plot area, labels, and color
fig, ax = plt.subplots(figsize=(12, 6))

bars = ax.bar(category_counts.index, category_counts.values, color=palette)

# Add labels for height and weight on each bar
for bar, height, weight in zip(bars, df['Height'], df['Weight']):
    ax.text(bar.get_x() + bar.get_width() / 2 - 0.1, bar.get_height() + 0.1, f'Height: {height}\nWeight: {weight}', ha='center', color='black', weight='bold')

# Set plot area labels
ax.set_title('BMI Category Distribution with Height and Weight')
ax.set_xlabel('BMI Categories')
ax.set_ylabel('Count')

# Display the chart
plt.show()
