# NumPy Tutorial 4 - Shaping and Reshaping Arrays

# Importing relevant modules
import numpy as np

# Shape of an array
array = np.array([[1, 2, 3, 10], [4, 5, 6, 10], [7, 8, 9, 10]])
print(array)
print(array.shape) # shows that there are 3 elements with 4 elements in each of those

# Notice what happens when different numbers of elements
# array2 = np.array([[1, 2, 3], [4, 5, 6, 7]])
# print(array2.shape)

# Reshaping arrays
