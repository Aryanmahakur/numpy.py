import numpy as np  # Importing NumPy

# -----------------------------------------
# Dot Product of Two 1D Arrays (Vectors)
# -----------------------------------------
np1 = np.array([1, 2, 3, 4, 5])
np2 = np.array([6, 7, 8, 9, 10])
dot_product = np.dot(np1, np2)
print("Dot Product:", dot_product)

# --------------------------------------------------------
# Matrix Multiplication using multi_dot (Efficient Method)
# --------------------------------------------------------
np3 = np.array([[1, 2, 3], [4, 5, 6]])
np4 = np.array([[1, 2, 3], [4, 5, 6]])
multi_dot_result = np.linalg.multi_dot([np3, np4.T])
print("Matrix Multiplication:", multi_dot_result)

# --------------------------------------------------
# Euclidean Norm (Distance from Origin) and Distance
# --------------------------------------------------
point = np.array([1, 2, 3])
distance_origin = np.linalg.norm(point)
print("Distance from Origin:", distance_origin)

point1 = np.array([1, 2, 3])
point2 = np.array([4, 5, 6])
euclidean_distance = np.linalg.norm(point1 - point2)
print("Euclidean Distance:", euclidean_distance)

# -----------------------------
# Element-wise Operations
# -----------------------------
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("Element-wise Addition:", a + b)
print("Element-wise Subtraction:", a - b)
print("Element-wise Multiplication:", a * b)

# ------------------------------------------
# Cosine Similarity (Angle between Vectors)
# ------------------------------------------
dot_product_ab = np.dot(a, b)
magnitudes = np.linalg.norm(a) * np.linalg.norm(b)
cos_theta = dot_product_ab / magnitudes
print("Cosine of Angle:", cos_theta)

# -----------------------
# Magnitude of a Vector
# -----------------------
magnitude_a = np.linalg.norm(a)
print("Magnitude of Vector a:", magnitude_a)

# -----------------------
# Matrix Operations
# -----------------------
mat1 = np.array([[1, 2, 3], [4, 5, 6]])
mat2 = np.array([[7, 8, 9], [10, 11, 12]])
print("Matrix Addition:", mat1 + mat2)
print("Matrix Subtraction:", mat1 - mat2)
print("Element-wise Matrix Multiplication:", mat1 * mat2)

# -------------------------------------------------
# Checking Orthogonality of Matrices
# (Dot Product should be an Identity Matrix)
# -------------------------------------------------
mat6 = np.array([[1, 0], [0, -1]])
mat7 = np.array([[0, 1], [-1, 0]])
orthogonality_check = np.dot(mat6, mat7)
print("Orthogonality Check:", orthogonality_check)

# -----------------------------
# Matrix Transpose
# -----------------------------
mat_tran = np.array([[1, 2, 3], [4, 5, 6]])
print("Matrix Transpose:", np.transpose(mat_tran))

# -----------------------------
# Matrix Inverse & Determinant
# -----------------------------
mat10 = np.array([[1, 2], [3, 4]])
print("Matrix Inverse:", np.linalg.inv(mat10))
print("Matrix Determinant:", np.linalg.det(mat10))

# -----------------------------------
# Determinant of a Singular Matrix
# -----------------------------------
mat_singular = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Determinant of Singular Matrix:", np.linalg.det(mat_singular))

# -------------------------------
# Matrix Equality Check
# -------------------------------
mat12 = np.array([[1, 2, 3], [4, 5, 6]])
mat13 = np.array([[1, 2, 3], [4, 5, 6]])
print("Are Matrices Equal:", np.array_equal(mat12, mat13))

# -----------------------------
# Scalar Multiplication
# -----------------------------
scalar_mat = 2 * mat12
print("Scalar Multiplication:", scalar_mat)

# -----------------------------
# Rank of a Matrix
# -----------------------------
mat_rank = np.array([[1, 3, 5], [2, -1, 4], [-2, 8, 2]])
print("Rank of Matrix:", np.linalg.matrix_rank(mat_rank))

# -----------------------------
# Linear Transformation
# -----------------------------
mat21 = np.array([[1, 2], [3, 4]])
mat22 = np.array([[1, 2], [3, 4]])
print("Linear Transformation:", np.dot(mat21, mat22))

# -----------------------------
# Tensor Operations
# -----------------------------
tensor1 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("Tensor:", tensor1)
print("Tensor Transpose:", np.transpose(tensor1, (1, 0, 2)))

# --------------------------------
# Eigenvalues and Eigenvectors
# --------------------------------
mat24 = np.array([[8, -8, -2], [4, -3, -2], [2, -4, 1]])
eigenvalues, eigenvectors = np.linalg.eig(mat24)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:", eigenvectors)

mat25 = np.array([[4, 2], [1, 3]])
eigenvalues, eigenvectors = np.linalg.eig(mat25)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:", eigenvectors)

# -------------------------------
# Adjoint of a Matrix
# -------------------------------


# Define the matrix
mat26 = np.array([[1, 2, 3], [-1, 2, 5], [4, 3, 1]])

# Compute the cofactor matrix
cofactor_matrix = np.linalg.inv(mat26).T * np.linalg.det(mat26)

# Print the adjugate matrix (which is the transpose of the cofactor matrix)
print("Adjoint of Matrix:\n", cofactor_matrix)
transpose_matrix = np.transpose(cofactor_matrix)
print("Transpose of Matrix:\n", transpose_matrix)
# -------------------------------
# Unit Vector Normalization
# -------------------------------
unit_vector = np.array([3, 4])
normalized_vector = unit_vector / np.linalg.norm(unit_vector)
print("Normalized Vector:", normalized_vector)
ddd