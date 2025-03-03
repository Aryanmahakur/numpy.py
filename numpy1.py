import numpy as np  # Importing the NumPy library

# Filtering NumPy arrays using Boolean indexing
np1 = np.array([1, 2, 3, 4, 5])  # Creating a NumPy array
x = [True, False, False, False, False]  # Boolean list to filter elements
print(np1)  # Print original array
print(np1[x])  # Print elements where x is True

# Filtering even numbers using a loop
filtered = []  # Initialize an empty list
for things in np1:
    if things % 2 == 0:  # Check if number is even
        filtered.append(True)  # Append True for even numbers
    else:
        filtered.append(False)  # Append False for odd numbers

print(np1)  # Print original array
print(filtered)  # Print the boolean list
print(np1[filtered])  # Print elements that satisfy the condition

# Shortcut method for filtering even numbers
filtered = np1 > 2  # Create a Boolean array where elements >2 are True
print(np1)  # Print original array
print(filtered)  # Print the Boolean mask
print(np1[filtered])  # Print filtered array

# Slicing NumPy arrays
np1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  # Creating a NumPy array
print(np1[1:4])  # Slicing elements from index 1 to 3 (excludes 4)
print(np1[0:9:2])  # Slicing with step 2 (every second element)
print(np1[0:9:3])  # Slicing with step 3
print(np1[::2])  # Get every second element
print(np1[::3])  # Get every third element
print(np1[3:])  # Slice from index 3 to the end
print(np1[3:-1])  # Slice from index 3 to second last element
print(np1[-3:-1])  # Slice the last three elements
print(np1[::-1])  # Reverse the array

# Slicing 2D NumPy arrays
np2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])  # Creating a 2D array
print(np2)  # Print the 2D array
print(np2[0, 1])  # Access element at row 0, column 1
print(np2[1, 2])  # Access element at row 1, column 2
print(np2[0:1, 1:4])  # Slice first row, columns 1 to 3
print(np2[0:2, 1:3])  # Slice both rows, columns 1 to 2
print(np2[0:1, 0:3])  # Slice first row, first three columns
print(np2[0:2, 0:3])  # Slice both rows, first three columns

# NumPy universal functions
np1 = np.array([-1, 0, 1, 2, 3, 4, 5])  # Creating a NumPy array
print(np1)  # Print original array

# Finding square root, absolute, exponential, max, min, sine, sign, log
print(np.sqrt(np1))  # Compute square root (gives NaN for negative values)
print(np.absolute(np1))  # Compute absolute values
print(np.exp(np1))  # Compute exponential (e^x)
print(np.max(np1))  # Get maximum value in array
print(np.min(np1))  # Get minimum value in array
print(np.sin(np1))  # Compute sine of each element
print(np.sign(np1))  # Returns 1 if positive, 0 if zero, -1 if negative
print(np.log(np1))  # Compute natural log (log(x)), returns -inf for negative values

# Creating a view of NumPy array
np1 = np.array([0, 1, 2, 3, 4, 5])  # Creating array
np2 = np1.view()  # Creating a view of np1 (shared memory)
print(f'original np1 {np1}')
print(f'view np2 {np2}')
np1[0] = 42  # Modifying np1 also affects np2 since it's a view
print(f'changed np1 {np1}')
print(f'original np2 {np2}')

# Creating a copy of NumPy array
np2 = np1.copy()  # Creating a copy (separate memory)
print(f'original np1 {np1}')
print(f'copy np2 {np2}')
np1[0] = 42  # Changing np1 doesn't affect np2
print(f'changed np1 {np1}')
print(f'original np2 {np2}')

# Reshaping arrays
np2 = np.array([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]])  # Creating 2D array
print(np2.reshape(3, 4))  # Reshape into 3 rows, 4 columns
print(np2.shape)  # Print shape of original array (2, 6)
print(np2.reshape(5, 2))  # Reshape into 5 rows, 2 columns
print(np2.reshape(1, 10))  # Reshape into 1 row, 10 columns
print(np2.reshape(10, 1))  # Reshape into 10 rows, 1 column
print(np2.ravel())  # Flatten array to 1D
print(np2.T)  # Transpose (swap rows and columns)

# Iterating over arrays
np1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  # Creating an array
for x in np1:
    print(x)  # Print each element

np2 = np.array([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]])  # Creating 2D array
for x in np2:
    print(x)  # Print each row
    for y in x:
        print(y)  # Print each element in row

np3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])  # 3D array
for x in np3:
    for y in x:
        for z in y:
            print(z)  # Print each element

# Using np.nditer() for efficient iteration
for x in np.nditer(np3):
    print(x)

# Sorting arrays
np1 = np.array([5, 3, 8, 9, 10])
print(np.sort(np1))  # Sort array (does not modify original)
print(np1)  # Original array remains unchanged

np2 = np.array(["banana", "cherry", "apple", "mango"])
print(np.sort(np2))  # Sort strings alphabetically

np3 = np.array([True, False, True, False])
print(np.sort(np3))  # Sort Boolean values (False before True)

np4 = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(np4))  # Sort each row separately

# Finding positions of elements
np6 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 4])
x = np.where(np6 == 4)  # Get indices where value is 4
print(x)
y = np.where(np6 % 2 == 0)  # Get indices of even numbers
print(y)
print(np6[y])  # Print even numbers
y = np.where(np6 % 2 == 1)  # Get indices of odd numbers
print(y)
print(np6[y])  # Print odd numbers
