import numpy as matrik
from scipy.linalg import lu

def lu_decomposition(matrix):
    """Fungsi untuk melakukan LU Decomposition"""
    try:
        P, L, U = lu(matrix)
        return P, L, U
    except Exception as e:
        print(f"Error dalam melakukan LU Decomposition: {e}")
        return None, None, None

def validate_lu(P, A, L, U):
    """Fungsi untuk memvalidasi P * A = L * U"""
    PA = matrik.dot(P, A)
    LU = matrik.dot(L, U)

    return 0 if matrik.allclose(PA, LU) else 1