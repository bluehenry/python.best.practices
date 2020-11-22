# A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
this_tuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(this_tuple)
print(this_tuple[1])
print(this_tuple[-1])
print(this_tuple[2:5])
print(this_tuple[-4:-1])

# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
# Convert the tuple into a list to be able to change it:
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
