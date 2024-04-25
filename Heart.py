def f(x):
    return 2 * x - 1

def SIMP(a, b, n):
    h = (b - a) / n
    sum_result = 0

    for i in range(1, n // 2 + 1):
        term1 = f(a + (2 * i - 2) * h)
        term2 = 4 * f(a + (2 * i - 1) * h)
        term3 = f(a + 2 * i * h)
        
        sum_result += term1 + term2 + term3

    return (1 / 3) * sum_result * h

result = SIMP(1, 3, 4)
print(result)
