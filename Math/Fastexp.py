# function to find remainder Modular Exponentiation (a==base, b==exponent, c==modulus)

def mod_exp(a, b, c):
    x = 1
    y = a
    while b > 0:
        if b % 2 == 0:
            y = (y * y) % c
            b = b // 2
        else:
            x = (x * y) % c
            b = b - 1
    return x % c

input_a = int(input("Enter the base: "))
input_b = int(input("Enter the exponent: "))
input_c = int(input("Enter the modulus: "))

print("The remainder is: ", mod_exp(input_a, input_b, input_c))


    