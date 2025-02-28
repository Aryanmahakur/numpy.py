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
np2=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(np2)