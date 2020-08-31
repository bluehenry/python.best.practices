# A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.
thisset = {"apple", "banana", "cherry"}
print(thisset)
print(len(thisset))

for x in thisset:
  print(x)

print("banana" in thisset)


thisset.add("orange")
print(thisset)

thisset.remove("banana")
print(thisset)

thisset.update(["orange", "mango", "grapes"])
print(thisset)

x = thisset.pop()
print(x)

thisset.clear()
print(thisset)

del thisset
# print(thisset) # NameError: name 'thisset' is not defined