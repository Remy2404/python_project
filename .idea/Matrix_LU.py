import numpy as np

def get_matrix_input():
    """Prompts the user to input a matrix and returns it as a NumPy array."""
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    matrix = []
    for i in range(rows):
        row = list(map(float, input(f"Enter row {i+1}: ").split()))
        matrix.append(row)
    return np.array(matrix)

def print_matrix(matrix):
    """Prints a matrix."""
    for row in matrix:
        print(row)

def lu_decomposition_gauss_elimination(A):
    """Performs LU decomposition on matrix A using Gauss Elimination Method."""
    n = len(A)
    L = np.eye(n)  # Initialize L as the identity matrix
    U = A.copy()  # Copy A to U

    print("\nInitial Matrix A:")
    print_matrix(A)

    for i in range(n - 1):
        print("\nStep", i+1, ":")
        for j in range(i + 1, n):
            # Calculate the multiplier factor for elimination
            factor = U[j, i] / U[i, i]
            
            # Update L with the multiplier factor
            L[j, i] = factor
            
            # Perform Gaussian elimination to update U
            U[j, i:] -= factor * U[i, i:]

            print("\nApplying Gaussian Elimination:")
            print("L matrix:")
            print_matrix(L)
            print("U matrix:")
            print_matrix(U)

    return L, U

def solve_linear_equations(A, C):
    """Solves the linear system A * X = C using LU decomposition."""
    L, U = lu_decomposition_gauss_elimination(A)

    print("\nLU Decomposition:")
    print("Matrix L:")
    print_matrix(L)
    print("Matrix U:")
    print_matrix(U)

    # Solve for L * Z = C
    Z = np.linalg.solve(L, C)
    print("\nSolving for L * Z = C:")
    print("Vector Z:")
    print(Z)

    # Solve for U * X = Z
    X = np.linalg.solve(U, Z)
    print("\nSolving for U * X = Z:")
    print("Solution Vector X:")
    print(X)

    return X

# Example usage:
A = get_matrix_input()
C = get_matrix_input()

print("\nMatrix A:")
print_matrix(A)

print("\nMatrix C:")
print_matrix(C)

solution_X = solve_linear_equations(A, C)

print("\nFinal Solution for X:")
print(solution_X)

   