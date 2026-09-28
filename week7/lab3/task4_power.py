# task4_power.py

def power(base, exp):
    """Calculate base raised to exp using recursion."""

    # Base case
    if exp == 0:
        return 1

    # Negative exponent
    if exp < 0:
        return 1 / power(base, -exp)

    # Recursive case
    return base * power(base, exp - 1)


# Get input from the user
base = float(input("Enter the base: "))
exp = int(input("Enter the exponent: "))

# Handle 0 raised to a negative number
if base == 0 and exp < 0:
    print("Undefined: 0 cannot have a negative exponent.")
else:
    result = power(base, exp)
    print("Result:", result)


'''output:
Enter the base: 64
Enter the exponent: 3
Result: 262144.0'''
