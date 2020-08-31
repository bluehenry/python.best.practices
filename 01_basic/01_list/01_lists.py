# There are four collection data types in the Python programming language:
#
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered and unindexed. No duplicate members.
# Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
thislist = []
thislist.append("apple")
thislist.append("banana")
thislist.append("cherry")
print(thislist)

for x in thislist:
    print(x)

if "apple" in thislist:
    print("apple is in this list.")


student_names= ["Mark", "Katarina", "Jessica"]
student_names[0] = "Jerry"
student_names[-1] = "Tom"  # In reverse order
print(student_names)
del student_names[2]
print(len(student_names))   #  list' object has no attribute 'length'


# List Slicing
student_names = ["Mark", "Katarina", "Tome", "Homer"]
print(student_names[1:])
print(student_names[1:-1])     #  ['Katarina', 'Tome']
