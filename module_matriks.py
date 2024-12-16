import numpy as np

def add_matrices(A, B):
    try:
        return A + B
    except ValueError:
        return "Error: Dimensi matriks tidak sesuai"

def subtract_matrices(A, B):
    try:
        return A - B
    except ValueError:
        return "Error: Dimensi matriks tidak sesuai"

def multiply_matrices(A, B):
    try:
        return np.dot(A, B)
    except ValueError:
        return "Error: Dimensi matriks tidak sesuai untuk perkalian"

def determinant(A):
    try:
        return np.linalg.det(A)
    except:
        return "Error: Tidak dapat menghitung determinan"
    
def inverse_matrix(A):
    try:
        return np.linalg.inv(A)
    except:
        return "Error: Tidak dapat menghitung inverse_matrix"
        
def transpose_matrix(A):
    try:
        return np.transpose(A)
    except:
        return "Error: Tidak dapat menghitung transpose"