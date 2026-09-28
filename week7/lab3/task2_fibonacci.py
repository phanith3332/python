# task2_fibonacci.py

def fibonacci(n):
    """Return the nth term of the Fibonacci series using recursion."""
    
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    # Recursive case
    return fibonacci(n - 1) + fibonacci(n - 2)


# Print the first 15 terms
print("First 15 Fibonacci terms:")

for i in range(15):
    print(fibonacci(i), end=" ")

print()


# Count how many times fibonacci(5) is called
count = 0

def fibonacci_count(n):
    global count
    
    if n == 5:
        count += 1
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    return fibonacci_count(n - 1) + fibonacci_count(n - 2)


result = fibonacci_count(10)

print("fibonacci(10) =", result)
print("fibonacci(5) is computed", count, "times")

'''output:
First 15 Fibonacci terms:
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 
fibonacci(10) = 55
fibonacci(5) is computed 8 times'''


