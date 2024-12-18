import numpy as np
from scipy.linalg import lu

def lu_decomposition(matrix):
    """Fungsi untuk melakukan LU Decomposition"""
    try:
        P, L, U = lu(matrix)
        print(L, matrix)
        return P, L, U
    except Exception as e:
        print(f"Error dalam melakukan LU Decomposition: {e}")
        return None, None, None

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

def validate_lu(P, A, L, U):
    """Fungsi untuk memvalidasi P * A = L * U"""
    PA = np.dot(P, A)
    LU = np.dot(L, U)

    return 0 if np.allclose(PA, LU) else 1