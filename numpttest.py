import numpy as np
a=np.array([2,3,4])
b=np.array([5,6,7])
c=np.dot(a,b)
print(c)
#distance from origin
dista=np.array([2,3,4])
answer=np.linalg.norm(dista)
print(answer)
#euclidean norm
point1 = np.array([1, 2, 3])
point2 = np.array([4, 5, 6])
euclidean_distance = np.linalg.norm(point1 - point2)
print("Euclidean Distance:", euclidean_distance)
#scalar addition
a=np.array([2,3,4])
b=np.array([1,0,-1])
c=np.dot(a,b)
print(c)
#angle between two vector
a=np.array([2,3])
b=np.array([1,4])
multiplication=np.dot(a,b)
print(multiplication)
norma=np.linalg.norm(a)
normb=np.linalg.norm(b)
normab=norma*normb
anglebetween=multiplication/normab
print("angle beteen",anglebetween)
#matrix addition
mat1=np.array([[1,2],[3,4]])
mat2=np.array([[5,6],[7,8]])
add=mat1+mat2
print(add)
#matrix substraction
mat1=np.array([[9,8],[7,6]])
mat2=np.array([[5,4],[3,2]])
sub=mat1-mat2
print(sub)
#matrix multiplication
mat1=np.array([[1,2],[3,4]])
mat2=np.array([[5,6],[7,8]])
mul=np.dot(mat1,mat2)
print(mul)
#determinanta
mat1=np.array([[1,2,3],[4,5,6],[7,8,9]])
mat2=np.linalg.det(mat1)
print(mat2)
#euality
mat1=np.array([[1,2],[3,4]])
mat2=np.array([[5,6],[7,8]])
mat3=np.array_equal(mat1,mat2)
print(mat3)
#scalr multiplication
k=3
mat1=np.array([[4,-2],[1,5]])
mul=k*mat1
print(mul)
#inverse of matrix
mat1=np.array([[1,2,3],[0,1,4],[5,6,0]])
print(np.linalg.inv(mat1))
#rank of matrix
mat1=np.array([[1,3,3],[0,0,0],[1,2,0]])
print(np.linalg.matrix_rank(mat1))
#eigen vlaue and eigen vector
