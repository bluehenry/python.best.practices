students = ["Mark", "Katarina", "Tome", "Homer"]

# for loop
for student in students:
    print(student)

# while loop
n = 0
while n < len(students):
    print(students[n])
    n += 1

# Infinite Loops
n = 0
while True:
    if n == len(students):
        break

    print(students[n])
    n += 1
