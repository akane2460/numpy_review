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
# Suppose have array of students, 3 of each each age
students = np.array([19, 19, 19, 20, 20, 20, 21, 21, 21])
# also have their average exam score
exam_score = np.array([57, 60, 65, 59, 63, 70, 65, 72, 75])
# Splitting up exam score
exam_split = exam_score.reshape(3, 3)
print(exam_split)
    # Cant reshape every array
        # if you multiply the dimensions to reshape by, need to = # of elements reshaping

# Reshape into three dimensional
one_dim = np.array([1, 2, 3, 4, 5, 6])
three_dim = one_dim.reshape(2, 3, 1)
print(three_dim)
    # takes 6 elements and breaks it into 2 arrays
    # inside those arrays, it will have 3 arrays of 1 element