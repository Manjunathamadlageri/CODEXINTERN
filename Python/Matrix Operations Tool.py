import numpy as np

def matrix_operations():
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])

    print("Matrix A:\n", A)
    print("Matrix B:\n", B)

    print("Addition:\n", A + B)
    print("Subtraction:\n", A - B)
    print("Multiplication:\n", A @ B)
    print("Transpose of A:\n", A.T)
    print("Determinant of A:", np.linalg.det(A))

matrix_operations()
