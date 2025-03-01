import numpy as np

#filtering numpy arrays using boolean indexing
# np1=np.array([1,2,3,4,5])
# x=[True,False,False,False,False]
# print(np1)
# print(np1[x])

# filtered=[]
# for things in np1:
#     if things%2==0:
#         filtered.append(True) #True
#     else:
#         filtered.append(False) #False
# print(np1)
# print(filtered)
# print(np1[filtered])
#shortcut

# filtered=np1>2
# print(np1)
# print(filtered)
# print(np1[filtered])

#slicing numpy arrays
# np1 = np.array([1,2,3,4,5,6,7,8,9,10])
# print(np1[1:4])
# print(np1[0:9:2])
# print(np1[0:9:3])
# print(np1[::2])
# print(np1[::3])
# print(np1[3:])
# print(np1[3:-1])
# print(np1[-3:-1]) #from the end of the array
# print(np1[::2])
# print(np1[::-1])

#slicing 2D numpy arrays
# np2=np.array([[1,2,3,4,5],[6,7,8,9,10]])
# # print(np2)
# # print(np2[0,1])
# # print(np2[1,2])
# print(np2[0:1,1:4],",")
# print(np2[0:2,1:3])
# print(np2[0:1,0:3])
# print(np2[0:2,0:3])

#numpy universal functions
# np1=np.array([-1,0,1,2,3,4,5])
# print(np1)

#find squareroot of each element
# print(np.sqrt(np1))
# print(np.absolute(np1))
# print(np.exp(np1))
# print(np.max(np1))
# print(np.min(np1))
# print(np.sin(np1))
# print(np.sign(np1)) #returns 1 if positive, 0 if 0, -1 if negative
# print(np.log(np1)) #returns -inf for negative numbers
# there are more functions

# np1=np.array([0,1,2,3,4,5])
# # # cretae a view
# # np2=np1.view()
# # print(f'orignal np1{np1}')
# # print(f'view np2{np2}')
# # np1[0]=42
# # print(f'changed np1{np1}')
# # print(f'original np2{np2}')
# #create a copy
# np2=np1.copy()
# print(f'original np1{np1}')
# print(f'copy np2{np2}')
# np1[0]=42
# print(f'changed np1{np1}')
# print(f'original np2{np2}')

# np1 = np.array([1,2,3,4,5,6,7,8,9,10])
# print(np1)
# print(np1.shape)


# np2 = np.array([[1,2,3,4,5,6], [7,8,9,10,11,12]])
# print(np2) 
# print(np2.reshape(3,4)) #2 rows and 6 columns
# print(np2.shape) #2 rows and 5 columns
# print(np2.reshape(5,2)) #5 rows and 2 columns
# print(np2.reshape(1,10)) #1 row and 10 columns
# print(np2.reshape(10,1)) #10 rows and 1 column
# print(np2.ravel()) #converts 2D array to 1D array
# print(np2.T) #transpose of the array
# np4=np2.reshape(2,3,2)
# print(np4)
# print(np4.shape)
# print(np4.ravel())
# np5=np4.reshape(-1)
# print(np5)
# print(np5.shape)
# np1=np.array([1,2,3,4,5,6,7,8,9,10])
# print(np1)
# for x in np1:
#     print(x)

# np2=np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])
# print(np2)
# for x in np2:
#     #print rows
#     print(x)
#     for y in x:
#         print(y)
# np3=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
# print(np3)
# for x in np3:
#     print(x)
#     for y in x:
#         print(y)
#         for z in y:
#             print(z)
#use np.nditer()
# for x in np.nditer(np3):
#     print(x)
# np1=np.array([5,3,8,9,10])
# print(np.sort(np1))
# print(np1)
# np2=np.array(["banana","cherry","apple","mango"])
# print(np2)
# print(np.sort(np2))

# np3=np.array([True,False,True,False])
# print(np3)
# print(np.sort(np3))
# np4=np.array([[3,2,4],[5,0,1]])
# print(np4)
# print(np.sort(np4))
# np5=np.array([2,3,1,4,5])
# print(np5)
# print(np.sort(np5))
# print(np5)
# np6=np.array([[3,2,4,5,0,1,4],[7,4,9,10,11,12]])
# np6=np.array([1,2,3,4,5,6,7,8,9,10,4])
# x=np.where(np6==4)
# print(x)
# print(np6[0])
# y=np.where(np6%2==0)
# print(y)
# print(np6[y])
# y=np.where(np6%2==1)
# print(y)
# print(np6[y])
np7=np.array([1,2,3,4,5,6,7,8,9,10])
# filtered=[]
# for things in np7:
#     if things%2==0:
#         filtered.append(True) #True
#     else:
#         filtered.append(False) #False
# print(np7)
# print(filtered)
# print(np7[filtered])
filtered=np7%2==0
print(np7)
print(filtered)
print(np7[filtered])


