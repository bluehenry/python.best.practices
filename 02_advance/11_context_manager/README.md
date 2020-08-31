# Context Manager
* an object design to be used in a with-statement
* A context manager ensures that resources are properly and automatically managed
* Don't pass a list into context manager
* enter() prepares the manager for use
* exit() cleans it up
* files are context managers. file's exit() code closes the file
```python
with open('data.txt', 'w') as f:
    f.write('abc')
```

## Context Mnager Protocol
```python
__enter__(self)

__exit__(self, exec_type, exec_val, exec_tb)
```


## contextlib
* A standard library module for working with context managers
