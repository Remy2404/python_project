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

# Find all solutions to the system Ax = 0
def find_null_space(A):
    U = gaussian_elimination(A)
    # The null space (kernel) of A is the space of all solutions to Ax = 0
    # The dimension of the null space is equal to the number of free variables
    # which is the number of columns of U without full pivots
    pivots = np.where(np.abs(U.diagonal()) > 1e-10)[0]  # Find indices of non-zero pivots
    null_space_dim = A.shape[1] - len(pivots)
    null_space_basis = np.zeros((A.shape[1], null_space_dim))
    free_columns = np.setdiff1d(np.arange(A.shape[1]), pivots)
    for i, col in enumerate(free_columns):
        # Set the i-th basis vector of the null space to be the i-th free column of the identity matrix
        null_space_basis[col, i] = 1
        for j in range(col):
            # Back-substitution to find the corresponding non-free variables
            null_space_basis[:, i] -= U[:, j] * null_space_basis[j, i]
    return null_space_basis

# Find all solutions to the system Ax = 0
null_space_basis = find_null_space(A)

# Suppose that b = [2, -3, 1]
b = np.array([2, -3, 1])

# Solve the system Ax = b
# We have already performed LU decomposition, so we can directly solve for x using forward and backward substitution
def solve_linear_system(L, U, b):
    # Solve Ly = b using forward substitution
    y = np.linalg.solve(L, b)
    # Solve Ux = y using backward substitution
    x = np.linalg.solve(U, y)
    return x

# Calculate the solution to Ax = b
L, U = lu_decomposition(A)
x = solve_linear_system(L, U, b)
#Calculate the upper triangular matrix U
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
print("\n(d) All solutions to the system Ax = 0:")
print(null_space_basis)
print("\n(e) Complete solution to Ax = b:")
print("x =", x)
