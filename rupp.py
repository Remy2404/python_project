import numpy as np
import matplotlib.pyplot as plt

# Define score parameters
average_score = 650
standard_deviation = 100
max_possible_score = 800

# Simulate scores from a truncated normal distribution (optional)
# You can replace this with actual score data if available
np.random.seed(10)  # Set seed for reproducibility
truncated_scores = np.random.normal(loc=average_score, scale=standard_deviation, size=1000)  # Simulate 1000 scores
truncated_scores = np.clip(truncated_scores, a_min=0, a_max=max_possible_score)  # Truncate at max score

# Analyze the distribution
plt.hist(truncated_scores, bins=20, density=True, label='Truncated Normal Distribution')  # Plot histogram

# Optional: Plot theoretical normal distribution (considering full range)
x = np.linspace(average_score - 3*standard_deviation, average_score + 3*standard_deviation, 1000)  # Extend beyond max score for visualization
normal_dist = np.exp(-(x - average_score)**2 / (2*standard_deviation**2)) / (standard_deviation * np.sqrt(2*np.pi))
plt.plot(x, normal_dist, label='Normal Distribution (Full Range)')

# Customize plot
plt.xlabel('Math Score')
plt.ylabel('Probability Density')
plt.title('Distribution of RUPP Math Scores (Truncated at 800)')
plt.legend()
plt.grid(True)
plt.show()

# Additional analysis (optional)
# 1. Calculate descriptive statistics (mean, median, standard deviation) of the truncated scores using functions like np.mean, np.median, np.std

# 2. Explore alternative distributions like the beta distribution using libraries like `scipy.stats`
