import numpy as np
np1 = np.array([1, 2, 3, 4, 5])
np2 = np.array([6, 7, 8, 9, 10])
np3= np.dot(np1, np2)
print(np3)

np4 = np.array([[1, 2, 3], [4, 5, 6]])
np5=np.array([[1,2,3],[4,5,6]])
np6=np.linalg.multi_dot([np4,np5.T])
print(np6)

#distance from origin
point=np.array([1,2,3])
distance=np.linalg.norm(point)
print(distance)
#euclidean distance
point1=np.array([1,2,3])
point2=np.array([4,5,6])
distance=np.linalg.norm(point1-point2)
print(distance)
#scalar addition
a=np.array([1,2,3])
b=np.array([4,5,6])
c=a+b
print(c)
#scalar subtraction
d=a-b
print(d)
#scalar dot product
e=a*b
print("multiplication",e)
#angle between two vectors
f=np.dot(a,b)
g=np.linalg.norm(a)*np.linalg.norm(b)
print(f/g)
#magnitude of a vector
h=np.linalg.norm(a)
print(h)
#matrix addition
mat1=np.array([[1,2,3],[4,5,6]])
mat2=np.array([[7,8,9],[10,11,12]])
mat3=mat1+mat2
print(mat3)
#matrix subtraction
mat4=mat1-mat2
print(mat4)
#matrix multiplication
mat5=mat1*mat2
print(mat5)
#matrix orthogonal
mat6=np.array([[1,0],[0,-1]])
mat7=np.array([[0,1],[-1,0]])
mat8=np.dot(mat6,mat7)
print(mat8)
#matrix transpose
mattran=np.array([[1,2,3],[4,5,6]])
mat9=np.transpose(mattran)
print(mat9)
#matrix inverse
mat10=np.array([[1,2],[3,4]])
mat11=np.linalg.inv(mat10)
print(mat11)
#matrix determinant
matdet1=np.array([[1,2],
                  [3,4]])
matdet2=np.linalg.det(matdet1)
print(matdet2)
matdet3=np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9]])
                  
mat4=np.linalg.det(matdet3)
print(mat4)
#matrix equallity
mat12=np.array([[1,2,3],[4,5,6]])
mat13=np.array([[1,2,3],[4,5,6]])
mat14=np.array_equal(mat12,mat13)
print(mat14)
#scalar multiplication
mat15=np.array([[1,2,3],[4,5,6]])
mat16=2*mat15
print(mat16)
#inverse of a matrix
mat17=np.array([[1,2],[3,4]])
mat18=np.linalg.inv(mat17)
print(mat18)
a=np.linalg.det(mat18)
print(a)
#rank of a matrix
mat19=np.array([[1,3,5],[2,-1,4],[-2,8,2]])
mat20=np.linalg.matrix_rank(mat19)
print(mat20)