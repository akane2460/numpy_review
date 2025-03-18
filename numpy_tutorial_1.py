# NumPy Tutorial 1 - Creating Arrays and Dimensional Arrays

# Importing relevant modules
import numpy as np

# Creating a simple array
array = np.array([1, 2, 3, 4, 5])
print(array)

# Let's explore the different size dimensions
# zero dimensional array
zero_dim = np.array([12222374])
print(zero_dim)

# one dimensional array
one_dim = np.array([1, 2, 3])
print(one_dim)

# two dimensional array
two_dim = np.array(([1, 2, 3], [4, 5, 6]))
print(two_dim)

# three dimensional array
three_dim = np.array([([1, 2, 3], [4, 5, 6]),([7, 8, 9], [10, 11, 12])])
print(three_dim)

# finding the dimension of a given array
print(three_dim.ndim) # prints the array dimension

# create arrays of any dimension
new_array = np.array(17, ndmin = 5)
print(new_array)


