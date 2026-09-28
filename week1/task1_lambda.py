# task1_lambda.py

# (a) Square a number
square = lambda x: x * x
# (b) Check if a number is even
is_even = lambda x: x % 2 == 0
# (c) Find the larger of two numbers
larger = lambda a, b: a if a > b else b
# Calling the lambda functions
print("Square of 5:", square(5))
print("Is 8 even?", is_even(8))
print("Larger of 10 and 20:", larger(10, 20))

'''output:
Square of 5: 25
Is 8 even? True
Larger of 10 and 20: 20'''
