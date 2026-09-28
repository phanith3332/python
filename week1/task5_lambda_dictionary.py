# task5_lambda_dictionary.py

# Dictionary of items and prices
items = {
    "Laptop": 50000,
    "Mouse": 800,
    "Keyboard": 1500,
    "Headphones": 2500,
    "Monitor": 12000
}
# Sort items by price from cheapest to most expensive
sorted_items = sorted(items.items(), key=lambda item: item[1])
# Display the sorted items
print("Items sorted by price:")
for item, price in sorted_items:
    print(item, ":", price)

'''output:
Items sorted by price:
Mouse : 800
Keyboard : 1500
Headphones : 2500
Monitor : 12000
Laptop : 50000'''
