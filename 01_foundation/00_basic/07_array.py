# List vs Numpy Array
# Basically, Python lists are very flexible and can hold completely heterogeneous, arbitrary data,
# and they can be appended to very efficiently,
# https://stackoverflow.com/questions/176011/python-list-vs-array-when-to-use

import numpy as np
import array as arr


array_1 = np.array([1, 2, 3.5, "hello"])
print(array_1)
print(f'numpy array length is: {len(array_1)}')
print(f'numpy array type is: {type(array_1)}')

array_2 = np.array([1, 2, 3])
print(f'array/3 is: {array_2 / 3}')

array_3 = arr.array("i", [1, 2, 3])
print(array_3)
print(f'array length is: {len(array_3)}')
print(f'array type is: {type(array_3)}')
