import numpy as np

def divided_differences(x, y):
    n = len(x)
    table = np.zeros((n, n))
    
    # Isi kolom pertama dengan nilai f(x)
    table[:, 0] = y
    
    for j in range(1, n):
        for i in range(n - j):
            table[i][j] = (table[i + 1][j - 1] - table[i][j - 1]) / (x[i + j] - x[i])
    
    return table

def newton_polynomial(x, y, xi):
    table = divided_differences(x, y)
    n = len(x)
    
    # Koefisien polinom diambil dari kolom pertama tabel
    coefficients = table[0, :]
    
    # Evaluasi polinom Newton
    result = coefficients[0]
    for i in range(1, n):
        term = 1
        for j in range(i):
            term *= (xi - x[j])
        result += coefficients[i] * term
    
    return result

def linear_interpolation(x0, y0, x1, y1, x):
    return str(y0 + (y1 - y0) * (x - x0) / (x1 - x0))

def quadratic_interpolation(x0, y0, x1, y1, x2, y2, x):
    a0 = y0
    a1 = (y1 - y0) / (x1 - x0)
    a2 = (((y2 - y0) / (x2 - x0)) - a1) / (x2 - x1)
    
    return a0 + a1 * (x - x0) + a2 * (x - x0) * (x - x1)