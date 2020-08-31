# Python Unit Test
##Unit testing framework
[unittest](https://docs.python.org/3/library/unittest.html)

## Python Mock Object Library
[Understanding the Python Mock Object Library](https://realpython.com/python-mock-library/)

Mock is use for replacing or mocking an object in python unittest while MagicMock is a subclass of Mock with all the magic methods pre-created and ready to use
These are the pre-created magic methods and its default values for MagicMock.
```python
__lt__: NotImplemented
__gt__: NotImplemented
__le__: NotImplemented
__ge__: NotImplemented
__int__: 1
__contains__: False
__len__: 0
__iter__: iter([])
__exit__: False
__complex__: 1j
__float__: 1.0
__bool__: True
__index__: 1
__hash__: default hash for the mock
__str__: default str for the mock
__sizeof__: default sizeof for the mock
```