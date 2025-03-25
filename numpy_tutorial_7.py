# NumPy Tutorial 6 - Operations for Data Analysis

# Importing relevant modules
import numpy as np

one_dim = np.array([1, 2, 3, 4, 5])
two_dim = np.array([[1, 2, 3], [4, 5, 6]])

# summations
print(sum(one_dim)) # 15, simple bc one dimensional array
print(sum(two_dim)) # [5 7 9] adds up the respective elements of each dimension
print(one_dim.sum()) # produces 15
print(two_dim.sum()) # produces 21, lets you look at the

# Maximum and minimum
print(two_dim.min()) # produces 1
print(two_dim.max()) # produces 6

# Adding elements in rows vs columns
two_dim2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(two_dim2)
# returning elements in each column
print(two_dim2.sum(axis = 0)) # axis = 0 adds across columns
# returning elements in each row
print(two_dim2.sum(axis = 1)) # axis = 1 adds across rows
