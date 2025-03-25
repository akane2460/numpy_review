# NumPy Tutorial 4 - Copy and View Arrays

# Importing relevant modules
import numpy as np

# Copy
array = np.array([1, 2, 3, 4, 5]) # one-dim array
copy = array.copy() # creates a copy of og array
array[0] = 10 # changes the og array
print(array)
print(copy) # but no changes are made to the copy

# View
array2 = np.array([1, 2, 3, 4, 5]) # one-dim array
view = array2.view() # creates a copy of og array
array2[0] = 10
print(array2) # prints updated version of og array
print(view) # view shows the updated version of og array
# if you do view[0] = 10, will also change the original array2

# Python to recall whether it's a copy or a view
print(view.base) # will return array (with changes)
print(copy.base) # will return None