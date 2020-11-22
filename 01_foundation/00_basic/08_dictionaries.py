this_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(this_dict)
print(this_dict.keys())
print(this_dict.values())

for key, value in this_dict.items():
    print(key, ': ', value)

print(this_dict['brand'])

try:
    print(this_dict['nosuchkey'])
except KeyError:
    print("Error finding nosuchkey")

print(this_dict.get("model"))

# Adding value
this_dict["color"] = "red"
print(this_dict)

# Removing values
this_dict.pop("model")
print(this_dict)

del this_dict["color"]
print(this_dict)

# List of students
students = [
    {"name": "Mark", "student_id": 15163},
    {"name": "Katarina", "student_id": 63112},
    {"name": "Jessica", "student_id": 30021}
]

print(students[0]["name"])
# print(students[0]["last_name"]) #  KeyError
