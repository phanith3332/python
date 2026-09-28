# task3_reduce.py

from functools import reduce


# List of numbers
numbers = [2, 4, 6, 8, 10]
# (a) Find the product of all numbers
def multiply(a, b):
    return a * b
product = reduce(multiply, numbers)
# (b) Find the maximum value without using max()
def find_max(a, b):
    if a > b:
        return a
    else:
        return b
maximum = reduce(find_max, numbers)
# (c) Concatenate strings into a single sentence
words = ["Python", "is", "easy", "to", "learn"]
def concatenate(a, b):
    return a + " " + b
sentence = reduce(concatenate, words)
# Display results
print("Numbers:", numbers)
print("Product:", product)
print("Maximum value:", maximum)
print("\nWords:", words)
print("Sentence:", sentence)

'''output:
Numbers: [2, 4, 6, 8, 10]
Product: 3840
Maximum value: 10

Words: ['Python', 'is', 'easy', 'to', 'learn']
Sentence: Python is easy to learn'''
