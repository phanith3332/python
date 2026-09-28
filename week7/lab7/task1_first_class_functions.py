# task1_first_class_functions.py

# A simple function
def greet(name):
    return "Hello, " + name
# (a) Assign a function to another variable
new_greet = greet
print("(a) Calling function through a new variable:")
print(new_greet("Phanith"))
# (b) Pass a function as an argument
def apply_function(func, value):
    return func(value)
print("\n(b) Passing a function as an argument:")
print(apply_function(greet, "Ravi"))
# (c) Return a function from another function
def create_greeting():
    def welcome(name):
        return "Welcome, " + name
    return welcome
my_function = create_greeting()
print("\n(c) Returning a function from another function:")
print(my_function("Asha"))

'''output:
(a) Calling function through a new variable:
Hello, Phanith

(b) Passing a function as an argument:
Hello, Ravi

(c) Returning a function from another function:
Welcome, Asha'''
