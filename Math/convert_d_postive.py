def convert_to_positive(d, m):
    """Convert a negative modular inverse to its positive equivalent."""
    return d % m

# Example usage
d = -4
m = 21

positive_d = convert_to_positive(d, m)
print(f"The positive equivalent of {d} modulo {m} is: {positive_d}")