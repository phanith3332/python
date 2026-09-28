

fruits = ["apple", "banana", "mango", "orange", "grapes"]

fruit = input("Enter a fruit name: ").lower()

print("Fruit List:", fruits)


if fruit in fruits:
    print(fruit, "is in the list.")
else:
    print(fruit, "is not in the list.")


if fruit not in fruits:
    print(fruit, "is not in the list.")
else:
    print(fruit, "is in the list.")

    #output:Enter a fruit name: apple
    #Fruit List: ['apple', 'banana', 'mango', 'orange', 'grapes']
    #apple is in the list.
    #apple is in the list.