# NumPy Tutorial 1 - Indexing Arrays

# Importing relevant modules
import numpy as np

# Let's start indexing arrays
# One Dimensional Indexing
array = np.array([1, 2, 3, 4, 5]) # one-d array
    # indexing is when you direct python to return a specific part of the array
print(array[0]) # returns the first element in the array, 1
    # for one-dimensional arrays, indexing rules same as lists

# Two Dimension Indexing
two_dim = np.array([[1, 2, 3], [4, 5, 6]])
print(two_dim[0]) # returns first element, [1, 2, 3]
print(two_dim[1]) # returns second element [4, 5, 6]
# returns first element of first dimension
print(two_dim[0,0]) # pulls 1 because [dimension, element in array]
# returns second element of second dimension
print(two_dim[1,1])

# Third Dimension Indexing
three_dim = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(three_dim[0, 1, 2])
    # first number (0) corresponds to first dimension
        # should be [[1, 2, 3], [4, 5, 6]], the first element in first dimension
    # second number (1) corresponds to second dimension
        # should be [4, 5, 6], the second element in second dimension
    # third number (2) corresponds to third dimension
        # should be 6, the third element in third dimension