# lab2_task2.py

def calculate_price(price, tax_rate=18, discount=0):
    """Calculate the final price after adding tax and applying discount."""
    tax = price * tax_rate / 100
    total = price + tax
    final_price = total - (total * discount / 100)
    return final_price
# (a) Only price - default tax_rate and discount are used
price1 = calculate_price(1000)
print("Final Price (only price):", price1)
# (b) Price and custom tax_rate
price2 = calculate_price(1000, 10)
print("Final Price (custom tax):", price2)
# (c) All three arguments overridden
price3 = calculate_price(1000, 10, 20)
print("Final Price (tax and discount):", price3)

'''output:
Final Price (only price): 1180.0
Final Price (custom tax): 1100.0
Final Price (tax and discount): 880.0'''

