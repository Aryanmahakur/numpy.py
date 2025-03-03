import numpy as np

#boolean indexing
np1 = np.array([1, 2, 3, 4, 5])
x = [True, False, False, False, False]
print(np1)
print(np1[x])

#filtering even numbers using a loop
filtered = []
for things in np1:
    if things %2==0:
        filtered.append(True)
    else:
        filtered.append(False)
print(np1)
print(filtered)
print(np1[filtered])

#shortcut method for filtering even numbers
filtered = np1 %2==0
print(np1)
print(filtered)
print(np1[filtered])

#slicing numpy arrays
np1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(np1[1:4])
print(np1[0:9:2])
print(np1[-3:-1])
print(np1[::-1])
print(np1[::2])
print(np1[3:])
print(np1[3:-1])

#slicing 2d numpy arrays
np2 = np.array([[1, 2, 3, 4, 5], 
                [6, 7, 8, 9, 10]])
print(np2)
print(np2[0, 1])
print(np2[1, 2])
print(np2[0:1, 1:4])
print(np2[0:2, 1:3])

#numpy universal functions
np1 = np.array([-1, 0, 1, 2, 3, 4, 5])
print(np1)
print(np.sqrt(np1))
print(np.absolute(np1))
print(np.exp(np1))
print(np.max(np1))
print(np.min(np1))
print(np.sin(np1))
print(np.sign(np1))
print(np.log(np1))

#creating a view of numpy array
np1 = np.array([1, 2, 3, 4, 5])
np2 = np1.view()
print(np2)
np1[0] = 10
print(np1)
print(np2)

#creating a copy of numpy array
np1 = np.array([1, 2, 3, 4, 5])
np2 = np1.copy()
print(np2)
np1[0] = 10
print(np1)
print(np2)

#reshaping numpy arrays
np1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(np1)
print(np1.reshape(2, 5))
print(np1.reshape(5, 2))

#iterating over numpy arrays
np1=np.array([1, 2, 3, 4, 5])
for x in np1:
    print(x)

np2=np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]])
for x in np2:
    print("2d array",x)
    for y in x:
        print(y)
     
np3=np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in np3:
    print("3d array",x)
    for y in x:
        print(y)
        for z in y:
            print(z)