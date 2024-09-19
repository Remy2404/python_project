def modular_exponentiation(base, exponent, modulus):
    """Compute (base^exponent) mod modulus using modular exponentiation."""
    result = 1
    base = base % modulus  # Handle base larger than modulus

    while exponent > 0:
        # If exponent is odd, multiply base with result
        if (exponent % 2) == 1:
            result = (result * base) % modulus
        
        # Now exponent must be even
        exponent = exponent // 2
        base = (base * base) % modulus  # Square the base

    return result

# Example usage
x = 2
n = 4
m = 260

result = modular_exponentiation(x, n, m)
print(f"{x}^{n} mod {m} = {result}")