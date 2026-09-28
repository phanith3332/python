# task1_map.py

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32
# Function to convert string to uppercase
def to_uppercase(text):
    return text.upper()
# List of temperatures in Celsius
temperatures = [0, 10, 20, 30, 40]
# Use map() to convert Celsius to Fahrenheit
fahrenheit = list(map(celsius_to_fahrenheit, temperatures))
print("Celsius temperatures:", temperatures)
print("Fahrenheit temperatures:", fahrenheit)
# List of strings
words = ["python", "programming", "college", "student"]
# Use map() to convert strings to uppercase
uppercase_words = list(map(to_uppercase, words))
print("\nOriginal strings:", words)
print("Uppercase strings:", uppercase_words)

'''output:
Celsius temperatures: [0, 10, 20, 30, 40]
Fahrenheit temperatures: [32.0, 50.0, 68.0, 86.0, 104.0]

Original strings: ['python', 'programming', 'college', 'student']
Uppercase strings: ['PYTHON', 'PROGRAMMING', 'COLLEGE', 'STUDENT']'''
