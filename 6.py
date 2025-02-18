import numpy as np  # Importing the NumPy library

a = np.array([1, 2, 3, 4, 5, 6])  # Creating a 1D NumPy array
print(np.append(a, [10, 20]))  # Appending elements [10, 20] to the array 'a'

print(np.insert(a, 1, 50))  # Inserting the value 50 at index 1 in the 1D array 'a'

arr = np.array([[10, 20], [40, 50]])  # Creating a 2D NumPy array

print(np.insert(arr, 1, [50, 60], axis=1))  # Inserting a column [50, 60] at column index 1

print(np.insert(arr, 1, [50, 60], axis=0))  # Inserting a row [50, 60] at row index 1

print(np.insert(arr, 1, [50, 60]))  # Inserting elements [50, 60] into the flattened array (default axis=None)

print(np.delete(arr, 1))  # Deleting the element at index 1 from the flattened array
# 1. Insert column:
#    [[10, 50, 20]
#     [40, 60, 50]]

# 2. Insert row:
#    [[10, 20]
#     [50, 60]
#     [40, 50]]

# 3. Flattened insertion:
#    [10, 50, 60, 20, 40, 50]
