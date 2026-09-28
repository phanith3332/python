# task5_gcd_lcm.py

def gcd(a, b):
    """Return the GCD of two numbers using recursion."""
    
    if b == 0:
        return abs(a)
    
    return gcd(b, a % b)


def lcm(a, b):
    """Return the LCM of two numbers using the GCD function."""
    
    if a == 0 or b == 0:
        return 0
    
    return abs(a * b) // gcd(a, b)


# Get input from the user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Calculate GCD and LCM
gcd_result = gcd(a, b)
lcm_result = lcm(a, b)

# Display results
print("GCD:", gcd_result)
print("LCM:", lcm_result)

'''output:
Enter first number: 34
Enter second number: 78
GCD: 2
LCM: 1326'''

