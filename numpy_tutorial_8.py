# NumPy Tutorial 8 - Iterating arrays

# Importing relevant modules
import numpy as np

one_dim = np.array([1, 2, 3, 4, 5])

# Iterating over one dimensional array
for element in one_dim:
    print(element)

two_dim = np.array([[1, 2, 3], [4, 5, 6]])

# Creating a two dimensional array
for element in two_dim:
    print(element)
    # iterates over each element, meaning [1 2 3] and [4 5 6]
    # how do we get it to produce the numbers? can nest the for loops
for element in two_dim:
    for number in element:
        print(number)

# Using 'nditer', really good way to iterate without a bunch of nested for loops
for element in np.nditer(two_dim):
    print(element)

# Figuring out the index using ndenumerate
for index, element in np.ndenumerate(two_dim):
    print(index, element)
