class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name}, {self.age}'

    def __repr__(self):
        return f'Employee(name={self.name}, age={self.age})'

    def __format__(self, format_spec):
        if format_spec == 'r':
            return f'Employee(age={self.age}, name={self.name})'
        else:
            return f'Employee(name={self.name}, age={self.age})'


employee = Employee('Tom', 29)
print(employee)
print(employee.__repr__())
print(repr(employee))
print('({:r}'.format(employee))