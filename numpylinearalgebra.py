import numpy as np  # Importing NumPy

# Dot product of two 1D arrays (vectors)
np1 = np.array([1, 2, 3, 4, 5])
np2 = np.array([6, 7, 8, 9, 10])
np3 = np.dot(np1, np2)  # Computes the dot product of np1 and np2
print(np3)

# Matrix multiplication using multi_dot (efficient for multiple matrices)
np4 = np.array([[1, 2, 3], [4, 5, 6]])
np5 = np.array([[1, 2, 3], [4, 5, 6]])
np6 = np.linalg.multi_dot([np4, np5.T])  # Matrix multiplication of np4 and the transpose of np5
print(np6)

# Distance of a point from the origin (Euclidean norm)
point = np.array([1, 2, 3])
distance = np.linalg.norm(point)
print(distance)

# Euclidean distance between two points in 3D space
point1 = np.array([1, 2, 3])
point2 = np.array([4, 5, 6])
distance = np.linalg.norm(point1 - point2)  # Euclidean distance formula
print(distance)

# Scalar addition (element-wise)
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = a + b  # Element-wise addition
print(c)

# Scalar subtraction (element-wise)
d = a - b  # Element-wise subtraction
print(d)

# Element-wise multiplication (Hadamard product)
e = a * b
print("Multiplication:", e)

# Angle between two vectors (Cosine similarity)
f = np.dot(a, b)  # Dot product
g = np.linalg.norm(a) * np.linalg.norm(b)  # Magnitudes of a and b
print(f / g)  # Cosine of the angle

# Magnitude (norm) of a vector
h = np.linalg.norm(a)  # Norm of vector a
print(h)

# Matrix addition
mat1 = np.array([[1, 2, 3], [4, 5, 6]])
mat2 = np.array([[7, 8, 9], [10, 11, 12]])
mat3 = mat1 + mat2  # Element-wise addition
print(mat3)

# Matrix subtraction
mat4 = mat1 - mat2  # Element-wise subtraction
print(mat4)

# Element-wise matrix multiplication (not dot product)
mat5 = mat1 * mat2  # Element-wise multiplication
print(mat5)

# Check if two matrices are orthogonal (dot product should be an identity matrix)
mat6 = np.array([[1, 0], [0, -1]])
mat7 = np.array([[0, 1], [-1, 0]])
mat8 = np.dot(mat6, mat7)  # Dot product
print(mat8)

# Matrix transpose
mattran = np.array([[1, 2, 3], [4, 5, 6]])
mat9 = np.transpose(mattran)  # Transpose of matrix
print(mat9)

# Matrix inverse (only works for square, non-singular matrices)
mat10 = np.array([[1, 2], [3, 4]])
mat11 = np.linalg.inv(mat10)  # Inverse of matrix
print(mat11)

# Matrix determinant (helps in checking if a matrix is invertible)
matdet1 = np.array([[1, 2], [3, 4]])
matdet2 = np.linalg.det(matdet1)  # Determinant of matdet1
print(matdet2)

# Determinant of a 3x3 matrix (should be zero for a singular matrix)
matdet3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
mat4 = np.linalg.det(matdet3)  # Determinant
print(mat4)

# Check if two matrices are equal
mat12 = np.array([[1, 2, 3], [4, 5, 6]])
mat13 = np.array([[1, 2, 3], [4, 5, 6]])
mat14 = np.array_equal(mat12, mat13)  # Returns True if matrices are identical
print(mat14)

# Scalar multiplication (each element multiplied by scalar)
mat15 = np.array([[1, 2, 3], [4, 5, 6]])
mat16 = 2 * mat15  # Each element multiplied by 2
print(mat16)

# Inverse of a matrix
mat17 = np.array([[1, 2], [3, 4]])
mat18 = np.linalg.inv(mat17)  # Compute inverse
print(mat18)

# Determinant of the inverse matrix
a = np.linalg.det(mat18)  # Should be 1/det(original matrix)
print(a)

# Rank of a matrix (number of linearly independent rows or columns)
mat19 = np.array([[1, 3, 5], [2, -1, 4], [-2, 8, 2]])
mat20 = np.linalg.matrix_rank(mat19)  # Rank of the matrix
print(mat20)

#linear transformation
mat21 = np.array([[1, 2], [3, 4]])
mat22 = np.array([[1, 2], [3, 4]])
mat23 = np.dot(mat21, mat22)  # Matrix multiplication
print(mat23)
#tensor
tensor1 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(tensor1)

#transpose of a tensor
tensor2 = np.transpose(tensor1, (1, 0, 2))
print(tensor2)

#eigen values and eigen vectors
mat24 = np.array([[8,-8,-2], [4,-3,-2], [2,-4,1]])
eigenvalues, eigenvectors = np.linalg.eig(mat24)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:", eigenvectors)

mat25 = np.array([[4,2], [1,3]])
eigenvalues, eigenvectors = np.linalg.eig(mat25)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:", eigenvectors)
#unit vector
unit_vector = np.array([3,4])
normalized_vector = unit_vector / np.linalg.norm(unit_vector)
print("Normalized vector:", normalized_vector)


