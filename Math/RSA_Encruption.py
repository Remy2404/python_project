import sympy
import matplotlib.pyplot as plt
from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox

# Disable LaTeX rendering
plt.rc('text', usetex=False)
plt.rc('font', family='serif')

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

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

def generate_keypair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = sympy.randprime(2, phi)
    if gcd(e, phi) != 1:
        raise Exception('e and phi are not coprime')
    d = modular_inverse(e, phi)
    return ((e, n), (d, n))

def display_keys(public_key, private_key):
    print("Public Key:")
    print(f"  e (public exponent): {public_key[0]}")
    print(f"  n (modulus): {public_key[1]}")
    print("Private Key:")
    print(f"  d (private exponent): {private_key[0]}")
    print(f"  n (modulus): {private_key[1]}")
    print()

def encrypt(pk, plaintext):
    key, n = pk
    number_representation = [ord(char) for char in plaintext]
    cipher = [pow(num, key, n) for num in number_representation]
    return cipher

def decrypt(pk, ciphertext):
    key, n = pk
    plain = [chr(pow(num, key, n)) for num in ciphertext]
    return ''.join(plain)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_large_prime(bits):
    while True:
        prime_candidate = sympy.randprime(2**(bits-1), 2**bits)
        if is_prime(prime_candidate):
            return prime_candidate

def display_encrypted_decrypted(encrypted_msg, decrypted_msg):
    print("Encrypted message (in hex):")
    print(" ".join([hex(num) for num in encrypted_msg]))
    print("Decrypted message:")
    print(decrypted_msg)
    print()

def display_rsa_process_plain(p, q, public, private, message, encrypted_msg, decrypted_msg):
    fig, ax = plt.subplots(figsize=(12, 10))
    ax.axis('off')

    steps = [
        "1. Choose two distinct prime numbers p and q.",
        f"   p = {p}, q = {q}",
        "2. Compute n = p * q.",
        f"   n = {p} * {q} = {p * q}",
        "3. Compute the totient phi = (p - 1) * (q - 1).",
        f"   phi = ({p} - 1) * ({q} - 1) = {(p - 1) * (q - 1)}",
        "4. Choose an integer e such that 1 < e < phi and gcd(e, phi) = 1.",
        f"   e = {public[0]}",
        "5. Compute d as the modular multiplicative inverse of e modulo phi.",
        f"   d = {private[0]}",
        "6. The public key is (e, n) and the private key is (d, n).",
        f"   Public Key: (e = {public[0]}, n = {public[1]})",
        f"   Private Key: (d = {private[0]}, n = {private[1]})",
        "7. To encrypt a message, convert the message to a number representation.",
        f"   Message: {message}",
        f"   Number representation: {[ord(char) for char in message]}",
        "8. Encrypt each number using the public key (e, n).",
        f"   Encrypted message: {encrypted_msg}",
        "9. To decrypt the message, use the private key (d, n).",
        f"   Decrypted message: {decrypted_msg}"
    ]

    text = '\n'.join(steps)
    ax.text(0.05, 0.95, text, fontsize=12, va='top', ha='left', transform=ax.transAxes, wrap=True)

    plt.tight_layout()
    plt.show()

def main():
    # Input prime numbers p and q
    p = int(input("Enter the first prime number (p): "))
    q = int(input("Enter the second prime number (q): "))

    if not (is_prime(p) and is_prime(q)):
        print("Error: Both numbers must be prime.")
        return

    print(f"Chosen primes: p = {p}, q = {q}")
    print("Generating keypair...")

    public, private = generate_keypair(p, q)

    display_keys(public, private)

    message = input("Enter a message to encrypt: ")
    encrypted_msg = encrypt(public, message)
    decrypted_msg = decrypt(private, encrypted_msg)

    display_encrypted_decrypted(encrypted_msg, decrypted_msg)
    display_rsa_process_plain(p, q, public, private, message, encrypted_msg, decrypted_msg)

if __name__ == "__main__":
    main()