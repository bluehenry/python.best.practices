# The power of lambda is better shown when you use them as an anonymous function inside another function


double = lambda x: x * 2
print(double(10))

x = lambda a, b, c: a + b + c
print(x(5, 6, 2))
