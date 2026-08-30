#lists_15
squares=[number * number for number in range(1,21)]
print(squares)

'''sample output:
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]
  '''

#lists_16
even=[number for number in range(1,51) if number%2==0]
print("even numbers between 1 to 50 are ", even)

'''sample output:
even numbers between 1 to 50 are  [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50] '''

#lists_17
words=['success','failure','disappointment','sacrife','big','brave']
result = [word for word in words if len(word) > 4]
print(result)

'''sample output:
['success', 'failure', 'disappointment', 'sacrife', 'brave']  '''

#lists_18
matrix = [[1 + row * 3 + col for col in range(3)] for row in range(3)]
print("Matrix:")
for row in matrix:
    print(row)

'''sample output:
Matrix:
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]  '''

#lists_19
numbers = [5, -2, 8, -7, 3, -1,0]
result = [number if number >= 0 else 0 for number in numbers]
print("Original list:", numbers)
print("New list:", result)

'''sample output:
Original list: [5, -2, 8, -7, 3, -1, 0]
New list: [5, 0, 8, 0, 3, 0, 0]  '''

    
    





