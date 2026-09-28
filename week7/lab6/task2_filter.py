# task2_filter.py

# Helper function to check whether a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
# List of integers from 1 to 50
numbers = list(range(1, 51))
# Use filter() to extract prime numbers
prime_numbers = list(filter(is_prime, numbers))
print("Prime numbers from 1 to 50:")
print(prime_numbers)
# Function to check whether a word is a palindrome
def is_palindrome(word):
    return word.lower() == word.lower()[::-1]
# List of words
words = [
    "madam",
    "python",
    "level",
    "hello",
    "radar",
    "world",
    "civic"
]
# Use filter() to keep only palindromes
palindromes = list(filter(is_palindrome, words))
print("\nPalindromes:")
print(palindromes)

'''output:
Prime numbers from 1 to 50:
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

Palindromes:
['madam', 'level', 'radar', 'civic']'''
