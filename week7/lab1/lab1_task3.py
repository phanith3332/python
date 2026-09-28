# lab1_task3.py

def is_even(n):
    """Return True if the number is even, otherwise return False."""
    return n % 2 == 0
# Driver program
for i in range(5):
    n = int(input("Enter a number: "))
    if is_even(n):
        print(n, "is Even")
    else:
        print(n, "is Odd")

'''output:
Enter a number: 32
32 is Even
Enter a number: 33
33 is Odd
Enter a number: 13
13 is Odd
Enter a number: 56
56 is Even
Enter a number: 7
7 is Odd'''
