# NumPy Tutorial 3 - Slicing Arrays

# Importing relevant modules
import numpy as np

# Slicing one dimensional arrays
one_dim = np.array([1, 2, 3, 4, 5]) # one dimensional array
print(one_dim[0:4]) # returns first through fourth element [1, 2, 3, 4]
print(one_dim[1:3]) # returns elements from second through third element [2, 3]
print(one_dim[1:]) # returns everything starting from second element
print(one_dim[:]) # returns entire array unless import additional values
# can recall elements in steps
print(one_dim[:5:2]) # returns every second element in the sliced array

# Slicing two dimensional arrays
two_dim = np.array([[1, 2, 3], [4, 5, 6]])
print(two_dim[1, 0:2]) # returns slice of first through second element in second dimension

two_dim2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(two_dim2[0:3, 0:2]) # from all elements, slice from index 0 to 2