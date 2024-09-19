def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def mod_inverse(e, phi):
    gcd, x, y = extended_gcd(e, phi)
    if gcd != 1:
        raise Exception("Modular inverse does not exist")
    else:
        return x % phi

def rsa_encrypt(message, e, n):
    return pow(message, e, n)

def rsa_decrypt(ciphertext, d, n):
    return pow(ciphertext, d, n)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def factorize():
    n = int(input("Enter a number to factorize: "))
    factors = prime_factors(n)
    print(f"The prime factors of {n} are: {factors}")

def rsa_algorithm():
    # User input for prime numbers p and q
    while True:
        p = int(input("Enter a prime number p: "))
        if is_prime(p):
            break
        print("Error: p is not prime. Please try again.")

    while True:
        q = int(input("Enter a prime number q: "))
        if is_prime(q):
            break
        print("Error: q is not prime. Please try again.")

    # Calculate n
    n = p * q
    print(f"n = p * q = {n}")

    # Calculate phi(n)
    phi_n = (p - 1) * (q - 1)
    print(f"phi(n) = (p - 1) * (q - 1) = {phi_n}")

    # User input for e
    while True:
        e = int(input("Enter an integer e such that 1 < e < phi(n) and gcd(e, phi(n)) = 1: "))
        if 1 < e < phi_n and extended_gcd(e, phi_n)[0] == 1:
            break
        print("Error: Invalid e. Please try again.")

    # Calculate d (modular inverse of e modulo phi(n))
    d = mod_inverse(e, phi_n)
    print(f"The decryption key d is: {d}")

    # Encrypt a message
    message_type = input("Enter 'text' for plaintext or 'int' for integer message: ").lower()
    if message_type == 'text':
        message = input("Enter the plaintext message: ")
        message = int.from_bytes(message.encode(), 'big')
    else:
        message = int(input("Enter the message as an integer: "))
    
    ciphertext = rsa_encrypt(message, e, n)
    print(f"Encrypted message: {ciphertext}")

    # Decrypt the message
    decrypted_message = rsa_decrypt(ciphertext, d, n)
    if message_type == 'text':
        decrypted_text = decrypted_message.to_bytes((decrypted_message.bit_length() + 7) // 8, 'big').decode()
        print(f"Decrypted message (plaintext): {decrypted_text}")
    else:
        print(f"Decrypted message: {decrypted_message}")

def encrypt_message():
    e = int(input("Enter the public exponent (e): "))
    n = int(input("Enter the modulus (n): "))
    message_type = input("Enter 'text' for plaintext or 'int' for integer message: ").lower()
    if message_type == 'text':
        message = input("Enter the plaintext message: ")
        message = int.from_bytes(message.encode(), 'big')
    else:
        message = int(input("Enter the message as an integer: "))
    ciphertext = rsa_encrypt(message, e, n)
    print(f"Encrypted message: {ciphertext}")
    print(f"Public key (e, n): ({e}, {n})")

def decrypt_message():
    d = int(input("Enter the private exponent (d): "))
    n = int(input("Enter the modulus (n): "))
    ciphertext = int(input("Enter the ciphertext as an integer: "))
    decrypted_message = rsa_decrypt(ciphertext, d, n)
    message_type = input("Enter 'text' for plaintext or 'int' for integer message: ").lower()
    if message_type == 'text':
        try:
            decrypted_text = decrypted_message.to_bytes((decrypted_message.bit_length() + 7) // 8, 'big').decode()
            print(f"Decrypted message (plaintext): {decrypted_text}")
        except UnicodeDecodeError:
            print(f"Decrypted message (integer): {decrypted_message}")
            print("Warning: Unable to decode the message as text. It might be an integer message.")
    else:
        print(f"Decrypted message: {decrypted_message}")

def generate_rsa_keys():
    while True:
        p = int(input("Enter a prime number p: "))
        if is_prime(p):
            break
        print("Error: p is not prime. Please try again.")

    while True:
        q = int(input("Enter a prime number q: "))
        if is_prime(q):
            break
        print("Error: q is not prime. Please try again.")

    n = p * q
    phi_n = (p - 1) * (q - 1)

    while True:
        e = int(input("Enter an integer e such that 1 < e < phi(n) and gcd(e, phi(n)) = 1: "))
        if 1 < e < phi_n and extended_gcd(e, phi_n)[0] == 1:
            break
        print("Error: Invalid e. Please try again.")

    d = mod_inverse(e, phi_n)

    print(f"Public key (e, n): ({e}, {n})")
    print(f"Private key (d, n): ({d}, {n})")

def check_prime():
    n = int(input("Enter a number to check if it's prime: "))
    if is_prime(n):
        print(f"{n} is prime.")
    else:
        print(f"{n} is not prime.")

def calculate_gcd():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    gcd, x, y = extended_gcd(a, b)
    print(f"The greatest common divisor of {a} and {b} is: {gcd}")

def find_mod_inverse():
    a = int(input("Enter the number: "))
    m = int(input("Enter the modulus: "))
    try:
        inverse = mod_inverse(a, m)
        print(f"The modular inverse of {a} modulo {m} is: {inverse}")
    except Exception as e:
        print(str(e))

def mod_exponentiation():
    base = int(input("Enter the base: "))
    exponent = int(input("Enter the exponent: "))
    modulus = int(input("Enter the modulus: "))
    result = pow(base, exponent, modulus)
    print(f"{base}^{exponent} mod {modulus} = {result}")

def main():
    while True:
        print("\nChoose an option:")
        print("1. Factorize a number")
        print("2. Run RSA algorithm")
        print("3. Encrypt a message")
        print("4. Decrypt a message")
        print("5. Generate RSA keys")
        print("6. Check if a number is prime")
        print("7. Calculate the greatest common divisor (GCD)")
        print("8. Find the modular inverse")
        print("9. Perform modular exponentiation")
        print("10. Exit")
        choice = input("Enter your choice (1/2/3/4/5/6/7/8/9/10): ")

        if choice == '1':
            factorize()
        elif choice == '2':
            rsa_algorithm()
        elif choice == '3':
            encrypt_message()
        elif choice == '4':
            decrypt_message()
        elif choice == '5':
            generate_rsa_keys()
        elif choice == '6':
            check_prime()
        elif choice == '7':
            calculate_gcd()
        elif choice == '8':
            find_mod_inverse()
        elif choice == '9':
            mod_exponentiation()
        elif choice == '10':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()