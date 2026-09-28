# task4_lambda_map_filter.py

# List of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12]
# Use map() with lambda to find cubes
cubes = list(map(lambda x: x ** 3, numbers))
# Use filter() with lambda to find numbers divisible by 3
divisible_by_3 = list(filter(lambda x: x % 3 == 0, numbers))
# Display results
print("Original numbers:", numbers)
print("Cubes:", cubes)
print("Numbers divisible by 3:", divisible_by_3)

'''output:
Original numbers: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12]
Cubes: [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1728]
Numbers divisible by 3: [3, 6, 9, 12]'''
