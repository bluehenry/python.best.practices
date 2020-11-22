# Variables do not need to be declared with any particular type and can even change type after they have been set.
x = 4  # x is of type int
x = "Sally"  # x is now of type str
print("x is " + x)

y = None  # None and None is False
print(y)
if y:
    print('This will NOT execute')
