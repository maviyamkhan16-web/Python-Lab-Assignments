import numpy as np

# Take input for 5x3 matrix
print("Enter elements for 5x3 matrix:")
matrix1 = []
for i in range(5):
    row = list(map(int, input(f"Row {i+1} (3 integers): ").split()))
    matrix1.append(row)
matrix1 = np.array(matrix1)

# Take input for 3x2 matrix
print("Enter elements for 3x2 matrix:")
matrix2 = []
for i in range(3):
    row = list(map(int, input(f"Row {i+1} (2 integers): ").split()))
    matrix2.append(row)
matrix2 = np.array(matrix2)

# Perform multiplication
product_matrix = np.dot(matrix1, matrix2)

print("Product Matrix:")
print(product_matrix)