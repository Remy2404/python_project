import matplotlib.pyplot as plt
import numpy as np

# Generate some random data
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

# Try converting BMI data into numerics before plotting the distribution
try:
  # If it is string type, remove all characters except numbers, ".", "+" or "-".
  if pd.api.types.is_string_dtype(bmi_data):
    for i in range(len(bmi_data)):
      bmi_data.iloc[i] = re.sub(r"[^\d\-+\.]", "", bmi_data.iloc[i])
  bmi_data = pd.to_numeric(bmi_data)
except:
  pass

# Plot the distribution of the BMI data
plt.hist(bmi_data)
plt.xlabel('BMI')
plt.ylabel('Number of people')
plt.title('Distribution of BMI data')
plt.show()