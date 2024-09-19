import matplotlib.pyplot as plt
from scipy.stats import binom
import numpy as np
# Parameters
n = 35
p = 0.1
k = 10
# Calculate the cumulative probability of having 10 or fewer
cumulative_prob = binom.cdf(k, n, p)
# The probability of having more than 10 active users
prob_more_than_10 = 1 - cumulative_prob
# Print the probability
print(f"Probability of more than 10 active users: {prob_more_than_10:.4f}")
# Generate data for plotting
x = np.arange(0, n+1)
y = binom.pmf(x, n, p)
# Create a colormap
colors = plt.cm.viridis(np.linspace(0, 1, n+1))
# Plot the probability mass function with different colors
plt.figure(figsize=(10, 6))
for i in range(n+1):
    plt.bar(x[i], y[i], color=colors[i], alpha=0.7)
plt.axvline(x=k, color='red', linestyle='--', label=f'k={k}')
plt.xlabel("Number of Active Users")
plt.ylabel('Probability')
plt.title('Binomial Distribution of Active Users')
plt.legend()
plt.grid(True)
# Save the plot as an image file
plt.savefig('binomial_distribution_colored.png')
# Show the plot
plt.show()