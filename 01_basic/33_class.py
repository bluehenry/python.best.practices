class Employee:
    name = "Tom Cruise"

    def function(self):
        print("This is a message inside the class.")


employeeTom = Employee()

employeeJerry = Employee()
employeeJerry.name = "Jerry"
print(employeeTom.name)
print(employeeJerry.name)
print(employeeJerry.function())
