# The yield statement suspends function’s execution and sends a value back to caller,
# but retains enough state to enable function to resume where it is left off. When resumed,
# the function continues execution immediately after the last yield run.
# This allows its code to produce a series of values over time,
# rather them computing them at once and sending them back like a list.

# A Simple Python program to demonstrate working of yield


# A generator function that yields 1 for first time, 2 second time and 3 third time
def simple_generator():
    yield 1
    yield 2
    yield 3


# Driver code to check above generator function
for value in simple_generator():
    print(value)

students = []


def read_file():
    try:
        f = open("students.txt", "r")
        for student in read_students(f):
            students.append(student)
        f.close()
    except Exception:
        print("Could not read file")


def read_students(f):
    for line in f:
        yield line


read_file()
print(students)
