# All parameters (arguments) in the Python language are passed by reference.
# It means if you change what a parameter refers to within a function,
# the change also reflects back in the calling function.


# Function definition is here
def change_me(my_list):
    my_list.append([1, 2, 3, 4])
    print("Values inside the function: " + str(my_list))
    return


# Now you can call change_me function
my_list = [10, 20, 30]
change_me(my_list)
print("Values outside the function: " + str(my_list))


# Keyword Arguments
def my_function(child3, child2, child1):
    print("The youngest child is " + child3)


my_function(child1="Emil", child2="Tobias", child3="Linus")


# Arbitrary Arguments
def my_function(*kids):
    print("The youngest child is " + kids[2])


my_function("Emil", "Tobias", "Linus")
