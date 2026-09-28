# lab1_task5.py

def celsius_to_fahrenheit(c):
    """Convert Celsius to Fahrenheit."""
    return (c * 9 / 5) + 32
def fahrenheit_to_celsius(f):
    """Convert Fahrenheit to Celsius."""
    return (f - 32) * 5 / 9
# Menu-driven program
while True:
    print("\n--- Temperature Converter ---")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        c = float(input("Enter temperature in Celsius: "))
        result = celsius_to_fahrenheit(c)
        print("Temperature in Fahrenheit:", result)
    elif choice == "2":
        f = float(input("Enter temperature in Fahrenheit: "))
        result = fahrenheit_to_celsius(f)
        print("Temperature in Celsius:", result)
    elif choice == "3":
        print("Program exited.")
        break
    else:
        print("Invalid choice. Please try again.")

'''output:
--- Temperature Converter ---
1. Celsius to Fahrenheit
2. Fahrenheit to Celsius
3. Exit
Enter your choice: 1
Enter temperature in Celsius: 45
Temperature in Fahrenheit: 113.0

--- Temperature Converter ---
1. Celsius to Fahrenheit
2. Fahrenheit to Celsius
3. Exit
Enter your choice: 2
Enter temperature in Fahrenheit: 212
Temperature in Celsius: 100.0'''
