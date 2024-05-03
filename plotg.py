import matplotlib.pyplot as plt
import numpy as np  # Import numpy library and assign alias 'np'
from scipy.stats import norm

# Define function for normal distribution (optional for visualization)
def normal_distribution(x, mu, sigma):
  return norm.pdf(x, loc=mu, scale=sigma)

# Set parameters for the normal distribution
mu = 0  # Mean
sigma = 1  # Standard deviation

# Define x-axis values for plotting
x = np.linspace(-5, 5, 1000)  # Adjust range as needed

# Calculate y-axis values for the normal distribution (optional for visualization)
y = normal_distribution(x, mu, sigma)

# Plot the normal distribution curve (optional for visualization)
plt.plot(x, y, label='Normal Distribution')

# Calculate areas under the curve for different cases
def area_under_curve(z_lower, z_upper):
  # Use scipy.stats.norm.cdf for cumulative distribution function
  if z_lower < z_upper:
    area = norm.cdf(z_upper, loc=mu, scale=sigma) - norm.cdf(z_lower, loc=mu, scale=sigma)
  else:
    # Handle case where upper bound is less than lower bound (area in tail)
    area = 1 - norm.cdf(z_upper, loc=mu, scale=sigma) + norm.cdf(z_lower, loc=mu, scale=sigma)
  return area

# Example calculations (replace with your specific cases from previous question)
area_right_tail = area_under_curve(-0.85, float('inf'))  # To the right of z = -0.85
area_between = area_under_curve(-2.93, -2.06)  # Between z = -2.93 and z = -2.06
area_middle = area_under_curve(-0.30, 0.90)  # Between z = -0.30 and z = 0.90
area_outside = 1 - area_under_curve(0.96, 1.62)  # Outside z = 0.96 to z = 1.62

# Print the calculated areas
print("Area to the right of z = -0.85:", area_right_tail)
print("Area between z = -2.93 and z = -2.06:", area_between)
print("Area between z = -0.30 and z = 0.90:", area_middle)
print("Area outside z = 0.96 to z = 1.62:", area_outside)

# Show the plot (optional for visualization)
plt.xlabel('z-scores')
plt.ylabel('Probability Density')
plt.title('Normal Distribution (μ=0, σ=1)')
plt.legend()
plt.grid(True)
plt.show()
