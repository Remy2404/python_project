import matplotlib.pyplot as plt
import numpy as np

# BMI values
bmi_values = [
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
]

# Corresponding index values for the x-axis
indices = list(range(1, len(bmi_values) + 1))

# Plotting the BMI values as a line graph
plt.plot(indices, bmi_values, marker='o', linestyle='-', color='b', label='BMI Values')

# Adding shaded regions for BMI categories
categories = {
    'Severe Thinness': (0, 16, 'gray'),
    'Moderate Thinness': (16, 17, 'orange'),
    'Mild Thinness': (17, 18.5, 'yellow'),
    'Normal': (18.5, 25, 'green'),
    'Overweight': (25, 30, 'yellow'),
    'Obese Class I': (30, 35, 'orange'),
    'Obese Class II': (35, 40, 'red'),
    'Obese Class III': (40, 50, 'darkred'),
}

for category, (lower, upper, color) in categories.items():
    plt.fill_between(indices, lower, upper, color=color, alpha=0.3, label=category)

# Statistical information
mean_value = 20.37193233
std_error_value = 0.483598872
median_value = 20.04744562
std_dev_value = 3.838447051
sample_var_value = 14.73367577
range_value = 15.79077973
sum_value = 1283.431737
count_value = 63

# Adding statistical information to the graph
info_text = f'''
Mean: {mean_value:.2f}
Standard Error: {std_error_value:.2f}
Median: {median_value:.2f}
Standard Deviation: {std_dev_value:.2f}
Sample Variance: {sample_var_value:.2f}
Range: {range_value:.2f}
Sum: {sum_value:.2f}
Count: {count_value}
'''
plt.gcf().text(0.02, 0.02, info_text, fontsize=10, ha='left', va='bottom')

# Adding labels and title
plt.xlabel('Index')
plt.ylabel('BMI')
plt.title('BMI Values with Categories and Statistical Information')

# Adding legend
plt.legend()

# Display the plot
plt.show()
