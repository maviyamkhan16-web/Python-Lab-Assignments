import numpy as np
# Generate two 3x3 matrices with random integers (1 to 9)
matrix1 = np.random.randint(1, 10, (3, 3))
matrix2 = np.random.randint(1, 10, (3, 3))
print("Matrix 1:")
print(matrix1)
print("Matrix 2:")
print(matrix2)
# Matrix addition
addition_result = matrix1 + matrix2
print("Matrix Addition Result:")
print(addition_result)
# Matrix multiplication
multiplication_result = np.dot(matrix1, matrix2)
print("Matrix Multiplication Result:")
print(multiplication_result)