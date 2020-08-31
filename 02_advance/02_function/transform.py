from pprint import pprint

list1 = [11, 12, 13, 14, 15]
list2 = [21, 22, 23, 24, 25]
list3 = [31, 32, 33, 34, 35]

print(type(zip(list1, list2, list3)))
for item in zip(list1, list2, list3):
    print(type(item))
    print(item)

list_all = [list1, list2, list3]
print(list_all)
pprint(list_all)

for item in zip(list_all[0], list_all[1], list_all[2]):
    print(type(item))
    print(item)


for item in list_all:
    print(item)


for item in zip(*list_all):
    print(item)