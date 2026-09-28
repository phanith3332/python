# task3_digits.py

def sum_of_digits(n):
    """Return the sum of digits of a positive integer using recursion."""
    
    if n == 0:
        return 0
    
    return (n % 10) + sum_of_digits(n // 10)


def reverse_number(n, rev=0):
    """Return the digits of n in reverse order using recursion."""
    
    if n == 0:
        return rev
    
    return reverse_number(n // 10, rev * 10 + n % 10)


# Get input from the user
n = int(input("Enter a positive integer: "))

if n > 0:
    print("Sum of digits:", sum_of_digits(n))
    print("Reversed number:", reverse_number(n))
else:
    print("Please enter a positive integer.")

'''output:
Enter a positive integer: 24
Sum of digits: 6
Reversed number: 42'''

