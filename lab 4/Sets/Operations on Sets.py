#sets_4
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))
print("Difference:", set1.difference(set2))
print("Symmetric Difference:", set1.symmetric_difference(set2))

'''sample Output:
Union: {1, 2, 3, 4, 5, 6, 7, 8}
Intersection: {4, 5}
Difference: {1, 2, 3}
Symmetric Difference: {1, 2, 3, 6, 7, 8} '''


#sets_5
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
print("set1 is subset of set2:", set1.issubset(set2))
print("set2 is superset of set1:", set2.issuperset(set1))

'''sample Output:
set1 is subset of set2: True
set2 is superset of set1: True'''


#sets_6
my_set = {10, 20, 30, 40}
my_set.remove(20)
print("After remove():", my_set)
my_set.discard(30)
print("After discard():", my_set)
my_set.discard(50)
print("After discarding a non-existing element:", my_set)

'''Output:
After remove(): {10, 30, 40}
After discard(): {10, 40}
After discarding a non-existing element: {10, 40} '''


#sets_7
set1 = {1, 2, 3}
set2 = {4, 5, 6}
set3 = {3, 4, 5}
print("set1 and set2 are disjoint:", set1.isdisjoint(set2))
print("set1 and set3 are disjoint:", set1.isdisjoint(set3))

'''Output:
set1 and set2 are disjoint: True
set1 and set3 are disjoint: False '''


#sets_8
numbers = [5, 2, 8, 2, 3, 5, 1, 8, 4, 3]
unique_numbers = set(numbers)
sorted_numbers = sorted(unique_numbers)
print("Unique elements:", unique_numbers)
print("Sorted list:", sorted_numbers)

'''sample Output:
Unique elements: {1, 2, 3, 4, 5, 8}
Sorted list: [1, 2, 3, 4, 5, 8]  '''


#sets_9
squares = {number ** 2 for number in range(1, 21) if number % 2 != 0}
print(squares)

'''Output:
{1, 9, 25, 49, 81, 121, 169, 225, 289, 361} '''
