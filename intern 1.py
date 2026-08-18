import numpy as np

# Create two grids (matrices)
A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

B = np.array([
    [7, 8, 9],
    [10, 11, 12]
])

# Display the matrices
print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

# Basic math
print("\nA + B:")
print(A + B)

print("\nA - B:")
print(A - B)

# Element-by-element multiplication
print("\nA * B (element-by-element):")
print(A * B)

# Matrix multiplication requires compatible dimensions.
# Here, transpose B from 2x3 to 3x2.
print("\nA @ B.T (matrix multiplication):")
print(A @ B.T)

# Other useful operations
print("\nA multiplied by 2:")
print(A * 2)

print("\nSum of all values in A:")
print(np.sum(A))

print("\nAverage of values in A:")
print(np.mean(A))