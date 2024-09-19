def extended_gcd(a, b):
    """Return GCD of a and b along with coefficients x and y such that ax + by = gcd(a, b)"""
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def modular_inverse(a: object, m):
    """Return the modular inverse of a modulo m, if it exists."""
    gcd, x, _ = extended_gcd(a, m)
    if gcd != 1:
        raise ValueError(f"No modular inverse exists for {a} modulo {m}")
    else:
        # x may be negative, convert it to a positive equivalent
        return x % m

# Example usage
a = 5
m = 21

try:
    inverse = modular_inverse(a, m)
    print(f"The modular inverse of {a} modulo {m} is: {inverse}")
except ValueError as e:
    print(e)