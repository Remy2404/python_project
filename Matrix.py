import numpy as np
from fractions import Fraction

# Define matrices A and B
A = np.array([[1, 0], [1, 1], [1, 2]])
B = np.array([[3, 3], [3, 5]])
# Calculate the inverse of matrix B
B_inv = np.linalg.inv(B)

# Calculate A multiplied by the inverse of B
A_times_B_inv = np.dot(A, B_inv)

# Calculate the transpose of matrix A
A_transpose = A.T

# Calculate the final result
P = np.dot(A_times_B_inv, A_transpose)
def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(Fraction(format(element)).limit_denominator(), end=' ')
        print()
#print matrix A and B

print_matrix(P)
print()
print_matrix(B_inv)
print()
print_matrix(A_times_B_inv)
print()
print_matrix(A_transpose)
