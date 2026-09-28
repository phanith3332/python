# lab2_task1.py

def student_info(name, roll_no, branch):
    """Print student details."""
    print("Name:", name)
    print("Roll No:", roll_no)
    print("Branch:", branch)
# Calling using positional arguments
print("Using Positional Arguments:")
student_info("Phanith","5M2", "CSE")
# Calling using keyword arguments in a different order
print("\nUsing Keyword Arguments:")
student_info(branch="CSE", name="Phanith", roll_no="5M2")

'''output:
Using Positional Arguments:
Name: Phanith
Roll No: 5M2
Branch: CSE

Using Keyword Arguments:
Name: Phanith
Roll No: 5M2
Branch: CSE'''
