# task3_unbound_local_error.py

counter = 0
# Incorrect function
def wrong_increment():
    print("Before:", counter)
    counter = counter + 1
    print("After:", counter)
print("Trying without global keyword:")
try:
    wrong_increment()
except UnboundLocalError as e:
    print("Error:", e)
# Correct function
def correct_increment():
    global counter
    counter = counter + 1
    print("Counter after increment:", counter)
print("\nUsing global keyword:")
correct_increment()
correct_increment()

'''output:
Trying without global keyword:
Error: cannot access local variable 'counter' where it is not associated with a value

Using global keyword:
Counter after increment: 1
Counter after increment: 2'''
