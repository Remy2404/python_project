def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Example usage
num1 = 50
num2 = 5815841

result = gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is: {result}")
