students = []


class Student:
    school_name = "Applecross Primary"

    # built-in __init__() function is always executed when the class is being initiated.
    # Use the __init__() function to assign values to object properties,
    # or other operations that are necessary to do when the object is being created:
    def __init__(self, name, id=999):
        self.name = name
        self.id = id
        students.append(self)

    def __str__(self):
        return "Student " + self.name

    def get_name_capitalize(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name

