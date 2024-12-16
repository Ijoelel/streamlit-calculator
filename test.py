import numpy as np

def lu_no_pivoting(A):
    """
    Perform LU decomposition without row pivoting.
    Args:
        A (numpy.ndarray): Square matrix to decompose.
    Returns:
        L (numpy.ndarray): Lower triangular matrix.
        U (numpy.ndarray): Upper triangular matrix.
    """
    n = A.shape[0]
    L = np.zeros_like(A, dtype=float)
    U = np.zeros_like(A, dtype=float)
    
    for i in range(n):
        # Upper Triangular U
        for j in range(i, n):
            U[i, j] = A[i, j] - np.sum(L[i, :i] * U[:i, j])
        
        # Lower Triangular L
        L[i, i] = 1  # Diagonal of L is 1
        for j in range(i+1, n):
            L[j, i] = (A[j, i] - np.sum(L[j, :i] * U[:i, i])) / U[i, i]
    
    return L, U

# Example matrix
A = np.array([
    [2, -4, 3, -2],
    [4, 1, 2, 3],
    [5, -2, 3, -1],
    [2, 3, 5, -2]
])

# Perform LU decomposition without pivoting
L, U = lu_no_pivoting(A)

print("Matrix L (Lower Triangular):")
print(L)

print("\nMatrix U (Upper Triangular):")
print(U)

# Verify: Does L @ U equal A?
print("\nVerification: Does L @ U equal A?")
print(np.allclose(L @ U, A))
