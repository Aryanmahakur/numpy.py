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

np1 = np.array([1,2,3,4,5,6,7,8,9,10])
print(np1)
print(np1.shape)
