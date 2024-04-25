import numpy as np

# Define the vectors
a = np.array([1, -1, 0], dtype=np.float64) 
b = np.array([2, 0, -2], dtype=np.float64)
c = np.array([3, -3, 3], dtype=np.float64)

# Gram-Schmidt process
def gram_schmidt(*vectors):
    ortho_vectors = []
    for vector in vectors:
        for ortho_vector in ortho_vectors:
            vector -= np.dot(vector, ortho_vector) / np.dot(ortho_vector, ortho_vector) * ortho_vector
        ortho_vectors.append(vector / np.linalg.norm(vector))
    return np.array(ortho_vectors)

# Orthonormal set
Q = gram_schmidt(a, b, c)

# Compute R
def new_func(Q, A):
    R = np.dot(Q.T, A)
    return R

A = np.array([[1, 0], 
              [2, 1],
              [0, 1]], dtype=np.float64)

# Compute R using the modified function
R = new_func(Q, A)


# Print the results
print("Orthonormal set Q:")
print(Q)
print("\nUpper triangular matrix R:")
print(R)