# Collection Protocols

## Container
* str, list, range, tuple 
* testing using 'in' and 'not in'

## Sized
* Number of items using len(sized) function
* Must not consume or modify collection

## Iterable
* Obtain an iteration with iter(iterable) function
* Special method: __iter__()

## Sequence
* Retrieve slices by slicing
* Sepcial method __getitem__()
```python
item = seq[index]
item = seq[start:stop]

```

* Find items by value
* No special method
```python
index = seq.index(item)
```

* Concatenation with + operator
* Special method __add__()

* Produce a reversed sequence
```python
r = reversed(seq)
```
* Special method __reversed__()
* Fallback to __getitem__() and __len__()

* Count items
* No special method
```python
num = seq.count(item)
```

* Repetition with * operator
* Special methods __mul() and __rmul__()

## Equality 
* Equality: lhs == rhs
* Special method: __eq__(self, rhs)
* self argument is lhs (left-hand-side operand)

##  Inequality
* Inequality: lhs != rhs
* Special method: __eq__(self, rhs)
* self argument is lhs (left-hand-side operand)


## Set
* set

## Mutable Sequence
* list

## Mutable Set
* set

## Mutable Mapping
* dict

# collections.abc
[collections.abc — Abstract Base Classes for Containers](https://docs.python.org/3/library/collections.abc.html)
This module provides abstract base classes that can be used to test whether a class provides a particular interface.