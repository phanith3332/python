# task1_factorial.py

def factorial(n):
    """Calculate factorial of n using recursion."""
    
    # Handle negative input
    if n < 0:
        return None
    
    # Base case
    if n == 0:
        return 1
    
    # Recursive case
    return n * factorial(n - 1)


def factorial_iterative(n):
    """Calculate factorial of n using a loop."""
    
    if n < 0:
        return None
    
    result = 1
    
    for i in range(1, n + 1):
        result = result * i
    
    return result


# Get input from the user
n = int(input("Enter a number: "))

# Recursive version
recursive_result = factorial(n)

if recursive_result is None:
    print("Factorial is not defined for negative numbers.")
else:
    print("Factorial using recursion:", recursive_result)

    # Iterative version
    iterative_result = factorial_iterative(n)
    print("Factorial using iteration:", iterative_result)

'''output:
Enter a number: 5
Factorial using recursion: 120
Factorial using iteration: 120'''


