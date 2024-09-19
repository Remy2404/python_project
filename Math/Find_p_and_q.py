from sympy import factorint

def prime_factors(n):
    factors = factorint(n)
    return list(factors.keys())

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_big_prime(n):
    return is_prime(n) and n > 1000000

# Input number
n = 251122026675195444766682608981937920228236940581725427491007980646579040856171620212691861040318704518756988836758103649

factors = prime_factors(n)
print("Prime factors:", factors)

if len(factors) == 1 and is_big_prime(factors[0]):
    print("n is a big prime number")
else:
    print("n is not a big prime number")
