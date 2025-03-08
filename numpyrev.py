import numpy as np

# Create an array of numbers from 1 to 20 and reshape it into a 4x5 matrix.
np1 = np.arange(1, 21)
print(np1)
print(np1.reshape(4, 5))

# Find the sum and mean of all elements in a NumPy array.
print(np1.sum())
print(np1.mean())

# Find the maximum and minimum values in a given NumPy array.
print(np1.max())
print(np1.min())

# Extract all even numbers from an array of numbers from 1 to 50.
array_1_to_50 = np.arange(1, 51)
print(array_1_to_50[array_1_to_50 % 2 == 0])  # Direct filtering

# Compute element-wise square root, logarithm, and exponential for a given NumPy array.
arr = np.arange(1, 6)
print(arr)
print(np.sqrt(arr))
print(np.exp(arr))

arr1 = np.arange(1, 10)
print(arr1)
print(np.cumsum(arr1))  # Corrected function
print(np.sin(arr1))
print(np.cos(arr1))

# Dot product and cross product
mat1 = np.array([1, 2, 3, 4])
mat2 = np.array([1, 2, 3, 4])
print(np.dot(mat1, mat2))

vector3 = np.array([1, 2])
vector4 = np.array([3, 4])
cross_product2d = np.cross(vector3, vector4)
print(cross_product2d)

vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])
cross_product = np.cross(vector1, vector2)
print(cross_product)

# Determinant calculation
det1 = np.array([[1, 2, 3], [4, 5, 6], [7,8,9]])
print(np.linalg.det(det1))  # Output will be 0 (singular matrix)

# Inverse of a non-singular matrix
A = np.array([[2, 3], [1, 4]])
inv1 = np.linalg.inv(A)
print(inv1)
I = np.dot(A, inv1)
print("A * A_inv:\n", np.round(I, 2))  # Should be the identity matrix

# Checking inverse for another matrix
mat2 = np.array([[1, 2, 3], [0, 1, 4], [5, 6, 0]])
if np.linalg.det(mat2) != 0:  # Check before inverting
    inv2 = np.linalg.inv(mat2)
    print(inv2)
    I1 = np.dot(mat2, inv2)
    print("A * A_inv:\n", np.round(I1, 2))  # Should be identity matrix
else:
    print("Matrix is singular, no inverse exists.")

# Eigenvalues and eigenvectors
arr2 = np.array([[6, 2, 1], [2, 3, 1], [1, 1, 1]])
eig_vals, eig_vecs = np.linalg.eig(arr2)
print("Eigenvalues:", eig_vals)
print("Eigenvectors:\n", eig_vecs)
