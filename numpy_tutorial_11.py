# NumPy Tutorial 11 - Sorting arrays

# Importing relevant modules
import numpy as np

# Sorting arrays using 'sort' function
    # will sort an array in mathematical order
array1 = np.array([12904, -1298, 209, 17246, 233333333, 7, -91, 182934])
array1_sorted = np.sort(array1)
print(array1_sorted)

# Can sort two dimensional arrays
array2 = np.array([[91, -45, 9], [8, -3, 4]])
array2_sorted = np.sort(array2)
print(array2_sorted) # this sorts within the elements

# We don't just have to use numbers, can do booleans
bool_array = np.array([True, False, True, False, False, True])
bool_array_sorted = np.sort(bool_array)
print(bool_array_sorted) # false comes first, true comes second

# Sort array with strings into alphabetical order
string_array = np.array(['London', 'New York', 'Mumbai', 'Brazil', 'Tokyo', 'Cape Town', 'Sydney'])
string_array_sorted = np.sort(string_array)
print(string_array_sorted)

# Another cool function: 'searchsorted'
    # will return the index where the inputted value would need to be placed to maintain the order
array3 = np.array([1, 2, 3, 5, 6])
location1 = np.searchsorted(array3, 4)
print(location1) # returns 3, showing that to maintain numeric order we would place '4' at index 3

array4 = np.array([1, 3, 5, 6])
location2 = np.searchsorted(array4, [2, 4, 9])
print(location2) # returns [1 2 4], showing that each respective number in [2 4 9] need to be placed at those
# indices to maintain numeric order