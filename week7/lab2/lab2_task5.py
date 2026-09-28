# lab2_task5.py

def order_summary(customer, *items, discount=0, **extra):
    """Display customer, ordered items, discount, and extra information."""
    print("\n--- Order Summary ---")
    # Customer name
    print("Customer:", customer)
    # Ordered items
    print("Items:")
    for item in items:
        print("-", item)
    # Discount
    print("Discount:", discount, "%")
    # Extra information
    print("Extra Information:")
    for key, value in extra.items():
        print(f"{key.replace('_', ' ').capitalize()}: {value}")
    print("---------------------")
# Calling the function with all four argument types
order_summary(
    "phanith",
    "Laptop",
    "Mouse",
    discount=10,
    delivery_address="jagannadhapuram",
    gift_wrap=True
)

'''output:
--- Order Summary ---
Customer: phanith
Items:
- Laptop
- Mouse
Discount: 10 %
Extra Information:
Delivery address: jagannadhapuram
Gift wrap: True'''
