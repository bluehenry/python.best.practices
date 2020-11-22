# Python Basic

# Fundamental 
REPL or Read-Evaluate-Print-Loop

## Significant Whitespace Rules
* Prefer four spaces
* Never mix spaces and tabs
* Be consistent on consecutive lines
* Only deviate to improve readability

# Syntax 
## Object 
* Think of named references to objects rather than variables
* The garbage collector reclaims unreachable objects
* id()returns a unique and constant identifier, rarely used in production
* The is operator determines equality of identity
* Test for equivalence using ==
* Function arguments are passed by object-reference. 
* Functions can modify mutable arguments
* To change a mutable argument, replace its contents
* Default argument expressions evaluated once, when def is executed
* Python uses dynamic typing: We don't specify types in advance
* Python uses strong typing: Types are not coerced to match
* Names are looked up in four nested scopes: LEGB rule: Local, Enclosing, Global, and Built-ins
* Global references can be read from a local scope
* Use global to assign to global references from a local scope
* Everything in Python is an object: This includes modules and functions. They can be treated just like other objects
 
## Collections
### tuple: heterogeneous immutable sequence
### str
### range
### list: heterogeneous mutable sequence
### dict: unordered mapping from unique, immutable keys to mutable values
### set: unordered collection of unique, immutable objects

## Exception Handling
* Raise an exception to interrupt program flow.
* Handle an exception to resume control.
* Unhandled exceptions will terminate the program.
* Exception objects contain information about the exceptional event.

# Cheatsheet
* If you cannot run the pip command directly in Windows, add the following path in $PATH 
```
C:\Users\UserName\AppData\Local\Programs\Python\Python37-32\Scripts
```

## Document your code using docstring
```bash
import words
help(words)
```
### pprint

### shebang
A special comment on the first line beginning #! controls module execution by the program loader
Mac OS: 
```bash
#!/usr/local/bin/python3
```
Then run
```bash
chmod +x words.py
./words.py http://sixty-north.com/c/t.txt'#!/usr/local/bin/python3
```
