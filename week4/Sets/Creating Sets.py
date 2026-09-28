#sets_1
my_set = {10, 20, 30, 20, 40, 50, 10, 60}
print(my_set)

'''sample output:
{40, 10, 50, 20, 60, 30} '''


#sets_2
numbers = [1, 2, 3, 2, 4, 1, 5]
text = "programming"
set_from_list = set(numbers)
set_from_string = set(text)
print("Set from list:", set_from_list)
print("Set from string:", set_from_string)

''' sample Output:
Set from list: {1, 2, 3, 4, 5}
Set from string: {'p', 'r', 'o', 'g', 'a', 'm', 'i', 'n'} '''


#sets_3
my_set = {1, 2, 3}
my_set.add(4)
print("After add():", my_set)
my_set.update([5, 6, 7])
print("After update():", my_set)

'''sample Output:
After add(): {1, 2, 3, 4}
After update(): {1, 2, 3, 4, 5, 6, 7} '''

