# task2_global.py

counter = 0
def increment_counter():
    global counter
    counter = counter + 1
    return counter
for i in range(5):
    print("Counter:", increment_counter())

'''output:
Counter: 1
Counter: 2
Counter: 3
Counter: 4
Counter: 5'''
