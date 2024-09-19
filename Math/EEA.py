def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def modular_inverse(e, phi):
    gcd, x, y = extended_gcd(e, phi)
    if gcd != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % phi

def input_inverse():
    e = int(input("Enter the value of e: "))
    phi = int(input("Enter the value of phi: "))
    return e, phi


# Example to find the modular inverse of 5 modulo 21
e = 50
phi = 5788811
inverse = modular_inverse(e, phi)
print(f"The modular inverse of {e} modulo {phi} is {inverse}")

# Verify the result
print(f"Verification: {e} * {inverse} % {phi} = {(e * inverse) % phi}")
