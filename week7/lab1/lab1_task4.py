# lab1_task4.py

def stats(numbers):
    """Return the minimum, maximum, and average of a list of numbers."""
    minimum = min(numbers)
    maximum = max(numbers)
    average = sum(numbers) / len(numbers)
    return minimum, maximum, average
# Create a list of numbers
numbers = [10, 20, 30, 40, 50]
# Unpack the returned tuple
minimum, maximum, average = stats(numbers)
# Display the results
print("Minimum:", minimum)
print("Maximum:", maximum)
print("Average:", average)

'''output:
Minimum: 10
Maximum: 50
Average: 30.0'''
