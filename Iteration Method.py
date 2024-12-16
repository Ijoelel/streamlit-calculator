import numpy as np

class IterationCalculator:
    def _init_(self):
        self.n = 0
        self.A = None
        self.b = None
        self.x0 = None
        
    def input_matrix(self, prompt):
        data = []
        print(f"\n{prompt}")
        for i in range(self.n):
            if prompt.startswith("Masukkan matriks"):
                row = [float(input(f"A[{i+1}][{j+1}]: ")) for j in range(self.n)]
                data.append(row)
            else:
                elem = float(input(f"{prompt[0].lower()}[{i+1}]: "))
                data.append(elem)
        return np.array(data)
    
    def input_system(self):
        self.n = int(input("Masukkan ukuran sistem (n x n): "))
        self.A = self.input_matrix("Masukkan matriks koefisien A:")
        self.b = self.input_matrix("Masukkan vektor b:")
        self.x0 = self.input_matrix("Masukkan tebakan awal x0:")
        
    def solve_iteration(self, method='gauss-seidel', max_iter=100, tol=1e-6):
        x = self.x0.copy()
        
        for iter in range(max_iter):
            x_old = x.copy()
            x_new = np.zeros_like(x)
            
            for i in range(self.n):
                if method == 'gauss-seidel':
                    sum1 = np.dot(self.A[i,:i], x[:i])
                    sum2 = np.dot(self.A[i,i+1:], x_old[i+1:])
                    x[i] = (self.b[i] - sum1 - sum2) / self.A[i,i]
                else:  # jacobi
                    sum_ax = np.dot(self.A[i,:i], x_old[:i]) + np.dot(self.A[i,i+1:], x_old[i+1:])
                    x_new[i] = (self.b[i] - sum_ax) / self.A[i,i]
            
            if method == 'jacobi':
                if np.allclose(x, x_new, rtol=tol):
                    return x_new, iter + 1
                x = x_new.copy()
            else:  # gauss-seidel
                if np.allclose(x, x_old, rtol=tol):
                    return x, iter + 1
                    
        return x if method == 'gauss-seidel' else x_new, max_iter

def main():
    calc = IterationCalculator()
    methods = {
        '1': ('gauss-seidel', 'Gauss-Seidel'),
        '2': ('jacobi', 'Jacobi')
    }
    
    while True:
        print("\nKalkulator Metode Iterasi")
        print("1. Metode Gauss-Seidel")
        print("2. Metode Jacobi")
        print("0. Keluar")
        
        choice = input("\nPilih metode (0-2): ")
        
        if choice == '0':
            break
            
        if choice in methods:
            calc.input_system()
            method, name = methods[choice]
            result, iterations = calc.solve_iteration(method=method)
            print(f"\nHasil Metode {name}:")
            print(f"Solusi: {result}")
            print(f"Jumlah iterasi: {iterations}")
        else:
            print("Pilihan tidak valid!")
            
        input("\nTekan Enter untuk melanjutkan...")

if __name__ == "__main__":
    main()


    