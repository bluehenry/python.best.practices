# Class Properties and Methods
## Best Practices
* Always creates an instance attribute, never a class attribute
* static methods with the @staticmethod decorator
* class methods with the @classmethod decorator. Requires access to the class object to call other class methods or the constructor.
* Encapsulation (getter, setter) using the @property decorator