# NumPy Tutorial 10 - Searching arrays

# Importing relevant modules
import numpy as np

# Search in given array to tell whether located in it
array1 = np.array([1, 2, 3, 4, 4, 6, 8, 9, 9, 8])

# finding if a given value is in this array
location = np.where(array1 == 4)
print(location)
    # prints (array([3, 4]),): tells us that '4' is located at index 3 and 4 in 0th element (1 dimensional array)

# can do more than just locate an element in array, can do logic!
less_than_five = np.where(array1 < 5)
print(less_than_five)
    # prints (array([0, 1, 2, 3, 4]),), tells us that at index 0, 1, 2, 3, 4 are integers < 5

# elements divisible by 3
divisible_by_three = np.where(array1 % 3 == 0)
print(divisible_by_three)
    # prints (array([2, 5, 7, 8]),), tell sus that at index 2, 5, 7, 8 are integers divisible by 3

