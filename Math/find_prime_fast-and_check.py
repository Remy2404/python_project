#find prime numbers faster than checking divisibility up to n
import random

def miller_rabin(n, k=5):
    if n < 2: return False
    for p in [2,3,5,7,11,13,17,19,23,29]:
        if n % p == 0: return n == p
    s, d = 0, n-1
    while d % 2 == 0:
        s, d = s+1, d//2
    for _ in range(k):
        a = random.randrange(2, n-1)
        x = pow(a, d, n)
        if x == 1 or x == n-1: continue
        for _ in range(s-1):
            x = pow(x, 2, n)
            if x == n-1: break
        else: return False
    return True

def find_next_prime(start):
    candidate = start
    while True:
        if miller_rabin(candidate):
            return candidate
        candidate += 1

# User input
start = int(input("Enter a number to find the next prime after: "))
prime = find_next_prime(start)
print(f"The next prime after {start} is {prime}")
