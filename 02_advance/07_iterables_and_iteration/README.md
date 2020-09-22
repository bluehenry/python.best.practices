# Comprehensions
Comprehensions is a short-hand syntax for creating collections and iterable objects.
Comprehensions can use multiple input sequences and multiple if-clauses.

```python
l = [i * 2 for i in range(10)]

d = {i * 2 for i in range(10)}
```
```python
[(x, y) for x in range(10) for y in range(3)]
```
```python
points = []
for x in range(5):
    for y in range(3):
        points.append((x,y))
```

Comprehensions can be nested in other comprehensions.
```python
values = [[y * 3 for y in range(x)] for x in range(10)]
```

# map()
Returns a list of the results after applying the given function to each item of a given iterable (list, tuple etc.) 
map() can accept any number of input sequences. The number of input sequences must match the number of function arguments.
```python
# Python program to demonstrate working 
# of map. 

# Return double of n 
def addition(n): 
	return n + n 

# We double all numbers using map() 
numbers = (1, 2, 3, 4) 
result = map(addition, numbers) 
print(list(result)) 

```

```python
i = map(str, range(5))
```

# filter()
filter() apply a function to each element in a sequence, constructing a new sequence with the elements for which the function returns True.
Passing None as the first argument to filter() will remove elements which evaluate to False.
```python
filter(is_odd, [1,2,3,4,5])

positives = filter(lambda x: x > 0, [1, -1, 0, 2, -2])

```

# functools.reduce()
repeatedly apply a function to the elements of a sequence, reducing them to a single value.
Optional initial value is conceptually just added to the start of the input sequence.
```python
from functools import reduce
import operator
values = [1, 2, 3]
reduce(operator.add, values, 0)

```

# map-reduce = map() and reduce()

# The iteration Protocols
* iter() create an iterator
* next() get net element in sequence
* StopIteration signal the end of the sequence
* iterable is an object which implements the __iter__() method
* iterator is an object which implements the iterable protocol and which implements the __next__() method
* [Difference between iterable and iterator](https://www.geeksforgeeks.org/python-difference-iterable-iterator/)

# __getitem__()
The alternative iterable protocol works with any object that supports consecutive integer indexing via __getitem__()

# Extended iter()
iter() calls callable to produce values
Extended iter() is often used for creating infinite sequences from existing functions
```python
iter(callable, sentinel)
# callable: callable object that takes zero arugments
# sentinel: iteration stops when callable produces this value

```

```python
import datetime
i = iter(datetime.datetime.now, None)
next(i)
next(i)
```
```python
with open('ending_file.txt', 'rt') as f:
    for line in iter(lambda: f.readline().stirp(), 'END'):
        print(line)

```