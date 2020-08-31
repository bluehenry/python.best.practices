thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(thisdict)
print(thisdict.keys())
print(thisdict.values())

for key, value in thisdict.items():
    print(key, ': ', value)

print(thisdict['brand'])

try:
    print(thisdict['nosuchkey'])
except KeyError:
    print("Error finding nosuchkey")

print(thisdict.get("model"))

# Adding value
thisdict["color"] = "red"
print(thisdict)

# Removing values
thisdict.pop("model")
print(thisdict)

del thisdict["color"]
print(thisdict)

# List of students
students = [
    {"name": "Mark", "student_id": 15163},
    {"name": "Katarina", "student_id": 63112},
    {"name": "Jessica", "student_id": 30021}
]

print(students[0]["name"])
# print(students[0]["last_name"]) #  KeyError