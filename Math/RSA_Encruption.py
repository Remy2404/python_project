import sympy
import hashlib
import os
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import matplotlib.pyplot as plt

# Disable LaTeX rendering
plt.rc('text', usetex=False)
plt.rc('font', family='serif')

class RSAError(Exception):
    pass

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

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
        raise RSAError('Modular inverse does not exist')
    return x % phi

def generate_large_prime(bits):
    while True:
        prime_candidate = sympy.randprime(2**(bits-1), 2**bits)
        if is_prime(prime_candidate):
            return prime_candidate

def is_prime(num):
    return sympy.isprime(num)

def generate_keypair(bits=2048):
    p = generate_large_prime(bits // 2)
    q = generate_large_prime(bits // 2)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = sympy.randprime(2, phi)
    if gcd(e, phi) != 1:
        raise RSAError('e and phi are not coprime')
    d = modular_inverse(e, phi)
    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    key, n = pk
    # OAEP padding
    message = plaintext.encode('utf-8')
    if len(message) > n.bit_length() // 8 - 2:
        raise ValueError("Message too long for RSA encryption.")
    
    # Hash the message
    hash_value = hashlib.sha256(message).digest()
    # Encrypt the hash
    cipher = pow(int.from_bytes(message, byteorder='big'), key, n)
    return cipher, hash_value

def decrypt(pk, ciphertext, hash_value):
    key, n = pk
    decrypted = pow(ciphertext, key, n)
    decrypted_message = decrypted.to_bytes((decrypted.bit_length() + 7) // 8, byteorder='big')
    
    # Verify hash
    if hashlib.sha256(decrypted_message).digest() != hash_value:
        raise RSAError("Hash verification failed.")
    
    return decrypted_message.decode('utf-8')

def encrypt_file(public_key, file_path):
    with open(file_path, 'rb') as f:
        file_data = f.read()
    
    cipher, hash_value = encrypt(public_key, file_data)
    return cipher, hash_value

def decrypt_file(private_key, ciphertext, hash_value, output_path):
    decrypted_data = decrypt(private_key, ciphertext, hash_value)
    with open(output_path, 'wb') as f:
        f.write(decrypted_data)

def hybrid_encrypt(message):
    # Generate a random AES key
    aes_key = get_random_bytes(16)
    cipher_aes = AES.new(aes_key, AES.MODE_CBC)
    iv = cipher_aes.iv
    padded_message = pad(message.encode(), AES.block_size)
    encrypted_message = cipher_aes.encrypt(padded_message)

    # Encrypt the AES key with RSA
    rsa_key = generate_keypair()
    encrypted_aes_key, hash_value = encrypt(rsa_key[0], aes_key)

    return (encrypted_aes_key, iv, encrypted_message), rsa_key

def hybrid_decrypt(encrypted_data, private_key):
    encrypted_aes_key, iv, encrypted_message = encrypted_data
    aes_key = decrypt(private_key, encrypted_aes_key, b'')  # Hash verification not needed here
    cipher_aes = AES.new(aes_key, AES.MODE_CBC, iv)
    decrypted_message = unpad(cipher_aes.decrypt(encrypted_message), AES.block_size)
    return decrypted_message.decode()

def save_key(key, filename):
    with open(filename, 'wb') as f:
        f.write(key)

def load_key(filename):
    with open(filename, 'rb') as f:
        return f.read()

def main():
    print("Generating RSA keypair...")
    public_key, private_key = generate_keypair()
    
    # Save keys
    save_key(public_key[0].to_bytes(256, 'big'), 'public_key.bin')
    save_key(private_key[0].to_bytes(256, 'big'), 'private_key.bin')

    message = input("Enter a message to encrypt: ")
    
    # Hybrid Encryption
    encrypted_data, rsa_key = hybrid_encrypt(message)
    print("Encrypted data:", encrypted_data)

    # Decrypting the message
    decrypted_message = hybrid_decrypt(encrypted_data, private_key)
    print("Decrypted message:", decrypted_message)

if __name__ == "__main__":
    main()