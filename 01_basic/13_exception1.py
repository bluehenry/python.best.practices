try:
  print(a)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
finally:
  print("The 'try except' is finished")


# Raise an exception
x = -1
if x < 0:
  raise Exception("Sorry, no numbers below zero")


student = {
	"name": "Mark",
	"student_id": 15163,
	"feedback": None
}

student["last_name"] = "Kowalski"

try:
	last_name = student["last_name"]
	numbered_last_name = 3 + last_name
except KeyError:
	print("Error finding last_name")
except TypeError as error:
	print("I can't add these two together!")
	print(error)


print("This code executes!")