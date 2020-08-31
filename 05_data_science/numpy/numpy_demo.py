# At the core, numpy provides the excellent ndarray objects, short for n-dimensional arrays.

# In a ‘ndarray’ object, aka ‘array’, you can store multiple items of the same data type.
# It is the facilities around the array object that makes numpy so convenient for performing math and data manipulations.

import numpy as np


# Create an 1d array from a list
list = [0, 1, 2, 3, 4]
array_1d = np.array(list)

# The key difference between an array and a list is, arrays are designed to handle vectorized operations while a python list is not.
# That means, if you apply a function it is performed on every item in the array, rather than on the whole array object.
new_array_1d = array_1d + 2
print(new_array_1d)


# Create a 2d array from a list of lists
list2 = [[0,1,2], [3,4,5], [6,7,8], [9,10,11]]
array_2d = np.array(list2)

# Convert an array back to a list
array_2d.tolist()

# Inspect the size and shape of a numpy array
print(array_2d.shape, array_2d.dtype, array_2d.size, array_2d.ndim)

# Extract the first 2 rows and columns
# create a new array from an existing array
print(array_2d[:2, :2])

# Reverse the row and column positions
print(array_2d[::-1, ::-1])

# mean, max and min
print("Mean value is: ", array_2d.mean())
print("Max value is: ", array_2d.max())
print("Min value is: ", array_2d.min())

# By row and by column min
print("Column wise minimum: ", np.amin(array_2d, axis=0))
print("Row wise minimum: ", np.amin(array_2d, axis=1))

# Resharping
# Reshape a 3x4 array to 4x3 array
array_2d.reshape(4, 3)

# Flatten it to a 1d array
array_2d.flatten()

# Create sequences, repetitions and random numbers
# Lower limit is 0 be default
print(np.arange(5))

# 0 to 9
print(np.arange(0, 10))

# 0 to 9 with step of 2
print(np.arange(0, 10, 2))

# 10 to 1, decreasing order
print(np.arange(10, 0, -1))

# The np.zeros and np.ones functions lets you create arrays of desired shape where all the items are either 0’s or 1’s.
np.zeros([2,2])
np.ones([2,2])


#  create repeating sequences
a = [1,2,3]

# Repeat whole of 'a' two times
print('Tile:   ', np.tile(a, 2))

# Repeat each element of 'a' two times
print('Repeat: ', np.repeat(a, 2))


# generate random numbers
# Random numbers between [0,1) of shape 2,2
print(np.random.rand(2,2))

# Normal distribution with mean=0 and variance=1 of shape 2,2
print(np.random.randn(2,2))

# Random integers between [0, 10) of shape 2,2
print(np.random.randint(0, 10, size=[2,2]))

# One random number between [0,1)
print(np.random.random())