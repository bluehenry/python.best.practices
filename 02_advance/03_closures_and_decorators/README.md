# Scope Resolution in Python
[Scope Resolution in Python | LEGB Rule](https://www.geeksforgeeks.org/scope-resolution-in-python-legb-rule/)
* Local(L): Defined inside function/class
* Enclosed(E): Defined inside enclosing functions(Nested function concept)
* Global(G): Defined at the uppermost level
* Built-in(B): Reserved names in Python builtin modules

# Local function
* Useful for specialized, one-off functions
* Aid in code organization and readability
* Similar to lambdas, but more general: 
    * May contain multiple expressions. 
    * May contain statements.
    
# Returning Functions
Functions are first-class. Functions can be treated like any other objects.
```python
def enclosing():
    def local_func():
        print('local func')

    # Return local functions
    return local_func
```    

# Closure
Local functions can reference bindings in their enclosing scope via the LEGB rule. 
Furthermore, local functions can be returned from their defining scope and executed in another scope. 
This raises an interesting question. How does a local function use bindings to objects defined in a scope that no longer exists? 
That is once a local function is returned from its enclosing scope, that enclosing scope is gone along with any local objects it defined. 
How can the local function operate without that enclosing scope? The answer is that the local function forms what is known as a closure. 
A closure essentially remembers the objects from the enclosing scope that the local function needs. 
It then keeps them alive so that when the local function is executed they can still be used. 
One way to think of this is that the local function closes over the objects it needs preventing them from being garbage collected.

# Function Factories
Fhe factory function takes some arguments. 
It then creates a local function, which takes its own arguments, but also uses the arguments passed to the factory. 
The combination of runtime function definition enclosures makes this possible. 
A typical example of this kind of factory creates a function, which raises numbers to a particular power. 

# global
global keyword introduce names from global namespace into local namespace.

# nonlocal
nonlocal keyword introduce names from enclosing namespace into local namespace.

# Decorators
At a high level decorators are a way to modify or enhance existing functions in a nonintrusive and maintainable way. 
In Python a decorator is a callable object that takes in a callable and returns a callable.
* Replace, enhance, or modify existing functions without changing those functions. 
* Callers of the original function don't have to change their code because the decorator mechanism ensures that the same name is used for both the decorated and undecorated function.
* Functions, Classes, Class instances could be decorators.
* Use functools.wrap() to prevent lost metadata
