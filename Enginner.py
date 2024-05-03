import numpy as np

# Sample data (torque needed to break bolts)
data_1 = [107, 109, 111, 113, 113, 114, 114, 115, 117, 119, 122, 124]
data_2 = [108, 110, 112, 114, 114, 115, 115, 116, 118, 120, 123, 140]

def calculate_statistics(data):
  sample_mean = np.mean(data)
  sample_std = np.std(data, ddof=1)  # Use ddof=1 for unbiased sample standard deviation
  return sample_mean, sample_std
def proportion_below_threshold(mean, std, threshold):
 
  from scipy.stats import norm
  z_score = (threshold - mean) / std
  proportion = norm.cdf(z_score)
  return proportion

sample_mean_1, sample_std_1 = calculate_statistics(data_1)
proportion_less_than_100_1 = proportion_below_threshold(sample_mean_1, sample_std_1, 100)

sample_mean_2, sample_std_2 = calculate_statistics(data_2)
proportion_less_than_100_2 = proportion_below_threshold(sample_mean_2, sample_std_2, 100)

acceptance_threshold = 0.01  # Less than 1% of bolts can have breaking torque less than 100 J

print("Sample 1:")
print(f"  Mean torque: {sample_mean_1:.2f} J")
print(f"  Standard deviation: {sample_std_1:.2f} J")
print(f"  Proportion less than 100 J: {proportion_less_than_100_1:.4f}")
print(f"  Shipment accepted: {'Yes' if proportion_less_than_100_1 < acceptance_threshold else 'No'}")

print("\nSample 2:")
print(f"  Mean torque: {sample_mean_2:.2f} J")
print(f"  Standard deviation: {sample_std_2:.2f} J")
print(f"  Proportion less than 100 J: {proportion_less_than_100_2:.4f}")
print(f"  Shipment accepted: {'Yes' if proportion_less_than_100_2 < acceptance_threshold else 'No'}")

# Comparison
print("\nComparison:")
if sample_mean_1 > sample_mean_2:
  print("  Sample 1 bolts are stronger.")
elif sample_mean_1 < sample_mean_2:
  print("  Sample 2 bolts are stronger.")
else:
  print("  Samples have the same average strength.")

# Method validity
print("\nMethod validity:")
print("  The method assumes a normal population distribution.")
print("  For sample 1, the assumption may be reasonable based on the data spread.")
print("  For sample 2, the presence of an outlier (140 J) might violate the normality assumption.")
print("  Therefore, the method may be less reliable for sample 2.")