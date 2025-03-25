# NumPy Tutorial 6 - Basic Operations on Arrays

# Importing relevant modules
import numpy as np

# We can create an array between numbers like can do with lists and 'range' command
# When using arrays, use 'arange' command
a = np.arange(0, 5) # for np.arange(x, n) goes [x, ... , n - 1]
print(a)

# Basic Mathematical Operations on Arrays
b = np.array([4, 6, 19, 23, 45])
# adding
print(a + b) # adds respective elements from a and b
# subtracting
print(b - a) # subtracts respective elements a from b
# exponentials
print(a**2)
print(b**4)

# NumPy actually has own functions built in
print(np.sqrt(a)) # becomes floats with sqrt()

# multiplying everything in 'a' by 3
print(a*3) # multiplies each element from a by 3

# less than/more than
c = np.array([1, 2, 3, 4])
print(c < 2) # turns into an array of booleans
print(c > 2)