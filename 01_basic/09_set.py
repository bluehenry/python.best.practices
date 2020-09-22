# A set is a collection which is unordered and un-indexed. In Python sets are written with curly brackets.
this_set = {"apple", "banana", "cherry"}
print(this_set)
print(len(this_set))

for x in this_set:
    print(x)

print("banana" in this_set)

this_set.add("orange")
print(this_set)

this_set.remove("banana")
print(this_set)

this_set.update(["orange", "mango", "grapes"])
print(this_set)

x = this_set.pop()
print(x)

this_set.clear()
print(this_set)

del this_set
#  print(thisset) # NameError: name 'thisset' is not defined
