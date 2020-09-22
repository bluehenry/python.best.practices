from student import Student


class HighSchoolStudent(Student):
    school_name = "Springfield High Scholl"

    # By using the super() function, you do not have to use the name of the parent element,
    # it will automatically inherit the methods and properties from its parent.
    def get_name_capitalize(self):
        return super().get_name_capitalize() + "-HS"