import numpy as np

# Define the matrix A with integer values
A = np.array([[1, 0, 1],
              [2, 2, 2],
              [3, 4, 5]], dtype=np.float64)  # Specify dtype=np.float64

# Perform Gaussian elimination to transform A into an upper triangular matrix U
def gaussian_elimination(A):
    n = len(A)
    U = A.copy()
    for i in range(n):
        for j in range(i+1, n):
            factor = U[j, i] / U[i, i]
            U[j, i:] -= factor * U[i, i:]
    return U

# Perform LU decomposition
def lu_decomposition(A):
    n = len(A)
    L = np.eye(n)
    U = A.copy()
    for i in range(n):
        for j in range(i+1, n):
            factor = U[j, i] / U[i, i]
            L[j, i] = factor
            U[j, i:] -= factor * U[i, i:]
    return L, U

# Calculate the upper triangular matrix U
U = gaussian_elimination(A)

# Calculate the LU decomposition
L, U = lu_decomposition(A)

# Print the results
print("Upper triangular matrix U:")
print(U)
print("\nLU decomposition:")
print("L:")
print(L)
print("U:")
print(U)
