from scipy.stats import norm

# Define the z-scores
z1 = 0.71
z2 = 1.28

# Calculate the area to the left of each z-score using the standard normal distribution function (norm.cdf)
area_left_z1 = norm.cdf(z1)
area_left_z2 = norm.cdf(z2)

# The area between z1 and z2 is the difference between the areas to the left of each z-score
area_between = area_left_z2 - area_left_z1

# Print the area between z1 and z2
print("Area between z = {:.2f} and z = {:.2f}: {:.4f}".format(z1, z2, area_between))
