
numbers = input("Enter numbers separated by spaces: ")
numbers = list(map(int, numbers.split()))
print("Sum =", sum(numbers))
#output:Enter numbers separated by spaces: 5 6 3
#Sum = 14