# List vs Array
# https://stackoverflow.com/questions/176011/python-list-vs-array-when-to-use

import numpy as np

a = np.array([1, 2, 3.5, "hello"])
print(a)
print(len(a))
print(type(a))

aa = np.array([1, 2, 3])
print(aa/3)

import array as arr
b = arr.array("i", [1, 2, 3])
print(b)
print(len(b))
print(type(b))