# Exceptions and Errors
* Don't catch all exceptions
* Exceptions are arranged in an inheritance hierarchy

```python
IndexError.mro()
KeyError.mro()

```

## Exception hierarchy
[Exception hierarchy](https://docs.python.org/3/library/exceptions.html#exception-hierarchy)

## Traceback
* Don't keep references to __traceback__ beyond the sceop of the except block
* Prefer to render __traceback__ to a string

## Assert