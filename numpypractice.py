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
np2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(np2)