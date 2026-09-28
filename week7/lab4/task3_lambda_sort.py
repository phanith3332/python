# task3_lambda_sort.py

# List of students with their marks
students = [
    ("Ravi", 78),
    ("Sita", 92),
    ("Amit", 65)
]
# Sort students by marks in descending order
sorted_students = sorted(students, key=lambda s: s[1], reverse=True)
print("Students sorted by marks:")
for student in sorted_students:
    print(student)
# List of strings
words = ["Python", "C", "Programming", "AI", "Computer"]
# Sort strings by length
sorted_words = sorted(words, key=lambda word: len(word))
print("\nStrings sorted by length:")
for word in sorted_words:
    print(word)

'''output:
Students sorted by marks:
('Sita', 92)
('Ravi', 78)
('Amit', 65)

Strings sorted by length:
C
AI
Python
Computer
Programming'''
