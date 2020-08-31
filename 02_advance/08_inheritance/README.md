# Sinlge inheritance
* Subclasses will want to initialize base classes
* Base class initializer will only be called automatically if subclass initializer is undefined
```python
class SubClass(BaseClass)
```

# isinstance()
* Use isinstance() for runtime type checking 
* determines if an object is of a specified type

# issubclass()
* determines if one type is a subclass of another

# Multiple inheritance
* Defining a class with more than one base class
* Subclasses inherit methods of all bases
```python
class SubClass(Base1, Base2, ...)
```

* Without conflict, names resolve in the obvious way
* Method Resolution Order (MRO) determines name lookup in all cases

# Method Resolution Order (MRO)
## initializer
If a class 
* A. has multiple base classes
* B. defines no initializer

then only the initializer of the first base class is automatically called 

## __bases__

## C3 Method Resolution Order 
* Subclasses come before base classes
* Base class order from class definition is preserved
* First two qualities are preserved no matter where you start in the inheritance graph

## super()
* [Supercharge Your Classes With Python super()](https://realpython.com/python-super/)
* Like in other object-oriented languages, it allows you to call methods of the superclass in your subclass.
* super() uses everything after a specific class in an MRO to resolve method calls 
* super() returns a proxy object which routes method calls
* Bound proxy: bound to a specific class or instance
* Unbound proxy: not bound to a class or instance
* There are two types of bound proxies: instance-bound and class-bound

### Class-baound proxy
```python
super(base-class, derived-class)
```
* Python finds MRO for derived-class
* It then finds base-class in that MRO
* It take everything after base-class in the MRO, and finds the first class in that sequence with a matching method name

### Instance-bound proxy
```python
super(class, instance-of-class)
``` 
* Finds the MRO for the type of the second argument
* Finds the location of the first argument in the MRO
* Uses everything after that for resolving methods

### super()
If you call super() 
* instance method: super(class-of-method, self)
* class method: super(class-of-method, class)
* Calling super() with no arguments inside an instance method produces an instance-bound proxy. 
Calling super() with no arguments inside an class method produces an class-bound proxy.
In both cases, the no argument form of super() is the same as 
calling super with the method's class as the first argument and the method's first argument as the second.



# Object
* Object is the ultimate base class of every class. 
* Object is automatically added as a base class.

# Interfaces in Python: 
* [nterfaces in Python: Protocols and ABCs](http://masnun.rocks/2017/04/15/interfaces-in-python-protocols-and-abcs/)

# Informal Interfaces: Protocols / Duck Typing
* Polymorphism
* There’s no interface keyword in Python.
* decide a class features by methods, not by base class 

# Formal Interface: Abstract Base Classes (ABC)
* [PEP 3119 -- Introducing Abstract Base Classes](https://www.python.org/dev/peps/pep-3119/)
* A way to overload isinstance() and issubclass().
* A new module abc which serves as an "ABC support framework". It defines a metaclass for use with ABCs and a decorator that can be used to define abstract methods.
* Specific ABCs for containers and iterators, to be added to the collections module.