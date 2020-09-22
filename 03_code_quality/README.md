# Python Enhancement Proposal (PEP)
* A design document providing information to the python community or describing a new feature for python or its processes or environment
* [PEP 0 -- Index of Python Enhancement Proposals (PEPs)](https://www.python.org/dev/peps/)

# [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
* It's a bout style, not about program correctness

## Layout
* Indentation: 4 spaces per level
* Max line length 79 characters
* 2 lines between top-level functions and classes
* 1 line between methods inside a class
* Use of space in expressions

## Imports
* Should be separate lines
* Three groups, separated by blank lines
    - Stand library
    - Third-part libraries
    - Local application/library

## Naming
* Modules: short, lowercase names
* Classes: CapitalizedNaming
* Functions: lowercase_with_underscores 
* Constants: ALL_CAPS    
* Non_public name start with underscore

## Documentation
* Dostrings for all public modules, functions, classes and methods

# Other tools
## pylint
```bash
pylint --generate-rcfile > pylintrc
```

## pycodestyle
```bash
pycodestyle folder_name
```

## black

[# PEP 257 Docstring Conventions](https://www.python.org/dev/peps/pep-0257/)
* Semantics and conventions for docstrings
* Docstrings: String as first statement of a module, function, class or method
* Becomes the __doc__ attribute
* Always use """three doulbe quotes"
* Phrase ending in a period
* Methods: specify return value

## Sphinx
* Python documentation generator
* De-facto standard

## sphinx-apidoc
[sphinx-apidoc](https://www.sphinx-doc.org/en/master/man/sphinx-apidoc.html)

# Type Hints and Static Type checking
* Improve your code with type hints and static type chekcing

## Type Hints
* Optionally add type information
* Ignored by Python interpreter
* Running gives the same results
* Type checker: mypy or Pycharm
```python
def average(a: int, b: int, c: int) -> float:
    return a + b + c / 3
```

```python
age: int = 1
```