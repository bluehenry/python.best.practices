# There are three numeric types in Python:
i = 1  # int
f1 = 2.8  # float
f2 = 12E4  # float
c1 = 1j  # complex
c2 = 3 + 5j  # complex
print(type(i))
print(type(f1))
print(type(f2))
print(type(c1))
print(type(c2))

# Integer and Float
answer = 42
pi = 3.14
print(answer + pi)  # Don't worry about conversion


# Type Hinting
# Function parameters and return value
def add_numbers(a: int, b: int) -> int:
    return a + b


c = add_numbers(10, 15)
print(c)
