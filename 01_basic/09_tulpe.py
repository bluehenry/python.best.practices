# A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple)
print(thistuple[1])
print(thistuple[-1])
print(thistuple[2:5])
print(thistuple[-4:-1])

# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
# Convert the tuple into a list to be able to change it:
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)