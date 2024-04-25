import numpy as np

def get_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = list(map(float, input(f"Enter values for row {i+1} separated by space: ").split()))
        matrix.append(row)
    return np.array(matrix)

def get_vector(size):
    vector = list(map(float, input(f"Enter values for the vector separated by space: ").split()))
    return np.array(vector).reshape((size, 1))

def print_matrix(matrix):
    for row in matrix:
        print(row)

def print_vector(vector):
    for val in vector:
        print(val[0])

def lu_decomposition(matrix):
    n = len(matrix)
    L = np.eye(n)
    U = matrix.copy()

    for i in range(n - 1):
        for j in range(i + 1, n):
            # Compute the factor for elimination
            factor = U[j, i] / U[i, i]
            
            # Store the factor in the lower triangular matrix L
            L[j, i] = factor
            
            # Perform elimination in the upper triangular matrix U
            U[j, i:] -= factor * U[i, i:]

    return L, U

def solve_linear_equations(A, C):
    L, U = lu_decomposition(A)

    print("\nLU Decomposition:")
    print("Matrix L:")
    print_matrix(L)
    print("Matrix U:")
    print_matrix(U)

    # Solve for L * Z = C
    Z = np.linalg.solve(L, C)
    print("\nSolving for L * Z = C:")
    print("Vector Z:")
    print_vector(Z)

    # Solve for U * X = Z
    X = np.linalg.solve(U, Z)
    print("\nSolving for U * X = Z:")
    print("Solution Vector X:")
    print_vector(X)

    return X

# Example usage:
rows = int(input("Enter the number of rows for the matrix: "))
cols = int(input("Enter the number of columns for the matrix: "))
matrix_A = get_matrix(rows, cols)

print("\nMatrix A:")
print_matrix(matrix_A)

# Ask the user whether to enter the right-hand side vector b or not
enter_b = input("Do you want to enter the right-hand side vector b? (y/n): ").lower()

if enter_b == 'y':
    if rows == cols:
        vector_b = get_vector(rows)
        print("\nVector b:")
        print_vector(vector_b)

        solution_X = solve_linear_equations(matrix_A, vector_b)

        print("\nFinal Solution for X:")
        print_vector(solution_X)
    else:
        print("\nMatrix A must be a square matrix for LU decomposition.")
else:
    # Default right-hand side vector
    vector_b = np.ones((rows, 1))
    print("\nUsing default right-hand side vector b = [1, 1, ..., 1]")

    solution_X = solve_linear_equations(matrix_A, vector_b)

    print("\nFinal Solution for X:")
    print_vector(solution_X)
