import numpy as np

def gauss_elimination():
    # Input jumlah persamaan
    n = int(input("Masukkan jumlah persamaan: "))
    
    # Input matriks augmented [A|B]
    print("Masukkan elemen matriks augmented [A|B]:")
    augmented_matrix = []
    for i in range(n):
        row = list(map(float, input(f"Baris {i + 1}: ").split()))
        augmented_matrix.append(row)
    
    augmented_matrix = np.array(augmented_matrix, dtype=float)

    # Eliminasi maju
    for i in range(n):
        # Pivot utama
        if augmented_matrix[i][i] == 0:
            raise ValueError("Pivot nol ditemukan. Sistem tidak dapat diselesaikan menggunakan metode ini.")
        
        for j in range(i + 1, n):
            ratio = augmented_matrix[j][i] / augmented_matrix[i][i]
            augmented_matrix[j, i:] -= ratio * augmented_matrix[i, i:]

    print("\nMatriks setelah eliminasi maju:")
    print(augmented_matrix)

    solutions = np.zeros(n)
    for i in range(n - 1, -1, -1):
        solutions[i] = (augmented_matrix[i, -1] - np.dot(augmented_matrix[i, i+1:n], solutions[i+1:])) / augmented_matrix[i, i]

    print("\nSolusi:")
    for i in range(n):
        print(f"x{i + 1} = {solutions[i]:.4f}")