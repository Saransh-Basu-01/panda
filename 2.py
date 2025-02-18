import numpy as np  # Importing the NumPy library for numerical operations

arr = np.array([[1, 2, 3], [2, 3, 4], [3, 4, 5]])  # Creating a 2D NumPy array

print(arr[0:3, 0:2])  # Slicing rows 0 to 2 (inclusive) and columns 0 to 1 (inclusive)

print(arr[2, 1:2])  # Accessing row 2 and slicing column 1 to 1 (inclusive, gives [4])

print(np.shape(arr))  # Printing the shape of the array (rows, columns)

print(np.size(arr))  # Printing the total number of elements in the array

print(np.ndim(arr))  # Printing the number of dimensions (2D array here)
print(len(arr))
# a = np.array([1, 2, 3, 4, 5])  # Creating a 1D NumPy array (commented out)
# print(a[0:3])  # Slicing elements from index 0 to 2 (inclusive, [1, 2, 3])
