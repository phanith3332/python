
list1 = [10, 20, 30, 40]
list2 = [10, 20, 30, 40]  
list3 = list1              
print("list1:", list1)
print("list2:", list2)
print("list3:", list3)
print("\nMemory Addresses:")
print("id(list1):", id(list1))
print("id(list2):", id(list2))
print("id(list3):", id(list3))
print("\nUsing 'is' operator:")
print("list1 is list2:", list1 is list2)
print("list1 is list3:", list1 is list3)
print("\nUsing 'is not' operator:")
print("list1 is not list2:", list1 is not list2)
print("list1 is not list3:", list1 is not list3)