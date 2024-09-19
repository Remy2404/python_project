def modular_exponentiation(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent // 2
        base = (base * base) % modulus
    return result

def miller_rabin_test(n, a):
    if n <= 1:
        return "n is composite"
    
    n_prime = n - 1
    
    while n_prime % 2 == 0:
        if modular_exponentiation(a, n_prime, n) == n - 1:
            return "n is a probable prime"
        if modular_exponentiation(a, n_prime, n) != 1:
            return "n is composite"
        n_prime //= 2
    
    if modular_exponentiation(a, n_prime, n) != 1:
        return "n is composite"
    
    return "n is a probable prime"

def main():
    n = int(input("Enter a number to test: "))
    a = random.randint(2, n - 1)
    result = miller_rabin_test(n, a)
    print(result)

if __name__ == "__main__":
    import random
    main()
