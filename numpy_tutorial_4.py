# NumPy Tutorial 4 - Copy and View Arrays

# Importing relevant modules
import numpy as np

# Copy
array = np.array([1, 2, 3, 4, 5]) # one-dim array
copy = array.copy() # creates a copy of og array
array[0] = 10
print(array)



