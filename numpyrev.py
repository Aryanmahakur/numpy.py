import numpy as np

#Create an array of numbers from 1 to 20 and reshape it into a 4x5 matrix.
np1=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
print(np1)
print(np1.reshape(4,5))

#Find the sum and mean of all elements in a NumPy array.
print(np1.sum())
print(np1.mean())

#Find the maximum and minimum values in a given NumPy array.
print(np1.max())
print(np1.min())