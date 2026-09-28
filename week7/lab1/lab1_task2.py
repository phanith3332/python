# lab1_task2.py

def simple_interest(principal, rate, time):
    """Calculate and return the simple interest."""
    si = (principal * rate * time) / 100
    return si
# Get values from the user
principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time in years: "))
# Call the function
result = simple_interest(principal, rate, time)
# Display the result
print("Simple Interest =", result)

'''output:
Enter principal amount: 900
Enter rate of interest: 20
Enter time in years: 5
Simple Interest = 900.0'''
